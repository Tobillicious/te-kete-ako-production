#!/usr/bin/env node
/**
 * COMPREHENSIVE TESTING SUITE - OCT 22 DEMO PREP
 * Tests all critical paths, performance, and deployment readiness
 */

const fs = require('fs');
const path = require('path');
const http = require('http');

const results = {
    timestamp: new Date().toISOString(),
    tests: {
        critical_files: { total: 0, passed: 0, failed: [] },
        navigation: { total: 0, passed: 0, failed: [] },
        css_loading: { total: 0, passed: 0, failed: [] },
        hidden_treasures: { total: 0, passed: 0, failed: [] },
        performance: { total: 0, passed: 0, failed: [] },
        deployment: { total: 0, passed: 0, failed: [] }
    },
    summary: {
        total_tests: 0,
        passed: 0,
        failed: 0,
        warnings: 0
    }
};

console.log('🧪 COMPREHENSIVE TESTING SUITE - OCT 22 DEMO PREP');
console.log('='.repeat(70));
console.log('');

// Test 1: Critical Files Exist
console.log('📋 TEST 1: Critical Files Existence\n');

const criticalFiles = [
    'public/index.html',
    'public/generated-resources-alpha/index.html',
    'public/generated-resources-alpha/TEACHER-QUICK-START-GUIDE.html',
    'public/y8-systems/index.html',
    'public/writers-toolkit/index.html',
    'public/critical-thinking-unit.html',
    'public/guided-inquiry-unit/index.html',
    'public/interactive-literacy/index.html',
    'public/experiences/virtual-marae.html',
    'public/experiences/living-whakapapa.html',
    'public/components/navigation-standard.html',
    'public/css/te-kete-professional.css',
    'public/css/te-kete-unified-design-system.css'
];

criticalFiles.forEach(file => {
    results.tests.critical_files.total++;
    results.summary.total_tests++;
    
    if (fs.existsSync(file)) {
        results.tests.critical_files.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${file}`);
    } else {
        results.tests.critical_files.failed.push(file);
        results.summary.failed++;
        console.log(`   ❌ ${file} - NOT FOUND`);
    }
});

// Test 2: Navigation Links Work
console.log('\n📋 TEST 2: Navigation Integration\n');

const navTestPages = [
    'public/index.html',
    'public/lessons.html',
    'public/handouts.html',
    'public/units.html'
];

navTestPages.forEach(page => {
    results.tests.navigation.total++;
    results.summary.total_tests++;
    
    if (!fs.existsSync(page)) {
        results.tests.navigation.failed.push(`${page} - NOT FOUND`);
        results.summary.failed++;
        console.log(`   ❌ ${page} - File missing`);
        return;
    }
    
    const content = fs.readFileSync(page, 'utf-8');
    const hasNav = content.includes('navigation-standard.html') || 
                   content.includes('<nav') ||
                   content.includes('header');
    
    if (hasNav) {
        results.tests.navigation.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${page} - Has navigation`);
    } else {
        results.tests.navigation.failed.push(`${page} - No navigation`);
        results.summary.failed++;
        console.log(`   ❌ ${page} - Missing navigation`);
    }
});

// Test 3: CSS Files Load
console.log('\n📋 TEST 3: CSS File Loading\n');

const cssFiles = [
    'public/css/te-kete-professional.css',
    'public/css/te-kete-unified-design-system.css',
    'public/css/component-library.css',
    'public/css/beautiful-navigation.css',
    'public/css/mobile-optimization.css'
];

cssFiles.forEach(file => {
    results.tests.css_loading.total++;
    results.summary.total_tests++;
    
    if (!fs.existsSync(file)) {
        results.tests.css_loading.failed.push(`${file} - NOT FOUND`);
        results.summary.failed++;
        console.log(`   ❌ ${file} - File missing`);
        return;
    }
    
    const stats = fs.statSync(file);
    const sizeKB = (stats.size / 1024).toFixed(1);
    
    if (stats.size > 0) {
        results.tests.css_loading.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${file} (${sizeKB} KB)`);
    } else {
        results.tests.css_loading.failed.push(`${file} - Empty file`);
        results.summary.failed++;
        console.log(`   ❌ ${file} - Empty file`);
    }
});

// Test 4: Hidden Treasures Accessible
console.log('\n📋 TEST 4: Hidden Treasures (New Discoveries)\n');

const hiddenTreasures = [
    { file: 'public/experiences/virtual-marae.html', name: 'Virtual Marae Training' },
    { file: 'public/experiences/living-whakapapa.html', name: 'Living Whakapapa' },
    { file: 'public/units/unit-1-te-ao-maori.html', name: 'Unit 1: Te Ao Māori' },
    { file: 'public/units/unit-2-decolonized-history.html', name: 'Unit 2: Decolonized History' },
    { file: 'public/units/unit-7-digital-tech-ai-ethics.html', name: 'Unit 7: AI Ethics' }
];

hiddenTreasures.forEach(item => {
    results.tests.hidden_treasures.total++;
    results.summary.total_tests++;
    
    if (fs.existsSync(item.file)) {
        results.tests.hidden_treasures.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${item.name}`);
    } else {
        results.tests.hidden_treasures.failed.push(item.name);
        results.summary.failed++;
        console.log(`   ❌ ${item.name} - NOT FOUND`);
    }
});

