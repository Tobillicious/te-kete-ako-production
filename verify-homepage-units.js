#!/usr/bin/env node
/**
 * Quick verification script for new homepage unit additions
 * Checks if all 5 new unit links point to existing pages
 */

const fs = require('fs');
const path = require('path');

const units = [
    {
        name: 'Guided Inquiry Unit',
        path: 'public/guided-inquiry-unit/guided-inquiry-society-design.html',
        alternates: ['public/guided-inquiry-unit/index.html']
    },
    {
        name: 'Critical Thinking Unit',
        path: 'public/critical-thinking-unit.html',
        alternates: ['public/critical-thinking/critical-thinking-toolkit.html']
    },
    {
        name: 'Writers Toolkit',
        path: 'public/writers-toolkit/index.html',
        alternates: ['public/lessons/writers-toolkit/index.html']
    },
    {
        name: 'Y8 Systems Unit',
        path: 'public/y8-systems/index.html',
        alternates: []
    },
    {
        name: 'Interactive Literacy Workbook',
        path: 'public/interactive-literacy/index.html',
        alternates: []
    }
];

console.log('\n🔍 VERIFYING HOMEPAGE UNIT LINKS\n');
console.log('='.repeat(60) + '\n');

let allGood = true;

units.forEach((unit, idx) => {
    const mainExists = fs.existsSync(unit.path);
    
    if (mainExists) {
        console.log(`✅ ${idx + 1}. ${unit.name}`);
        console.log(`   📄 ${unit.path}`);
        
        // Check file size
        const stats = fs.statSync(unit.path);
        console.log(`   📊 Size: ${(stats.size / 1024).toFixed(1)}KB`);
    } else {
        // Check alternates
        let foundAlternate = false;
        for (const alt of unit.alternates) {
            if (fs.existsSync(alt)) {
                console.log(`⚠️  ${idx + 1}. ${unit.name}`);
                console.log(`   ❌ Primary not found: ${unit.path}`);
                console.log(`   ✅ Found alternate: ${alt}`);
                foundAlternate = true;
                break;
            }
        }
        
        if (!foundAlternate) {
            console.log(`❌ ${idx + 1}. ${unit.name}`);
            console.log(`   ❌ NOT FOUND: ${unit.path}`);
            if (unit.alternates.length > 0) {
                console.log(`   ❌ No alternates found either`);
            }
            allGood = false;
        }
    }
    console.log('');
});

console.log('='.repeat(60));
if (allGood) {
    console.log('✅ ALL HOMEPAGE UNITS VERIFIED - Ready for demo!\n');
    process.exit(0);
} else {
    console.log('⚠️  SOME LINKS NEED ATTENTION - Check above for details\n');
    process.exit(1);
}

