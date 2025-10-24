#!/usr/bin/env node

/**
 * Batch Navigation Integration Script
 * Apply standard navigation to all HTML files missing it
 * Part of 5-agent coordinated development sprint
 */

const fs = require('fs');
const path = require('path');

// Navigation integration code to inject
const navigationIntegration = `
    <!-- NAVIGATION INTEGRATION -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/components/navigation-standard.html')
                .then(response => response.text())
                .then(html => {
                    document.body.insertAdjacentHTML('afterbegin', html);
                });
        });
    </script>`;

// Files that need navigation (identified in previous scan)
const filesToFix = [
    'public/unit-plans/kaitiaki-generated-y10-math-cultural-geometry.html',
    'public/ai-assistant.html',
    'public/intelligence-hub.html', 
    'public/massive-collection-hero.html',
    'public/guided-inquiry-unit/materials/cultural-values-framework-worksheet.html',
    'public/guided-inquiry-unit/materials/group-formation-strengths-inventory.html',
    'public/guided-inquiry-unit/materials/presentation-protocols-poster.html',
    'public/guided-inquiry-unit/materials/society-integration-summary.html',
    'public/guided-inquiry-unit/materials/society-exploration-gallery-walk-stations.html',
    'public/guided-inquiry-unit/materials/government-testing-scenarios.html'
];

function addNavigationToFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Skip if already has navigation integration
        if (content.includes('navigation-standard.html') || content.includes('NAVIGATION INTEGRATION')) {
            console.log(`⏭️  Skipping ${filePath} (already has navigation)`);
            return false;
        }
        
        // Find </head> tag and insert navigation code before it
        const headCloseIndex = content.indexOf('</head>');
        if (headCloseIndex === -1) {
            console.log(`⚠️  No </head> tag found in ${filePath}`);
            return false;
        }
        
        const beforeHead = content.substring(0, headCloseIndex);
        const afterHead = content.substring(headCloseIndex);
        
        const newContent = beforeHead + navigationIntegration + '\n' + afterHead;
        
        fs.writeFileSync(filePath, newContent, 'utf8');
        console.log(`✅ Added navigation to ${filePath}`);
        return true;
        
    } catch (error) {
        console.log(`❌ Error processing ${filePath}: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('🚀 BATCH NAVIGATION INTEGRATION - 5-Agent Sprint');
    console.log('=' * 60);
    
    let processed = 0;
    let succeeded = 0;
    let skipped = 0;
    
    filesToFix.forEach(filePath => {
        processed++;
        const result = addNavigationToFile(filePath);
        if (result === true) {
            succeeded++;
        } else if (result === false) {
            skipped++;
        }
    });
    
    console.log('\n' + '=' * 60);
    console.log('📊 BATCH RESULTS:');
    console.log('=' * 60);
    console.log(`✅ Successfully integrated: ${succeeded}`);
    console.log(`⏭️  Files skipped:         ${skipped}`);
    console.log(`📁 Total processed:       ${processed}`);
    console.log('=' * 60);
    
    if (succeeded > 0) {
        console.log('🎯 Navigation consistency improved! Coordinating with other agents...');
    }
    
    console.log('🚀 Phase 1 navigation fixes complete!');
}

if (require.main === module) {
    main();
}