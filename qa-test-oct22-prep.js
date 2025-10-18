#!/usr/bin/env node
/**
 * QA Testing Script for Oct 22 Demo Preparation
 * Tests: Auth flows, Navigation, Links, Mobile-readiness
 * Agent continuing work from 12-agent activation
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';

// Color output helpers
const colors = {
  green: (text) => `\x1b[32m${text}\x1b[0m`,
  red: (text) => `\x1b[31m${text}\x1b[0m`,
  yellow: (text) => `\x1b[33m${text}\x1b[0m`,
  blue: (text) => `\x1b[36m${text}\x1b[0m`,
  bold: (text) => `\x1b[1m${text}\x1b[0m`
};

// Test results storage
const results = {
  authPages: {},
  navigation: {},
  links: { broken: [], working: 0 },
  mobileReady: {},
  performance: {},
  totalTests: 0,
  passed: 0,
  failed: 0,
  warnings: 0
};

console.log('\n' + '='.repeat(70));
console.log(colors.bold('🧪 TE KETE AKO - OCT 22 DEMO QA TEST SUITE'));
console.log('='.repeat(70) + '\n');

// ========================================
// TEST 1: Authentication Pages Exist & Have Required Components
// ========================================
function testAuthPages() {
  console.log(colors.blue('\n📋 TEST 1: Authentication Pages\n'));
  
  const authPages = {
    'login.html': ['form', 'email', 'password', 'button[type="submit"]', 'supabase'],
    'signup-student.html': ['form', 'email', 'password', 'school', 'year-level', 'iwi'],
    'signup-teacher.html': ['form', 'email', 'password', 'school', 'subject'],
    'student-dashboard.html': ['h1', 'nav', 'dashboard', 'recommendations'],
    'teachers/dashboard.html': ['h1', 'nav', 'dashboard', 'class-management']
  };
  
  for (const [page, requiredElements] of Object.entries(authPages)) {
    results.totalTests++;
    const filePath = path.join(PUBLIC_DIR, page);
    
    if (!fs.existsSync(filePath)) {
      console.log(`  ${colors.red('❌')} ${page} - File not found`);
      results.failed++;
      results.authPages[page] = { exists: false, components: [] };
      continue;
    }
    
    const content = fs.readFileSync(filePath, 'utf-8');
    const foundComponents = [];
    
    // Check for required elements (simplified - just check if keywords exist)
    requiredElements.forEach(element => {
      if (content.toLowerCase().includes(element.toLowerCase())) {
        foundComponents.push(element);
      }
    });
    
    const allFound = foundComponents.length === requiredElements.length;
    
    if (allFound) {
      console.log(`  ${colors.green('✅')} ${page} - All components present (${foundComponents.length}/${requiredElements.length})`);
      results.passed++;
    } else {
      console.log(`  ${colors.yellow('⚠️ ')} ${page} - Missing some components (${foundComponents.length}/${requiredElements.length})`);
      results.warnings++;
    }
    
    results.authPages[page] = {
      exists: true,
      components: foundComponents,
      required: requiredElements,
      complete: allFound
    };
  }
}

// ========================================
// TEST 2: Navigation Component Integration
// ========================================
function testNavigation() {
  console.log(colors.blue('\n📋 TEST 2: Navigation Integration\n'));
  
  const keyPages = [
    'index.html',
    'lessons.html',
    'handouts.html',
    'units.html',
    'games/index.html',
    'generated-resources-alpha/index.html'
  ];
  
  keyPages.forEach(page => {
    results.totalTests++;
    const filePath = path.join(PUBLIC_DIR, page);
    
    if (!fs.existsSync(filePath)) {
      console.log(`  ${colors.red('❌')} ${page} - Not found`);
      results.failed++;
      return;
    }
    
    const content = fs.readFileSync(filePath, 'utf-8');
    
    // Check for navigation
    const hasNav = content.includes('navigation') || content.includes('<nav') || 
                   content.includes('site-header') || content.includes('main-nav');
    const hasCSS = content.includes('.css') || content.includes('<style>');
    const hasMobileViewport = content.includes('viewport');
    
    if (hasNav && hasCSS && hasMobileViewport) {
      console.log(`  ${colors.green('✅')} ${page} - Nav ✓ CSS ✓ Mobile ✓`);
      results.passed++;
    } else {
      console.log(`  ${colors.yellow('⚠️ ')} ${page} - Nav:${hasNav ? '✓':'✗'} CSS:${hasCSS ? '✓':'✗'} Mobile:${hasMobileViewport ? '✓':'✗'}`);
      results.warnings++;
    }
    
    results.navigation[page] = { hasNav, hasCSS, hasMobileViewport };
  });
}

// ========================================
// TEST 3: Critical Links Check
// ========================================
function testCriticalLinks() {
  console.log(colors.blue('\n📋 TEST 3: Critical Links\n'));
  
  const linksToTest = [
    { from: 'index.html', to: '/generated-resources-alpha/', label: 'AI Resources' },
    { from: 'index.html', to: '/games/', label: 'Games' },
    { from: 'index.html', to: '/login.html', label: 'Login' },
    { from: 'index.html', to: '/signup-student.html', label: 'Student Signup' },
    { from: 'index.html', to: '/signup-teacher.html', label: 'Teacher Signup' },
    { from: 'generated-resources-alpha/index.html', to: 'handouts/index.html', label: 'Handouts Index' },
    { from: 'generated-resources-alpha/index.html', to: 'lessons/index.html', label: 'Lessons Index' },
    { from: 'games/index.html', to: 'te-reo-wordle.html', label: 'Te Reo Wordle' }
  ];
  
  linksToTest.forEach(link => {
    results.totalTests++;
    const fromPath = path.join(PUBLIC_DIR, link.from);
    
    if (!fs.existsSync(fromPath)) {
      console.log(`  ${colors.red('❌')} Source file not found: ${link.from}`);
      results.failed++;
      results.links.broken.push(link);
      return;
    }
    
    // Check if link exists in source file
    const content = fs.readFileSync(fromPath, 'utf-8');
    const hasLink = content.includes(link.to) || content.includes(link.to.replace(/^\//, ''));
    
    // Determine target path based on link type
    let toPath;
    if (link.to.startsWith('/')) {
      // Absolute path from public root
      toPath = path.join(PUBLIC_DIR, link.to);
    } else {
      // Relative path from source file
      toPath = path.resolve(path.dirname(fromPath), link.to);
    }
    
    // For directory links, check if index.html exists
    if (link.to.endsWith('/')) {
      toPath = path.join(toPath, 'index.html');
    }
    
    // Check if target exists
    const targetExists = fs.existsSync(toPath);
    
    if (hasLink && targetExists) {
      console.log(`  ${colors.green('✅')} ${link.label}: ${link.from} → ${link.to}`);
      results.passed++;
      results.links.working++;
    } else if (hasLink && !targetExists) {
      console.log(`  ${colors.yellow('⚠️ ')} ${link.label}: Link exists but target missing (${toPath.replace(PUBLIC_DIR, '')})`);
      results.warnings++;
      results.links.broken.push(link);
    } else {
      console.log(`  ${colors.red('❌')} ${link.label}: Link:${hasLink?'✓':'✗'} Target:${targetExists?'✓':'✗'}`);
      results.failed++;
      results.links.broken.push(link);
    }
  });
}

// ========================================
// TEST 4: Mobile Readiness
// ========================================
function testMobileReadiness() {
  console.log(colors.blue('\n📋 TEST 4: Mobile Readiness\n'));
  
  const pagesToTest = [
    'index.html',
    'login.html',
    'signup-student.html',
    'games/te-reo-wordle.html',
    'generated-resources-alpha/index.html'
  ];
  
  pagesToTest.forEach(page => {
    results.totalTests++;
    const filePath = path.join(PUBLIC_DIR, page);
    
    if (!fs.existsSync(filePath)) {
      console.log(`  ${colors.red('❌')} ${page} - Not found`);
      results.failed++;
      return;
    }
    
    const content = fs.readFileSync(filePath, 'utf-8');
    
    // Mobile readiness checks
    const hasViewportMeta = content.includes('name="viewport"');
    const hasResponsiveCSS = content.includes('mobile') || content.includes('@media') || 
                             content.includes('min-width') || content.includes('max-width');
    const hasTouchOptimization = content.includes('touch') || !content.includes(':hover');
    
    const mobileScore = [hasViewportMeta, hasResponsiveCSS].filter(Boolean).length;
    
    if (mobileScore >= 2) {
      console.log(`  ${colors.green('✅')} ${page} - Mobile ready (score: ${mobileScore}/2)`);
      results.passed++;
    } else {
      console.log(`  ${colors.yellow('⚠️ ')} ${page} - Mobile needs work (score: ${mobileScore}/2)`);
      results.warnings++;
    }
    
    results.mobileReady[page] = {
      hasViewportMeta,
      hasResponsiveCSS,
      score: mobileScore
    };
  });
}

// ========================================
// TEST 5: Performance Basics
// ========================================
function testPerformanceBasics() {
  console.log(colors.blue('\n📋 TEST 5: Performance Basics\n'));
  
  const criticalPages = ['index.html', 'login.html', 'lessons.html'];
  
  criticalPages.forEach(page => {
    results.totalTests++;
    const filePath = path.join(PUBLIC_DIR, page);
    
    if (!fs.existsSync(filePath)) {
      console.log(`  ${colors.red('❌')} ${page} - Not found`);
      results.failed++;
      return;
    }
    
    const content = fs.readFileSync(filePath, 'utf-8');
    const stats = fs.statSync(filePath);
    const sizeKB = Math.round(stats.size / 1024);
    
    // Performance checks
    const hasCriticalCSS = content.includes('<style') && content.indexOf('<style') < 5000;
    const hasAsyncJS = content.includes('async') || content.includes('defer');
    const hasLazyLoading = content.includes('loading="lazy"');
    const isReasonableSize = sizeKB < 500; // Less than 500KB
    
    const perfScore = [hasCriticalCSS, hasAsyncJS, isReasonableSize].filter(Boolean).length;
    
    if (perfScore >= 2) {
      console.log(`  ${colors.green('✅')} ${page} - Good perf (${sizeKB}KB, score: ${perfScore}/3)`);
      results.passed++;
    } else {
      console.log(`  ${colors.yellow('⚠️ ')} ${page} - Perf needs work (${sizeKB}KB, score: ${perfScore}/3)`);
      results.warnings++;
    }
    
    results.performance[page] = {
      sizeKB,
      hasCriticalCSS,
      hasAsyncJS,
      hasLazyLoading,
      isReasonableSize,
      score: perfScore
    };
  });
}

// ========================================
// RUN ALL TESTS
// ========================================
testAuthPages();
testNavigation();
testCriticalLinks();
testMobileReadiness();
testPerformanceBasics();

// ========================================
// FINAL REPORT
// ========================================
console.log('\n' + '='.repeat(70));
console.log(colors.bold('📊 QA TEST RESULTS SUMMARY'));
console.log('='.repeat(70));

const passRate = ((results.passed / results.totalTests) * 100).toFixed(1);
const warningRate = ((results.warnings / results.totalTests) * 100).toFixed(1);
const failRate = ((results.failed / results.totalTests) * 100).toFixed(1);

console.log(`\nTotal Tests: ${colors.bold(results.totalTests)}`);
console.log(`${colors.green('✅ Passed:')} ${results.passed} (${passRate}%)`);
console.log(`${colors.yellow('⚠️  Warnings:')} ${results.warnings} (${warningRate}%)`);
console.log(`${colors.red('❌ Failed:')} ${results.failed} (${failRate}%)`);

// Demo Readiness Assessment
console.log('\n' + '='.repeat(70));
console.log(colors.bold('🎯 OCT 22 DEMO READINESS'));
console.log('='.repeat(70) + '\n');

if (results.failed === 0 && results.warnings <= 2) {
  console.log(colors.green('🎉 EXCELLENT! Site is DEMO READY! 🎉'));
  console.log('   All critical systems operational.');
  console.log('   Minor warnings acceptable for demo.\n');
} else if (results.failed <= 2) {
  console.log(colors.yellow('⚠️  GOOD, but needs minor fixes'));
  console.log(`   ${results.failed} critical issues to address`);
  console.log(`   ${results.warnings} warnings to review\n`);
} else {
  console.log(colors.red('🚨 NEEDS WORK before demo'));
  console.log(`   ${results.failed} critical issues must be fixed`);
  console.log(`   ${results.warnings} warnings to review\n`);
}

// Priority Actions
if (results.failed > 0 || results.warnings > 5) {
  console.log(colors.bold('🔧 PRIORITY ACTIONS:\n'));
  
  if (results.links.broken.length > 0) {
    console.log(`   1. Fix ${results.links.broken.length} broken links`);
  }
  
  const authIssues = Object.values(results.authPages).filter(p => !p.complete).length;
  if (authIssues > 0) {
    console.log(`   2. Complete ${authIssues} auth page components`);
  }
  
  const mobileIssues = Object.values(results.mobileReady).filter(p => p.score < 2).length;
  if (mobileIssues > 0) {
    console.log(`   3. Improve mobile readiness for ${mobileIssues} pages`);
  }
}

console.log('\n' + '='.repeat(70) + '\n');

// Write detailed JSON report
const reportPath = path.join(__dirname, 'qa-test-report-oct22.json');
fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
console.log(`📄 Detailed report written to: ${colors.blue('qa-test-report-oct22.json')}\n`);

// Exit with appropriate code
process.exit(results.failed > 0 ? 1 : 0);

