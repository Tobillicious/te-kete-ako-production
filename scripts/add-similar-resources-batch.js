#!/usr/bin/env node

/**
 * Batch Add Similar Resources Component
 * Adds the GraphRAG Similar Resources component to top 50 gold standard lessons
 */

const fs = require('fs');
const path = require('path');

// Top 50 gold standard lesson paths from GraphRAG query
const lessonPaths = [
  "public/lessons/career-pathways-in-stem-for-māori-students.html",
  "public/lessons/argumentative-writing-on-contemporary-māori-issues.html",
  "public/lessons/creative-writing-inspired-by-whakataukī.html",
  "/public/units/y9-maths-geometry-patterns/lessons/lesson-8-final-project.html",
  "public/units/y7-maths-algebra/lessons/lesson-3-equations.html",
  "/public/critical-thinking/lessons/lesson-3-evaluating-sources.html",
  "/public/units/y7-science-ecosystems/lessons/lesson-4-ecosystem-balance.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-1-introduction-to-digital-kaitiakitanga.html",
  "/units/y8-digital-kaitiakitanga/lessons/lesson-4-body-as-sensor.html",
  "/public/units/y7-science-ecosystems/lessons/lesson-2-food-webs-energy-flow.html",
  "public/units/y7-science-ecosystems/lessons/lesson-1-intro-ecosystems.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-2-online-safety-cultural-values.html",
  "public/units/y7-maths-algebra/lessons/lesson-1-intro-to-algebra.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-15-portfolio-assessment.html",
  "/public/units/y10-physics-navigation/lessons/lesson-1.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-12-digital-rights.html",
  "/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html",
  "public/units/y7-science-ecosystems/lessons/lesson-3-conservation.html",
  "/public/units/y7-science-ecosystems/lessons/lesson-3-human-impact-conservation.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-11-ethical-tech.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-3-digital-citizenship.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-5-cyberbullying-prevention.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-14-storytelling-project.html",
  "/public/units/y9-maths-geometry-patterns/lessons/lesson-2-tessellations-tukutuku.html",
  "/public/units/y8-digital-kaitiakitanga/lessons/lesson-19-reflection.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-10-critical-thinking.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-13-online-communities.html",
  "public/lessons/research-skills-using-traditional-and-digital-sources.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-9-information-literacy.html",
  "/public/units/y7-science-ecosystems/lessons/lesson-3-food-chains-webs.html",
  "public/units/y8-digital-kaitiakitanga/lessons/lesson-4-social-media-identity.html",
  "/public/units/y7-science-ecosystems/lessons/lesson-1-what-makes-an-ecosystem.html",
  "/public/units/y8-digital-kaitiakitanga/lessons/lesson-20-celebration.html",
  "public/units/y7-maths-algebra/lessons/lesson-2-variables-expressions.html",
  "/public/guided-inquiry-unit/lessons/lesson-2-research-design.html",
  "public/units/y7-maths-algebra/lessons/lesson-5-problem-solving.html",
  "public/lessons/media-literacy-analyzing-māori-representation.html",
  "/units/unit-1-te-ao-maori/lessons/career-pathways-in-stem-for-māori-students.html",
  "public/units/y7-maths-algebra/lessons/lesson-4-patterns.html",
  "public/lessons/digital-storytelling-with-pūrākau-framework.html",
  "/units/unit-1-te-ao-maori/lessons/media-literacy-analyzing-māori-representation.html",
  "public/lessons/genetics-and-whakapapa-scientific-and-cultural-perspectives.html",
  "public/lessons/renewable-energy-and-māori-innovation.html",
  "public/lessons/climate-change-through-te-taiao-māori-lens.html",
  "/units/unit-1-te-ao-maori/lessons/scientific-method-using-traditional-māori-practices.html",
  "/public/units/unit-1-te-ao-maori/lessons/lesson-6-te-reo-basics.html",
  "public/lessons/poetry-analysis-through-māori-literary-traditions.html",
  "dist/generated-resources-alpha/lessons/climate-change-through-te-taiao-māori-lens.html",
  "public/lessons/debate-skills-with-māori-oratory-traditions.html",
  "/public/units/y9-maths-geometry-patterns/lessons/lesson-3-rotational-symmetry.html"
];

