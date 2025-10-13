#!/usr/bin/env node

/**
 * COMPREHENSIVE FOLDER CRAWLER FOR TE KETE AKO
 * 
 * This script crawls the entire te-kete-ako-clean directory to identify
 * all valuable content that could be integrated into the published site.
 * 
 * Usage: node comprehensive-folder-crawler.js
 */

const fs = require('fs');
const path = require('path');

// Configuration
const PROJECT_ROOT = __dirname;
const IGNORED_DIRS = [
  'node_modules',
  '.git',
  'backups',
  'archived-bloat',
  'dist',
  'build'
];

// Statistics
const stats = {
  totalFiles: 0,
  htmlFiles: 0,
  markdownFiles: 0,
  teachingFiles: 0,
  culturalFiles: 0,
  potentialPages: 0,
  categorized: {
    lessons: 0,
    handouts: 0,
    units: 0,
    activities: 0,
    assessments: 0,
    resources: 0,
    other: 0
  },
  duplicates: {},
  orphaned: [],
  treasures: []
};

// Main crawler function
async function crawlProject() {
  console.log('🔍 Starting comprehensive project crawl...');
  
  // Crawl the entire project
  await crawlDirectory(PROJECT_ROOT, '');
  
  // Analyze findings
  analyzeFindings();
  
  // Generate report
  generateReport();
  
  // Create integration plan
  createIntegrationPlan();
  
  console.log('✅ Project crawl complete!');
}

// Recursively crawl directory
async function crawlDirectory(dirPath, relativePath) {
  try {
    const items = fs.readdirSync(dirPath);
    
    for (const item of items) {
      const itemPath = path.join(dirPath, item);
      const itemRelativePath = path.join(relativePath, item);
      const stat = fs.statSync(itemPath);
      
      if (stat.isDirectory() && !IGNORED_DIRS.includes(item)) {
        await crawlDirectory(itemPath, itemRelativePath);
      } else if (stat.isFile()) {
        await processFile(itemPath, itemRelativePath);
      }
    }
  } catch (error) {
    console.error(`Error crawling ${dirPath}: ${error.message}`);
  }
}

// Process individual file
async function processFile(filePath, relativePath) {
  stats.totalFiles++;
  
  try {
    const ext = path.extname(filePath).toLowerCase();
    const fileName = path.basename(filePath, ext);
    
    // Count file types
    if (ext === '.html') {
      stats.htmlFiles++;
      await processHtmlFile(filePath, relativePath);
    } else if (ext === '.md') {
      stats.markdownFiles++;
      await processMarkdownFile(filePath, relativePath);
    }
    
    // Track potential duplicates
    if (!stats.duplicates[fileName]) {
      stats.duplicates[fileName] = [];
    }
    stats.duplicates[fileName].push(relativePath);
    
  } catch (error) {
    console.error(`Error processing ${filePath}: ${error.message}`);
  }
}

// Process HTML files
async function processHtmlFile(filePath, relativePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Check for teaching content indicators
    const teachingIndicators = [
      'lesson', 'handout', 'unit', 'activity', 'assessment',
      'māori', 'maori', 'whakatauki', 'tikanga', 'kaitiaki',
      'curriculum', 'learning', 'teaching', 'education',
      'student', 'teacher', 'classroom', 'school'
    ];
    
    const hasTeachingContent = teachingIndicators.some(indicator => 
      content.toLowerCase().includes(indicator)
    );
    
    if (hasTeachingContent) {
      stats.teachingFiles++;
      
      // Extract title
      const titleMatch = content.match(/<title>(.*?)<\/title>/i);
      const title = titleMatch ? titleMatch[1] : '';
      
      // Categorize the content
      const category = categorizeContent(relativePath, content);
      stats.categorized[category]++;
      
      // Check if it's a treasure (high-quality content)
      if (isTreasure(content, relativePath)) {
        stats.treasures.push({
          path: relativePath,
          title,
          category,
          reason: 'High-quality teaching content'
        });
      }
      
      // Check if it's orphaned (not in public directory)
      if (!relativePath.startsWith('public/')) {
        stats.orphaned.push({
          path: relativePath,
          title,
          category
        });
      }
    }
    
    // Check for cultural content
    const culturalIndicators = [
      'mātauranga māori', 'matauranga maori', 'te ao māori', 'te ao maori',
      'whakapapa', 'kaitiakitanga', 'mana', 'tapu', 'noa',
      'marae', 'iwi', 'hapū', 'whānau', 'whanau',
      'rongoā', 'moko', 'haka', 'poi', 'waiata'
    ];
    
    const hasCulturalContent = culturalIndicators.some(indicator => 
      content.toLowerCase().includes(indicator)
    );
    
    if (hasCulturalContent) {
      stats.culturalFiles++;
    }
    
  } catch (error) {
    console.error(`Error processing HTML ${filePath}: ${error.message}`);
  }
}

// Process Markdown files
async function processMarkdownFile(filePath, relativePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Check for teaching content indicators
    const teachingIndicators = [
      '# lesson', '# handout', '# unit', '# activity', '# assessment',
      'māori', 'maori', 'whakatauki', 'tikanga', 'kaitiaki',
      'curriculum', 'learning', 'teaching', 'education'
    ];
    
    const hasTeachingContent = teachingIndicators.some(indicator => 
      content.toLowerCase().includes(indicator)
    );
    
    if (hasTeachingContent) {
      stats.teachingFiles++;
      stats.potentialPages++;
      
      // Extract title
      const titleMatch = content.match(/^#\s+(.+)$/m);
      const title = titleMatch ? titleMatch[1] : '';
      
      // Categorize the content
      const category = categorizeContent(relativePath, content);
      stats.categorized[category]++;
      
      // All markdown files are potential treasures
      stats.treasures.push({
        path: relativePath,
        title,
        category,
        reason: 'Markdown teaching content',
        needsConversion: true
      });
      
      // Most markdown files are orphaned
      if (!relativePath.startsWith('public/')) {
        stats.orphaned.push({
          path: relativePath,
          title,
          category,
          needsConversion: true
        });
      }
    }
    
  } catch (error) {
    console.error(`Error processing Markdown ${filePath}: ${error.message}`);
  }
}

