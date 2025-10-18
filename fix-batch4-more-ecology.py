#!/usr/bin/env python3
"""
🔧 BATCH 4: More Y9 Ecology Templates & Games
"""

from pathlib import Path

ECOLOGY_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public/units/y9-science-ecology/resources')

FIXES = {
    'kaitiakitanga-commitment-template.html': '''
<div class="worksheet-content">
<h1>🌿 Kaitiakitanga Commitment Template</h1>
<p><strong>Purpose:</strong> Make a personal commitment to act as a kaitiaki (guardian) of our environment</p>

<div class="intro" style="background: linear-gradient(135deg, #f0f8f0, #e8f5e9); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0; border-left: 4px solid var(--color-pounamu);">
<h3>What is Kaitiakitanga?</h3>
<p><strong>Kaitiakitanga</strong> is the Māori concept of guardianship and protection. A <strong>kaitiaki</strong> is a guardian - someone who takes responsibility for caring for and protecting the natural world.</p>

<p>This isn't just about conservation - it's about recognizing that:</p>
<ul>
<li>We are connected to and part of the natural world</li>
<li>We have a responsibility to protect it for future generations</li>
<li>Our actions have consequences for all living things</li>
<li>Caring for the environment is caring for ourselves and our whānau</li>
</ul>
</div>

<h2>My Kaitiakitanga Commitment</h2>

<div style="background: white; padding: 2rem; border-radius: 12px; border: 3px solid var(--color-pounamu); margin: 2rem 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">

<div style="background: rgba(27, 67, 50, 0.05); padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">
<p><strong>My Name:</strong> _______________________________________</p>
<p><strong>Date:</strong> _______________________________________</p>
<p><strong>Place:</strong> _______________________________________</p>
</div>

<h3>Part 1: Understanding My Connection</h3>

<p><strong>The ecosystem I am committing to protect:</strong></p>
<div style="background: var(--color-gray-50); padding: 1rem; border-radius: 6px; margin: 0.5rem 0;">
<label style="display: flex; align-items: center; margin: 0.5rem 0;">
<input type="checkbox" style="margin-right: 0.5rem;"> Local stream or river
</label>
<label style="display: flex; align-items: center; margin: 0.5rem 0;">
<input type="checkbox" style="margin-right: 0.5rem;"> Native forest or bush
</label>
<label style="display: flex; align-items: center; margin: 0.5rem 0;">
<input type="checkbox" style="margin-right: 0.5rem;"> Coastal area or beach
</label>
<label style="display: flex; align-items: center; margin: 0.5rem 0;">
<input type="checkbox" style="margin-right: 0.5rem;"> School grounds
</label>
<label style="display: flex; align-items: center; margin: 0.5rem 0;">
<input type="checkbox" style="margin-right: 0.5rem;"> Other: _______________________________
</label>
</div>

<p style="margin-top: 1rem;"><strong>Why this place matters to me:</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>Native species I want to protect:</strong> (List at least 3)</p>
<ol>
<li style="margin-bottom: 0.5rem;">__________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">__________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">__________________________________________________________</li>
</ol>

<h3 style="margin-top: 2rem;">Part 2: My Commitments</h3>

<p><em>Choose at least 3 specific actions you will take. Be realistic - small, consistent actions matter more than big promises you can't keep!</em></p>

<div style="background: rgba(27, 67, 50, 0.05); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<h4>Individual Actions (things I will do personally):</h4>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Reduce plastic use:</strong> I will bring reusable bags/containers and refuse single-use plastics</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Plant natives:</strong> I will plant at least ___ native plants this year</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Clean up:</strong> I will pick up rubbish when I see it, especially near waterways</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Support predator control:</strong> I will help with trapping or report predator sightings</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Educate others:</strong> I will share what I've learned about native species with friends and family</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Other:</strong> ___________________________________________________________</span>
</label>
</div>

<div style="background: rgba(241, 143, 1, 0.1); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<h4>Collective Actions (things I will do with others):</h4>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Join a group:</strong> I will participate in _____________________________ (conservation group)</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Organize events:</strong> I will help organize community clean-up or planting days</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Advocate:</strong> I will write to decision-makers about environmental issues</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Support whānau:</strong> I will encourage my family to make eco-friendly choices</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Other:</strong> ___________________________________________________________</span>
</label>
</div>

<h3 style="margin-top: 2rem;">Part 3: Making It Real</h3>

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">My Top 3 Actions</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">When I'll Start</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">How I'll Measure Success</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">1.</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">2.</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">3.</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
</tbody>
</table>

<p style="margin-top: 1.5rem;"><strong>Who will support me in these commitments?</strong></p>
<p style="font-size: 0.9rem; color: var(--color-text-secondary); margin: 0.5rem 0;">(Friends, whānau, teachers, community groups)</p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<h3 style="margin-top: 2rem;">Part 4: My Promise</h3>

<div style="background: rgba(27, 67, 50, 0.1); padding: 2rem; border-radius: 8px; border: 2px solid var(--color-pounamu); margin: 1.5rem 0;">
<p style="text-align: center; font-size: 1.1rem; line-height: 1.8; margin: 1rem 0;">
I, <strong>_______________________________</strong>, commit to being a kaitiaki.  
<br>I understand that small actions make a big difference.  
<br>I will protect and care for our natural world,  
<br>not just for myself, but for all living things  
<br>and for future generations.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
<div>
<p><strong>Signature:</strong></p>
<div style="border-bottom: 2px solid #333; margin-top: 3rem;"></div>
</div>
<div>
<p><strong>Date:</strong></p>
<div style="border-bottom: 2px solid #333; margin-top: 3rem;"></div>
</div>
</div>
</div>

<h3 style="margin-top: 2rem;">Part 5: Reflection (Complete after 3 months)</h3>

<p><strong>What have I achieved so far?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>What challenges have I faced?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p><strong>What will I do next?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

</div>

<div style="margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #fff7ed, #ffedd5); border-radius: 12px; border-left: 4px solid var(--color-accent);">
<h3>🎯 Teacher Notes</h3>
<ul style="font-size: 0.9rem;">
<li>Consider inviting local kaitiaki or conservation workers to share their experiences</li>
<li>Create a classroom display of commitments to build collective accountability</li>
<li>Schedule regular check-ins for students to share progress and challenges</li>
<li>Connect students with community groups for mentorship and support</li>
<li>Celebrate successes - even small actions deserve recognition!</li>
<li>Consider creating a school-wide kaitiakitanga challenge or competition</li>
</ul>
</div>
</div>
''',

    'field-report-template.html': '''
<div class="worksheet-content">
<h1>📊 Ecological Field Report Template</h1>
<p><strong>Purpose:</strong> Document your ecological fieldwork using systematic scientific methods</p>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
<h3>📋 Report Information</h3>
<p><strong>Student Name(s):</strong> __________________________________________________</p>
<p><strong>Date of Field Visit:</strong> __________________________________________________</p>
<p><strong>Location:</strong> __________________________________________________</p>
<p><strong>Weather Conditions:</strong> __________________________________________________</p>
<p><strong>Time of Day:</strong> __________________________________________________</p>
</div>

<h2>Section 1: Introduction & Background</h2>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<h3>1.1 Site Description</h3>
<p><strong>Describe the field site:</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="What does the area look like? What types of habitats are present? Any notable features?"></textarea>

<p style="margin-top: 1rem;"><strong>GPS Coordinates (if available):</strong> _____________________________</p>

<p style="margin-top: 1rem;"><strong>Ecosystem Type:</strong></p>
<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 0.5rem 0;">
<label><input type="checkbox"> Native forest</label>
<label><input type="checkbox"> Wetland</label>
<label><input type="checkbox"> Coastal</label>
<label><input type="checkbox"> Stream/River</label>
<label><input type="checkbox"> Modified/Urban</label>
<label><input type="checkbox"> Other: __________</label>
</div>

<h3 style="margin-top: 1.5rem;">1.2 Investigation Purpose</h3>
<p><strong>What question(s) are you investigating?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Example: What is the biodiversity of native birds in this forest patch?"></textarea>

<p style="margin-top: 1rem;"><strong>Why is this investigation important?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Section 2: Methodology</h2>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<h3>2.1 Data Collection Methods</h3>
<p><strong>Describe how you collected data:</strong></p>
<div style="margin: 1rem 0;">
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Visual observation:</strong> Details: _________________________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Transect sampling:</strong> Length: ______m, Number of transects: _______</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Quadrat sampling:</strong> Size: ______m², Number of quadrats: _______</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Pitfall traps:</strong> Number: _______, Duration: _______hours</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Water quality testing:</strong> Tests performed: _____________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Other:</strong> ________________________________________________________</span>
</label>
</div>

<h3 style="margin-top: 1.5rem;">2.2 Equipment Used</h3>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="List all equipment and measuring tools"></textarea>
</div>

<h2>Section 3: Results & Observations</h2>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<h3>3.1 Species Recorded</h3>
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<thead>
<tr style="background: var(--color-pounamu); color: white;">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Species Name (Te Reo & English)</th>
<th style="padding: 0.75rem; text-align: center; border: 1px solid #ddd;">Count/Abundance</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"></td>
</tr>
</tbody>
</table>

<p style="margin-top: 1rem;"><strong>Total species count:</strong> ___________</p>

<h3 style="margin-top: 1.5rem;">3.2 Environmental Data</h3>
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Temperature:</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">_________°C</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Humidity:</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">_________%</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Light Level:</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">_________lux (or description)</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Soil pH:</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">_________</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Water pH (if applicable):</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">_________</td>
</tr>
</table>

<h3 style="margin-top: 1.5rem;">3.3 Evidence of Threats</h3>
<div style="margin: 1rem 0;">
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Invasive species:</strong> Specify: _________________________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Predator signs:</strong> Specify: _________________________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Pollution:</strong> Type/Source: _________________________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Habitat damage:</strong> Description: _________________________________________</span>
</label>
<label style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
<input type="checkbox" style="margin-right: 0.5rem; margin-top: 0.25rem;">
<span><strong>Other:</strong> _________________________________________________________</span>
</label>
</div>

<h3 style="margin-top: 1.5rem;">3.4 Photographs & Sketches</h3>
<p><em>Attach photos or draw sketches of key observations. Include captions!</em></p>
<div style="min-height: 150px; border: 2px dashed #ddd; border-radius: 8px; margin: 1rem 0; padding: 1rem; text-align: center; color: var(--color-text-secondary);">
[Attach or draw observations here]
</div>
</div>

<h2>Section 4: Analysis & Interpretation</h2>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<p><strong>What patterns did you observe?</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>What might explain these patterns?</strong></p>
<textarea style="width: 100%; min-height: 100px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>How does this ecosystem compare to what it might have been like before human impact?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Section 5: Kaitiakitanga Reflection</h2>

<div style="background: rgba(27, 67, 50, 0.1); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--color-pounamu); margin: 1rem 0;">
<p><strong>What role does mātauranga Māori play in understanding this ecosystem?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;" placeholder="Consider traditional knowledge about this area, cultural significance of species, etc."></textarea>

<p style="margin-top: 1rem;"><strong>How can kaitiakitanga principles guide conservation of this area?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>

<p style="margin-top: 1rem;"><strong>Who are the current kaitiaki of this place? (Consider both formal conservation groups and local hapū/iwi)</strong></p>
<textarea style="width: 100%; min-height: 60px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Section 6: Conclusions & Recommendations</h2>

<div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin: 1rem 0;">
<h3>Key Findings</h3>
<ol>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
</ol>

<h3 style="margin-top: 1.5rem;">Recommendations for Conservation</h3>
<p><strong>What actions could help protect or improve this ecosystem?</strong></p>
<ol>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
</ol>

<h3 style="margin-top: 1.5rem;">Further Investigation</h3>
<p><strong>What questions remain? What would you like to study next?</strong></p>
<textarea style="width: 100%; min-height: 80px; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; font-family: inherit;"></textarea>
</div>

<h2>Section 7: References</h2>

<div style="background: var(--color-gray-50); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p><em>List all sources used (field guides, websites, experts consulted, etc.) in APA format:</em></p>
<ol>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
<li style="margin-bottom: 0.5rem;">_________________________________________________________________</li>
</ol>
</div>

<div style="margin-top: 2rem; padding: 1rem; background: rgba(241, 143, 1, 0.1); border-radius: 8px; border-left: 4px solid var(--color-accent);">
<h4>🎯 Teacher Tips</h4>
<ul style="font-size: 0.9rem;">
<li>Provide scaffolding for younger students - pre-fill some sections or create simpler versions</li>
<li>Consider digital submission with embedded photos vs paper-based</li>
<li>Invite experts to review student reports and provide feedback</li>
<li>Display exemplary reports to inspire future students</li>
<li>Connect findings to local conservation efforts - make it real!</li>
</ul>
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
        print(f"❌ Error: {e}")
        return False

print("🔧 BATCH 4: MORE Y9 ECOLOGY TEMPLATES")
print("=" * 80)

fixed = 0
growth = 0

for filename, content in FIXES.items():
    filepath = ECOLOGY_DIR / filename
    
    if filepath.exists():
        before = len(filepath.read_text(encoding='utf-8').split('\n'))
        
        if fix_file(filepath, content):
            after = len(filepath.read_text(encoding='utf-8').split('\n'))
            diff = after - before
            print(f"✅ {filename}")
            print(f"   {before} → {after} (+{diff} lines)")
            fixed += 1
            growth += diff

print(f"\n✅ BATCH 4 COMPLETE! {fixed} files, +{growth} lines")
print(f"📊 TOTAL SO FAR: 8 files transformed!")

