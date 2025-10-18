#!/usr/bin/env python3
"""
SYSTEMATIC WORDSEARCH GENERATOR FOR TE KETE AKO
Generates lesson-specific interactive wordsearches for 500+ lessons

Creates beautiful, interactive wordsearches that:
- Follow exact site structure and styling
- Include cultural integration (whakataukī)
- Have 2-per-A4 print layout
- Include vocabulary definitions
- Auto-save progress
- Link to specific lessons
"""

import os
import re
import json
import random
from pathlib import Path
from typing import List, Dict, Tuple
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = Path(__file__).parent / 'public'
UNITS_DIR = BASE_DIR / 'units'
OUTPUT_LESSONS = []

# Whakataukī database by subject
WHAKATAUKĪ_DB = {
    'mathematics': [
        ("He tukutuku whakairo, he mea hanga nā te hinengaro", "A woven pattern is something created by the mind"),
        ("Ahakoa he iti, he pounamu", "Although it is small, it is precious - every mathematical concept matters"),
        ("Kia kaha, kia maia, kia manawanui", "Be strong, be brave, be steadfast - persist in problem solving")
    ],
    'science': [
        ("Kia whakatōmuri te haere whakamua", "I walk backwards into the future with my eyes fixed on my past"),
        ("Ko te taiao ko au, ko au ko te taiao", "I am the environment, the environment is me"),
        ("Toitū te whenua, toitū te tangata", "If the land is well, the people are well")
    ],
    'english': [
        ("He kōrero purakau mo nga uri whakatipu", "Stories are treasures for future generations"),
        ("Ko te reo te tuakiri, ko te tuakiri te reo", "Language is identity, identity is language"),
        ("Kōrero mai, kōrero atu, ka ora te iwi", "Through speaking together, the people flourish")
    ],
    'digital': [
        ("Kia tūpato ki te ao kikokiko, kia tūpato ki te ao tāhiko", "Be mindful in the physical world, be mindful in the digital world"),
        ("He waka eke noa", "We are all in this together - collective digital responsibility"),
        ("Manaaki tangata, manaaki whenua, manaaki tāhiko", "Care for people, care for land, care for digital spaces")
    ],
    'social_studies': [
        ("Whāia te iti kahurangi", "Pursue excellence - seek what is precious"),
        ("E kore e ngaro te kakano i ruia mai i Rangiātea", "The seeds sown in Rangiātea will never be lost"),
        ("Kia tau te rangimārie", "Let there be peace and harmony")
    ]
}

def extract_vocabulary_from_lesson(lesson_path: Path) -> List[Dict]:
    """Extract key vocabulary from a lesson HTML file"""
    try:
        with open(lesson_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        vocab = []
        
        # Look for vocabulary sections
        vocab_sections = soup.find_all(['h3', 'h4'], string=re.compile(r'vocabulary|glossary|key terms', re.I))
        
        for section in vocab_sections:
            # Find list items near this heading
            parent = section.parent
            if parent:
                items = parent.find_all('li')
                for item in items[:20]:  # Max 20 words per wordsearch
                    text = item.get_text().strip()
                    # Extract word and definition
                    if ':' in text:
                        word, definition = text.split(':', 1)
                        vocab.append({
                            'word': word.strip().upper(),
                            'definition': definition.strip()
                        })
        
        # If no explicit vocabulary, extract from lesson objectives
        if not vocab:
            vocab = extract_from_objectives(soup)
        
        return vocab[:15]  # Return max 15 words
    
    except Exception as e:
        print(f"Error processing {lesson_path}: {e}")
        return []

def extract_from_objectives(soup) -> List[Dict]:
    """Extract vocabulary from learning objectives"""
    vocab = []
    objectives = soup.find_all(string=re.compile(r'learning|objective|understand', re.I))
    
    # Extract capitalized terms that appear important
    for obj in objectives:
        words = re.findall(r'\b[A-Z][a-z]+\b', obj)
        for word in words[:5]:
            if len(word) > 3:
                vocab.append({
                    'word': word.upper(),
                    'definition': f'Key concept from lesson'
                })
    
    return vocab

def create_wordsearch_grid(words: List[str], size: int = 14) -> Tuple[List[List[str]], Dict]:
    """Generate a wordsearch grid with words placed"""
    grid = [['' for _ in range(size)] for _ in range(size)]
    positions = {}
    
    # Directions: horizontal, vertical, diagonal
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal down-right
        (-1, 1),  # diagonal up-right
    ]
    
    for word in words:
        placed = False
        attempts = 0
        
        while not placed and attempts < 100:
            direction = random.choice(directions)
            start_row = random.randint(0, size - 1)
            start_col = random.randint(0, size - 1)
            
            if can_place_word(grid, word, start_row, start_col, direction, size):
                place_word(grid, word, start_row, start_col, direction)
                positions[word] = {
                    'row': start_row,
                    'col': start_col,
                    'dir': 'h' if direction == (0, 1) else 'v',
                    'len': len(word)
                }
                placed = True
            
            attempts += 1
    
    # Fill empty cells with random letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for r in range(size):
        for c in range(size):
            if grid[r][c] == '':
                grid[r][c] = random.choice(letters)
    
    return grid, positions