// Categorize content based on path and content
function categorizeContent(relativePath, content) {
  const path = relativePath.toLowerCase();
  
  if (path.includes('lesson')) return 'lessons';
  if (path.includes('handout')) return 'handouts';
  if (path.includes('unit')) return 'units';
  if (path.includes('activity')) return 'activities';
  if (path.includes('assessment')) return 'assessments';
  if (path.includes('resource')) return 'resources';
  
  // Check content for category indicators
  if (content.includes('learning outcome') || content.includes('objective')) {
    if (content.includes('assessment') || content.includes('rubric')) return 'assessments';
    if (content.includes('activity') || content.includes('exercise')) return 'activities';
    return 'lessons';
  }
  
  return 'other';
}

// Check if content is a treasure (high-quality)
function isTreasure(content, relativePath) {
  // Quality indicators
  const qualityIndicators = [
    content.length > 1000, // Substantial content
    content.includes('learning outcome') || content.includes('objective'),
    content.includes('māori') || content.includes('maori'),
    content.includes('activity') || content.includes('exercise'),
    content.includes('assessment') || content.includes('rubric')
  ];
  
  const qualityScore = qualityIndicators.filter(Boolean).length;
  
  // High quality if it meets 3+ criteria
  return qualityScore >= 3;
}

// Analyze findings
function analyzeFindings() {
  console.log('\n📊 Analyzing findings...');
  
  // Find duplicates
  const duplicates = {};
  for (const [fileName, paths] of Object.entries(stats.duplicates)) {
    if (paths.length > 1) {
      duplicates[fileName] = paths;
    }
  }
  stats.duplicates = duplicates;
  
  // Sort treasures by category
  stats.treasures.sort((a, b) => a.category.localeCompare(b.category));
  
  // Sort orphaned by category
  stats.orphaned.sort((a, b) => a.category.localeCompare(b.category));
}

// Generate report
function generateReport() {
  console.log('\n📊 COMPREHENSIVE PROJECT CRAWL REPORT\n');
  console.log(`Total Files: ${stats.totalFiles}`);
  console.log(`HTML Files: ${stats.htmlFiles}`);
  console.log(`Markdown Files: ${stats.markdownFiles}`);
  console.log(`Teaching Files: ${stats.teachingFiles}`);
  console.log(`Cultural Files: ${stats.culturalFiles}`);
  console.log(`Potential Pages: ${stats.potentialPages}`);
  
  console.log('\n📚 Content Categories:');
  for (const [category, count] of Object.entries(stats.categorized)) {
    console.log(`  ${category}: ${count}`);
  }
  
  console.log(`\n💎 Teaching Treasures: ${stats.treasures.length}`);
  console.log(`🏝️ Orphaned Teaching Files: ${stats.orphaned.length}`);
  console.log(`📋 Duplicate Files: ${Object.keys(stats.duplicates).length}`);
  
  // Save detailed report
  const reportData = {
    timestamp: new Date().toISOString(),
    stats,
    treasures: stats.treasures,
    orphaned: stats.orphaned,
    duplicates: stats.duplicates
  };
  
  fs.writeFileSync(
    path.join(PROJECT_ROOT, 'comprehensive-crawl-report.json'),
    JSON.stringify(reportData, null, 2)
  );
  
  console.log('\n💾 Detailed report saved to comprehensive-crawl-report.json');
}

// Create integration plan
function createIntegrationPlan() {
  console.log('\n📋 Creating integration plan...');
  
  const plan = {
    timestamp: new Date().toISOString(),
    phases: [
      {
        phase: 1,
        title: "Integrate Orphaned Treasures",
        description: "Move high-quality teaching content to public directory",
        tasks: [
          "Convert markdown files to HTML",
          "Fix CSS paths for moved files",
          "Add navigation links",
          "Test functionality"
        ],
        items: stats.orphaned.filter(item => item.needsConversion || item.category === 'lessons' || item.category === 'handouts').slice(0, 10)
      },
      {
        phase: 2,
        title: "Resolve Duplicates",
        description: "Consolidate duplicate content",
        tasks: [
          "Identify best version of each duplicate",
          "Merge unique content",
          "Remove redundant files",
          "Update links"
        ],
        items: Object.entries(stats.duplicates).slice(0, 5)
      },
      {
        phase: 3,
        title: "Enhance Cultural Content",
        description: "Strengthen Mātauranga Māori integration",
        tasks: [
          "Add cultural context where missing",
          "Include te reo Māori terms",
          "Add whakataukī",
          "Connect to cultural framework"
        ],
        items: stats.treasures.filter(item => item.category === 'units' || item.category === 'resources').slice(0, 10)
      }
    ]
  };
  
  fs.writeFileSync(
    path.join(PROJECT_ROOT, 'content-integration-plan.json'),
    JSON.stringify(plan, null, 2)
  );
  
  console.log('💾 Integration plan saved to content-integration-plan.json');
}

// Run the crawler
crawlProject().catch(console.error);
