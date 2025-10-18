#!/usr/bin/env python3
"""
🔧 FIX NEXT BATCH OF PLACEHOLDERS
Batch 2: More Y9 Ecology + Guided Inquiry resources
"""

import re
from pathlib import Path

# Resources to fix in this batch
ECOLOGY_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/units/y9-science-ecology/resources')
INQUIRY_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/guided-inquiry-unit/materials')

FIXES = {
    # Y9 Ecology Resources
    'assessment-rubric-species-report.html': '''
<div class="assessment-content">
<h2>📊 Species Report Assessment Rubric</h2>
<p><strong>Type:</strong> Research-Based Assessment | <strong>Curriculum Level:</strong> 4-5 (Years 9-10)</p>

<h3>🎯 Assessment Overview</h3>
<p>Students research and report on a New Zealand endemic species, demonstrating understanding of:</p>
<ul>
<li>Species characteristics, habitat, and ecological niche</li>
<li>Threats to species survival and conservation status</li>
<li>Connection between kaitiakitanga and species protection</li>
<li>Research and communication skills</li>
</ul>

<h3>📝 Assessment Rubric</h3>
<table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Criteria</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Not Yet (0-7)</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Achieved (8-10)</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Merit (11-13)</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Excellence (14-15)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Species Information</strong><br><small>Accuracy and depth of biological details</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Basic facts with gaps or inaccuracies</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Accurate description of key characteristics</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Comprehensive information with ecological context</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Exceptional detail showing deep understanding of species biology</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Conservation Status</strong><br><small>Understanding of threats and protection</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Limited awareness of conservation issues</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Clear explanation of main threats and status</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Thorough analysis of multiple threats and conservation efforts</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Sophisticated understanding linking threats to broader ecological systems</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Māori Perspective</strong><br><small>Cultural significance and kaitiakitanga</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Minimal or superficial cultural connection</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Meaningful inclusion of Māori names and basic cultural significance</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Well-researched cultural perspective with kaitiakitanga principles</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Respectful, deep integration showing understanding of mātauranga Māori approach to this species</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Research Quality</strong><br><small>Use of credible sources and citations</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Few sources or unreliable information</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Multiple credible sources with basic citations</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Excellent range of sources properly referenced</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Exceptional research including primary sources, experts, or local iwi knowledge</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Presentation</strong><br><small>Visual appeal and communication</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Unclear or poorly organized</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Well-structured with clear headings and images</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Professional presentation engaging the reader</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Outstanding presentation that educates and inspires action</td>
</tr>
</tbody>
</table>

<h3>📋 Required Sections</h3>
<ol>
<li><strong>Species Profile</strong>
<ul>
<li>Te reo Māori name and English name</li>
<li>Scientific classification (kingdom, phylum, class, order, family, genus, species)</li>
<li>Physical characteristics (size, appearance, unique features)</li>
<li>Habitat and distribution in Aotearoa</li>
</ul>
</li>
<li><strong>Ecological Role</strong>
<ul>
<li>What does this species eat? What eats it?</li>
<li>How does it interact with its environment?</li>
<li>Why is it important to the ecosystem?</li>
</ul>
</li>
<li><strong>Conservation Status</strong>
<ul>
<li>Current DOC threat classification</li>
<li>Main threats (predators, habitat loss, climate change, etc.)</li>
<li>Conservation efforts underway</li>
<li>What can be done to help?</li>
</ul>
</li>
<li><strong>Cultural Significance</strong>
<ul>
<li>Importance to Māori (historical and contemporary)</li>
<li>Connection to local hapū/iwi (if applicable)</li>
<li>Kaitiakitanga: How can we be guardians of this species?</li>
</ul>
</li>
<li><strong>Visual Elements</strong>
<ul>
<li>High-quality images or drawings</li>
<li>Maps showing distribution</li>
<li>Diagrams or infographics</li>
</ul>
</li>
<li><strong>References</strong>
<ul>
<li>Properly cited sources (APA format recommended)</li>
</ul>
</li>
</ol>

<h3>💡 Suggested Species</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1rem 0;">
<div style="padding: 0.75rem; background: rgba(27, 67, 50, 0.1); border-radius: 6px;">
<strong>Birds:</strong> Kākāpō, Kiwi, Tūī, Kererū, Takahē, Kākā
</div>
<div style="padding: 0.75rem; background: rgba(27, 67, 50, 0.1); border-radius: 6px;">
<strong>Reptiles:</strong> Tuatara, Skinks, Geckos
</div>
<div style="padding: 0.75rem; background: rgba(27, 67, 50, 0.1); border-radius: 6px;">
<strong>Insects:</strong> Wētā, Peripatus (velvet worm)
</div>
<div style="padding: 0.75rem; background: rgba(27, 67, 50, 0.1); border-radius: 6px;">
<strong>Marine:</strong> Hector's Dolphin, Yellow-eyed Penguin
</div>
</div>

<h3>⏰ Time Allocation</h3>
<ul>
<li><strong>Research:</strong> 2-3 lessons (110-165 min)</li>
<li><strong>Draft creation:</strong> 2 lessons (110 min)</li>
<li><strong>Peer review:</strong> 1 lesson (55 min)</li>
<li><strong>Final presentation:</strong> 1 lesson + homework</li>
<li><strong>Total:</strong> Approximately 6-7 lessons</li>
</ul>

<div style="margin-top: 2rem; padding: 1rem; background: rgba(241, 143, 1, 0.1); border-radius: 8px; border-left: 4px solid var(--color-accent);">
<h4>🎯 Teacher Tips</h4>
<ul style="margin: 0.5rem 0; font-size: 0.9rem;">
<li>Connect students with local hapū/iwi who can share traditional knowledge</li>
<li>Consider inviting a DOC ranger or conservation expert as guest speaker</li>
<li>Encourage students to visit habitats if possible (field trip!)</li>
<li>Display finished reports - they make excellent classroom decoration and inspire others</li>
<li>Consider submitting excellent reports to DOC or local conservation groups</li>
</ul>
</div>
</div>
''',

    'rights-charter-template.html': '''
<div class="worksheet-content">
<h1>📜 Rights Charter Template</h1>
<p><strong>Purpose:</strong> Design a comprehensive set of rights for your imagined society</p>

<div class="instructions" style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<h3>📖 Instructions for Students</h3>
<p>Every society needs to protect the rights and wellbeing of its people. Your task is to create a Rights Charter that ensures everyone in your society is treated fairly and has opportunities to thrive.</p>

<p><strong>Think about:</strong></p>
<ul>
<li>What rights do ALL people deserve, regardless of who they are?</li>
<li>What special protections might vulnerable groups need?</li>
<li>How do these rights connect to your society's core values?</li>
<li>How will rights be protected and enforced?</li>
</ul>
</div>

<h2>🏛️ Our Society's Rights Charter</h2>

<div class="charter-header" style="background: white; padding: 1rem; border-radius: 8px; margin: 1rem 0; border: 2px solid var(--color-pounamu);">
<p><strong>Society Name:</strong> _________________________________________________</p>
<p><strong>Charter Authors:</strong> _________________________________________________</p>
<p><strong>Date:</strong> _________________________________________________</p>
</div>

<h3>Section 1: Universal Rights</h3>
<p><em>Rights that EVERY person in our society has, no matter what</em></p>

<div class="rights-list" style="background: rgba(27, 67, 50, 0.05); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<ol>
<li style="margin-bottom: 1.5rem;">
<strong>Right #1:</strong> _______________________________________________________________
<br><small>Why is this right important?</small>
<br>___________________________________________________________________________
</li>
<li style="margin-bottom: 1.5rem;">
<strong>Right #2:</strong> _______________________________________________________________
<br><small>Why is this right important?</small>
<br>___________________________________________________________________________
</li>
<li style="margin-bottom: 1.5rem;">
<strong>Right #3:</strong> _______________________________________________________________
<br><small>Why is this right important?</small>
<br>___________________________________________________________________________
</li>
<li style="margin-bottom: 1.5rem;">
<strong>Right #4:</strong> _______________________________________________________________
<br><small>Why is this right important?</small>
<br>___________________________________________________________________________
</li>
<li style="margin-bottom: 1.5rem;">
<strong>Right #5:</strong> _______________________________________________________________
<br><small>Why is this right important?</small>
<br>___________________________________________________________________________
</li>
</ol>

<p><strong>Add more rights as needed!</strong></p>
</div>

<h3>Section 2: Special Protections</h3>
<p><em>Additional rights or protections for specific groups who might need extra support</em></p>

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Group</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Special Protections/Rights</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Why Needed?</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Children & Youth</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Elders</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">People with Disabilities</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Minority Groups</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Other: ___________</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
</tbody>
</table>

<h3>Section 3: Rights of Nature</h3>
<p><em>How will your society protect the natural world? (Inspired by kaitiakitanga principles)</em></p>

<div style="background: rgba(241, 143, 1, 0.1); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Environmental Rights:</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: Rivers have the right to flow freely and be clean. Native forests have the right to regenerate without interference..."></textarea>

<p style="margin-top: 1rem;"><strong>How will these be protected?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: A Ministry of Environmental Guardianship will monitor ecosystems and enforce protections..."></textarea>
</div>

<h3>Section 4: Responsibilities</h3>
<p><em>Rights come with responsibilities. What responsibilities do citizens have?</em></p>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<ul>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
</ul>
</div>

<h3>Section 5: Enforcement & Protection</h3>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>How will rights be enforced?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: An independent Rights Commission will investigate violations. Courts will hear cases. Community elders will mediate disputes..."></textarea>

<p style="margin-top: 1rem;"><strong>What happens if someone's rights are violated?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: Restorative justice processes, compensation, or legal penalties depending on severity..."></textarea>

<p style="margin-top: 1rem;"><strong>Can rights ever be limited? When and why?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: Only in extreme emergencies and with community approval. Your freedom ends where another's begins..."></textarea>
</div>

<h3>🌿 Reflection Questions</h3>

<div style="background: rgba(241, 143, 1, 0.1); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; border-left: 4px solid var(--color-accent);">
<ol>
<li style="margin-bottom: 1rem;"><strong>How does your Rights Charter reflect your society's core values?</strong>
<br>___________________________________________________________________________
<br>___________________________________________________________________________
</li>

<li style="margin-bottom: 1rem;"><strong>Compare your charter to the UN Declaration of Human Rights or Te Tiriti o Waitangi. What's similar? What's different?</strong>
<br>___________________________________________________________________________
<br>___________________________________________________________________________
</li>

<li style="margin-bottom: 1rem;"><strong>How does your charter reflect principles of kaitiakitanga and collective responsibility?</strong>
<br>___________________________________________________________________________
<br>___________________________________________________________________________
</li>

<li><strong>What was the hardest right to define or protect? Why?</strong>
<br>___________________________________________________________________________
<br>___________________________________________________________________________
</li>
</ol>
</div>

<div style="margin-top: 2rem; padding: 1rem; background: var(--color-gray-50); border-radius: 8px; text-align: center;">
<p style="margin: 0; font-size: 0.9rem;">
<strong>💚 Remember:</strong> A strong Rights Charter protects everyone, especially the most vulnerable.  
It should reflect your deepest values about what it means to live together in harmony.
</p>
</div>
</div>
'''
}

