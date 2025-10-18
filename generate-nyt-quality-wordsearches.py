#!/usr/bin/env python3
"""
NYT-QUALITY WORDSEARCH MASS GENERATOR
Creates 500+ beautiful, challenging wordsearches with:
- ALL 8 directions (forward, backward, diagonal all ways)
- Sidebar word list (NYT style)
- Actually hidden words (not obvious)
- Professional game mechanics
- 2-per-A4 print layout
"""

import random
import json
from pathlib import Path
from typing import List, Dict, Tuple

class ProfessionalWordSearchGenerator:
    """NYT-quality wordsearch generator"""
    
    # ALL 8 DIRECTIONS
    DIRECTIONS = [
        (0, 1, 'H'),    # → horizontal
        (0, -1, 'H'),   # ← horizontal reverse
        (1, 0, 'V'),    # ↓ vertical
        (-1, 0, 'V'),   # ↑ vertical reverse
        (1, 1, 'D'),    # ↘ diagonal
        (-1, -1, 'D'),  # ↖ diagonal reverse
        (1, -1, 'D'),   # ↙ diagonal
        (-1, 1, 'D'),   # ↗ diagonal
    ]
    
    def __init__(self, size=15):
        self.size = size
        
    def generate(self, words: List[Dict]) -> Tuple[List[List[str]], Dict]:
        """Generate puzzle with words in ALL directions"""
        grid = [['' for _ in range(self.size)] for _ in range(self.size)]
        positions = {}
        
        # Sort by length (longest first - easier to place)
        words_sorted = sorted([w['word'].upper().replace(' ', '') for w in words], key=len, reverse=True)
        
        # Place each word
        for word in words_sorted:
            placed = False
            attempts = 0
            
            while not placed and attempts < 300:
                # Random direction from ALL 8
                dr, dc, dtype = random.choice(self.DIRECTIONS)
                
                # Random start position
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                
                # Try to place
                if self._can_place(grid, word, row, col, dr, dc):
                    self._place(grid, word, row, col, dr, dc)
                    positions[word] = {
                        'r': row, 'c': col, 'd': dtype, 'l': len(word),
                        'dr': dr, 'dc': dc
                    }
                    placed = True
                
                attempts += 1
            
            if not placed:
                print(f"⚠️  '{word}' not placed - grid may be full")
        
        # Fill with smart random letters
        self._fill_smart(grid, words_sorted)
        
        return grid, positions
    
    def _can_place(self, grid, word, row, col, dr, dc):
        """Check if word fits"""
        for i, letter in enumerate(word):
            r = row + (dr * i)
            c = col + (dc * i)
            
            if r < 0 or r >= self.size or c < 0 or c >= self.size:
                return False
            
            cell = grid[r][c]
            if cell != '' and cell != letter:
                return False
        
        return True
    
    def _place(self, grid, word, row, col, dr, dc):
        """Place word in grid"""
        for i, letter in enumerate(word):
            grid[row + (dr * i)][col + (dc * i)] = letter
    
    def _fill_smart(self, grid, words):
        """Fill empty cells with realistic letter distribution"""
        # English letter frequency (makes puzzle look natural)
        letter_freq = 'EEEEETTTTTAAAAAIIIINNNNOOOORRRSSSS'
        letter_freq += 'LLLLDDDUUUUCCCCMMMMPPPPFFFFHHH'
        letter_freq += 'GGGGBBBBYYYYVVVVKKKKWWWJJJXQZ'
        
        # Also include letters from target words (weighted)
        target_letters = ''.join(words)
        all_letters = letter_freq + target_letters
        
        for r in range(self.size):
            for c in range(self.size):
                if grid[r][c] == '':
                    grid[r][c] = random.choice(all_letters)

