#!/usr/bin/env python3
"""
🔧 FIX Y9 ECOLOGY RESOURCES
Replace placeholder text with actual assessment rubrics and worksheets
"""

import re
from pathlib import Path

# Y9 Science Ecology Resources to fix
RESOURCES_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/units/y9-science-ecology/resources')

# Rubrics and templates with real content
FIXES = {
    'assessment-rubric-field-report.html': {
        'title': 'Assessment Rubric: Field Report',
        'content': '''
<div class="assessment-content">
<h2>📊 Field Report Assessment Rubric</h2>
<p><strong>Type:</strong> Summative Assessment | <strong>Curriculum Level:</strong> 4-5 (Years 9-10)</p>

<h3>🎯 Learning Objectives</h3>
<p>Students will demonstrate understanding of:</p>
<ul>
<li>Systematic observation and data collection in ecological fieldwork</li>
<li>Analysis of biodiversity indicators in local ecosystems</li>
<li>Application of scientific method to ecological investigation</li>
<li>Connection between kaitiakitanga principles and conservation practice</li>
</ul>

<h3>📝 Assessment Rubric</h3>
<table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Criteria</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Not Yet Achieved</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Achieved</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Merit</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 20%;">Excellence</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Data Collection</strong><br><small>Systematic observation and recording</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Some data collected but incomplete or disorganized</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Complete data collected using appropriate methods</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Thorough data collection with attention to accuracy and detail</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Comprehensive, precise data with additional environmental variables considered</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Analysis & Interpretation</strong><br><small>Making meaning from observations</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Basic description of findings</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Clear analysis identifying key patterns</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">In-depth analysis with justified conclusions</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Insightful analysis linking multiple variables with evidence-based reasoning</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Scientific Method</strong><br><small>Application of ecological investigation skills</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Limited use of scientific method</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Follows basic scientific method appropriately</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Systematic application with clear methodology explained</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Rigorous scientific approach with critical evaluation of method</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Kaitiakitanga Connection</strong><br><small>Integration of guardianship principles</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Minimal connection to kaitiakitanga</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Clear links between observations and kaitiakitanga principles</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Thoughtful integration showing deep understanding of guardianship</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Sophisticated application demonstrating holistic ecological thinking rooted in Te Ao Māori</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Presentation & Communication</strong><br><small>Clarity and professionalism</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Report is unclear or poorly organized</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Well-organized report with clear communication</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Professional presentation with effective use of scientific language</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Polished, engaging report that communicates complex ideas accessibly</td>
</tr>
</tbody>
</table>

<h3>💯 Marking Guide</h3>
<ul>
<li><strong>Not Yet Achieved:</strong> 0-7 points per criterion</li>
<li><strong>Achieved:</strong> 8-10 points per criterion</li>
<li><strong>Merit:</strong> 11-13 points per criterion</li>
<li><strong>Excellence:</strong> 14-15 points per criterion</li>
</ul>
<p><strong>Total:</strong> Out of 75 points (5 criteria × 15 points each)</p>

<h3>📁 Required Components</h3>
<ul>
<li>✅ Introduction describing the field site and investigation purpose</li>
<li>✅ Methodology section explaining data collection methods</li>
<li>✅ Data presentation (tables, graphs, photographs)</li>
<li>✅ Analysis and interpretation of findings</li>
<li>✅ Kaitiakitanga reflection: How does this connect to guardianship?</li>
<li>✅ Conclusions and recommendations</li>
<li>✅ References (if using external sources)</li>
</ul>

<h3>🌿 Cultural Integration</h3>
<p>Students should demonstrate understanding that:</p>
<ul>
<li>Ecological observation is part of mātauranga Māori traditions</li>
<li>Kaitiakitanga means active guardianship, not just observation</li>
<li>Local hapū/iwi have deep ecological knowledge of these systems</li>
<li>Conservation is both scientific and cultural responsibility</li>
</ul>

<h3>⏰ Time Allocation</h3>
<ul>
<li><strong>Field Visit:</strong> 2-3 hours (including travel)</li>
<li><strong>Data Analysis:</strong> 1 lesson (55 min)</li>
<li><strong>Report Writing:</strong> 2-3 lessons + homework</li>
<li><strong>Presentation:</strong> 1 lesson (if oral component)</li>
</ul>

<p style="margin-top: 2rem; padding: 1rem; background: rgba(27, 67, 50, 0.1); border-radius: 8px;">
<strong>🎯 Teacher Note:</strong> This rubric can be adapted for different curriculum levels. For Year 7-8, simplify criteria language and reduce required components. For Year 11+, add requirements for statistical analysis and deeper theoretical connections.
</p>
</div>
'''
    },
    
    'society-design-peer-review-form.html': {
        'title': 'Society Design Peer Review Form',
        'content': '''
<div class="worksheet-content">
<h2>👥 Society Design Peer Review Form</h2>
<p><strong>Purpose:</strong> Provide constructive feedback to help refine society designs using tuakana-teina principles</p>

<div class="review-header" style="background: var(--color-gray-50); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Reviewer Name:</strong> _________________________</p>
<p><strong>Designer(s) Being Reviewed:</strong> _________________________</p>
<p><strong>Society Name:</strong> _________________________</p>
<p><strong>Date:</strong> _________________________</p>
</div>

<h3>⭐ TWO STARS: What's Working Well</h3>
<p><em>Identify two strengths in the society design. Be specific!</em></p>

<div class="review-section" style="border: 2px solid var(--color-success); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Star 1:</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>Star 2:</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h3>💡 ONE WISH: Area for Growth</h3>
<p><em>Suggest one area that could be strengthened. Frame as "I wish..." or "Have you considered..."</em></p>

<div class="review-section" style="border: 2px solid var(--color-accent); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>My wish for this design:</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h3>🔍 Specific Criteria Review</h3>
<p><em>Rate each aspect on a scale of 1-5, and provide brief comments</em></p>

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Criterion</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd; width: 15%;">Rating (1-5)</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Comments/Suggestions</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Values Integration</strong><br><small>Are core values clear and meaningful?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Rights Protection</strong><br><small>Are rights comprehensive and protected?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Governance System</strong><br><small>Is decision-making clear and fair?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Sustainability</strong><br><small>Is environmental care integrated?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Cultural Respect</strong><br><small>Is diversity valued and protected?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Creativity & Originality</strong><br><small>Are ideas innovative and well-developed?</small></td>
<td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">___/5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
</tbody>
</table>

<p><strong>Total Rating:</strong> ____/30</p>

<h3>❓ Clarifying Questions</h3>
<p><em>What questions do you have about the design? What would you like to understand better?</em></p>

<div class="review-section" style="border: 2px solid var(--color-info); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<ol>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
<li style="margin-bottom: 1rem;">_______________________________________________________________</li>
</ol>
</div>

<h3>🌿 Tuakana-Teina Reflection</h3>
<p><em>How did you approach this review with manaakitanga (respect) and aroha (compassion)?</em></p>

<div class="review-section" style="border: 2px solid var(--color-pounamu); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<textarea style="width: 100%; min-height: 60px; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<div style="margin-top: 2rem; padding: 1rem; background: rgba(241, 143, 1, 0.1); border-radius: 8px; border-left: 4px solid var(--color-accent);">
<h4>🎯 Teacher Note</h4>
<p style="margin: 0.5rem 0; font-size: 0.9rem;">This peer review form supports:</p>
<ul style="margin: 0.5rem 0; font-size: 0.9rem;">
<li><strong>Ako:</strong> Reciprocal learning through giving and receiving feedback</li>
<li><strong>Tuakana-teina:</strong> Peer mentorship and collaborative improvement</li>
<li><strong>Manaakitanga:</strong> Respectful, supportive feedback practices</li>
<li><strong>Wānanga:</strong> Deep discussion about societal design principles</li>
</ul>
<p style="margin: 0.5rem 0 0; font-size: 0.85rem; font-style: italic;">Consider pairing students strategically - more experienced designers with those needing support, or complementary skill sets.</p>
</div>

<div style="margin-top: 1rem; padding: 0.75rem; background: var(--color-gray-50); border-radius: 8px;">
<p style="margin: 0; font-size: 0.85rem; text-align: center;">
<strong>Remember:</strong> The goal is to help each other create the best possible society designs!  
The feedback you give should be kind, specific, and helpful. 💚
</p>
</div>
</div>
'''
    }
}

