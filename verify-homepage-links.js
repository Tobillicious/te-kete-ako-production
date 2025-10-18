#!/usr/bin/env node
/**
 * HOMEPAGE LINK VERIFICATION
 * Verify every link on the homepage actually works
 * Focus on QUALITY, not quantity
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';
const HOMEPAGE = path.join(PUBLIC_DIR, 'index.html');

const colors = {
  green: (text) => `\x1b[32m${text}\x1b[0m`,
  red: (text) => `\x1b[31m${text}\x1b[0m`,
  yellow: (text) => `\x1b[33m${text}\x1b[0m`,
  bold: (text) => `\x1b[1m${text}\x1b[0m`
};

console.log('\n' + '='.repeat(70));
console.log(colors.bold('✅ HOMEPAGE LINK VERIFICATION - QUALITY CHECK'));
console.log('='.repeat(70) + '\n');

const homepage = fs.readFileSync(HOMEPAGE, 'utf-8');

// Extract all href links from homepage
const linkMatches = homepage.matchAll(/href=["']([^"']+)["']/g);
const links = Array.from(linkMatches).map(match => match[1]);

// Filter to internal links only (not http/https or #anchors)
const internalLinks = links.filter(link => 
  !link.startsWith('http') && 
  !link.startsWith('#') &&
  !link.startsWith('mailto:') &&
  link !== '/'
);

console.log(`📊 Found ${internalLinks.length} internal links to verify\n`);

const results = {
  working: [],
  broken: [],
  warnings: []
};

// Check each link
internalLinks.forEach(link => {
  // Clean up link
  const cleanLink = link.startsWith('/') ? link.substring(1) : link;
  const filePath = path.join(PUBLIC_DIR, cleanLink);
  
  // For directory links, check for index.html
  let checkPath = filePath;
  if (link.endsWith('/')) {
    checkPath = path.join(filePath, 'index.html');
  }
  
  // Check if file exists
  if (fs.existsSync(checkPath)) {
    results.working.push({ link, path: checkPath });
    console.log(`  ${colors.green('✅')} ${link}`);
  } else if (fs.existsSync(filePath)) {
    // Directory exists but no index
    results.warnings.push({ link, path: filePath, issue: 'Directory but no index.html' });
    console.log(`  ${colors.yellow('⚠️ ')} ${link} - Directory exists but no index.html`);
  } else {
    results.broken.push({ link, path: checkPath });
    console.log(`  ${colors.red('❌')} ${link} - NOT FOUND`);
  }
});

// Summary
console.log('\n' + '='.repeat(70));
console.log(colors.bold('📊 VERIFICATION SUMMARY'));
console.log('='.repeat(70));

console.log(`\n${colors.green('✅ Working Links:')} ${results.working.length}`);
console.log(`${colors.yellow('⚠️  Warnings:')} ${results.warnings.length}`);
console.log(`${colors.red('❌ Broken Links:')} ${results.broken.length}`);

const totalChecked = results.working.length + results.warnings.length + results.broken.length;
const successRate = ((results.working.length / totalChecked) * 100).toFixed(1);

console.log(`\n${colors.bold('Success Rate:')} ${successRate}%`);

if (results.broken.length > 0) {
  console.log(`\n${colors.bold(colors.red('🚨 CRITICAL ISSUES TO FIX:'))}`);
  results.broken.forEach(({ link, path }) => {
    console.log(`  ❌ ${link}`);
    console.log(`     Expected: ${path}`);
  });
}

if (results.warnings.length > 0) {
  console.log(`\n${colors.bold(colors.yellow('⚠️  WARNINGS TO REVIEW:'))}`);
  results.warnings.forEach(({ link, issue }) => {
    console.log(`  ⚠️  ${link} - ${issue}`);
  });
}

// Write report
const report = {
  timestamp: new Date().toISOString(),
  totalLinks: totalChecked,
  working: results.working.length,
  warnings: results.warnings.length,
  broken: results.broken.length,
  successRate: parseFloat(successRate),
  brokenLinks: results.broken,
  warningLinks: results.warnings,
  readyForDemo: results.broken.length === 0
};

fs.writeFileSync('homepage-link-verification.json', JSON.stringify(report, null, 2));

console.log(`\n📄 Report saved: homepage-link-verification.json`);

if (results.broken.length === 0 && results.warnings.length === 0) {
  console.log(`\n${colors.green(colors.bold('🎉 HOMEPAGE IS READY FOR DEMO!'))} All links verified working!`);
} else if (results.broken.length === 0) {
  console.log(`\n${colors.yellow('✅ HOMEPAGE OK')} - Only minor warnings, no critical issues`);
} else {
  console.log(`\n${colors.red('🚨 FIX REQUIRED')} - ${results.broken.length} broken links must be fixed!`);
}

console.log('\n' + '='.repeat(70) + '\n');

process.exit(results.broken.length > 0 ? 1 : 0);