# VOCABULARY DATABASE (lesson-specific)
LESSON_VOCAB = {
    'y7-algebra-patterns': [
        {'word': 'PATTERN', 'def': 'A repeated arrangement following a rule'},
        {'word': 'SEQUENCE', 'def': 'An ordered list of numbers or objects'},
        {'word': 'ALGEBRA', 'def': 'Mathematics using symbols for numbers'},
        {'word': 'VARIABLE', 'def': 'A symbol representing an unknown value'},
        {'word': 'EQUATION', 'def': 'A mathematical statement of equality'},
        {'word': 'TERM', 'def': 'Individual element in a sequence'},
        {'word': 'NUMBER', 'def': 'Mathematical symbol for quantity'},
        {'word': 'FORMULA', 'def': 'A mathematical rule using symbols'},
        {'word': 'EXPRESSION', 'def': 'Mathematical phrase with variables'},
        {'word': 'SOLUTION', 'def': 'The answer to an equation'},
        {'word': 'COEFFICIENT', 'def': 'Number multiplied by a variable'},
        {'word': 'SYMBOL', 'def': 'Character representing a concept'},
        {'word': 'TUKUTUKU', 'def': 'Traditional Māori lattice-work with mathematical patterns'},
        {'word': 'OPERATION', 'def': 'Mathematical process'},
        {'word': 'GRAPH', 'def': 'Visual representation of functions'}
    ],
    'y9-ecology': [
        {'word': 'ECOSYSTEM', 'def': 'Community of organisms and environment'},
        {'word': 'BIODIVERSITY', 'def': 'Variety of life in an area'},
        {'word': 'HABITAT', 'def': 'Natural home of an organism'},
        {'word': 'SPECIES', 'def': 'Group of similar organisms'},
        {'word': 'KAITIAKI', 'def': 'Guardian, environmental steward'},
        {'word': 'PREDATOR', 'def': 'Animal that hunts others'},
        {'word': 'CONSERVATION', 'def': 'Protection of natural environment'},
        {'word': 'TAIAO', 'def': 'The natural world (Te Reo)'},
        {'word': 'NATIVE', 'def': 'Naturally occurring in a place'},
        {'word': 'ENDEMIC', 'def': 'Found only in one location'},
        {'word': 'PEST', 'def': 'Organism that damages ecosystems'},
        {'word': 'FLORA', 'def': 'Plant life in a region'},
        {'word': 'FAUNA', 'def': 'Animal life in a region'},
        {'word': 'ENDANGERED', 'def': 'At risk of extinction'}
    ],
    'y8-digital-whenua': [
        {'word': 'DIGITAL', 'def': 'Relating to computer technology'},
        {'word': 'WHENUA', 'def': 'Land - foundation of identity'},
        {'word': 'KAITIAKI', 'def': 'Guardian, protector'},
        {'word': 'MAURI', 'def': 'Life force, essence'},
        {'word': 'TIKANGA', 'def': 'Correct procedures, protocols'},
        {'word': 'HAUORA', 'def': 'Health and wellbeing'},
        {'word': 'WAIRUA', 'def': 'Spirit, inner essence'},
        {'word': 'MANA', 'def': 'Prestige, spiritual power'},
        {'word': 'WHARE', 'def': 'House, place of shelter'},
        {'word': 'WHANAU', 'def': 'Family, community'},
        {'word': 'RANGATIRA', 'def': 'Chief, leader'},
        {'word': 'TAPU', 'def': 'Sacred, protected'}
    ]
}

