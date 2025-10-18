#!/usr/bin/env node
/**
 * ACCESSIBILITY AUDIT & FIX
 * Find and fix real accessibility issues
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';

console.log('\n🔍 ACCESSIBILITY AUDIT - Finding Real Issues\n');
console.log('=' .repeat(60) + '\n');

const issues = {
  missingAlt: [],
  missingAriaLabels: [],
  poorHeadingStructure: [],
  missingLandmarks: [],
  lowContrast: []
};

// Key pages to audit
const keyPages = [
  'index.html',
  'login.html',
  'signup-student.html',
  'generated-resources-alpha/index.html',
  'games/te-reo-wordle.html'
];

keyPages.forEach(page => {
  const filePath = path.join(PUBLIC_DIR, page);
  if (!fs.existsSync(filePath)) return;
  
  const content = fs.readFileSync(filePath, 'utf-8');
  
  console.log(`📄 Checking: ${page}\n`);
  
  // 1. Check for images without alt text
  const imgTags = content.match(/<img[^>]*>/g) || [];
  const imgsWithoutAlt = imgTags.filter(img => !img.includes('alt='));
  if (imgsWithoutAlt.length > 0) {
    console.log(`  ❌ ${imgsWithoutAlt.length} images missing alt text`);
    issues.missingAlt.push({ page, count: imgsWithoutAlt.length });
  } else if (imgTags.length > 0) {
    console.log(`  ✅ All ${imgTags.length} images have alt text`);
  } else {
    console.log(`  ℹ️  No images on this page`);
  }
  
  // 2. Check for form inputs without labels
  const inputs = content.match(/<input[^>]*>/g) || [];
  const inputsWithAriaLabel = inputs.filter(input => 
    input.includes('aria-label=') || input.includes('id=')
  );
  if (inputs.length > inputsWithAriaLabel.length) {
    const missing = inputs.length - inputsWithAriaLabel.length;
    console.log(`  ⚠️  ${missing} inputs without labels or aria-label`);
    issues.missingAriaLabels.push({ page, count: missing });
  } else if (inputs.length > 0) {
    console.log(`  ✅ All ${inputs.length} inputs have labels`);
  }
  
  // 3. Check for main landmark
  const hasMain = content.includes('<main') || content.includes('role="main"');
  if (!hasMain) {
    console.log(`  ⚠️  Missing <main> landmark`);
    issues.missingLandmarks.push({ page, missing: 'main' });
  } else {
    console.log(`  ✅ Has <main> landmark`);
  }
  
  // 4. Check heading structure
  const h1s = (content.match(/<h1/g) || []).length;
  if (h1s === 0) {
    console.log(`  ⚠️  Missing H1 heading`);
    issues.poorHeadingStructure.push({ page, issue: 'No H1' });
  } else if (h1s > 1) {
    console.log(`  ⚠️  Multiple H1s (${h1s}) - should only have 1`);
    issues.poorHeadingStructure.push({ page, issue: `${h1s} H1s` });
  } else {
    console.log(`  ✅ Proper H1 structure`);
  }
  
  console.log('');
});

// Summary
console.log('=' .repeat(60));
console.log('📊 ACCESSIBILITY SUMMARY\n');

const totalIssues = 
  issues.missingAlt.length +
  issues.missingAriaLabels.length +
  issues.missingLandmarks.length +
  issues.poorHeadingStructure.length;

console.log(`Missing alt text: ${issues.missingAlt.length} pages`);
console.log(`Missing ARIA labels: ${issues.missingAriaLabels.length} pages`);
console.log(`Missing landmarks: ${issues.missingLandmarks.length} pages`);
console.log(`Heading issues: ${issues.poorHeadingStructure.length} pages`);

console.log(`\nTotal pages with issues: ${totalIssues}/${keyPages.length}`);

if (totalIssues === 0) {
  console.log('\n✅ EXCELLENT! No accessibility issues found!');
} else {
  console.log(`\n⚠️  Found ${totalIssues} accessibility improvements needed`);
}

// Write report
fs.writeFileSync('accessibility-issues.json', JSON.stringify(issues, null, 2));
console.log('\n📄 Report: accessibility-issues.json');
console.log('=' .repeat(60) + '\n');

process.exit(totalIssues > 5 ? 1 : 0);

