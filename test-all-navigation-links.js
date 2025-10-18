#!/usr/bin/env node
/**
 * TEST ALL NAVIGATION LINKS
 * Verifies every unit link we added today actually works
 * Run: node test-all-navigation-links.js
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = path.join(__dirname, 'public');

// All units we added to navigation today
const UNITS_TO_TEST = [
  // Complete Curriculum (Units 1-7)
  { name: 'Unit 1: Te Ao Māori', path: '/units/unit-1-te-ao-maori.html' },
  { name: 'Unit 2: Decolonized History', path: '/units/unit-2-decolonized-history.html' },
  { name: 'Unit 3: STEM & Mātauranga', path: '/units/unit-3-stem-matauranga.html' },
  { name: 'Unit 4: Economic Justice', path: '/units/unit-4-economic-justice.html' },
  { name: 'Unit 5: Global Connections', path: '/units/unit-5-global-connections.html' },
  { name: 'Unit 6: Future Rangatiratanga', path: '/units/unit-6-future-rangatiratanga.html' },
  { name: 'Unit 7: Digital Tech & AI', path: '/units/unit-7-digital-tech-ai-ethics.html' },
  
  // Cross-Curricular
  { name: 'Math-Science Toolkit', path: '/lessons/mathematics-science-interactive-toolkit/index.html' },
  { name: 'Mathematics & Māori Games', path: '/units/mathematics-maori-games/index.html' },
  { name: 'Walker Unit', path: '/units/walker-unit/index.html' },
  { name: 'Hērangi Unit', path: '/lessons/herangi/index.html' },
  { name: 'Unit 1 Te Ao Māori (alt)', path: '/units/unit-1-te-ao-maori/index.html' },
  
  // Year 7
  { name: 'Y7 Algebra', path: '/units/y7-maths-algebra/index.html' },
  { name: 'Y7 Science Ecosystems', path: '/units/y7-science-ecosystems/index.html' },
  { name: 'Y7 Digital Tech', path: '/units/y7-digital-technology/index.html' },
  { name: 'Y7 Reading', path: '/units/y7-foundational-reading/index.html' },
  
  // Year 8
  { name: 'Y8 Statistics', path: '/units/y8-statistics/index.html' },
  { name: 'Y8 Digital Kaitiakitanga', path: '/units/y8-digital-kaitiakitanga/index.html' },
  { name: 'Y8 Critical Thinking', path: '/units/y8-critical-thinking/index.html' },
  
  // Year 9-10
  { name: 'Y9 Geometry Patterns', path: '/units/y9-mathematics-geometry-maori-patterns/index.html' },
  { name: 'Y9 Science Ecology', path: '/units/y9-science-ecology/index.html' },
  { name: 'Y10 Physics Forces', path: '/units/y10-physics-forces/index.html' },
  { name: 'Y10 Physics Navigation', path: '/units/y10-physics-navigation/index.html' },
];

console.log('🔍 TESTING ALL NAVIGATION LINKS');
console.log('=' + '='.repeat(59));
console.log(`\nTotal units to test: ${UNITS_TO_TEST.length}\n`);

const results = {
  passed: [],
  failed: [],
  warnings: []
};

// Test each unit
UNITS_TO_TEST.forEach((unit, index) => {
  const filePath = path.join(PUBLIC_DIR, unit.path.replace(/^\//, ''));
  const exists = fs.existsSync(filePath);
  
  console.log(`${index + 1}. ${unit.name}`);
  console.log(`   Path: ${unit.path}`);
  
  if (exists) {
    // File exists - check contents
    const content = fs.readFileSync(filePath, 'utf-8');
    
    const checks = {
      hasTitle: /<title>(.+?)<\/title>/i.test(content),
      hasMainTag: /<main/i.test(content),
      hasCulturalContext: /cultural context|horopaki ahurea|whakataukī|whakatauaki/i.test(content),
      hasCSS: /te-kete-unified-design-system\.css|te-kete-professional\.css/i.test(content),
      hasNavigation: /navigation-standard\.html|navigation-mega-menu/i.test(content),
      notTooSmall: content.length > 1000, // At least 1KB
      noTemplatePlaceholders: !/{UNIT_TITLE}|{LESSON_|{TODO}/i.test(content)
    };
    
    const passed = Object.values(checks).every(v => v);
    
    if (passed) {
      console.log(`   ✅ PASS - All checks passed`);
      results.passed.push(unit);
    } else {
      console.log(`   ⚠️  ISSUES FOUND:`);
      if (!checks.hasTitle) console.log(`      - Missing <title> tag`);
      if (!checks.hasMainTag) console.log(`      - Missing <main> tag`);
      if (!checks.hasCulturalContext) console.log(`      - Missing cultural context`);
      if (!checks.hasCSS) console.log(`      - Missing professional CSS`);
      if (!checks.hasNavigation) console.log(`      - Missing navigation component`);
      if (!checks.notTooSmall) console.log(`      - File suspiciously small (${content.length} bytes)`);
      if (!checks.noTemplatePlaceholders) console.log(`      - Contains template placeholders!`);
      
      results.warnings.push({ ...unit, issues: checks });
    }
  } else {
    console.log(`   ❌ FAIL - File does not exist!`);
    results.failed.push(unit);
  }
  console.log('');
});

// Summary
console.log('=' + '='.repeat(59));
console.log('\n📊 TEST SUMMARY\n');
console.log(`✅ PASSED:  ${results.passed.length} units (${((results.passed.length / UNITS_TO_TEST.length) * 100).toFixed(1)}%)`);
console.log(`⚠️  WARNINGS: ${results.warnings.length} units (${((results.warnings.length / UNITS_TO_TEST.length) * 100).toFixed(1)}%)`);
console.log(`❌ FAILED:  ${results.failed.length} units (${((results.failed.length / UNITS_TO_TEST.length) * 100).toFixed(1)}%)`);

// Failed units
if (results.failed.length > 0) {
  console.log('\n🚨 BROKEN LINKS (Remove from navigation!):\n');
  results.failed.forEach(unit => {
    console.log(`   ❌ ${unit.name}`);
    console.log(`      Path: ${unit.path}`);
  });
}

// Warning units
if (results.warnings.length > 0) {
  console.log('\n⚠️  UNITS NEEDING FIXES:\n');
  results.warnings.forEach(unit => {
    console.log(`   ⚠️  ${unit.name} - Needs polish`);
  });
}

// Success units
console.log('\n✅ VERIFIED EXCELLENT UNITS:\n');
results.passed.forEach(unit => {
  console.log(`   ✅ ${unit.name}`);
});

// Save results
fs.writeFileSync('navigation-link-test-results.json', JSON.stringify(results, null, 2));
console.log('\n✅ Detailed results saved to: navigation-link-test-results.json\n');

// Recommendations
console.log('📋 RECOMMENDATIONS:\n');
if (results.failed.length > 0) {
  console.log(`   🔴 HIGH PRIORITY: Remove ${results.failed.length} broken units from navigation`);
}
if (results.warnings.length > 0) {
  console.log(`   🟡 MEDIUM PRIORITY: Polish ${results.warnings.length} units with issues`);
}
if (results.passed.length >= 10) {
  console.log(`   ✅ EXCELLENT: ${results.passed.length} units ready for users!`);
}

console.log('\n' + '=' + '='.repeat(59) + '\n');

