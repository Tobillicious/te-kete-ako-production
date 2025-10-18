#!/usr/bin/env node
/**
 * DEEP SITE INVESTIGATION
 * Explores areas we haven't checked yet:
 * - Content duplication analysis
 * - Cross-linking between resources
 * - Year level coverage gaps
 * - Cultural depth assessment
 * - Search functionality
 * - Accessibility features
 * - Hidden gems and orphaned treasures
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';

const colors = {
  green: (text) => `\x1b[32m${text}\x1b[0m`,
  red: (text) => `\x1b[31m${text}\x1b[0m`,
  yellow: (text) => `\x1b[33m${text}\x1b[0m`,
  blue: (text) => `\x1b[36m${text}\x1b[0m`,
  magenta: (text) => `\x1b[35m${text}\x1b[0m`,
  bold: (text) => `\x1b[1m${text}\x1b[0m`
};

const investigation = {
  duplicates: {},
  crossLinks: { found: 0, broken: 0, internal: 0 },
  yearLevels: { y7: 0, y8: 0, y9: 0, y10: 0, y11: 0, y12: 0, y13: 0, unspecified: 0 },
  culturalDepth: { whakatauaki: 0, maoriWords: 0, culturalContext: 0, tikangaNotes: 0 },
  searchPresent: false,
  accessibility: { altText: 0, ariaLabels: 0, skipLinks: 0, headingStructure: 0 },
  hiddenGems: [],
  orphaned: []
};

console.log('\n' + '='.repeat(80));
console.log(colors.bold('🔍 DEEP SITE INVESTIGATION - Unexplored Territory'));
console.log('='.repeat(80) + '\n');

// ============================================
// INVESTIGATION 1: Content Duplication Analysis
// ============================================
function investigateDuplication() {
  console.log(colors.blue('\n🔬 INVESTIGATION 1: Content Duplication Analysis\n'));
  
  const titleMap = new Map();
  const contentHashes = new Map();
  
  function scanDirectory(dir, prefix = '') {
    try {
      const items = fs.readdirSync(dir);
      
      items.forEach(item => {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
          scanDirectory(fullPath, path.join(prefix, item));
        } else if (item.endsWith('.html')) {
          const content = fs.readFileSync(fullPath, 'utf-8');
          
          // Extract title
          const titleMatch = content.match(/<title>(.*?)<\/title>/);
          if (titleMatch) {
            const title = titleMatch[1].trim();
            if (!titleMap.has(title)) {
              titleMap.set(title, []);
            }
            titleMap.set(title, [...titleMap.get(title), path.join(prefix, item)]);
          }
          
          // Simple content hash (first 500 chars of body)
          const bodyMatch = content.match(/<body[^>]*>([\s\S]{0,500})/);
          if (bodyMatch) {
            const contentSnippet = bodyMatch[1].replace(/\s+/g, ' ').trim();
            if (!contentHashes.has(contentSnippet)) {
              contentHashes.set(contentSnippet, []);
            }
            contentHashes.set(contentSnippet, [...contentHashes.get(contentSnippet), path.join(prefix, item)]);
          }
        }
      });
    } catch (err) {
      // Skip directories we can't read
    }
  }
  
  scanDirectory(PUBLIC_DIR);
  
  // Find duplicates
  const duplicateTitles = Array.from(titleMap.entries()).filter(([_, files]) => files.length > 1);
  const duplicateContent = Array.from(contentHashes.entries()).filter(([_, files]) => files.length > 1);
  
  console.log(`  📊 Total unique titles: ${titleMap.size}`);
  console.log(`  🔁 Duplicate titles found: ${colors.yellow(duplicateTitles.length)}`);
  
  if (duplicateTitles.length > 0 && duplicateTitles.length <= 10) {
    console.log(`\n  ${colors.yellow('⚠️  Duplicate Titles:')}`);
    duplicateTitles.slice(0, 10).forEach(([title, files]) => {
      console.log(`    "${title}" - ${files.length} files:`);
      files.forEach(f => console.log(`      - ${f}`));
    });
  }
  
  console.log(`\n  🔁 Potential duplicate content: ${colors.yellow(duplicateContent.length)}`);
  
  investigation.duplicates = {
    totalTitles: titleMap.size,
    duplicateTitles: duplicateTitles.length,
    duplicateContent: duplicateContent.length,
    examples: duplicateTitles.slice(0, 5).map(([title, files]) => ({ title, files }))
  };
}

// ============================================
// INVESTIGATION 2: Cross-Linking Quality
// ============================================
function investigateCrossLinking() {
  console.log(colors.blue('\n🔬 INVESTIGATION 2: Cross-Linking Between Resources\n'));
  
  const resourceFiles = [
    path.join(PUBLIC_DIR, 'generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty.html'),
    path.join(PUBLIC_DIR, 'critical-thinking/lessons/lesson-1.html'),
    path.join(PUBLIC_DIR, 'y8-systems/index.html'),
    path.join(PUBLIC_DIR, 'units/y7-maths-algebra/index.html')
  ];
  
  let totalLinks = 0;
  let internalLinks = 0;
  let externalLinks = 0;
  let relatedResourceLinks = 0;
  
  resourceFiles.forEach(file => {
    if (!fs.existsSync(file)) return;
    
    const content = fs.readFileSync(file, 'utf-8');
    const links = content.match(/href=["']([^"']+)["']/g) || [];
    
    totalLinks += links.length;
    
    links.forEach(link => {
      const href = link.match(/href=["']([^"']+)["']/)[1];
      if (href.startsWith('http')) {
        externalLinks++;
      } else if (href.startsWith('/')) {
        internalLinks++;
        // Check if it links to another lesson/unit/handout
        if (href.includes('/lessons/') || href.includes('/units/') || href.includes('/handouts/')) {
          relatedResourceLinks++;
        }
      }
    });
  });
  
  console.log(`  📊 Sample of ${resourceFiles.length} resources analyzed`);
  console.log(`  🔗 Total links: ${totalLinks}`);
  console.log(`  🏠 Internal links: ${colors.green(internalLinks)}`);
  console.log(`  🌐 External links: ${externalLinks}`);
  console.log(`  🔗 Links to related resources: ${colors.yellow(relatedResourceLinks)}`);
  
  const crossLinkScore = totalLinks > 0 ? ((relatedResourceLinks / totalLinks) * 100).toFixed(1) : 0;
  console.log(`\n  ${colors.bold('Cross-Link Score:')} ${crossLinkScore}% ${crossLinkScore > 20 ? '✅' : '⚠️'}`);
  
  investigation.crossLinks = {
    totalLinks,
    internalLinks,
    externalLinks,
    relatedResourceLinks,
    crossLinkScore: parseFloat(crossLinkScore)
  };
}

// ============================================
// INVESTIGATION 3: Year Level Coverage
// ============================================
function investigateYearLevelCoverage() {
  console.log(colors.blue('\n🔬 INVESTIGATION 3: Year Level Coverage Gaps\n'));
  
  const unitsDir = path.join(PUBLIC_DIR, 'units');
  const yearLevelPattern = /y(\d+)|year[\s-]?(\d+)/i;
  
  function scanForYearLevels(dir) {
    try {
      const items = fs.readdirSync(dir);
      
      items.forEach(item => {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
          const match = item.match(yearLevelPattern);
          if (match) {
            const year = match[1] || match[2];
            const yearKey = `y${year}`;
            if (investigation.yearLevels[yearKey] !== undefined) {
              investigation.yearLevels[yearKey]++;
            }
          }
        }
      });
    } catch (err) {
      // Skip if can't read
    }
  }
  
  scanForYearLevels(unitsDir);
  
  console.log('  📊 Units by Year Level:');
  Object.entries(investigation.yearLevels).forEach(([year, count]) => {
    const bar = '█'.repeat(Math.min(count, 20));
    const color = count === 0 ? colors.red : count < 3 ? colors.yellow : colors.green;
    console.log(`    ${year.toUpperCase()}: ${color(bar)} ${count} units`);
  });
  
  const gaps = Object.entries(investigation.yearLevels).filter(([_, count]) => count === 0);
  if (gaps.length > 0) {
    console.log(`\n  ${colors.red('⚠️  Coverage Gaps:')} ${gaps.map(([y]) => y.toUpperCase()).join(', ')}`);
  } else {
    console.log(`\n  ${colors.green('✅ Full coverage across all year levels!')}`);
  }
}

// ============================================
// INVESTIGATION 4: Cultural Integration Depth
// ============================================
function investigateCulturalDepth() {
  console.log(colors.blue('\n🔬 INVESTIGATION 4: Cultural Integration Depth\n'));
  
  const sampleFiles = [
    path.join(PUBLIC_DIR, 'generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty.html'),
    path.join(PUBLIC_DIR, 'generated-resources-alpha/handouts/probability-and-chance-in-māori-games.html'),
    path.join(PUBLIC_DIR, 'critical-thinking/lessons/lesson-5.html')
  ];
  
  sampleFiles.forEach(file => {
    if (!fs.existsSync(file)) return;
    
    const content = fs.readFileSync(file, 'utf-8').toLowerCase();
    
    if (content.includes('whakataukī') || content.includes('whakatauaki')) investigation.culturalDepth.whakatauaki++;
    if (content.includes('tikanga') || content.includes('kaitiakitanga') || content.includes('manaakitanga')) investigation.culturalDepth.tikangaNotes++;
    if (content.includes('māori') || content.includes('maori')) investigation.culturalDepth.maoriWords++;
    if (content.includes('cultural context') || content.includes('te ao māori')) investigation.culturalDepth.culturalContext++;
  });
  
  const depthScore = (investigation.culturalDepth.whakatauaki + investigation.culturalDepth.culturalContext) / sampleFiles.length;
  
  console.log(`  📊 Sample of ${sampleFiles.length} resources analyzed:`);
  console.log(`  🌿 Files with Whakataukī: ${colors.green(investigation.culturalDepth.whakatauaki)}`);
  console.log(`  🏛️  Files with Tikanga notes: ${colors.green(investigation.culturalDepth.tikangaNotes)}`);
  console.log(`  📖 Files with Māori content: ${colors.green(investigation.culturalDepth.maoriWords)}`);
  console.log(`  🌏 Files with cultural context sections: ${colors.green(investigation.culturalDepth.culturalContext)}`);
  console.log(`\n  ${colors.bold('Cultural Depth Score:')} ${depthScore.toFixed(1)}/sample ${depthScore >= 1 ? '✅ Excellent' : '⚠️  Needs work'}`);
}

// ============================================
// INVESTIGATION 5: Search & Accessibility
// ============================================
function investigateFeatures() {
  console.log(colors.blue('\n🔬 INVESTIGATION 5: Search & Accessibility Features\n'));
  
  const indexPath = path.join(PUBLIC_DIR, 'index.html');
  const indexContent = fs.readFileSync(indexPath, 'utf-8');
  
  // Check for search
  investigation.searchPresent = indexContent.includes('search') || indexContent.includes('Search');
  console.log(`  🔍 Search functionality: ${investigation.searchPresent ? colors.green('✅ Present') : colors.yellow('⚠️  Not found')}`);
  
  // Check accessibility features
  const hasSkipLink = indexContent.includes('skip') || indexContent.includes('Skip to main');
  const hasAriaLabels = indexContent.match(/aria-label/g);
  const hasAltText = indexContent.match(/alt=/g);
  
  investigation.accessibility.skipLinks = hasSkipLink ? 1 : 0;
  investigation.accessibility.ariaLabels = hasAriaLabels ? hasAriaLabels.length : 0;
  investigation.accessibility.altText = hasAltText ? hasAltText.length : 0;
  
  console.log(`  ♿ Skip to main content: ${hasSkipLink ? colors.green('✅ Yes') : colors.yellow('⚠️  No')}`);
  console.log(`  🏷️  ARIA labels found: ${investigation.accessibility.ariaLabels > 0 ? colors.green(investigation.accessibility.ariaLabels) : colors.yellow('0')}`);
  console.log(`  🖼️  Alt text instances: ${investigation.accessibility.altText > 0 ? colors.green(investigation.accessibility.altText) : colors.yellow('0')}`);
}

// ============================================
// INVESTIGATION 6: Hidden Gems Discovery
// ============================================
function findHiddenGems() {
  console.log(colors.blue('\n🔬 INVESTIGATION 6: Hidden Gems & Orphaned Treasures\n'));
  
  const interestingDirs = [
    'experiences',
    'activities', 
    'interactive',
    'tools',
    'assessment-frameworks',
    'professional-development'
  ];
  
  interestingDirs.forEach(dir => {
    const fullPath = path.join(PUBLIC_DIR, dir);
    if (fs.existsSync(fullPath)) {
      const files = fs.readdirSync(fullPath).filter(f => f.endsWith('.html'));
      if (files.length > 0) {
        investigation.hiddenGems.push({
          directory: dir,
          fileCount: files.length,
          examples: files.slice(0, 3)
        });
        console.log(`  ${colors.magenta('💎')} Found: ${colors.bold(dir)} (${files.length} files)`);
        files.slice(0, 3).forEach(f => console.log(`      - ${f}`));
      }
    }
  });
  
  console.log(`\n  ${colors.bold('Total hidden gems found:')} ${investigation.hiddenGems.length} directories`);
}

// ============================================
// RUN ALL INVESTIGATIONS
// ============================================
investigateDuplication();
investigateCrossLinking();
investigateYearLevelCoverage();
investigateCulturalDepth();
investigateFeatures();
findHiddenGems();

// ============================================
// FINAL REPORT
// ============================================
console.log('\n' + '='.repeat(80));
console.log(colors.bold('📊 DEEP INVESTIGATION SUMMARY'));
console.log('='.repeat(80));

console.log(`\n${colors.bold('🔍 Key Findings:')}`);
console.log(`  1. Duplicate Content: ${investigation.duplicates.duplicateTitles} duplicate titles found`);
console.log(`  2. Cross-Linking: ${investigation.crossLinks.crossLinkScore}% of links connect resources`);
console.log(`  3. Year Coverage: ${Object.values(investigation.yearLevels).filter(c => c > 0).length}/8 year levels have content`);
console.log(`  4. Cultural Depth: ${investigation.culturalDepth.whakatauaki + investigation.culturalDepth.culturalContext} strong cultural elements`);
console.log(`  5. Accessibility: ${investigation.accessibility.ariaLabels} ARIA labels, ${investigation.accessibility.altText} alt texts`);
console.log(`  6. Hidden Gems: ${investigation.hiddenGems.length} undiscovered directories with content`);

console.log(`\n${colors.bold('🎯 Recommendations:')}`);

if (investigation.duplicates.duplicateTitles > 10) {
  console.log(`  ${colors.yellow('⚠️ ')} Address ${investigation.duplicates.duplicateTitles} duplicate titles`);
}

if (investigation.crossLinks.crossLinkScore < 20) {
  console.log(`  ${colors.yellow('⚠️ ')} Improve cross-linking between resources (currently ${investigation.crossLinks.crossLinkScore}%)`);
}

const gapYears = Object.entries(investigation.yearLevels).filter(([_, c]) => c < 2).map(([y]) => y);
if (gapYears.length > 0) {
  console.log(`  ${colors.yellow('⚠️ ')} Develop more content for: ${gapYears.join(', ')}`);
}

if (!investigation.searchPresent) {
  console.log(`  ${colors.yellow('⚠️ ')} Add search functionality to homepage`);
}

if (investigation.hiddenGems.length > 0) {
  console.log(`  ${colors.green('✅')} Integrate ${investigation.hiddenGems.length} hidden gem directories into navigation`);
}

console.log('\n' + '='.repeat(80));

// Write JSON report
const reportPath = path.join(__dirname, 'deep-investigation-report.json');
fs.writeFileSync(reportPath, JSON.stringify(investigation, null, 2));
console.log(`\n📄 Detailed report: ${colors.blue('deep-investigation-report.json')}\n`);

process.exit(0);

