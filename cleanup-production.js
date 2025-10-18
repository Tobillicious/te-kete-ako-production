#!/usr/bin/env node
/**
 * CLEANUP PRODUCTION CODE
 * Remove debug console.log, fix href="#", optimize large files
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🧹 CLEANING UP PRODUCTION CODE');
console.log('='.repeat(70));

let filesFixed = 0;
let issuesFixed = {
    console_logs: 0,
    placeholder_links: 0,
    empty_alt: 0,
    double_spaces: 0
};

// Remove console.log from HTML files
console.log('\n1️⃣ Removing console.log debug code...\n');

const htmlFiles = execSync('find public -name "*.html" -type f', { encoding: 'utf8' })
    .trim()
    .split('\n')
    .filter(f => f && !f.includes('lighthouse-report'));

htmlFiles.forEach(file => {
    try {
        let content = fs.readFileSync(file, 'utf8');
        const originalContent = content;
        
        // Remove console.log/error/warn
        const consoleRegex = /console\.(log|error|warn|debug)\([^)]*\);?/g;
        const consoleMatches = content.match(consoleRegex);
        if (consoleMatches && consoleMatches.length > 0) {
            content = content.replace(consoleRegex, '');
            issuesFixed.console_logs += consoleMatches.length;
        }
        
        // Fix href="#" links (make them buttons instead or remove)
        const hrefHashRegex = /<a\s+href="#"([^>]*)onclick="([^"]+)"([^>]*)>([^<]+)<\/a>/g;
        const linkMatches = content.match(hrefHashRegex);
        if (linkMatches) {
            content = content.replace(hrefHashRegex, (match, before, onclick, after, text) => {
                issuesFixed.placeholder_links++;
                return `<button${before}onclick="${onclick}"${after} class="link-button">${text}</button>`;
            });
        }
        
        // Clean up double spaces
        const doubleSpaces = content.match(/  +/g);
        if (doubleSpaces) {
            content = content.replace(/  +/g, ' ');
            issuesFixed.double_spaces += doubleSpaces.length;
        }
        
        // Write back if changed
        if (content !== originalContent) {
            fs.writeFileSync(file, content, 'utf8');
            filesFixed++;
            console.log(`   ✅ ${path.basename(file)}`);
        }
        
    } catch (err) {
        console.log(`   ⚠️ ${file} - ${err.message}`);
    }
});

console.log(`\n✅ Fixed ${filesFixed} files`);
console.log(`   • Removed ${issuesFixed.console_logs} console.log statements`);
console.log(`   • Fixed ${issuesFixed.placeholder_links} href="#" links`);
console.log(`   • Cleaned ${issuesFixed.double_spaces} spacing issues`);

// Remove that giant lighthouse report
console.log('\n2️⃣ Removing bloat files...\n');
const bloatFiles = [
    'public/integrated-lessons/mathematics/lighthouse-report.html'
];

bloatFiles.forEach(file => {
    if (fs.existsSync(file)) {
        const stats = fs.statSync(file);
        const sizeMB = (stats.size / 1024 / 1024).toFixed(2);
        fs.unlinkSync(file);
        console.log(`   ✅ Removed ${file} (${sizeMB} MB)`);
    }
});

console.log('\n' + '='.repeat(70));
console.log('✅ PRODUCTION CLEANUP COMPLETE!');
console.log('='.repeat(70));
console.log(`\n📊 Summary:`);
console.log(`   Files processed: ${htmlFiles.length}`);
console.log(`   Files improved: ${filesFixed}`);
console.log(`   Total fixes: ${Object.values(issuesFixed).reduce((a, b) => a + b, 0)}`);
console.log('\n🚀 Production code is now cleaner and more professional!\n');