def can_place_word(grid, word, row, col, direction, size):
    """Check if word can be placed at position"""
    dr, dc = direction
    
    for i, letter in enumerate(word):
        r = row + (dr * i)
        c = col + (dc * i)
        
        if r < 0 or r >= size or c < 0 or c >= size:
            return False
        
        if grid[r][c] != '' and grid[r][c] != letter:
            return False
    
    return True

def place_word(grid, word, row, col, direction):
    """Place word in grid"""
    dr, dc = direction
    
    for i, letter in enumerate(word):
        r = row + (dr * i)
        c = col + (dc * i)
        grid[r][c] = letter

def get_whakatauaki(subject: str) -> Tuple[str, str]:
    """Get appropriate whakataukī for subject"""
    subject_lower = subject.lower()
    
    for key in WHAKATAUKĪ_DB:
        if key in subject_lower:
            return random.choice(WHAKATAUKĪ_DB[key])
    
    # Default
    return random.choice(WHAKATAUKĪ_DB['science'])

def generate_wordsearch_html(
    lesson_path: Path,
    vocab: List[Dict],
    unit_name: str,
    lesson_title: str,
    subject: str,
    year_level: str
) -> str:
    """Generate complete wordsearch HTML"""
    
    words = [v['word'] for v in vocab]
    grid, positions = create_wordsearch_grid(words, size=14)
    whakatauaki, translation = get_whakatauaki(subject)
    
    # Create grid HTML
    grid_html = ''
    for row in grid:
        for cell in row:
            grid_html += f'<div class="wordsearch-cell">{cell}</div>'
    
    # Create vocabulary JSON
    vocab_json = '{'
    for v in vocab:
        word = v['word']
        definition = v.get('definition', 'Key term from this lesson').replace("'", "\\'")
        context = v.get('context', f'Important concept for understanding {lesson_title}').replace("'", "\\'")
        vocab_json += f"'{word}':"
        vocab_json += "{"
        vocab_json += f"definition:'{definition}',"
        vocab_json += f"context:'{context}'"
        vocab_json += "},"
    vocab_json = vocab_json.rstrip(',') + '}'
    
    # Generate HTML (using compressed version for efficiency)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <meta name="theme-color" content="#1b4332">
 <link rel="stylesheet" href="/components/badge-system.html">
 <link rel="stylesheet" href="/css/te-kete-professional.css">
 <link rel="stylesheet" href="/css/component-library.css"/>
 <link rel="stylesheet" href="/css/animations-professional.css"/>
 <link rel="stylesheet" href="/css/beautiful-navigation.css"/>
 <link rel="stylesheet" href="/css/mobile-optimization.css"/>
 <link rel="stylesheet" href="/css/print.css"/>
 <title>Wordsearch: {lesson_title} | {year_level}</title>
 <style>
 .wordsearch-grid{{display:grid;grid-template-columns:repeat(14,1fr);gap:3px;max-width:600px;margin:1rem auto;font-family:'Courier New',monospace;-webkit-user-select:none;-moz-user-select:none;user-select:none}}
 .wordsearch-cell{{aspect-ratio:1;display:flex;align-items:center;justify-content:center;border:2px solid #1a4d2e;font-weight:bold;font-size:0.9rem;background:white;cursor:pointer;transition:all 0.2s;border-radius:4px}}
 .wordsearch-cell:hover{{background:#e8f5e9;transform:scale(1.05)}}
 .wordsearch-cell.selected{{background:#ffd700;border-color:#f59e0b}}
 .wordsearch-cell.found{{background:#1a4d2e;color:white}}
 .word-list{{columns:2;column-gap:2rem;margin:1rem 0}}
 .word-list-item{{margin-bottom:0.75rem;padding:0.5rem;background:#f8fafc;border-radius:6px;border-left:4px solid #1a4d2e;cursor:pointer;transition:0.2s}}
 .word-list-item:hover{{background:#e8f5e9}}
 .word-list-item.found{{background:#d1fae5;text-decoration:line-through;opacity:0.7}}
 .word-name{{font-weight:600;color:#1a4d2e;display:block}}
 .word-definition{{font-size:0.85rem;color:#546e7a;font-style:italic}}
 .progress-section{{background:linear-gradient(135deg,#1a4d2e,#2d6a4f);color:white;padding:1.5rem;border-radius:12px;margin:1.5rem 0;text-align:center}}
 .progress-bar{{background:rgba(255,255,255,0.2);height:12px;border-radius:6px;margin:1rem 0}}
 .progress-fill{{background:#ffd700;height:100%;transition:0.5s}}
 .stats-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:1rem}}
 .stat-item{{background:rgba(255,255,255,0.1);padding:0.75rem;border-radius:8px}}
 .stat-number{{font-size:1.5rem;font-weight:700}}
 .stat-label{{font-size:0.85rem;opacity:0.9}}
 .definition-popup{{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:white;padding:2rem;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.3);max-width:500px;width:90%;z-index:1000;display:none}}
 .definition-popup.active{{display:block;animation:popupFadeIn 0.3s}}
 @keyframes popupFadeIn{{from{{opacity:0}}to{{opacity:1}}}}
 .popup-overlay{{position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:999;display:none}}
 .popup-overlay.active{{display:block}}
 .celebration{{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);font-size:4rem;pointer-events:none;opacity:0;animation:celebrate 1s}}
 @keyframes celebrate{{0%{{opacity:0;transform:translate(-50%,-50%) scale(0.5)}}50%{{opacity:1;scale:1.2}}100%{{opacity:0}}}}
 .btn{{padding:0.75rem 1.5rem;font-weight:600;border:none;border-radius:8px;cursor:pointer;transition:0.3s}}
 .btn-primary{{background:#1a4d2e;color:white}}
 .btn-primary:hover{{background:#2d6a4f;transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.2)}}
 .btn-secondary{{background:#d4a574;color:white}}
 @media print{{@page{{size:A4;margin:10mm}}.no-print{{display:none!important}}.wordsearch-grid{{max-width:180mm;gap:1px}}.wordsearch-cell{{font-size:8pt;border:1pt solid #1a4d2e;background:white!important;color:black!important}}.word-list{{font-size:8pt;columns:3}}.word-definition{{display:none}}}}
 </style>
</head>
<body>
 <script>fetch('/components/navigation-standard.html').then(r=>r.text()).then(h=>{{const d=document.createElement('div');d.innerHTML=h;document.body.insertBefore(d.firstElementChild,document.body.firstChild)}});</script>
 <header class="site-header no-print">
 <div class="nav-container">
 <a href="/index.html" class="nav-brand">Te Kete Ako</a>
 <nav class="main-nav">
 <ul>
 <li><a href="/unit-plans.html" class="nav-link"><span class="nav-icon">📚</span><span class="nav-text-en">Unit Plans</span></a></li>
 <li><a href="/lessons.html" class="nav-link"><span class="nav-icon">🎓</span><span class="nav-text-en">Lessons</span></a></li>
 <li><a href="/handouts.html" class="nav-link"><span class="nav-icon">📄</span><span class="nav-text-en">Handouts</span></a></li>
 </ul>
 </nav>
 </div>
 </header>

 <main role="main" class="container">
 <h1 class="wiley-hero-title no-print">🔍 {lesson_title} - Vocabulary Wordsearch</h1>

 <section class="cultural-integration no-print" style="background:linear-gradient(135deg,#fff7ed,#ffedd5);padding:2rem;border-radius:12px;margin:2rem 0;border-left:4px solid var(--color-accent)">
 <div style="background:white;padding:1.5rem;border-radius:8px;text-align:center;border:2px solid var(--color-accent)">
 <h3 style="font-size:0.9rem;color:#546e7a;margin:0 0 0.5rem;text-transform:uppercase">Whakataukī</h3>
 <p style="font-size:1.3rem;font-style:italic;color:#1a4d2e;margin:0.5rem 0;font-weight:500">"{whakatauaki}"</p>
 <p style="font-size:1rem;color:#546e7a">"{translation}"</p>
 </div>
 </section>

 <div class="progress-section no-print">
 <h3 style="margin-top:0">📊 Progress</h3>
 <div class="stats-grid">
 <div class="stat-item"><div class="stat-number" id="words-found">0</div><div class="stat-label">Found</div></div>
 <div class="stat-item"><div class="stat-number" id="total-words">{len(words)}</div><div class="stat-label">Total</div></div>
 <div class="stat-item"><div class="stat-number" id="time-elapsed">0:00</div><div class="stat-label">Time</div></div>
 </div>
 <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
 <p id="completion-message"></p>
 </div>

 <section style="background:white;padding:2rem;border-radius:12px;margin:2rem 0;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
 <h2 class="wiley-section-title">🔍 Find the Vocabulary</h2>
 <div class="wordsearch-grid" id="wordsearch-grid">{grid_html}</div>
 <div style="display:flex;gap:1rem;justify-content:center;margin:1.5rem 0" class="no-print">
 <button class="btn btn-primary" onclick="resetPuzzle()">🔄 Reset</button>
 <button class="btn btn-secondary" onclick="showHint()">💡 Hint</button>
 <button class="btn btn-primary" onclick="window.print()">🖨️ Print</button>
 </div>
 <div class="word-list" id="word-list"></div>
 </section>

 </main>

 <div class="popup-overlay" id="popup-overlay" onclick="closeDefinition()"></div>
 <div class="definition-popup" id="definition-popup">
 <h3 id="popup-word" style="color:#1a4d2e;margin-top:0"></h3>
 <p id="popup-definition" style="font-size:1.1rem;margin:1rem 0"></p>
 <p id="popup-context" style="font-size:0.95rem;color:#546e7a;font-style:italic"></p>
 <button class="btn btn-primary" onclick="closeDefinition()">Kei te pai!</button>
 </div>

 <div id="footer-component" class="no-print"></div>
 <script src="/js/shared-components.js" defer></script>
 <script>
 fetch('/components/footer.html').then(r=>r.text()).then(h=>{{document.getElementById('footer-component').innerHTML=h}});
 
 const VOCABULARY={vocab_json};
 const GRID={json.dumps(grid)};
 const WORD_POSITIONS={json.dumps(positions)};
 
 let foundWords=new Set(),selectedCells=[],isSelecting=false,startTime=Date.now();
 
 document.addEventListener('DOMContentLoaded',()=>{{generateGrid();generateWordList();loadProgress();startTimer();updateProgress()}});
 
 function generateGrid(){{const g=document.getElementById('wordsearch-grid');g.innerHTML='';GRID.forEach((row,r)=>{{row.forEach((letter,c)=>{{const cell=document.createElement('div');cell.className='wordsearch-cell';cell.textContent=letter;cell.dataset.row=r;cell.dataset.col=c;cell.addEventListener('mousedown',()=>startSelection(cell));cell.addEventListener('mouseenter',()=>continueSelection(cell));cell.addEventListener('mouseup',endSelection);g.appendChild(cell)}})}});document.addEventListener('mouseup',endSelection)}}
 
 function generateWordList(){{const list=document.getElementById('word-list');list.innerHTML='';Object.keys(VOCABULARY).forEach(word=>{{const item=document.createElement('div');item.className='word-list-item';if(foundWords.has(word))item.classList.add('found');item.innerHTML=`<span class="word-name">${{word}}</span><span class="word-definition">${{VOCABULARY[word].definition}}</span>`;item.onclick=()=>showDefinition(word);list.appendChild(item)}})}}
 
 function startSelection(cell){{isSelecting=true;selectedCells=[cell];cell.classList.add('selected')}}
 function continueSelection(cell){{if(!isSelecting||selectedCells.includes(cell))return;selectedCells.push(cell);cell.classList.add('selected')}}
 function endSelection(){{if(!isSelecting)return;isSelecting=false;const word=selectedCells.map(c=>c.textContent).join('');const rev=word.split('').reverse().join('');let f=null;if(VOCABULARY[word]&&!foundWords.has(word))f=word;else if(VOCABULARY[rev]&&!foundWords.has(rev))f=rev;if(f){{foundWords.add(f);selectedCells.forEach(c=>{{c.classList.remove('selected');c.classList.add('found')}});showCelebration();setTimeout(()=>showDefinition(f),500);generateWordList();updateProgress();saveProgress();if(foundWords.size===Object.keys(VOCABULARY).length)setTimeout(showCompletion,1000)}}else{{selectedCells.forEach(c=>c.classList.remove('selected'))}}selectedCells=[]}}
 
 function showDefinition(word){{const v=VOCABULARY[word];document.getElementById('popup-word').textContent=word;document.getElementById('popup-definition').textContent=v.definition;document.getElementById('popup-context').textContent='💡 '+v.context;document.getElementById('definition-popup').classList.add('active');document.getElementById('popup-overlay').classList.add('active')}}
 function closeDefinition(){{document.getElementById('definition-popup').classList.remove('active');document.getElementById('popup-overlay').classList.remove('active')}}
 function showCelebration(){{const c=document.createElement('div');c.className='celebration';c.textContent='🎉';document.body.appendChild(c);setTimeout(()=>c.remove(),1000)}}
 function showCompletion(){{document.getElementById('completion-message').innerHTML=`🎊 <strong>Kei te pai!</strong> All found in ${{document.getElementById('time-elapsed').textContent}}!`;for(let i=0;i<5;i++)setTimeout(showCelebration,i*200)}}
 function updateProgress(){{const f=foundWords.size;const t=Object.keys(VOCABULARY).length;document.getElementById('words-found').textContent=f;document.getElementById('progress-fill').style.width=(f/t*100)+'%'}}
 function startTimer(){{setInterval(()=>{{const e=Math.floor((Date.now()-startTime)/1000);document.getElementById('time-elapsed').textContent=`${{Math.floor(e/60)}}:${{(e%60).toString().padStart(2,'0')}}`}},1000)}}
 function resetPuzzle(){{if(confirm('Reset?')){{foundWords.clear();startTime=Date.now();document.querySelectorAll('.wordsearch-cell').forEach(c=>c.classList.remove('found','selected'));generateWordList();updateProgress()}}}}
 function showHint(){{const u=Object.keys(VOCABULARY).filter(w=>!foundWords.has(w));if(!u.length)return;alert(`💡 "${{u[0]}}"\n${{VOCABULARY[u[0]].definition}}`)}}
 function saveProgress(){{localStorage.setItem('ws-{lesson_path.stem}',JSON.stringify({{foundWords:Array.from(foundWords),startTime,date:new Date().toISOString()}}))}}
 function loadProgress(){{try{{const p=JSON.parse(localStorage.getItem('ws-{lesson_path.stem}'));if(p&&new Date(p.date).toDateString()===new Date().toDateString()){{foundWords=new Set(p.foundWords);startTime=p.startTime;generateWordList();updateProgress()}}}}catch(e){{}}}}
 </script>
</body>
</html>'''
    
    return html

def process_all_lessons():
    """Process all lessons and generate wordsearches"""
    print("🔍 SYSTEMATIC WORDSEARCH GENERATOR")
    print("=" * 60)
    
    lesson_files = list(UNITS_DIR.rglob('**/lessons/*.html'))
    lesson_files = [f for f in lesson_files if not f.name.endswith(('.backup', '.bak', '.master-backup'))]
    
    print(f"Found {len(lesson_files)} lesson files")
    
    generated = 0
    skipped = 0
    
    for lesson_path in lesson_files:
        # Skip if wordsearch already exists
        resources_dir = lesson_path.parent.parent / 'resources'
        wordsearch_path = resources_dir / f'wordsearch-{lesson_path.stem}.html'
        
        if wordsearch_path.exists():
            skipped += 1
            continue
        
        # Extract vocabulary
        vocab = extract_vocabulary_from_lesson(lesson_path)
        
        if len(vocab) < 5:
            print(f"⚠️  Skipping {lesson_path.name} - insufficient vocabulary ({len(vocab)} words)")
            skipped += 1
            continue
        
        # Determine unit info
        unit_parts = lesson_path.parts
        unit_name = unit_parts[-3] if len(unit_parts) > 3 else 'Unit'
        lesson_title = lesson_path.stem.replace('-', ' ').title()
        
        # Infer subject and year from path
        subject = 'General'
        year_level = 'Years 7-10'
        
        if 'math' in str(lesson_path).lower():
            subject = 'Mathematics'
        elif 'science' in str(lesson_path).lower() or 'ecology' in str(lesson_path).lower():
            subject = 'Science'
        elif 'english' in str(lesson_path).lower():
            subject = 'English'
        elif 'digital' in str(lesson_path).lower():
            subject = 'Digital Technologies'
        
        if 'y7' in str(lesson_path).lower():
            year_level = 'Year 7'
        elif 'y8' in str(lesson_path).lower():
            year_level = 'Year 8'
        elif 'y9' in str(lesson_path).lower():
            year_level = 'Year 9'
        elif 'y10' in str(lesson_path).lower():
            year_level = 'Year 10'
        
        # Generate wordsearch HTML
        html = generate_wordsearch_html(
            lesson_path,
            vocab,
            unit_name,
            lesson_title,
            subject,
            year_level
        )
        
        # Ensure resources directory exists
        resources_dir.mkdir(exist_ok=True)
        
        # Write file
        with open(wordsearch_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        generated += 1
        print(f"✅ Generated: {wordsearch_path.name}")
        
        OUTPUT_LESSONS.append({
            'lesson': str(lesson_path.relative_to(BASE_DIR)),
            'wordsearch': str(wordsearch_path.relative_to(BASE_DIR)),
            'vocab_count': len(vocab),
            'subject': subject,
            'year_level': year_level
        })
    
    print("\n" + "=" * 60)
    print(f"✅ Generated: {generated} wordsearches")
    print(f"⏭️  Skipped: {skipped} (already exist or insufficient vocab)")
    print(f"📊 Total: {len(lesson_files)} lessons processed")
    
    # Save manifest
    with open('wordsearch-generation-manifest.json', 'w') as f:
        json.dump({
            'generated': generated,
            'skipped': skipped,
            'total_lessons': len(lesson_files),
            'wordsearches': OUTPUT_LESSONS
        }, f, indent=2)
    
    print(f"\n📄 Manifest saved to wordsearch-generation-manifest.json")

if __name__ == '__main__':
    process_all_lessons()
    print("\n🎉 Wordsearch generation complete!")

