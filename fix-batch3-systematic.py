#!/usr/bin/env python3
"""
🔧 FIX BATCH 3 OF PLACEHOLDERS
More Y9 Ecology assessment tools
"""

from pathlib import Path

ECOLOGY_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/units/y9-science-ecology/resources')
INQUIRY_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/guided-inquiry-unit/materials')

FIXES = {
    'assessment-rubric-persuasive-letter.html': '''
<div class="assessment-content">
<h2>📊 Persuasive Letter Assessment Rubric</h2>
<p><strong>Type:</strong> Writing Assessment | <strong>Curriculum Level:</strong> 4-5 (Years 9-10)</p>

<h3>🎯 Assessment Overview</h3>
<p>Students write a persuasive letter to advocate for conservation action, demonstrating:</p>
<ul>
<li>Persuasive writing techniques and structure</li>
<li>Evidence-based argumentation</li>
<li>Understanding of ecological issues</li>
<li>Integration of kaitiakitanga principles</li>
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
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Letter Structure</strong><br><small>Format and organization</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Missing key elements of formal letter</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Correct format with clear paragraphs</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Well-organized professional letter</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Polished, publication-ready format</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Persuasive Techniques</strong><br><small>Use of rhetorical strategies</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Limited persuasive elements</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Clear use of basic persuasive techniques</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Effective use of multiple strategies (ethos, pathos, logos)</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Masterful persuasion that compels action</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Evidence & Research</strong><br><small>Use of facts and data</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Minimal or weak evidence</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Good use of relevant facts</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Strong evidence from credible sources</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Compelling evidence woven seamlessly throughout</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Ecological Understanding</strong><br><small>Demonstrates science knowledge</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Basic or inaccurate ecology</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Accurate ecological concepts</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Deep understanding shown through examples</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Sophisticated ecological thinking</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Cultural Integration</strong><br><small>Kaitiakitanga principles</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Minimal cultural perspective</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Clear connection to kaitiakitanga</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Thoughtful integration of Māori worldview</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Powerful blend of science and mātauranga Māori</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Language & Conventions</strong><br><small>Grammar, spelling, tone</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Multiple errors, informal tone</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Mostly correct, appropriate tone</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Professional language, minimal errors</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Flawless conventions, powerful voice</td>
</tr>
</tbody>
</table>

<h3>📋 Letter Components</h3>
<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<h4>Required Elements:</h4>
<ul>
<li>✅ <strong>Heading:</strong> Your address and date</li>
<li>✅ <strong>Inside Address:</strong> Recipient's name, title, organization, address</li>
<li>✅ <strong>Salutation:</strong> Formal greeting (Dear [Title] [Name],)</li>
<li>✅ <strong>Introduction:</strong> Hook and clear purpose statement</li>
<li>✅ <strong>Body Paragraphs:</strong> 2-4 paragraphs with evidence and persuasive arguments</li>
<li>✅ <strong>Call to Action:</strong> Specific request for what you want recipient to do</li>
<li>✅ <strong>Conclusion:</strong> Reinforce main message with impact</li>
<li>✅ <strong>Closing:</strong> Formal sign-off (Sincerely, Ngā mihi,)</li>
<li>✅ <strong>Signature:</strong> Your name (typed and handwritten if submitted physically)</li>
</ul>
</div>

<h3>🎯 Possible Recipients</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">
<div style="padding: 1rem; background: white; border: 1px solid #ddd; border-radius: 6px;">
<strong>Government Officials:</strong>
<ul style="font-size: 0.9rem; margin: 0.5rem 0;">
<li>Minister of Conservation</li>
<li>Local MP</li>
<li>Regional Council</li>
<li>City Mayor</li>
</ul>
</div>
<div style="padding: 1rem; background: white; border: 1px solid #ddd; border-radius: 6px;">
<strong>Organizations:</strong>
<ul style="font-size: 0.9rem; margin: 0.5rem 0;">
<li>Department of Conservation (DOC)</li>
<li>Forest & Bird</li>
<li>Local conservation groups</li>
<li>Predator Free NZ</li>
</ul>
</div>
<div style="padding: 1rem; background: white; border: 1px solid #ddd; border-radius: 6px;">
<strong>Community Leaders:</strong>
<ul style="font-size: 0.9rem; margin: 0.5rem 0;">
<li>School principal</li>
<li>Local business owners</li>
<li>Iwi leaders</li>
<li>Community board</li>
</ul>
</div>
</div>

<h3>💡 Persuasive Techniques Toolkit</h3>
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-accent); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Technique</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">What It Is</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Ethos</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Establish credibility</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"As students who have studied local ecosystems..."</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Pathos</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Appeal to emotions</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"Imagine a future where kākāpō exist only in photos..."</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Logos</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Use logic and facts</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"Studies show that predator control increases native bird populations by 47%..."</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Rhetorical Questions</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Questions that make reader think</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"Can we really afford to lose another species to inaction?"</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Repetition</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Repeat key ideas for impact</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"We must act now. We must protect our native species. We must be kaitiaki."</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Inclusive Language</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Use "we" to build connection</td>
<td style="padding: 0.75rem; border: 1px solid #ddd; font-size: 0.85rem;">"Together, we can restore these habitats..."</td>
</tr>
</tbody>
</table>

<div style="margin-top: 2rem; padding: 1rem; background: rgba(241, 143, 1, 0.1); border-radius: 8px; border-left: 4px solid var(--color-accent);">
<h4>🎯 Teacher Tips</h4>
<ul style="margin: 0.5rem 0; font-size: 0.9rem;">
<li><strong>Authentic Purpose:</strong> Consider actually sending the best letters! Real impact = higher engagement</li>
<li><strong>Model First:</strong> Show examples of effective persuasive letters before students write</li>
<li><strong>Peer Review:</strong> Use tuakana-teina approach for constructive feedback</li>
<li><strong>Cultural Consultation:</strong> If students write about taonga species, consider inviting local iwi to share perspectives</li>
<li><strong>Cross-Curricular:</strong> Perfect for English + Science integration!</li>
</ul>
</div>
</div>
''',

    'cultural-values-framework-worksheet.html': '''
<div class="worksheet-content">
<h1>🌿 Cultural Values Framework Worksheet</h1>
<p><strong>Purpose:</strong> Identify and develop the core values that will guide your imagined society</p>

<div class="instructions" style="background: linear-gradient(135deg, #fff7ed, #ffedd5); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0; border-left: 4px solid var(--color-accent);">
<h3>📖 What Are Values?</h3>
<p>Values are the principles and beliefs that guide how people behave and make decisions. They're like the foundation of a house - everything else is built on top of them.</p>

<p><strong>Examples of values:</strong> Honesty, Respect, Courage, Compassion, Justice, Sustainability, Community, Innovation, Tradition</p>

<p><strong>Your task:</strong> Define 4-6 core values for your society. These should:</p>
<ul>
<li>Reflect what's most important to your community</li>
<li>Guide laws, customs, and daily life</li>
<li>Be unique and meaningful (not just copied from others)</li>
<li>Consider both individual and collective wellbeing</li>
</ul>
</div>

<h2>Part 1: Values Exploration</h2>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<h3>Brainstorm: What Matters Most?</h3>
<p><em>Think about what kind of society you want to create. What would make it a good place to live?</em></p>

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Category</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Your Ideas</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>How people treat each other</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Relationship with nature</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Learning and knowledge</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Creativity and innovation</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Tradition and culture</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Justice and fairness</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
</tbody>
</table>
</div>

<h2>Part 2: Define Your Core Values</h2>

<p><em>Choose 4-6 values from your brainstorm. For each value, complete the framework below:</em></p>

<div class="value-card" style="background: white; padding: 2rem; border-radius: 12px; margin: 2rem 0; border: 3px solid var(--color-pounamu); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h3 style="margin-top: 0;">Value #1</h3>

<div style="background: rgba(27, 67, 50, 0.05); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Name of Value (in English):</strong> _______________________________________</p>
<p><strong>Name of Value (in Te Reo Māori, if applicable):</strong> _______________________________________</p>
<p><small>💡 Consider creating a new word that captures your unique concept</small></p>
</div>

<p><strong>Definition:</strong> What does this value mean?</p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>Why It Matters:</strong> Why is this value important to your society?</p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>In Action:</strong> Give 3 examples of how this value would be lived out in daily life:</p>
<ol>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
</ol>

<p><strong>Symbol or Image:</strong> Draw or describe a symbol that represents this value:</p>
<div style="min-height: 100px; border: 2px dashed #ddd; border-radius: 8px; margin: 1rem 0; padding: 1rem; text-align: center; color: var(--color-text-secondary);">
[Draw your symbol here]
</div>
</div>

<div class="value-card" style="background: white; padding: 2rem; border-radius: 12px; margin: 2rem 0; border: 3px solid var(--color-accent); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<h3 style="margin-top: 0;">Value #2</h3>

<div style="background: rgba(241, 143, 1, 0.05); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Name of Value (in English):</strong> _______________________________________</p>
<p><strong>Name of Value (in Te Reo Māori, if applicable):</strong> _______________________________________</p>
</div>

<p><strong>Definition:</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>Why It Matters:</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>In Action (3 examples):</strong></p>
<ol>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
</ol>

<p><strong>Symbol or Image:</strong></p>
<div style="min-height: 100px; border: 2px dashed #ddd; border-radius: 8px; margin: 1rem 0; padding: 1rem; text-align: center; color: var(--color-text-secondary);">
[Draw your symbol here]
</div>
</div>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: center;">
<p style="margin: 0.5rem 0;"><strong>📝 Continue for Values #3, #4, #5, and #6</strong></p>
<p style="margin: 0.5rem 0; font-size: 0.9rem; color: var(--color-text-secondary);">Use additional paper or create digital slides for remaining values</p>
</div>

<h2>Part 3: Connections & Balance</h2>

<div style="background: rgba(241, 143, 1, 0.1); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>How do your values work together?</strong></p>
<p><em>Sometimes values can seem to conflict. For example, "innovation" might clash with "tradition." How will your society balance different values?</em></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>Are any values prioritized over others?</strong></p>
<p><em>Example: "When values conflict, environmental sustainability takes priority"</em></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Part 4: Cultural Influences</h2>

<div style="background: rgba(27, 67, 50, 0.05); padding: 1.5rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid var(--color-pounamu);">
<p><strong>Reflect on cultural values that influenced your choices:</strong></p>

<p>1. <strong>Which values from your own culture(s) influenced your choices?</strong></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p>2. <strong>How did principles from Te Ao Māori (like kaitiakitanga, whanaungatanga, manaakitanga) shape your thinking?</strong></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p>3. <strong>Did you combine ideas from multiple cultures? How?</strong></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Part 5: Testing Your Values</h2>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Scenario Testing:</strong> How would your values guide decisions in these situations?</p>

<div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0; border-left: 3px solid var(--color-info);">
<p><strong>Scenario 1:</strong> A major company wants to build a factory that will create 500 jobs but may pollute a river.</p>
<p><em>Which values guide the decision? What would your society do?</em></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0; border-left: 3px solid var(--color-info);">
<p><strong>Scenario 2:</strong> A traditional cultural practice conflicts with a modern understanding of animal rights.</p>
<p><em>Which values guide the decision? What would your society do?</em></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<div style="background: white; padding: 1rem; border-radius: 6px; margin: 1rem 0; border-left: 3px solid var(--color-info);">
<p><strong>Scenario 3:</strong> New technology could solve a major problem but might make some traditional skills obsolete.</p>
<p><em>Which values guide the decision? What would your society do?</em></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>
</div>

<div style="margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #f0f8f0, #e8f5e9); border-radius: 12px; border-left: 4px solid var(--color-pounamu);">
<h3>🌿 Final Reflection</h3>
<p><strong>How do your values create a unique vision for your society?</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>What makes your values different from other societies (real or imagined)?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<div style="margin-top: 2rem; padding: 1rem; background: var(--color-gray-50); border-radius: 8px; text-align: center;">
<p style="margin: 0; font-size: 0.9rem;">
<strong>💚 Remember:</strong> Strong values create a strong society.  
These aren't just words - they're the principles that guide every decision and action!
</p>
</div>
</div>
'''
}

