#!/usr/bin/env python3
"""
HANDOUT WORDSEARCH GENERATOR
Process all 600 handouts and create vocabulary wordsearches
This will get us to 500+ wordsearches quickly!
"""

import os
import re
import random
import json
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).parent / 'public'

# Common academic vocabulary by domain
DOMAIN_VOCAB = {
    'mathematics': ['EQUATION', 'VARIABLE', 'COEFFICIENT', 'ALGEBRA', 'GEOMETRY', 'CALCULUS', 'STATISTICS', 'RATIO', 'PROPORTION', 'FORMULA'],
    'science': ['HYPOTHESIS', 'EXPERIMENT', 'OBSERVATION', 'ANALYSIS', 'CONCLUSION', 'EVIDENCE', 'THEORY', 'LAW', 'VARIABLE', 'CONTROL'],
    'english': ['THEME', 'CHARACTER', 'PLOT', 'SETTING', 'CONFLICT', 'METAPHOR', 'SIMILE', 'ANALYSIS', 'ARGUMENT', 'EVIDENCE'],
    'te_reo': ['AROHA', 'MANA', 'WHANAU', 'WHENUA', 'KAITIAKI', 'TIKANGA', 'MAURI', 'HAUORA', 'WAIRUA', 'TAPU']
}

def extract_handout_vocab(handout_path):
    """Extract vocabulary from handout"""
    try:
        with open(handout_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract all bold/strong terms
        vocab = []
        for tag in soup.find_all(['strong', 'b', 'em']):
            text = tag.get_text().strip()
            if len(text) > 3 and len(text) < 20 and text.isupper():
                vocab.append(text)
        
        # Extract from headings
        for heading in soup.find_all(['h3', 'h4']):
            text = heading.get_text().strip()
            words = text.split()
            for word in words:
                if len(word) > 4 and word[0].isupper():
                    vocab.append(word.upper())
        
        # Remove duplicates
        vocab = list(set(vocab))[:15]
        
        # Supplement with domain vocabulary if needed
        if len(vocab) < 10:
            path_str = str(handout_path).lower()
            for domain in DOMAIN_VOCAB:
                if domain in path_str:
                    vocab.extend(DOMAIN_VOCAB[domain][:15-len(vocab)])
                    break
        
        return vocab[:15]
    
    except Exception as e:
        return []

def quick_grid_gen(words, size=12):
    """Fast grid generation"""
    grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size)] for _ in range(size)]
    
    for word in words:
        word_clean = word.replace(' ', '')[:12]
        r, c = random.randint(0, size-3), random.randint(0, max(0, size-len(word_clean)-1))
        
        # Place horizontally
        for i, letter in enumerate(word_clean):
            if c + i < size:
                grid[r][c+i] = letter
    
    return grid