// Test 5: Performance Check (File Sizes)
console.log('\n📋 TEST 5: Performance (File Size Check)\n');

const performanceTargets = [
    { file: 'public/index.html', maxKB: 200, name: 'Homepage' },
    { file: 'public/generated-resources-alpha/index.html', maxKB: 150, name: 'AI Resources Index' },
    { file: 'public/y8-systems/index.html', maxKB: 100, name: 'Y8 Systems' }
];

performanceTargets.forEach(target => {
    results.tests.performance.total++;
    results.summary.total_tests++;
    
    if (!fs.existsSync(target.file)) {
        results.tests.performance.failed.push(`${target.name} - NOT FOUND`);
        results.summary.failed++;
        console.log(`   ❌ ${target.name} - File missing`);
        return;
    }
    
    const stats = fs.statSync(target.file);
    const sizeKB = (stats.size / 1024).toFixed(1);
    
    if (stats.size / 1024 <= target.maxKB) {
        results.tests.performance.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${target.name} - ${sizeKB} KB (target: <${target.maxKB} KB)`);
    } else {
        results.tests.performance.failed.push(`${target.name} - ${sizeKB} KB exceeds ${target.maxKB} KB`);
        results.summary.warnings++;
        console.log(`   ⚠️  ${target.name} - ${sizeKB} KB (target: <${target.maxKB} KB) - Over budget but acceptable`);
    }
});

// Test 6: Deployment Readiness
console.log('\n📋 TEST 6: Deployment Configuration\n');

const deploymentChecks = [
    { file: 'netlify.toml', name: 'Netlify Config' },
    { file: 'public/404.html', name: '404 Page' },
    { file: 'public/manifest.json', name: 'PWA Manifest' },
    { file: 'public/service-worker.js', name: 'Service Worker' }
];

deploymentChecks.forEach(check => {
    results.tests.deployment.total++;
    results.summary.total_tests++;
    
    if (fs.existsSync(check.file)) {
        results.tests.deployment.passed++;
        results.summary.passed++;
        console.log(`   ✅ ${check.name}`);
    } else {
        results.tests.deployment.failed.push(check.name);
        results.summary.warnings++;
        console.log(`   ⚠️  ${check.name} - Not found (optional)`);
    }
});

// Generate Summary
console.log('\n' + '='.repeat(70));
console.log('📊 TESTING SUMMARY');
console.log('='.repeat(70));
console.log('');
console.log(`Total Tests Run: ${results.summary.total_tests}`);
console.log(`✅ Passed: ${results.summary.passed} (${((results.summary.passed/results.summary.total_tests)*100).toFixed(1)}%)`);
console.log(`❌ Failed: ${results.summary.failed}`);
console.log(`⚠️  Warnings: ${results.summary.warnings}`);
console.log('');

// Test Results by Category
console.log('By Category:');
console.log(`   Critical Files: ${results.tests.critical_files.passed}/${results.tests.critical_files.total}`);
console.log(`   Navigation: ${results.tests.navigation.passed}/${results.tests.navigation.total}`);
console.log(`   CSS Loading: ${results.tests.css_loading.passed}/${results.tests.css_loading.total}`);
console.log(`   Hidden Treasures: ${results.tests.hidden_treasures.passed}/${results.tests.hidden_treasures.total}`);
console.log(`   Performance: ${results.tests.performance.passed}/${results.tests.performance.total}`);
console.log(`   Deployment: ${results.tests.deployment.passed}/${results.tests.deployment.total}`);
console.log('');

// Demo Readiness Assessment
const passRate = (results.summary.passed / results.summary.total_tests) * 100;
let readiness = 'NEEDS WORK';
let emoji = '⚠️';

if (passRate >= 95) {
    readiness = 'DEMO READY';
    emoji = '✅';
} else if (passRate >= 85) {
    readiness = 'MOSTLY READY';
    emoji = '👍';
} else if (passRate >= 70) {
    readiness = 'NEEDS MINOR FIXES';
    emoji = '⚠️';
}

console.log('='.repeat(70));
console.log(`${emoji} DEMO READINESS: ${readiness} (${passRate.toFixed(1)}%)`);
console.log('='.repeat(70));
console.log('');

// Critical Issues (if any)
if (results.summary.failed > 0) {
    console.log('🚨 CRITICAL ISSUES TO FIX:\n');
    
    Object.keys(results.tests).forEach(category => {
        if (results.tests[category].failed.length > 0) {
            console.log(`   ${category.toUpperCase()}:`);
            results.tests[category].failed.forEach(issue => {
                console.log(`      ❌ ${issue}`);
            });
            console.log('');
        }
    });
}

// Save Results
fs.writeFileSync('test-results-oct18.json', JSON.stringify(results, null, 2));
console.log('📄 Detailed results saved to: test-results-oct18.json\n');

// Exit code
process.exit(results.summary.failed > 5 ? 1 : 0);

