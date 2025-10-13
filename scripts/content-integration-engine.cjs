#!/usr/bin/env node

/**
 * TE KETE AKO CONTENT INTEGRATION ENGINE
 * 
 * This script identifies, processes, and integrates orphaned educational content
 * from across the te-kete-ako-clean directory into the published site.
 * 
 * Usage: node scripts/content-integration-engine.js [command] [options]
 */

const fs = require('fs');
const path = require('path');

// Configuration
const ROOT_DIR = path.join(__dirname, '..');
const PUBLIC_DIR = path.join(ROOT_DIR, 'public');
const BACKUP_DIR = path.join(ROOT_DIR, 'backups');
const CSS_FILE = path.join(PUBLIC_DIR, 'css', 'te-kete-professional.css');

// Target directories for integration
const TARGET_DIRS = {
  handouts: path.join(PUBLIC_DIR, 'handouts'),
  lessons: path.join(PUBLIC_DIR, 'lessons'),
  interactive: path.join(PUBLIC_DIR, 'interactive'),
  teacher: path.join(PUBLIC_DIR, 'teacher-resources'),
  units: path.join(PUBLIC_DIR, 'units')
};

// High-priority source directories identified from folder crawl
const HIGH_PRIORITY_SOURCES = [
  'backups/css-standardize-202510121404300/public/handouts',
  'backups/css-standardize-202508111249100/public/handouts',
  'backups/css-standardize-202508111350300/public/'
];

/**
 * Ensure target directories exist
 */
function ensureDirectories() {
  for (const [name, dirPath] of Object.entries(TARGET_DIRS)) {
    if (!fs.existsSync(dirPath)) {
      fs.mkdirSync(dirPath, { recursive: true });
      console.log(`Created directory: ${dirPath}`);
    }
  }
}

/**
 * Read the comprehensive folder crawl report
 */
function readCrawlReport() {
  const reportPath = path.join(ROOT_DIR, 'comprehensive-folder-crawl-report.json');
  
  if (!fs.existsSync(reportPath)) {
    console.error('Crawl report not found. Run comprehensive-folder-crawler.js first.');
    process.exit(1);
  }
  
  return JSON.parse(fs.readFileSync(reportPath, 'utf8'));
}

/**
 * Extract title from HTML file
 */
function extractTitle(content) {
  const titleMatch = content.match(/<title[^>]*>([^<]+)<\/title>/i);
  return titleMatch ? titleMatch[1].trim() : 'Untitled Resource';
}

/**
 * Extract description from HTML file
 */