def generate_compact_html(title, words, grid, subject="General"):
    """Ultra-compact HTML for mass generation"""
    grid_html = ''.join([f'<div class="c">{cell}</div>' for row in grid for cell in row])
    word_list = ''.join([f'<div class="wi"><b>{w}</b></div>' for w in words])
    
    whakatauaki_options = [
        ("Mā te mōhio ka ora", "Through knowledge comes wellbeing"),
        ("Kōrero mai, kōrero atu", "Speak and be spoken to"),
        ("He aha te mea nui? He tangata", "What is most important? It is people")
    ]
    whak, trans = random.choice(whakatauaki_options)
    
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<link rel="stylesheet" href="/css/te-kete-professional.css"><link rel="stylesheet" href="/css/component-library.css"/>
<title>{title}</title>
<style>
.g{{display:grid;grid-template-columns:repeat(12,1fr);gap:2px;max-width:500px;margin:1rem auto}}
.c{{aspect-ratio:1;display:flex;align-items:center;justify-content:center;border:2px solid #1a4d2e;font-weight:bold;background:white;cursor:pointer;font-size:0.85rem}}
.c:hover{{background:#e8f5e9}}
.c.sel{{background:#ffd700}}
.c.fnd{{background:#1a4d2e;color:white}}
.wl{{columns:2;margin:1rem 0}}
.wi{{padding:0.5rem;margin:0.5rem 0;background:#f8fafc;border-left:4px solid #1a4d2e}}
.wi.fnd{{background:#d1fae5;text-decoration:line-through}}
@media print{{@page{{size:A4}}.c{{font-size:8pt}}.wl{{columns:3;font-size:8pt}}}}
</style></head>
<body><main class="container">
<h1>🔍 {title}</h1>
<div style="background:#fff7ed;padding:1rem;border-radius:8px;margin:1rem 0;text-align:center"><p style="font-style:italic;color:#1a4d2e">"{whak}" - {trans}</p></div>
<div style="background:#1a4d2e;color:white;padding:1rem;border-radius:8px;text-align:center;margin:1rem 0"><span id="f">0</span>/{len(words)} <span id="t">0:00</span></div>
<div class="g" id="g">{grid_html}</div>
<div style="text-align:center;margin:1rem 0"><button onclick="r()" style="padding:0.75rem 1.5rem;background:#1a4d2e;color:white;border:none;border-radius:8px;cursor:pointer">🔄 Reset</button>
<button onclick="print()" style="padding:0.75rem 1.5rem;background:#d4a574;color:white;border:none;border-radius:8px;cursor:pointer;margin-left:0.5rem">🖨️ Print</button></div>
<div class="wl" id="l">{word_list}</div>
</main>
<script>
let w={json.dumps(words)},fnd=new Set(),sel=[],s=false,st=Date.now();
document.addEventListener('DOMContentLoaded',()=>{{init();upd()}});
function init(){{document.querySelectorAll('.c').forEach((c,i)=>{{c.dataset.i=i;c.onmousedown=()=>{{s=true;sel=[c];c.classList.add('sel')}};c.onmouseenter=()=>{{if(s){{sel.push(c);c.classList.add('sel')}}}};c.onmouseup=chk}});document.onmouseup=chk;setInterval(()=>{{document.getElementById('t').textContent=`${{Math.floor((Date.now()-st)/60000)}}:${{Math.floor(((Date.now()-st)/1000)%60).toString().padStart(2,'0')}}`}},1000)}}
function chk(){{if(!s)return;s=false;const wd=sel.map(c=>c.textContent).join('');if(w.includes(wd)&&!fnd.has(wd)){{fnd.add(wd);sel.forEach(c=>{{c.classList.remove('sel');c.classList.add('fnd')}});document.querySelectorAll('.wi').forEach(i=>{{if(i.textContent.includes(wd))i.classList.add('fnd')}});upd()}}else{{sel.forEach(c=>c.classList.remove('sel'))}}sel=[]}}
function upd(){{document.getElementById('f').textContent=fnd.size}}
function r(){{if(confirm('Reset?')){{fnd.clear();st=Date.now();document.querySelectorAll('.c,.wi').forEach(e=>e.classList.remove('fnd','sel'));upd()}}}}
</script></body></html>'''

def process_handouts():
    """Process all handouts and create wordsearches"""
    print("📄 Processing handouts...")
    
    handout_files = list(BASE_DIR.rglob('**/handouts/*.html'))
    handout_files += list(BASE_DIR.rglob('**/*handout*.html'))
    
    # Remove duplicates
    handout_files = list(set([f for f in handout_files if not any(x in f.name for x in ['.backup', '.bak', 'wordsearch'])]))
    
    print(f"Found {len(handout_files)} handout files")
    
    generated = 0
    for handout_path in handout_files[:200]:  # Process first 200
        try:
            vocab = extract_handout_vocab(handout_path)
            
            if len(vocab) < 5:
                continue
            
            # Create output path
            output_dir = handout_path.parent
            if not output_dir.name == 'resources':
                resources_dir = handout_path.parent.parent / 'resources'
                if not resources_dir.exists():
                    resources_dir = output_dir
                output_dir = resources_dir
            
            wordsearch_path = output_dir / f'wordsearch-{handout_path.stem}.html'
            
            if wordsearch_path.exists():
                continue
            
            # Generate
            grid = quick_grid_gen(vocab, size=12)
            title = handout_path.stem.replace('-', ' ').title()
            html = generate_compact_html(title, vocab, grid)
            
            output_dir.mkdir(parents=True, exist_ok=True)
            with open(wordsearch_path, 'w') as f:
                f.write(html)
            
            generated += 1
            if generated % 10 == 0:
                print(f"✅ Generated {generated} handout wordsearches...")
        
        except Exception as e:
            continue
    
    return generated

if __name__ == '__main__':
    print("🎯 HANDOUT WORDSEARCH MASS GENERATOR")
    print("="*60)
    
    count = process_handouts()
    
    print("\n" + "="*60)
    print(f"✅ Generated {count} handout wordsearches")
    print(f"📊 GRAND TOTAL WORDSEARCHES: ~{94 + count}")
    print("\n🚀 Run multiple times to reach 500+!")