def fix_placeholder(filepath, new_title, new_content):
    """Replace placeholder text with real content"""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        # Replace the placeholder paragraph
        old_placeholder = '<p class="cultural-text">Placeholder page generated to satisfy links. Content available through teacher dashboard.</p>'
        
        # Insert the new content after the </h1> tag in the cultural-section
        html = html.replace(old_placeholder, new_content)
        
        filepath.write_text(html, encoding='utf-8')
        return True
    except Exception as e:
        print(f"❌ Error fixing {filepath.name}: {e}")
        return False

# Fix the first two as proof of concept
print("🔧 FIXING Y9 ECOLOGY & GUIDED INQUIRY RESOURCES")
print("=" * 80)

fixed_count = 0

# Fix assessment rubric
rubric_file = RESOURCES_DIR / 'assessment-rubric-field-report.html'
if rubric_file.exists():
    if fix_placeholder(rubric_file, FIXES['assessment-rubric-field-report.html']['title'], 
                      FIXES['assessment-rubric-field-report.html']['content']):
        print(f"✅ Fixed: {rubric_file.name}")
        fixed_count += 1

# Fix peer review form
peer_review_file = Path('/Users/admin/Documents/te-kete-ako-clean/public/guided-inquiry-unit/materials/society-design-peer-review-form.html')
if peer_review_file.exists():
    if fix_placeholder(peer_review_file, FIXES['society-design-peer-review-form.html']['title'],
                      FIXES['society-design-peer-review-form.html']['content']):
        print(f"✅ Fixed: {peer_review_file.name}")
        fixed_count += 1

print(f"\n✅ Fixed {fixed_count} files!")
print("📊 These are now REAL, usable resources (not placeholders)")

