#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Find all HTML files
const htmlFiles = glob.sync('public/**/*.html');

console.log(`🔧 Fixing Tailwind CDN in ${htmlFiles.length} files...`);

let fixedCount = 0;

htmlFiles.forEach(file => {
  try {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;
    
    // Replace Tailwind CDN with local build
    if (content.includes('https://cdn.tailwindcss.com')) {
      content = content.replace(
        /<script src="https:\/\/cdn\.tailwindcss\.com"><\/script>/g,
        '<link rel="stylesheet" href="/css/tailwind.css">'
      );
      
      // Remove tailwind config script if present
      content = content.replace(
        /<script src="\/tailwind\.config\.ultimate\.js"><\/script>/g,
        ''
      );
      
      modified = true;
    }
    
    if (modified) {
      fs.writeFileSync(file, content);
      fixedCount++;
      console.log(`✅ Fixed: ${file}`);
    }
  } catch (error) {
    console.error(`❌ Error fixing ${file}:`, error.message);
  }
});

console.log(`\n🎉 Fixed ${fixedCount} files!`);
console.log('📝 Next steps:');
console.log('1. Run: npm install');
console.log('2. Run: npm run build-css-prod');
console.log('3. Deploy the updated files');
