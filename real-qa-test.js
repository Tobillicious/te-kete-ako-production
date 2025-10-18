// REAL QA TESTING - Find actual problems

const fs = require('fs');
const path = require('path');

const issues = [];

// Test pages I just created
const newPages = [
  'public/units/lessons/index.html',
  'public/units/resources/index.html',
  'public/units/urds/index.html',
  'public/critical-thinking/index.html',
];

console.log('🔍 REAL QA TESTING - Finding Actual Problems\n');

newPages.forEach(page => {
  const content = fs.readFileSync(page, 'utf-8');
  
  console.log(`Testing: ${page}`);
  
  // Check for broken CSS links
  const cssLinks = content.match(/href="([^"]+\.css)"/g) || [];
  cssLinks.forEach(link => {
    const cssPath = link.match(/href="([^"]+)"/)[1];
    const fullPath = path.join('public', cssPath);
    if (!fs.existsSync(fullPath)) {
      console.log(`  ❌ BROKEN CSS: ${cssPath}`);
      issues.push(`${page}: Broken CSS link ${cssPath}`);
    }
  });
  
  // Check for broken internal links
  const htmlLinks = content.match(/href="([^"http][^"]+\.html)"/g) || [];
  htmlLinks.forEach(link => {
    const linkPath = link.match(/href="([^"]+)"/)[1];
    if (!linkPath.startsWith('#') && !linkPath.startsWith('http')) {
      const fullPath = linkPath.startsWith('/') ? 
        path.join('public', linkPath) :
        path.join(path.dirname(page), linkPath);
      if (!fs.existsSync(fullPath)) {
        console.log(`  ❌ BROKEN LINK: ${linkPath}`);
        issues.push(`${page}: Broken link ${linkPath}`);
      }
    }
  });
  
  // Check for missing footer
  if (!content.includes('footer')) {
    console.log(`  ⚠️  NO FOOTER`);
    issues.push(`${page}: Missing footer`);
  }
  
  // Check if navigation loads
  if (!content.includes('navigation-standard.html')) {
    console.log(`  ⚠️  NO NAVIGATION`);
    issues.push(`${page}: Missing navigation`);
  }
  
  console.log(`  ✅ Checked\n`);
});

console.log('\n═══════════════════════════════════════════════════');
console.log(`📊 FOUND ${issues.length} REAL ISSUES\n`);
issues.forEach((issue, i) => console.log(`${i+1}. ${issue}`));

if (issues.length === 0) {
  console.log('✅ No critical issues found!');
} else {
  console.log(`\n❌ Need to fix ${issues.length} issues before claiming success!`);
}

fs.writeFileSync('real-qa-results.json', JSON.stringify({issues}, null, 2));
