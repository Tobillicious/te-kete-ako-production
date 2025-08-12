// Te Kete Ako - Fix CSS Head Corruption Script
// Repairs malformed CSS link tags with excessive spacing

const fs = require('fs');
const path = require('path');
const { glob } = require('fast-glob');

async function fixCSSCorruption() {
    console.log('🔧 KAITIAKI ARONUI: Fixing CSS Head Corruption...');
    
    const files = await glob('public/**/*.html', {
        ignore: ['**/node_modules/**', '**/backups/**']
    });
    
    let filesFixed = 0;
    let totalFixes = 0;
    
    // Standard head template with clean CSS includes
    const standardCSSIncludes = `    <link rel="stylesheet" href="/css/design-system-v3.css"/>
    <link rel="stylesheet" href="/css/award-winning-polish.css"/>
    <link rel="stylesheet" href="/css/print.css" media="print"/>
    <script src="/js/breadcrumbs.js" defer></script>`;

    for (const file of files) {
        try {
            let content = fs.readFileSync(file, 'utf8');
            let modified = false;
            let fileFixes = 0;
            
            // Fix corrupted CSS includes with excessive spacing
            const corruptedPatterns = [
                // Match any line with excessive spacing before CSS links
                /^[ ]{20,}<link rel="stylesheet".*$/gm,
                /^[ ]{20,}<script src="\/js\/breadcrumbs\.js".*$/gm,
                // Match patterns where spacing got corrupted
                /[ ]{10,}<link rel="stylesheet" href="\/css\/design-system-v3\.css"\/>/g,
                /[ ]{10,}<link rel="stylesheet" href="\/css\/award-winning-polish\.css"\/>/g,
                /[ ]{10,}<link rel="stylesheet" href="\/css\/print\.css" media="print"\/>/g,
                /[ ]{10,}<script src="\/js\/breadcrumbs\.js" defer><\/script>/g
            ];
            
            // Remove all corrupted CSS includes first
            for (const pattern of corruptedPatterns) {
                if (content.match(pattern)) {
                    content = content.replace(pattern, '');
                    modified = true;
                    fileFixes++;
                    totalFixes++;
                }
            }
            
            // Find the </head> tag and insert clean CSS includes before it
            if (content.includes('</head>') && !content.includes('design-system-v3.css')) {
                content = content.replace(
                    '</head>',
                    standardCSSIncludes + '\n</head>'
                );
                modified = true;
                fileFixes++;
                totalFixes++;
            }
            
            // Clean up any remaining excessive whitespace in head
            content = content.replace(/(<head[^>]*>[\s\S]*?)<\/head>/gi, function(match) {
                // Clean up excessive spacing in head section only
                return match.replace(/\n[ ]{20,}/g, '\n    ');
            });
            
            // Fix double/triple link inclusions if they exist
            const cssLinkPattern = /<link rel="stylesheet" href="\/css\/design-system-v3\.css"\/>/g;
            const matches = content.match(cssLinkPattern);
            if (matches && matches.length > 1) {
                // Keep only the first occurrence
                let firstFound = false;
                content = content.replace(cssLinkPattern, function(match) {
                    if (!firstFound) {
                        firstFound = true;
                        return match;
                    }
                    return '';
                });
                modified = true;
                fileFixes += matches.length - 1;
                totalFixes += matches.length - 1;
            }
            
            if (modified) {
                fs.writeFileSync(file, content, 'utf8');
                filesFixed++;
                const relativePath = path.relative('public', file);
                console.log(`✅ Fixed ${fileFixes} CSS issues in ${relativePath}`);
            }
            
        } catch (error) {
            console.error(`❌ Error processing ${file}:`, error.message);
        }
    }
    
    console.log(`\n🎉 CSS Head Corruption Fix Complete!`);
    console.log(`📊 Files scanned: ${files.length}`);
    console.log(`🔧 Files repaired: ${filesFixed}`);
    console.log(`🔗 Total fixes applied: ${totalFixes}`);
    
    // Verify the fixes by checking a few key files
    console.log(`\n🔍 Verification check...`);
    const keyFiles = ['public/handouts.html', 'public/lessons.html', 'public/unit-plans.html'];
    
    for (const file of keyFiles) {
        if (fs.existsSync(file)) {
            const content = fs.readFileSync(file, 'utf8');
            const hasDesignSystem = content.includes('design-system-v3.css');
            const hasExcessiveSpacing = /[ ]{20,}<link/.test(content);
            
            const status = hasDesignSystem && !hasExcessiveSpacing ? '✅' : '❌';
            console.log(`${status} ${path.basename(file)}: CSS=${hasDesignSystem}, Clean=${!hasExcessiveSpacing}`);
        }
    }
    
    return { filesScanned: files.length, filesFixed, totalFixes };
}

if (require.main === module) {
    fixCSSCorruption().catch(console.error);
}

module.exports = { fixCSSCorruption };