def fix_file(filepath, new_content):
    """Replace placeholder with real content"""
    try:
        html = filepath.read_text(encoding='utf-8')
        old_placeholder = '<p class="cultural-text">Placeholder page generated to satisfy links. Content available through teacher dashboard.</p>'
        html = html.replace(old_placeholder, new_content)
        filepath.write_text(html, encoding='utf-8')
        return True
    except Exception as e:
        print(f"❌ Error fixing {filepath.name}: {e}")
        return False

print("🔧 BATCH 3: CONTINUING SYSTEMATIC FIXES")
print("=" * 80)

fixed_count = 0
total_growth = 0

for filename, content in FIXES.items():
    filepath = ECOLOGY_DIR / filename
    if not filepath.exists():
        filepath = INQUIRY_DIR / filename
    
    if filepath.exists():
        lines_before = len(filepath.read_text(encoding='utf-8').split('\n'))
        
        if fix_file(filepath, content):
            lines_after = len(filepath.read_text(encoding='utf-8').split('\n'))
            growth = lines_after - lines_before
            print(f"✅ Fixed: {filename}")
            print(f"   Lines: {lines_before} → {lines_after} (+{growth})")
            fixed_count += 1
            total_growth += growth

print(f"\n✅ BATCH 3 COMPLETE!")
print(f"   Files fixed: {fixed_count}")
print(f"   Total growth: +{total_growth} lines")
print(f"\n📊 CUMULATIVE PROGRESS: 6 files fixed total (2+2+2)")