// Similar Resources component HTML
const similarResourcesHTML = `

<!-- 🔗 GraphRAG Similar Resources Component -->
<div id="similar-resources" data-resource-path="FILE_PATH_PLACEHOLDER"></div>
<script src="/components/graphrag-similar-resources.html"></script>`;

let successCount = 0;
let skipCount = 0;
let errorCount = 0;
const results = [];

console.log('🚀 Starting batch addition of Similar Resources component...\n');

lessonPaths.forEach((lessonPath, index) => {
  // Clean path - remove leading slash and resolve relative paths
  let cleanPath = lessonPath.replace(/^\//, '');
  if (!cleanPath.startsWith('public/') && !cleanPath.startsWith('dist/')) {
    cleanPath = 'public/' + cleanPath;
  }
  
  const fullPath = path.join('/Users/admin/Documents/te-kete-ako-clean', cleanPath);
  
  try {
    // Check if file exists
    if (!fs.existsSync(fullPath)) {
      console.log(`⚠️  [${index + 1}/50] SKIP: File not found: ${cleanPath}`);
      skipCount++;
      results.push({ path: cleanPath, status: 'skipped', reason: 'File not found' });
      return;
    }
    
    // Read file
    let content = fs.readFileSync(fullPath, 'utf8');
    
    // Check if already has Similar Resources
    if (content.includes('graphrag-similar-resources') || content.includes('id="similar-resources"')) {
      console.log(`✓ [${index + 1}/50] Already has component: ${cleanPath}`);
      skipCount++;
      results.push({ path: cleanPath, status: 'skipped', reason: 'Already has component' });
      return;
    }
    
    // Find the closing </body> tag
    const bodyCloseIndex = content.lastIndexOf('</body>');
    
    if (bodyCloseIndex === -1) {
      console.log(`⚠️  [${index + 1}/50] SKIP: No </body> tag found: ${cleanPath}`);
      skipCount++;
      results.push({ path: cleanPath, status: 'skipped', reason: 'No closing body tag' });
      return;
    }
    
    // Insert component before </body>
    const componentHTML = similarResourcesHTML.replace('FILE_PATH_PLACEHOLDER', '/' + cleanPath);
    const newContent = content.slice(0, bodyCloseIndex) + componentHTML + '\n' + content.slice(bodyCloseIndex);
    
    // Write updated content
    fs.writeFileSync(fullPath, newContent, 'utf8');
    
    console.log(`✅ [${index + 1}/50] SUCCESS: Added component to ${cleanPath}`);
    successCount++;
    results.push({ path: cleanPath, status: 'success' });
    
  } catch (error) {
    console.log(`❌ [${index + 1}/50] ERROR: ${cleanPath} - ${error.message}`);
    errorCount++;
    results.push({ path: cleanPath, status: 'error', reason: error.message });
  }
});

// Summary
console.log('\n' + '='.repeat(60));
console.log('📊 BATCH ADDITION SUMMARY');
console.log('='.repeat(60));
console.log(`✅ Success: ${successCount} lessons`);
console.log(`⚠️  Skipped: ${skipCount} lessons`);
console.log(`❌ Errors: ${errorCount} lessons`);
console.log(`📝 Total: ${lessonPaths.length} lessons processed`);
console.log('='.repeat(60) + '\n');

// Save detailed results
const resultsPath = '/Users/admin/Documents/te-kete-ako-clean/SIMILAR-RESOURCES-BATCH-RESULTS.json';
fs.writeFileSync(resultsPath, JSON.stringify(results, null, 2), 'utf8');
console.log(`📄 Detailed results saved to: SIMILAR-RESOURCES-BATCH-RESULTS.json\n`);

// Exit with appropriate code
process.exit(errorCount > 0 ? 1 : 0);

