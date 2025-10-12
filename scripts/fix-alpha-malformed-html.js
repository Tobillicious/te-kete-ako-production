#!/usr/bin/env node
/**
 * Agent 3: Fix malformed HTML in alpha handouts
 * Problem: <style> opening tag is MISSING, causing orphaned CSS code
 * Solution: Add missing <style> tag, then remove entire style block
 */

const fs = require('fs');
const path = require('path');

const alphaDir = './public/generated-resources-alpha/handouts';

console.log('🔧 Agent 3: Fixing malformed HTML in alpha handouts...\n');

function fixMalformedHTML(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let fixed = false;
    
    // Pattern: CSS code starting right after </title> without <style> tag
    // Look for: </title>\n    <link rel="stylesheet" href="/css/te-kete-professional.css">\n    <link rel="stylesheet" href="/css/print.css" media="print">\n            margin: 20px 0;
    const malformedPattern = /(\/css\/print\.css"[^>]*>\s*\n)(\s+)(margin:|\.[\w-]+\s*{|table\s*{)/;
    
    if (malformedPattern.test(content)) {
        console.log(`❌ MALFORMED: ${path.basename(filePath)}`);
        
        // Add missing <style> tag
        content = content.replace(malformedPattern, '$1$2<style>\n$2$3');
        
        // Now remove the entire style block (including the one we just added)
        content = content.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
        
        // Clean up extra blank lines
        content = content.replace(/\n\n\n+/g, '\n\n');
        
        // Ensure proper head closing
        if (!content.includes('</head>')) {
            content = content.replace(/(<link[^>]*>\s*\n)(\s*<body>)/, '$1</head>\n$2');
        }
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ FIXED: ${path.basename(filePath)}`);
        fixed = true;
    }
    
    return fixed;
}

// Process all HTML files in alpha handouts
const files = fs.readdirSync(alphaDir)
    .filter(f => f.endsWith('.html'))
    .map(f => path.join(alphaDir, f));

let fixedCount = 0;

for (const file of files) {
    if (fixMalformedHTML(file)) {
        fixedCount++;
    }
}

console.log(`\n📊 Results:`);
console.log(`   Checked ${files.length} files`);
console.log(`   Fixed ${fixedCount} malformed files`);
console.log(`   ✅ All alpha handouts should now have clean HTML structure!`);

