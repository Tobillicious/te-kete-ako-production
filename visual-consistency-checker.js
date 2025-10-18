#!/usr/bin/env node
/**
 * VISUAL CONSISTENCY CHECKER
 * Ensures professional, polished, consistent experience
 * Checks: Typography, Colors, Spacing, Components
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';

const colors = {
  green: (text) => `\x1b[32m${text}\x1b[0m`,
  red: (text) => `\x1b[31m${text}\x1b[0m`,
  yellow: (text) => `\x1b[33m${text}\x1b[0m`,
  blue: (text) => `\x1b[36m${text}\x1b[0m`,
  bold: (text) => `\x1b[1m${text}\x1b[0m`
};

console.log('\n' + '='.repeat(70));
console.log(colors.bold('🎨 VISUAL CONSISTENCY CHECK - PROFESSIONAL POLISH'));
console.log('='.repeat(70) + '\n');

const results = {
  typography: { issues: [], score: 0 },
  colors: { issues: [], score: 0 },
  spacing: { issues: [], score: 0 },
  components: { issues: [], score: 0 },
  cultural: { issues: [], score: 0 },
  mobile: { issues: [], score: 0 }
};

// Key pages to check
const keyPages = [
  'index.html',
  'generated-resources-alpha/index.html',
  'critical-thinking-unit.html',
  'login.html',
  'signup-student.html'
];

keyPages.forEach(page => {
  const filePath = path.join(PUBLIC_DIR, page);
  if (!fs.existsSync(filePath)) {
    console.log(`${colors.yellow('⚠️ ')} ${page} - Not found, skipping`);
    return;
  }
  
  const content = fs.readFileSync(filePath, 'utf-8');
  
  console.log(`${colors.blue('📄')} Checking: ${page}\n`);
  
  // 1. TYPOGRAPHY CONSISTENCY
  const headingSizes = content.match(/font-size:\s*(\d+(?:\.\d+)?(?:rem|px|em))/g) || [];
  const uniqueSizes = [...new Set(headingSizes)];
  if (uniqueSizes.length > 10) {
    results.typography.issues.push({
      page,
      issue: `Too many font sizes (${uniqueSizes.length})`,
      recommendation: 'Use consistent typography scale (6-8 sizes max)'
    });
    console.log(`  ${colors.yellow('⚠️ ')} Typography: ${uniqueSizes.length} different font sizes (should be 6-8)`);
  } else {
    console.log(`  ${colors.green('✅')} Typography: ${uniqueSizes.length} font sizes (good)`);
    results.typography.score++;
  }
  
  // 2. COLOR CONSISTENCY
  const hexColors = content.match(/#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b/g) || [];
  const rgbColors = content.match(/rgb\([^)]+\)/g) || [];
  const allColors = [...new Set([...hexColors, ...rgbColors])];
  if (allColors.length > 15) {
    results.colors.issues.push({
      page,
      issue: `Too many colors (${allColors.length})`,
      recommendation: 'Use design system with 8-12 colors max'
    });
    console.log(`  ${colors.yellow('⚠️ ')} Colors: ${allColors.length} different colors (should be 8-12)`);
  } else {
    console.log(`  ${colors.green('✅')} Colors: ${allColors.length} colors (good)`);
    results.colors.score++;
  }
  
  // 3. SPACING CONSISTENCY
  const hasVarSpacing = content.includes('--space-') || content.includes('var(--');
  if (!hasVarSpacing && content.length > 5000) {
    results.spacing.issues.push({
      page,
      issue: 'No CSS variables for spacing',
      recommendation: 'Use CSS variables for consistent spacing'
    });
    console.log(`  ${colors.yellow('⚠️ ')} Spacing: No CSS variables detected`);
  } else {
    console.log(`  ${colors.green('✅')} Spacing: Using CSS variables or inline consistent`);
    results.spacing.score++;
  }
  
  // 4. PROFESSIONAL COMPONENTS
  const hasNavigation = content.includes('navigation') || content.includes('<nav');
  const hasFooter = content.includes('<footer') || content.includes('footer');
  const hasBreadcrumbs = content.includes('breadcrumb');
  
  let componentScore = 0;
  if (hasNavigation) { console.log(`  ${colors.green('✅')} Navigation present`); componentScore++; }
  else { console.log(`  ${colors.red('❌')} Navigation missing`); }
  
  if (page !== 'login.html' && page !== 'signup-student.html') {
    if (hasBreadcrumbs) { console.log(`  ${colors.green('✅')} Breadcrumbs present`); componentScore++; }
    else { console.log(`  ${colors.yellow('⚠️ ')} Breadcrumbs missing`); }
  } else {
    componentScore++; // Auth pages don't need breadcrumbs
  }
  
  results.components.score += componentScore / 2;
  
  // 5. CULTURAL INTEGRATION
  const hasWhakatauaki = content.includes('Whakataukī') || content.includes('whakatauaki');
  const hasMaoriContent = content.includes('Māori') || content.includes('maori');
  const hasCulturalContext = content.includes('Cultural Context') || content.includes('Te Ao Māori');
  
  let culturalScore = 0;
  if (page.includes('generated-resources') || page.includes('unit') || page.includes('critical-thinking')) {
    if (hasWhakatauaki) { console.log(`  ${colors.green('✅')} Whakataukī integrated`); culturalScore++; }
    else { console.log(`  ${colors.yellow('⚠️ ')} Whakataukī missing`); }
    
    if (hasMaoriContent) { console.log(`  ${colors.green('✅')} Māori content present`); culturalScore++; }
    if (hasCulturalContext) { console.log(`  ${colors.green('✅')} Cultural context included`); culturalScore++; }
    
    results.cultural.score += culturalScore / 3;
  } else {
    console.log(`  ${colors.blue('ℹ️ ')} Cultural check N/A for this page type`);
    results.cultural.score += 1; // Don't penalize non-resource pages
  }
  
  // 6. MOBILE RESPONSIVENESS
  const hasViewport = content.includes('viewport');
  const hasMediaQueries = content.includes('@media') || content.includes('mobile-optimization.css');
  const hasResponsiveCSS = content.includes('mobile') || content.includes('responsive');
  
  let mobileScore = 0;
  if (hasViewport) { console.log(`  ${colors.green('✅')} Viewport meta tag`); mobileScore++; }
  else { console.log(`  ${colors.red('❌')} Viewport missing!`); }
  
  if (hasMediaQueries || hasResponsiveCSS) { 
    console.log(`  ${colors.green('✅')} Mobile optimization present`); 
    mobileScore++; 
  }
  
  results.mobile.score += mobileScore / 2;
  
  console.log('');
});

// Calculate overall scores
const categories = ['typography', 'colors', 'spacing', 'components', 'cultural', 'mobile'];
const totalPossible = keyPages.length * categories.length;
const totalScore = categories.reduce((sum, cat) => sum + results[cat].score, 0);
const overallScore = ((totalScore / totalPossible) * 100).toFixed(1);

// Summary
console.log('='.repeat(70));
console.log(colors.bold('📊 CONSISTENCY SCORECARD'));
console.log('='.repeat(70) + '\n');

categories.forEach(cat => {
  const score = results[cat].score;
  const max = keyPages.length;
  const percent = ((score / max) * 100).toFixed(0);
  const bar = '█'.repeat(Math.floor(percent / 10));
  const color = percent >= 80 ? colors.green : percent >= 60 ? colors.yellow : colors.red;
  
  console.log(`${cat.toUpperCase().padEnd(15)} ${color(bar.padEnd(10))} ${percent}%`);
});

console.log(`\n${colors.bold('OVERALL CONSISTENCY:')} ${overallScore >= 80 ? colors.green(overallScore + '%') : colors.yellow(overallScore + '%')}`);

// Recommendations
console.log(`\n${colors.bold('🎯 PRIORITY IMPROVEMENTS:')}\n`);

let priorities = [];

categories.forEach(cat => {
  const score = (results[cat].score / keyPages.length) * 100;
  if (score < 80) {
    priorities.push({ category: cat, score, issues: results[cat].issues });
  }
});

priorities.sort((a, b) => a.score - b.score);

if (priorities.length === 0) {
  console.log(colors.green('🎉 Excellent! All categories scoring above 80%'));
} else {
  priorities.forEach(({ category, score, issues }, index) => {
    console.log(`${index + 1}. ${colors.bold(category.toUpperCase())} (${score.toFixed(0)}%)`);
    if (issues.length > 0) {
      issues.forEach(issue => {
        console.log(`   ${colors.yellow('→')} ${issue.recommendation || issue.issue}`);
      });
    }
    console.log('');
  });
}

// Write report
const report = {
  timestamp: new Date().toISOString(),
  overallScore: parseFloat(overallScore),
  scores: {
    typography: (results.typography.score / keyPages.length) * 100,
    colors: (results.colors.score / keyPages.length) * 100,
    spacing: (results.spacing.score / keyPages.length) * 100,
    components: (results.components.score / keyPages.length) * 100,
    cultural: (results.cultural.score / keyPages.length) * 100,
    mobile: (results.mobile.score / keyPages.length) * 100
  },
  issues: results,
  recommendations: priorities,
  readyForDemo: overallScore >= 75
};

fs.writeFileSync('visual-consistency-report.json', JSON.stringify(report, null, 2));
console.log(`📄 Full report: visual-consistency-report.json`);

if (overallScore >= 80) {
  console.log(`\n${colors.green(colors.bold('✅ PROFESSIONAL POLISH ACHIEVED!'))}`);
} else if (overallScore >= 60) {
  console.log(`\n${colors.yellow(colors.bold('⚠️  GOOD BUT NEEDS POLISH'))}`);
} else {
  console.log(`\n${colors.red(colors.bold('🚨 SIGNIFICANT WORK NEEDED'))}`);
}

console.log('\n' + '='.repeat(70) + '\n');

process.exit(overallScore >= 60 ? 0 : 1);