def fix_file(filepath, new_content):
    """Replace placeholder with real content"""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        # Replace the placeholder paragraph
        old_placeholder = '<p class="cultural-text">Placeholder page generated to satisfy links. Content available through teacher dashboard.</p>'
        
        html = html.replace(old_placeholder, new_content)
        
        filepath.write_text(html, encoding='utf-8')
        return True
    except Exception as e:
        print(f"❌ Error fixing {filepath.name}: {e}")
        return False

print("🔧 BATCH 2: FIXING MORE PLACEHOLDERS")
print("=" * 80)

fixed_count = 0
total_lines_before = 0
total_lines_after = 0

for filename, content in FIXES.items():
    # Try ecology dir first
    filepath = ECOLOGY_DIR / filename
    if not filepath.exists():
        # Try inquiry dir
        filepath = INQUIRY_DIR / filename
    
    if filepath.exists():
        # Count lines before
        lines_before = len(filepath.read_text(encoding='utf-8').split('\n'))
        
        if fix_file(filepath, content):
            lines_after = len(filepath.read_text(encoding='utf-8').split('\n'))
            print(f"✅ Fixed: {filename}")
            print(f"   Lines: {lines_before} → {lines_after} (+{lines_after - lines_before})")
            fixed_count += 1
            total_lines_before += lines_before
            total_lines_after += lines_after
    else:
        print(f"⚠️  Not found: {filename}")

print(f"\n✅ BATCH 2 COMPLETE!")
print(f"   Files fixed: {fixed_count}")
print(f"   Total lines: {total_lines_before} → {total_lines_after} (+{total_lines_after - total_lines_before})")
print(f"   Average growth: {(total_lines_after - total_lines_before) // fixed_count if fixed_count > 0 else 0} lines per file")

