#!/usr/bin/env node
/**
 * TEST EVERY NAVIGATION LINK
 * No assumptions - actually check if every link works
 */

const fs = require('fs');
const path = require('path');

const navFile = 'public/components/navigation-standard.html';
const navContent = fs.readFileSync(navFile, 'utf-8');

// Extract all href links from navigation
const linkRegex = /href="([^"]+)"/g;
const links = [];
let match;

while ((match = linkRegex.exec(navContent)) !== null) {
  const href = match[1];
  // Skip external links, anchors, and mailto
  if (!href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto')) {
    links.push(href);
  }
}

console.log('🔍 TESTING EVERY NAVIGATION LINK');
console.log('═══════════════════════════════════════════════════════════════\n');
console.log(`Found ${links.length} internal links to test\n`);

const broken = [];
const working = [];
const warnings = [];

links.forEach((link, i) => {
  // Determine file path to check
  let filePath;
  
  if (link.startsWith('/')) {
    // Absolute path
    filePath = path.join('public', link);
    
    // If it's a directory link, check for index.html
    if (!link.endsWith('.html') && !link.endsWith('/')) {
      filePath = path.join('public', link, 'index.html');
    } else if (link.endsWith('/')) {
      filePath = path.join('public', link, 'index.html');
    }
  }
  
  // Check if file exists
  if (fs.existsSync(filePath)) {
    working.push({ link, path: filePath });
    console.log(`✅ ${link}`);
  } else {
    // Try directory
    const dirPath = path.join('public', link);
    if (fs.existsSync(dirPath) && fs.statSync(dirPath).isDirectory()) {
      const indexPath = path.join(dirPath, 'index.html');
      if (fs.existsSync(indexPath)) {
        working.push({ link, path: indexPath });
        console.log(`✅ ${link} (has index)`);
      } else {
        warnings.push({ link, reason: 'Directory exists but no index.html' });
        console.log(`⚠️  ${link} - Directory exists but NO INDEX`);
      }
    } else {
      broken.push({ link, expectedPath: filePath });
      console.log(`❌ ${link} - FILE NOT FOUND (expected: ${filePath})`);
    }
  }
});

console.log('\n═══════════════════════════════════════════════════════════════');
console.log('📊 NAVIGATION LINK TEST RESULTS\n');
console.log(`Total Links: ${links.length}`);
console.log(`✅ Working: ${working.length}`);
console.log(`⚠️  Warnings: ${warnings.length}`);
console.log(`❌ Broken: ${broken.length}`);

if (broken.length > 0) {
  console.log('\n❌ BROKEN LINKS TO FIX:');
  broken.forEach((item, i) => {
    console.log(`\n${i + 1}. ${item.link}`);
    console.log(`   Expected: ${item.expectedPath}`);
  });
}

if (warnings.length > 0) {
  console.log('\n⚠️  WARNINGS (directories need index.html):');
  warnings.forEach((item, i) => {
    console.log(`${i + 1}. ${item.link} - ${item.reason}`);
  });
}

// Save results
fs.writeFileSync('nav-link-test-results.json', JSON.stringify({
  total: links.length,
  working: working.length,
  warnings: warnings.length,
  broken: broken.length,
  brokenLinks: broken,
  warningLinks: warnings
}, null, 2));

console.log('\n💾 Results saved to: nav-link-test-results.json');

if (broken.length === 0 && warnings.length === 0) {
  console.log('\n✅ ALL NAVIGATION LINKS WORK!');
} else {
  console.log(`\n❌ NEED TO FIX: ${broken.length + warnings.length} issues`);
}