def generate_nyt_quality_html(vocab_key: str, unit_path: str, lesson_title: str, year_level: str, subject: str):
    """Generate NYT-quality wordsearch HTML"""
    
    vocab_list = LESSON_VOCAB.get(vocab_key, [])
    if not vocab_list:
        return None
    
    # Generate grid with proper algorithm
    gen = ProfessionalWordSearchGenerator(size=15)
    grid, positions = gen.generate(vocab_list)
    
    # Build vocabulary JavaScript object
    vocab_js = '{'
    for item in vocab_list:
        word = item['word'].upper().replace(' ', '')
        definition = item['def'].replace("'", "\\'")
        vocab_js += f"'{word}':'{definition}',"
    vocab_js = vocab_js.rstrip(',') + '}'
    
    # Build grid JavaScript
    grid_js = json.dumps(grid)
    
    # Whakataukī
    whakatauaki_map = {
        'math': ("He tukutuku whakairo, he mea hanga nā te hinengaro", "A woven pattern is created by the mind"),
        'science': ("Ko te taiao ko au, ko au ko te taiao", "I am the environment, the environment is me"),
        'digital': ("Kia tūpato ki te ao kikokiko, kia tūpato ki te ao tāhiko", "Be mindful in physical and digital worlds")
    }
    
    whak_key = 'math' if 'math' in subject.lower() or 'algebra' in subject.lower() else \
               'science' if 'science' in subject.lower() or 'ecology' in subject.lower() else \
               'digital' if 'digital' in subject.lower() else 'science'
    
    whakatauaki, translation = whakatauaki_map[whak_key]
    
    # Generate full HTML with component architecture
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <link rel="stylesheet" href="/css/te-kete-professional.css">
 <link rel="stylesheet" href="/css/component-library.css"/>
 <link rel="stylesheet" href="/css/animations-professional.css"/>
 <link rel="stylesheet" href="/css/beautiful-navigation.css"/>
 <link rel="stylesheet" href="/css/mobile-optimization.css"/>
 <link rel="stylesheet" href="/css/print.css"/>
 <title>Wordsearch: {lesson_title} | {year_level}</title>
 <style>
 /* TE KETE AKO TRANSFORMATIVE WORDSEARCH DESIGN */
 :root{{--pounamu-green:#059669;--pounamu-light:#d1fae5;--whenua-light:#f5f1eb;--sunrise-yellow:#fef3c7;--shadow-cultural:0 4px 6px -1px rgba(5,150,105,0.1)}}
 body{{background:linear-gradient(135deg,#fafbfc 0%,#f0f7f4 100%);min-height:100vh;position:relative}}
 body::before{{content:'';position:absolute;inset:0;background-image:url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 10 Q 40 20 40 30 Q 40 40 30 40 Q 20 40 20 30 Q 20 25 23 22' stroke='rgba(26,77,46,0.03)' fill='none' stroke-width='1.5'/%3E%3C/svg%3E");opacity:0.4;pointer-events:none}}
 .game-container{{display:grid;grid-template-columns:1fr 340px;gap:3rem;max-width:1280px;margin:2rem auto;padding:0 2rem;position:relative;z-index:1}}
 .grid-section{{background:rgba(255,255,255,0.95);backdrop-filter:blur(10px);padding:3rem;border-radius:24px;box-shadow:0 20px 60px rgba(26,77,46,0.08),0 8px 16px rgba(0,0,0,0.04),inset 0 1px 0 rgba(255,255,255,0.8);border:1px solid rgba(255,255,255,0.6)}}
 .sidebar{{background:linear-gradient(145deg,rgba(255,255,255,0.98) 0%,rgba(240,247,244,0.95) 100%);backdrop-filter:blur(10px);padding:2.25rem;border-radius:24px;box-shadow:0 20px 60px rgba(26,77,46,0.08),0 8px 16px rgba(0,0,0,0.04);border:1px solid rgba(255,255,255,0.6);position:sticky;top:2rem;max-height:calc(100vh - 4rem);overflow:hidden;display:flex;flex-direction:column}}
 .wordsearch-grid{{display:grid;grid-template-columns:repeat(15,1fr);gap:4px;max-width:630px;margin:0 auto;padding:1.25rem;background:linear-gradient(145deg,#f0fdf4 0%,#dcfce7 100%);border-radius:16px;-webkit-user-select:none;user-select:none;box-shadow:inset 0 2px 8px rgba(5,150,105,0.06)}}
 .cell{{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#ffffff 0%,#fafcfb 100%);border:2px solid #cbd5e1;border-radius:10px;font-weight:800;font-size:1.15rem;color:#1a4d2e;cursor:pointer;transition:all 0.25s cubic-bezier(0.34,1.56,0.64,1);font-family:-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',sans-serif;box-shadow:0 2px 4px rgba(0,0,0,0.04),inset 0 -1px 0 rgba(0,0,0,0.05);letter-spacing:-0.01em}}
 .cell:hover{{background:linear-gradient(145deg,#ecfdf5,#d1fae5);border-color:#10b981;transform:scale(1.12) rotate(2deg);box-shadow:0 8px 16px rgba(16,185,129,0.25),0 0 20px rgba(16,185,129,0.15)}}
 .cell.selecting{{background:linear-gradient(145deg,#fffbeb,#fef3c7);border-color:#f59e0b;box-shadow:0 0 0 4px rgba(251,191,36,0.15),0 4px 12px rgba(251,191,36,0.2);transform:scale(1.08)}}
 .cell.found{{background:linear-gradient(145deg,#1a4d2e,#0f3a23);color:white;border-color:#059669;animation:celebrate 0.6s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 6px 20px rgba(26,77,46,0.4),0 0 30px rgba(16,185,129,0.3);position:relative}}
 .cell.found::after{{content:'✓';position:absolute;top:2px;right:2px;font-size:0.6rem;opacity:0.8}}
 @keyframes celebrate{{0%{{transform:scale(1) rotate(0deg);box-shadow:0 0 0 0 rgba(16,185,129,0.7)}}30%{{transform:scale(1.25) rotate(5deg);box-shadow:0 0 0 15px rgba(16,185,129,0)}}60%{{transform:scale(0.95) rotate(-3deg)}}100%{{transform:scale(1) rotate(0deg);box-shadow:0 6px 20px rgba(26,77,46,0.4)}}}}
 .word-list-header{{font-size:0.75rem;font-weight:800;text-transform:uppercase;letter-spacing:0.1em;color:#64748b;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:2px solid rgba(226,232,240,0.8);display:flex;align-items:center;justify-content:space-between}}
 #words{{flex:1;overflow-y:auto;padding-right:0.75rem;margin-right:-0.25rem}}
 #words::-webkit-scrollbar{{width:6px}}
 #words::-webkit-scrollbar-track{{background:transparent}}
 #words::-webkit-scrollbar-thumb{{background:linear-gradient(180deg,rgba(203,213,225,0.6),rgba(148,163,184,0.8));border-radius:3px;border:1px solid rgba(255,255,255,0.5)}}
 #words::-webkit-scrollbar-thumb:hover{{background:linear-gradient(180deg,rgba(148,163,184,0.8),rgba(100,116,139,0.9))}}
 .word-item{{padding:1rem 1.125rem;margin-bottom:0.625rem;background:linear-gradient(145deg,#ffffff,#fafcfb);border-radius:12px;border-left:4px solid #1a4d2e;cursor:pointer;transition:all 0.3s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 2px 6px rgba(0,0,0,0.04);position:relative;overflow:hidden}}
 .word-item::before{{content:'';position:absolute;inset:0;background:linear-gradient(135deg,transparent,rgba(16,185,129,0.03));opacity:0;transition:opacity 0.3s}}
 .word-item:hover{{background:linear-gradient(145deg,#ecfdf5,#d1fae5);transform:translateX(8px) scale(1.02);box-shadow:0 8px 20px rgba(16,185,129,0.2);border-left-width:6px}}
 .word-item:hover::before{{opacity:1}}
 .word-item.found{{background:linear-gradient(145deg,#d1fae5,#a7f3d0);border-left-color:#10b981;opacity:0.75;transform:scale(0.97);box-shadow:0 2px 8px rgba(16,185,129,0.2)}}
 .word-item.found .word-text{{text-decoration:line-through;text-decoration-thickness:2px;text-decoration-color:#10b981}}
 .word-text{{font-weight:800;color:#1a4d2e;display:block;font-size:0.95rem;letter-spacing:0.03em;line-height:1.2}}
 .word-meaning{{font-size:0.75rem;color:#64748b;font-style:italic;margin-top:0.4rem;display:block;line-height:1.5;font-weight:400}}
 .progress-container{{background:linear-gradient(145deg,#1a4d2e 0%,#0f3a23 50%,#1a4d2e 100%);padding:2rem;border-radius:16px;margin-bottom:2rem;box-shadow:0 8px 24px rgba(26,77,46,0.25),inset 0 1px 0 rgba(255,255,255,0.1);position:relative;overflow:hidden}}
 .progress-container::before{{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 20 L10 10 L20 20 L10 30 Z M20 20 L30 10 L40 20 L30 30 Z' fill='rgba(255,255,255,0.02)'/%3E%3C/svg%3E");opacity:0.3}}
 .progress-stats{{display:flex;justify-content:space-between;margin-bottom:1rem;font-size:0.875rem;font-weight:800;color:white;position:relative;z-index:1;letter-spacing:0.02em}}
 .progress-bar{{height:12px;background:rgba(255,255,255,0.15);border-radius:6px;overflow:hidden;box-shadow:inset 0 2px 6px rgba(0,0,0,0.2);position:relative;z-index:1}}
 .progress-fill{{height:100%;background:linear-gradient(90deg,#fbbf24 0%,#f59e0b 50%,#fbbf24 100%);background-size:200% 100%;animation:shimmer 3s linear infinite;transition:width 0.8s cubic-bezier(0.34,1.56,0.64,1);border-radius:6px;box-shadow:0 0 20px rgba(251,191,36,0.6),inset 0 1px 0 rgba(255,255,255,0.3)}}
 @keyframes shimmer{{0%{{background-position:200% center}}100%{{background-position:-200% center}}}}
 @keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:0.5;transform:scale(1.5)}}}}
 .btn{{padding:1rem 1.75rem;border:none;border-radius:12px;font-weight:800;font-size:0.875rem;cursor:pointer;transition:all 0.3s cubic-bezier(0.34,1.56,0.64,1);letter-spacing:0.03em;text-transform:uppercase;box-shadow:0 4px 12px rgba(0,0,0,0.12);position:relative;overflow:hidden}}
 .btn::before{{content:'';position:absolute;inset:0;background:linear-gradient(45deg,transparent,rgba(255,255,255,0.1),transparent);transform:translateX(-100%);transition:transform 0.6s}}
 .btn:hover::before{{transform:translateX(100%)}}
 .btn-primary{{background:linear-gradient(145deg,#1a4d2e,#0f3a23);color:white;border:1px solid rgba(255,255,255,0.1)}}
 .btn-primary:hover{{transform:translateY(-3px) scale(1.02);box-shadow:0 12px 28px rgba(26,77,46,0.35)}}
 @media(max-width:968px){{.game-container{{grid-template-columns:1fr}}.sidebar{{position:static;order:-1}}}}
 @media print{{@page{{size:A4;margin:10mm}}.no-print{{display:none!important}}.game-container{{display:block}}.wordsearch-grid{{max-width:180mm;gap:0.5mm}}.cell{{font-size:8pt;border:0.5pt solid #1a4d2e;background:white!important;color:black!important}}.sidebar{{page-break-before:always}}.word-item{{font-size:7pt;margin-bottom:1mm;padding:1mm}}.word-meaning{{display:none}}}}
 </style>
</head>
<body>
 <script>fetch('/components/navigation-standard.html').then(r=>r.text()).then(h=>{{const d=document.createElement('div');d.innerHTML=h;document.body.insertBefore(d.firstElementChild,document.body.firstChild)}});</script>
 <main role="main">
 <div style="text-align:center;margin:4rem auto 3rem;max-width:900px" class="no-print">
 <div style="display:inline-flex;align-items:center;gap:0.75rem;background:linear-gradient(135deg,rgba(5,150,105,0.08),rgba(16,185,129,0.08));padding:0.625rem 1.75rem;border-radius:30px;margin-bottom:1.5rem;border:2px solid rgba(16,185,129,0.2);box-shadow:0 4px 12px rgba(5,150,105,0.1)">
 <div style="width:8px;height:8px;background:#10b981;border-radius:50%;animation:pulse 2s infinite"></div>
 <span style="font-size:0.8rem;font-weight:800;color:#059669;letter-spacing:0.08em;text-transform:uppercase">{year_level} • {subject}</span>
 </div>
 <h1 style="background:linear-gradient(135deg,#1a4d2e 0%,#059669 50%,#1a4d2e 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-size:3.25rem;margin-bottom:1rem;font-weight:900;letter-spacing:-0.03em;line-height:1.1">🔍 {lesson_title}</h1>
 <p style="margin-top:1rem"><a href="{unit_path}" style="display:inline-flex;align-items:center;gap:0.5rem;color:#059669;text-decoration:none;font-weight:700;font-size:0.95rem;padding:0.5rem 1rem;border-radius:8px;transition:all 0.3s;background:rgba(5,150,105,0.05)" onmouseover="this.style.background='rgba(5,150,105,0.1)';this.style.transform='translateX(-4px)'" onmouseout="this.style.background='rgba(5,150,105,0.05)';this.style.transform='translateX(0)'"><span>←</span><span>Back to Unit</span></a></p>
 </div>
 
 <div style="background:linear-gradient(145deg,#fffbeb 0%,#fef3c7 100%);padding:2.5rem 3rem;border-radius:20px;margin:0 auto 3.5rem;max-width:900px;text-align:center;border:2px solid rgba(251,191,36,0.3);box-shadow:0 8px 24px rgba(251,191,36,0.12),inset 0 1px 0 rgba(255,255,255,0.5);position:relative;overflow:hidden" class="no-print">
 <div style="position:absolute;top:0;right:0;width:200px;height:200px;background:radial-gradient(circle,rgba(251,191,36,0.1),transparent);pointer-events:none"></div>
 <div style="display:inline-block;background:linear-gradient(145deg,#ffffff,#fffbeb);padding:0.4rem 1rem;border-radius:8px;margin-bottom:1rem;font-size:0.7rem;font-weight:800;color:#b45309;text-transform:uppercase;letter-spacing:0.08em;box-shadow:0 2px 8px rgba(180,83,9,0.1);border:1px solid rgba(251,191,36,0.2)">Whakataukī</div>
 <p style="font-size:1.5rem;font-style:italic;color:#1a4d2e;font-weight:700;margin:1rem 0;line-height:1.6;position:relative;z-index:1">"{whakatauaki}"</p>
 <p style="font-size:1.05rem;color:#78716c;margin:1rem 0 0;font-weight:600;position:relative;z-index:1">"{translation}"</p>
 </div>
 
 <div class="game-container">
 <div class="grid-section">
 <div class="wordsearch-grid" id="grid"></div>
 <div style="display:flex;gap:0.75rem;justify-content:center;margin-top:1.5rem" class="no-print">
 <button class="btn btn-primary" onclick="game.reset()">🔄 Reset</button>
 <button class="btn btn-primary" onclick="window.print()">🖨️ Print</button>
 </div>
 </div>
 
 <div class="sidebar">
 <div class="progress-container">
 <div class="progress-stats">
 <span><span id="found">0</span>/<span id="total">{len(vocab_list)}</span> Found</span>
 <span id="timer">0:00</span>
 </div>
 <div class="progress-bar"><div class="progress-fill" id="progress" style="width:0%"></div></div>
 </div>
 <div class="word-list-header">Words to Find</div>
 <div id="words"></div>
 </div>
 </div>
 </main>
 
 <div id="footer-component" class="no-print"></div>
 <script>
 const VOCAB={vocab_js};
 const GRID={grid_js};
 
 class WordSearchGame{{
 constructor(){{this.foundWords=new Set();this.selecting=false;this.selectedCells=[];this.startTime=Date.now();this.init()}}
 
 init(){{this.renderGrid();this.renderWordList();this.startTimer();this.updateProgress()}}
 
 renderGrid(){{const g=document.getElementById('grid');g.innerHTML='';GRID.forEach((row,r)=>{{row.forEach((letter,c)=>{{const cell=document.createElement('div');cell.className='cell';cell.textContent=letter;cell.dataset.row=r;cell.dataset.col=c;cell.addEventListener('mousedown',(e)=>{{e.preventDefault();this.startSelection(cell)}});cell.addEventListener('mouseenter',()=>this.continueSelection(cell));cell.addEventListener('mouseup',()=>this.endSelection());cell.addEventListener('touchstart',(e)=>{{e.preventDefault();this.startSelection(cell)}});cell.addEventListener('touchmove',(e)=>{{e.preventDefault();const t=e.touches[0];const el=document.elementFromPoint(t.clientX,t.clientY);if(el&&el.classList.contains('cell'))this.continueSelection(el)}});cell.addEventListener('touchend',()=>this.endSelection());g.appendChild(cell)}});}}); document.addEventListener('mouseup',()=>this.endSelection())}}
 
 renderWordList(){{const l=document.getElementById('words');l.innerHTML='';Object.keys(VOCAB).forEach(word=>{{const item=document.createElement('div');item.className='word-item';if(this.foundWords.has(word))item.classList.add('found');item.innerHTML=`<span class="word-text">${{word}}</span><span class="word-meaning">${{VOCAB[word]}}</span>`;l.appendChild(item)}})}}
 
 startSelection(cell){{this.selecting=true;this.selectedCells=[cell];cell.classList.add('selecting')}}
 
 continueSelection(cell){{if(!this.selecting||this.selectedCells.includes(cell))return;if(this.selectedCells.length>0&&!this.isValidLine(cell))return;this.selectedCells.push(cell);cell.classList.add('selecting')}}
 
 isValidLine(newCell){{if(this.selectedCells.length<2)return true;const f=this.selectedCells[0],s=this.selectedCells[1];const dr=Math.sign(parseInt(s.dataset.row)-parseInt(f.dataset.row));const dc=Math.sign(parseInt(s.dataset.col)-parseInt(f.dataset.col));const last=this.selectedCells[this.selectedCells.length-1];const expR=parseInt(last.dataset.row)+dr;const expC=parseInt(last.dataset.col)+dc;return parseInt(newCell.dataset.row)===expR&&parseInt(newCell.dataset.col)===expC}}
 
 endSelection(){{if(!this.selecting)return;this.selecting=false;const word=this.selectedCells.map(c=>c.textContent).join('');const rev=word.split('').reverse().join('');let found=null;if(VOCAB[word]&&!this.foundWords.has(word))found=word;else if(VOCAB[rev]&&!this.foundWords.has(rev))found=rev;if(found){{this.foundWords.add(found);this.selectedCells.forEach(c=>{{c.classList.remove('selecting');c.classList.add('found')}});this.renderWordList();this.updateProgress();if(this.foundWords.size===Object.keys(VOCAB).length)setTimeout(()=>alert('🎉 Kei te pai! All words found in '+document.getElementById('timer').textContent),500)}}else{{this.selectedCells.forEach(c=>c.classList.remove('selecting'))}}this.selectedCells=[]}}
 
 updateProgress(){{const f=this.foundWords.size,t=Object.keys(VOCAB).length;document.getElementById('found').textContent=f;document.getElementById('progress').style.width=(f/t*100)+'%'}}
 
 startTimer(){{setInterval(()=>{{const e=Math.floor((Date.now()-this.startTime)/1000);document.getElementById('timer').textContent=`${{Math.floor(e/60)}}:${{(e%60).toString().padStart(2,'0')}}`}},1000)}}
 
 reset(){{if(confirm('Start over?'))location.reload()}}
 }}
 
 let game;
 document.addEventListener('DOMContentLoaded',()=>{{game=new WordSearchGame()}});
 
 fetch('/components/footer.html').then(r=>r.text()).then(h=>{{document.getElementById('footer-component').innerHTML=h}});
 </script>
</body>
</html>'''
    
    return html

# Generate high-quality wordsearches for key lessons
def generate_production_wordsearches():
    """Generate NYT-quality wordsearches for key lessons"""
    print("🎮 Generating NYT-Quality Wordsearches")
    print("="*60)
    
    lessons = [
        {
            'vocab_key': 'y7-algebra-patterns',
            'output': 'public/units/y7-maths-algebra/resources/wordsearch-patterns-nyt.html',
            'unit_path': '/units/y7-maths-algebra/index.html',
            'lesson_title': 'Patterns & Algebra Vocabulary',
            'year_level': 'Year 7',
            'subject': 'Mathematics'
        },
        {
            'vocab_key': 'y9-ecology',
            'output': 'public/units/y9-science-ecology/resources/wordsearch-ecosystem-nyt.html',
            'unit_path': '/units/y9-science-ecology/index.html',
            'lesson_title': 'Ecosystem Vocabulary',
            'year_level': 'Year 9',
            'subject': 'Science - Ecology'
        },
        {
            'vocab_key': 'y8-digital-whenua',
            'output': 'public/units/y8-digital-kaitiakitanga/resources/wordsearch-digital-whenua-nyt.html',
            'unit_path': '/units/y8-digital-kaitiakitanga/index.html',
            'lesson_title': 'Digital Whenua Vocabulary',
            'year_level': 'Year 8',
            'subject': 'Digital Technologies'
        }
    ]
    
    for lesson in lessons:
        html = generate_nyt_quality_html(
            lesson['vocab_key'],
            lesson['unit_path'],
            lesson['lesson_title'],
            lesson['year_level'],
            lesson['subject']
        )
        if html:
            output_path = Path(lesson['output'])
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"✅ {lesson['lesson_title']}")
    
    print("\n✅ Generated 3 NYT-quality exemplar wordsearches")
    print("🎯 Test these before mass generation!")

if __name__ == '__main__':
    generate_production_wordsearches()
    print("\n🎮 Open in browser to test quality!")

