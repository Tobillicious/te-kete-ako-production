#!/usr/bin/env node
/**
 * Test script to verify all 50 AI-generated resources
 * Checks: file existence, CSS links, cultural context, accessibility basics
 */

const fs = require('fs');
const path = require('path');

const HANDOUTS_DIR = path.join(__dirname, 'public/generated-resources-alpha/handouts');
const LESSONS_DIR = path.join(__dirname, 'public/generated-resources-alpha/lessons');

const results = {
    total: 0,
    passed: 0,
    failed: 0,
    warnings: 0,
    details: []
};

function testFile(filePath, type) {
    const fileName = path.basename(filePath);
    const test = {
        file: fileName,
        type: type,
        exists: false,
        hasCSS: false,
        hasCulturalContext: false,
        hasWhakataukī: false,
        hasTitle: false,
        hasMetaDescription: false,
        hasBreadcrumbs: false,
        issues: []
    };
    
    try {
        // Check if file exists
        if (fs.existsSync(filePath)) {
            test.exists = true;
            const content = fs.readFileSync(filePath, 'utf8');
            
            // Check for CSS links (should have at least 3 canonical CSS files)
            const cssMatches = content.match(/href="\/css\//g);
            test.hasCSS = cssMatches && cssMatches.length >= 3;
            if (!test.hasCSS) {
                test.issues.push(`Only ${cssMatches ? cssMatches.length : 0} CSS files linked (expected ≥3)`);
            }
            
            // Check for cultural context section
            test.hasCulturalContext = content.includes('Cultural Context') || content.includes('Horopaki Ahurea');
            if (!test.hasCulturalContext) {
                test.issues.push('Missing Cultural Context section');
            }
            
            // Check for Whakataukī
            test.hasWhakataukī = /whakataukī|whakatauki/i.test(content);
            if (!test.hasWhakataukī) {
                test.issues.push('Missing Whakataukī');
            }
            
            // Check for proper title tag
            const titleMatch = content.match(/<title>(.*?)<\/title>/);
            test.hasTitle = titleMatch && titleMatch[1].length > 10;
            if (!test.hasTitle) {
                test.issues.push('Missing or inadequate title tag');
            }
            
            // Check for meta description
            test.hasMetaDescription = content.includes('name="description"');
            if (!test.hasMetaDescription) {
                test.issues.push('Missing meta description');
            }
            
            // Check for breadcrumb navigation
            test.hasBreadcrumbs = content.includes('breadcrumb') || content.includes('Home</a>');
            if (!test.hasBreadcrumbs) {
                test.issues.push('Missing breadcrumb navigation');
            }
            
            // Determine if test passed
            const passedChecks = [
                test.hasCSS,
                test.hasCulturalContext,
                test.hasTitle,
                test.hasMetaDescription
            ].filter(Boolean).length;
            
            if (passedChecks >= 3) {
                results.passed++;
            } else {
                results.failed++;
            }
            
            if (!test.hasWhakataukī || !test.hasBreadcrumbs) {
                results.warnings++;
            }
            
        } else {
            test.issues.push('File does not exist');
            results.failed++;
        }
    } catch (error) {
        test.issues.push(`Error reading file: ${error.message}`);
        results.failed++;
    }
    
    results.total++;
    results.details.push(test);
}

// Get all handouts
console.log('🔍 Testing AI-Generated Resources Integrity...\n');
console.log('=' .repeat(60));

const handouts = fs.readdirSync(HANDOUTS_DIR)
    .filter(f => f.endsWith('.html') && f !== 'index.html');
const lessons = fs.readdirSync(LESSONS_DIR)
    .filter(f => f.endsWith('.html') && f !== 'index.html');

console.log(`\n📄 Testing ${handouts.length} handouts...`);
handouts.forEach(file => {
    testFile(path.join(HANDOUTS_DIR, file), 'handout');
});

console.log(`\n🎓 Testing ${lessons.length} lessons...`);
lessons.forEach(file => {
    testFile(path.join(LESSONS_DIR, file), 'lesson');
});

// Generate report
console.log('\n' + '='.repeat(60));
console.log('📊 TEST RESULTS SUMMARY');
console.log('='.repeat(60));
console.log(`Total Resources Tested: ${results.total}`);
console.log(`✅ Passed: ${results.passed} (${((results.passed/results.total)*100).toFixed(1)}%)`);
console.log(`❌ Failed: ${results.failed} (${((results.failed/results.total)*100).toFixed(1)}%)`);
console.log(`⚠️  Warnings: ${results.warnings}`);

// Show failed/warned resources
const problematicResources = results.details.filter(d => d.issues.length > 0);
if (problematicResources.length > 0) {
    console.log('\n' + '='.repeat(60));
    console.log('⚠️  RESOURCES WITH ISSUES');
    console.log('='.repeat(60));
    problematicResources.forEach(resource => {
        console.log(`\n📄 ${resource.file} (${resource.type})`);
        resource.issues.forEach(issue => {
            console.log(`   ❌ ${issue}`);
        });
    });
}

// Show perfect resources
const perfectResources = results.details.filter(d => 
    d.exists && d.hasCSS && d.hasCulturalContext && d.hasWhakataukī && 
    d.hasTitle && d.hasMetaDescription && d.hasBreadcrumbs
);
console.log('\n' + '='.repeat(60));
console.log(`✨ PERFECT RESOURCES: ${perfectResources.length}/${results.total}`);
console.log('='.repeat(60));
if (perfectResources.length > 0) {
    console.log('Resources with all checks passed:');
    perfectResources.slice(0, 10).forEach(r => {
        console.log(`   ✅ ${r.file}`);
    });
    if (perfectResources.length > 10) {
        console.log(`   ... and ${perfectResources.length - 10} more`);
    }
}

// Write detailed JSON report
const reportPath = path.join(__dirname, 'resource-integrity-report.json');
fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
console.log(`\n📄 Detailed report written to: resource-integrity-report.json`);

// Exit with appropriate code
const exitCode = results.failed === 0 ? 0 : 1;
console.log(`\n${exitCode === 0 ? '✅ All tests passed!' : '❌ Some tests failed.'}`);
process.exit(exitCode);

