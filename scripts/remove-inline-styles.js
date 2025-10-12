#!/usr/bin/env node
/**
 * Remove inline <style> blocks from HTML files
 * Let te-kete-professional.css handle all styling
 */

const fs = require('fs');
const path = require('path');

function removeInlineStyles(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Remove <style>...</style> blocks (including multi-line)
    content = content.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    
    // Clean up extra blank lines
    content = content.replace(/\n\n\n+/g, '\n\n');
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Cleaned: ${filePath}`);
}

// Get files from command line or stdin
const files = process.argv.slice(2);

if (files.length === 0) {
    console.error('Usage: node remove-inline-styles.js <file1> <file2> ...');
    process.exit(1);
}

files.forEach(removeInlineStyles);
console.log(`\n🎉 Cleaned ${files.length} files`);

