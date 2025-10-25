import { GRAPHRAG_CONFIG } from './graphrag-config.js';

// Simple Supabase client creator without bundlers
function createClient(url, key) {
  return {
    async rpc(fn, params) {
      const res = await fetch(`${url}/rest/v1/rpc/${fn}`, {
        method: 'POST',
        headers: {
          'apikey': key,
          'Authorization': `Bearer ${key}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(params || {})
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Supabase RPC ${fn} failed: ${res.status} ${text}`);
      }
      return res.json();
    },
    async select(table, query) {
      const qs = new URLSearchParams(query).toString();
      const res = await fetch(`${url}/rest/v1/${table}?${qs}`, {
        headers: {
          'apikey': key,
          'Authorization': `Bearer ${key}`,
          'Content-Type': 'application/json',
          'Accept-Profile': 'public'
        }
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Supabase select ${table} failed: ${res.status} ${text}`);
      }
      return res.json();
    }
  };
}

const supabase = createClient(GRAPHRAG_CONFIG.supabaseUrl, GRAPHRAG_CONFIG.supabaseAnonKey);

function setStatus(message) {
  const el = document.getElementById('status');
  if (el) el.textContent = message;
}

function renderChain(container, nodes) {
  container.innerHTML = '';
  nodes.forEach((node, idx) => {
    const row = document.createElement('div');
    row.className = 'row';

    const nodeCard = document.createElement('div');
    nodeCard.className = 'node';
    nodeCard.innerHTML = `
      <div style="display:flex; justify-content:space-between; gap:0.5rem;">
        <div>
          <div><strong>${node.title || node.file_path}</strong></div>
          <div class="muted">${node.file_path}</div>
        </div>
        <div>
          <span class="badge">confidence ${Number(node.confidence || 1).toFixed(2)}</span>
        </div>
      </div>
    `;

    row.appendChild(nodeCard);

    container.appendChild(row);

    if (idx < nodes.length - 1) {
      const arrow = document.createElement('div');
      arrow.className = 'arrow';
      arrow.textContent = '↓ prerequisite';
      arrow.style.margin = '0 0 0.25rem 1rem';
      container.appendChild(arrow);
    }
  });
}

async function fetchPrerequisiteChain(startPath) {
  // Fallback if no RPC: derive via iterative prerequisite_for relationships
  const chain = [];
  let current = startPath;
  const maxDepth = 12;
  const visited = new Set();

  for (let depth = 0; depth < maxDepth; depth++) {
    if (!current || visited.has(current)) break;
    visited.add(current);

    const resources = await supabase.select('graphrag_resources', {
      select: 'file_path,title',
      filter: `file_path=eq.${encodeURIComponent(current)}`,
      limit: '1'
    }).catch(() => []);
    const resource = resources[0];

    chain.push({ file_path: current, title: resource ? resource.title : undefined, confidence: 1 });

    const rels = await supabase.select('graphrag_relationships', {
      select: 'source_path,target_path,relationship_type,confidence',
      or: `and(source_path.eq.${encodeURIComponent(current)},relationship_type.eq.prerequisite_for),and(target_path.eq.${encodeURIComponent(current)},relationship_type.eq.required_by)`,
      order: 'confidence.desc',
      limit: '1'
    }).catch(() => []);

    if (!rels || !rels.length) break;
    const rel = rels[0];
    const next = rel.target_path && rel.source_path === current ? rel.target_path : rel.source_path;
    if (!next || next === current) break;
    current = next;
    chain[chain.length - 1].confidence = rel.confidence || 1;
  }

  return chain;
}

async function onExplore() {
  const input = document.getElementById('startPath');
  const chainEl = document.getElementById('chain');
  const path = (input.value || '').trim();
  if (!path) {
    setStatus('Please enter a starting resource path.');
    return;
  }

  setStatus('Loading pathway…');
  chainEl.innerHTML = '';
  try {
    const nodes = await fetchPrerequisiteChain(path);
    if (!nodes.length) {
      setStatus('No prerequisite chain found.');
      return;
    }
    renderChain(chainEl, nodes);
    setStatus(`Found ${nodes.length} steps.`);
  } catch (err) {
    // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        setStatus('Error loading pathway.');
  }
}

document.getElementById('exploreBtn')?.addEventListener('click', onExplore);
document.getElementById('startPath')?.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') onExplore();
});

// Support ?path=/some/file.html to prefill and auto-run
const params = new URLSearchParams(window.location.search);
const seedPath = params.get('path');
if (seedPath) {
  const input = document.getElementById('startPath');
  if (input) {
    input.value = seedPath;
    onExplore();
  }
}