function extractDescription(content) {
  const descMatch = content.match(/<meta[^>]*name=["']description["'][^>]*content=["']([^"']+)["']/i);
  if (descMatch) return descMatch[1].trim();
  
  // If no meta description, try to extract first paragraph
  const pMatch = content.match(/<p[^>]*>([^<]+)<\/p>/i);
  return pMatch ? pMatch[1].trim().substring(0, 160) : 'Educational resource from Te Kete Ako';
}

/**
 * Fix HTML structure for integration
 */
function fixHtmlStructure(content, filePath) {
  let fixedContent = content;
  
  // Ensure proper DOCTYPE
  if (!fixedContent.trim().startsWith('<!DOCTYPE')) {
    fixedContent = '<!DOCTYPE html>\n' + fixedContent;
  }
  
  // Fix CSS path references
  fixedContent = fixedContent.replace(
    /href=["']css\/te-kete-professional\.css["']/g,
    'href="/css/te-kete-professional.css"'
  );
  
  fixedContent = fixedContent.replace(
    /href=["']\.\.\/css\/te-kete-professional\.css["']/g,
    'href="/css/te-kete-professional.css"'
  );
  
  // Fix relative paths to absolute paths
  fixedContent = fixedContent.replace(
    /href=["']\.\.\/\.\.\/(handouts|lessons|units|interactive)\/([^"']+)["']/g,
    'href="/$1/$2"'
  );
  
  // Add proper header and footer if missing
  if (!fixedContent.includes('<div id="header-component"></div>')) {
    fixedContent = fixedContent.replace(
      /<body[^>]*>/,
      '$&\n    <div id="header-component"></div>\n    <div class="mobile-nav-overlay" id="mobileNavOverlay"></div>'
    );
  }
  
  if (!fixedContent.includes('<div id="footer-component"></div>')) {
    fixedContent = fixedContent.replace(
      /<\/body>/,
      '    <div id="footer-component"></div>\n  </body>'
    );
  }
  
  // Add breadcrumb navigation
  const title = extractTitle(fixedContent);
  const pathParts = filePath.split('/');
  const category = pathParts[1] || 'resources';
  
  const breadcrumb = `
    <nav class="breadcrumb-nav">
      <div class="container">
        <a href="/">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="/${category}/">${category.charAt(0).toUpperCase() + category.slice(1)}</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">${title}</span>
      </div>
    </nav>
  `;
  
  // Insert breadcrumb after header
  fixedContent = fixedContent.replace(
    /<div id="header-component"><\/div>\s*<div class="mobile-nav-overlay"[^>]*><\/div>/,
    '$&\n' + breadcrumb
  );
  
  return fixedContent;
}

/**
 * Process a single HTML file for integration
 */
function processHtmlFile(sourcePath, targetPath) {
  try {
    let content = fs.readFileSync(sourcePath, 'utf8');
    
    // Fix HTML structure
    content = fixHtmlStructure(content, targetPath);
    
    // Ensure target directory exists
    const targetDir = path.dirname(targetPath);
    if (!fs.existsSync(targetDir)) {
      fs.mkdirSync(targetDir, { recursive: true });
    }
    
    // Write the processed file
    fs.writeFileSync(targetPath, content);
    
    return {
      success: true,
      sourcePath,
      targetPath,
      title: extractTitle(content),
      description: extractDescription(content)
    };
  } catch (error) {
    return {
      success: false,
      sourcePath,
      error: error.message
    };
  }
}

/**
 * Integrate handouts from backup directories
 */
function integrateHandouts() {
  console.log('🔧 Starting handouts integration...');
  
  const results = {
    processed: [],
    failed: []
  };
  
  // Process each high-priority source directory
  for (const sourceDir of HIGH_PRIORITY_SOURCES) {
    if (!fs.existsSync(sourceDir)) {
      console.log(`Source directory not found: ${sourceDir}`);
      continue;
    }
    
    console.log(`Processing: ${sourceDir}`);
    
    // Find all HTML files in the source directory
    function findHtmlFiles(dir) {
      const files = [];
      
      if (!fs.existsSync(dir)) return files;
      
      const items = fs.readdirSync(dir);
      
      for (const item of items) {
        const itemPath = path.join(dir, item);
        const stats = fs.statSync(itemPath);
        
        if (stats.isDirectory()) {
          files.push(...findHtmlFiles(itemPath));
        } else if (item.endsWith('.html')) {
          files.push(itemPath);
        }
      }
      
      return files;
    }
    
    const htmlFiles = findHtmlFiles(sourceDir);
    console.log(`Found ${htmlFiles.length} HTML files in ${sourceDir}`);
    
    // Process each HTML file
    for (const sourcePath of htmlFiles) {
      // Determine target path
      const relativePath = path.relative(sourceDir, sourcePath);
      const targetPath = path.join(TARGET_DIRS.handouts, relativePath);
      
      // Process the file
      const result = processHtmlFile(sourcePath, targetPath);
      
      if (result.success) {
        results.processed.push(result);
      } else {
        results.failed.push(result);
      }
    }
  }
  
  console.log(`✅ Handouts integration complete:`);
  console.log(`   • Processed: ${results.processed.length} files`);
  console.log(`   • Failed: ${results.failed.length} files`);
  
  if (results.failed.length > 0) {
    console.log('\n❌ Failed files:');
    results.failed.forEach(f => console.log(`   • ${f.sourcePath}: ${f.error}`));
  }
  
  return results;
}

/**
 * Create an index page for integrated content
 */
function createIndexPage(contentType, items) {
  const template = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${contentType.charAt(0).toUpperCase() + contentType.slice(1)} | Te Kete Ako</title>
    <meta name="description" content="Browse our collection of ${contentType} resources integrating mātauranga Māori with contemporary learning">
    <link rel="stylesheet" href="/css/te-kete-professional.css">
    <link rel="stylesheet" href="/css/print.css" media="print"/>
</head>
<body data-auto-init="true" data-current-page="${contentType}">
    <div id="header-component"></div>
    <div class="mobile-nav-overlay" id="mobileNavOverlay"></div>
    
    <nav class="breadcrumb-nav">
        <div class="container">
            <a href="/">Home</a>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-current">${contentType.charAt(0).toUpperCase() + contentType.slice(1)}</span>
        </div>
    </nav>
    
    <main class="container" style="padding: 2rem 0;">
        <section class="page-header">
            <h1 class="page-title">${contentType.charAt(0).toUpperCase() + contentType.slice(1)}</h1>
            <p class="page-description">
                Browse our collection of ${contentType} resources integrating mātauranga Māori with contemporary learning.
            </p>
        </section>
        
        <section class="content-grid">
            ${items.map(item => `
                <div class="content-card">
                    <h3><a href="${item.url}">${item.title}</a></h3>
                    <p>${item.description}</p>
                </div>
            `).join('')}
        </section>
    </main>
    
    <div id="footer-component"></div>
    
    <script src="/js/components.js"></script>
</body>
</html>`;

  const indexPath = path.join(TARGET_DIRS[contentType], 'index.html');
  fs.writeFileSync(indexPath, template);
  
  return indexPath;
}

/**
 * Generate index pages for all integrated content
 */
function generateIndexPages() {
  console.log('📄 Generating index pages...');
  
  for (const [contentType, dirPath] of Object.entries(TARGET_DIRS)) {
    if (!fs.existsSync(dirPath)) continue;
    
    // Find all HTML files in the directory (excluding index.html)
    const items = [];
    
    function findHtmlFiles(dir, relativePath = '') {
      if (!fs.existsSync(dir)) return;
      
      const itemsList = fs.readdirSync(dir);
      
      for (const item of itemsList) {
        if (item === 'index.html') continue;
        
        const itemPath = path.join(dir, item);
        const stats = fs.statSync(itemPath);
        
        if (stats.isDirectory()) {
          findHtmlFiles(itemPath, path.join(relativePath, item));
        } else if (item.endsWith('.html')) {
          try {
            const content = fs.readFileSync(itemPath, 'utf8');
            const url = path.join('/', contentType, relativePath, item).replace(/\\/g, '/');
            
            items.push({
              url,
              title: extractTitle(content),
              description: extractDescription(content)
            });
          } catch (error) {
            console.log(`Error reading ${itemPath}: ${error.message}`);
          }
        }
      }
    }
    
    findHtmlFiles(dirPath);
    
    if (items.length > 0) {
      createIndexPage(contentType, items);
      console.log(`Generated index for ${contentType} with ${items.length} items`);
    }
  }
}

/**
 * Update main navigation to include new content sections
 */
function updateMainNavigation() {
  console.log('🧭 Updating main navigation...');
  
  const headerPath = path.join(PUBLIC_DIR, 'components', 'header.html');
  
  if (!fs.existsSync(headerPath)) {
    console.log('Header component not found, skipping navigation update');
    return;
  }
  
  let headerContent = fs.readFileSync(headerPath, 'utf8');
  
  // Check if handouts link already exists
  if (headerContent.includes('href="/handouts/"')) {
    console.log('Navigation already includes handouts link');
    return;
  }
  
  // Find the navigation list and add new items
  const navListMatch = headerContent.match(/<ul[^>]*class="nav-list"[^>]*>([\s\S]*?)<\/ul>/);
  
  if (navListMatch) {
    const navList = navListMatch[1];
    
    // Find where to insert the new links (before resources or at the end)
    const insertPoint = navList.includes('<li><a href="/resource-hub.html"') 
      ? navList.indexOf('<li><a href="/resource-hub.html"')
      : navList.length;
    
    const newLinks = `
                <li><a href="/handouts/">Handouts</a></li>
                <li><a href="/interactive/">Interactive</a></li>
                <li><a href="/teacher-resources/">Teacher Resources</a></li>`;
    
    const updatedNavList = navList.slice(0, insertPoint) + newLinks + navList.slice(insertPoint);
    
    headerContent = headerContent.replace(navListMatch[0], `<ul class="nav-list">${updatedNavList}</ul>`);
    
    fs.writeFileSync(headerPath, headerContent);
    console.log('✅ Navigation updated successfully');
  } else {
    console.log('Could not find navigation list in header');
  }
}

/**
 * Main execution function
 */
function main() {
  const command = process.argv[2] || 'all';
  
  console.log('🚀 Te Kete Ako Content Integration Engine');
  console.log('==========================================\n');
  
  switch (command) {
    case 'handouts':
      ensureDirectories();
      integrateHandouts();
      generateIndexPages();
      updateMainNavigation();
      break;
      
    case 'index':
      generateIndexPages();
      break;
      
    case 'nav':
      updateMainNavigation();
      break;
      
    case 'all':
    default:
      ensureDirectories();
      integrateHandouts();
      generateIndexPages();
      updateMainNavigation();
      console.log('\n✅ Content integration complete!');
      break;
  }
}

// Run the integration engine
if (require.main === module) {
  main();
}

module.exports = {
  processHtmlFile,
  integrateHandouts,
  generateIndexPages,
  updateMainNavigation
};
