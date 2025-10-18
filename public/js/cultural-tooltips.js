/**
 * CULTURAL TOOLTIPS SYSTEM
 * Hover over Māori terms to see translations and context
 */

class CulturalTooltips {
  constructor() {
    this.terms = {
      // Common Te Reo terms
      'kaitiakitanga': {
        translation: 'Guardianship and protection',
        context: 'The concept of stewardship and environmental responsibility'
      },
      'mātauranga': {
        translation: 'Knowledge, wisdom, understanding',
        context: 'Traditional Māori knowledge systems'
      },
      'whakapapa': {
        translation: 'Genealogy, lineage',
        context: 'Connections to ancestors and the land'
      },
      'tikanga': {
        translation: 'Customs, protocols, practices',
        context: 'The correct way of doing things'
      },
      'whakataukī': {
        translation: 'Proverb, saying',
        context: 'Traditional Māori proverbs containing wisdom'
      },
      'te ao māori': {
        translation: 'The Māori world',
        context: 'Māori worldview and way of life'
      },
      'mana': {
        translation: 'Prestige, authority, power',
        context: 'Spiritual power and influence'
      },
      'taonga': {
        translation: 'Treasure, valued possession',
        context: 'Something highly prized and protected'
      },
      'whānau': {
        translation: 'Extended family',
        context: 'Family group including extended relatives'
      },
      'ako': {
        translation: 'To learn, to teach',
        context: 'The reciprocal nature of learning and teaching'
      },
      'rangatira': {
        translation: 'Chief, leader',
        context: 'Person of high rank and authority'
      },
      'tapu': {
        translation: 'Sacred, prohibited',
        context: 'State of being sacred or restricted'
      },
      'noa': {
        translation: 'Free from restriction',
        context: 'Opposite of tapu, unrestricted'
      },
      'marae': {
        translation: 'Meeting grounds',
        context: 'Central community gathering place'
      },
      'kōrero': {
        translation: 'Speak, talk, story',
        context: 'Conversation or narrative'
      }
    };
  }

  init() {
    this.findAndEnhanceTerms();
    this.addStyles();
  }

  findAndEnhanceTerms() {
    // Get all text nodes in the page
    const walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      null,
      false
    );

    const textNodes = [];
    let node;
    while (node = walker.nextNode()) {
      if (node.parentElement.tagName !== 'SCRIPT' && 
          node.parentElement.tagName !== 'STYLE') {
        textNodes.push(node);
      }
    }

    // Find and wrap Māori terms
    textNodes.forEach(textNode => {
      const text = textNode.textContent;
      let modified = false;
      let newHTML = text;

      Object.keys(this.terms).forEach(term => {
        const regex = new RegExp(`\\b${term}\\b`, 'gi');
        if (regex.test(text)) {
          const termData = this.terms[term.toLowerCase()];
          newHTML = newHTML.replace(regex, (match) => {
            return `<span class="cultural-term" 
                          data-term="${match}" 
                          data-translation="${termData.translation}"
                          data-context="${termData.context}"
                          role="button"
                          tabindex="0"
                          aria-label="${match}: ${termData.translation}">${match}</span>`;
          });
          modified = true;
        }
      });

      if (modified) {
        const span = document.createElement('span');
        span.innerHTML = newHTML;
        textNode.parentNode.replaceChild(span, textNode);
      }
    });

    // Add event listeners to all cultural terms
    document.querySelectorAll('.cultural-term').forEach(term => {
      term.addEventListener('mouseenter', (e) => this.showTooltip(e));
      term.addEventListener('mouseleave', (e) => this.hideTooltip(e));
      term.addEventListener('focus', (e) => this.showTooltip(e));
      term.addEventListener('blur', (e) => this.hideTooltip(e));
    });
  }

  showTooltip(e) {
    const term = e.target;
    const translation = term.getAttribute('data-translation');
    const context = term.getAttribute('data-context');

    // Remove any existing tooltips
    document.querySelectorAll('.cultural-tooltip').forEach(t => t.remove());

    // Create tooltip
    const tooltip = document.createElement('div');
    tooltip.className = 'cultural-tooltip';
    tooltip.innerHTML = `
      <div class="tooltip-translation">${translation}</div>
      <div class="tooltip-context">${context}</div>
    `;

    document.body.appendChild(tooltip);

    // Position tooltip
    const rect = term.getBoundingClientRect();
    tooltip.style.left = `${rect.left + (rect.width / 2)}px`;
    tooltip.style.top = `${rect.top - 10}px`;

    // Animate in
    setTimeout(() => tooltip.classList.add('visible'), 10);
  }

  hideTooltip(e) {
    document.querySelectorAll('.cultural-tooltip').forEach(t => {
      t.classList.remove('visible');
      setTimeout(() => t.remove(), 200);
    });
  }

  addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .cultural-term {
        font-style: italic;
        color: #1a4d2e;
        font-weight: 600;
        border-bottom: 2px dotted #d4a574;
        cursor: help;
        position: relative;
        transition: all 0.2s ease;
      }

      .cultural-term:hover,
      .cultural-term:focus {
        color: #0f2818;
        border-bottom-style: solid;
        outline: none;
      }

      .cultural-tooltip {
        position: fixed;
        background: linear-gradient(135deg, #1a4d2e, #2d6a4f);
        color: white;
        padding: 1rem 1.25rem;
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        transform: translate(-50%, -100%);
        z-index: 10000;
        max-width: 300px;
        opacity: 0;
        transition: opacity 0.2s ease;
        pointer-events: none;
      }

      .cultural-tooltip.visible {
        opacity: 1;
      }

      .cultural-tooltip::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 8px solid transparent;
        border-top-color: #2d6a4f;
      }

      .tooltip-translation {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
      }

      .tooltip-context {
        font-size: 0.875rem;
        opacity: 0.9;
        font-style: italic;
      }

      @media (max-width: 768px) {
        .cultural-tooltip {
          max-width: 250px;
          font-size: 0.9rem;
        }
      }
    `;
    document.head.appendChild(style);
  }
}

// Initialize on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const tooltips = new CulturalTooltips();
    tooltips.init();
  });
} else {
  const tooltips = new CulturalTooltips();
  tooltips.init();
}

