const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// Supabase connection
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

// Configuration
const PROJECT_ROOT = __dirname;
const PUBLIC_DIR = path.join(PROJECT_ROOT, 'public');
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
  cssFiles: 0,
  jsFiles: 0,
  imageFiles: 0,
  otherFiles: 0,
  duplicates: {},
  relationships: new Map(),
  errors: []
};

// Main crawler function
async function crawlSite() {
  console.log('🕷️  Starting comprehensive site crawl...');
  
  // Run specialized crawlers in parallel
  await Promise.all([
    crawlHtmlStructure(),
    crawlCssDependencies(),
    crawlJsDependencies(),
    crawlMediaAssets(),
    crawlContentHierarchy()
  ]);
  
  // Analyze relationships and duplicates
  analyzeRelationships();
  findDuplicates();
  
  // Generate comprehensive report
  generateReport();
  
  console.log('✅ Site crawl complete!');
}

// Specialized crawler for HTML structure
async function crawlHtmlStructure() {
  console.log('📄 Crawling HTML structure...');
  
  await crawlDirectoryByType(PUBLIC_DIR, '', '.html', async (filePath, relativePath) => {
    await processHtmlFile(filePath, relativePath);
  });
}

// Specialized crawler for CSS dependencies
async function crawlCssDependencies() {
  console.log('🎨 Crawling CSS dependencies...');
  
  await crawlDirectoryByType(PUBLIC_DIR, '', '.css', async (filePath, relativePath) => {
    await processCssFile(filePath, relativePath);
  });
}

// Specialized crawler for JS dependencies
async function crawlJsDependencies() {
  console.log('⚡ Crawling JS dependencies...');
  
  await crawlDirectoryByType(PUBLIC_DIR, '', '.js', async (filePath, relativePath) => {
    await processJsFile(filePath, relativePath);
  });
}

// Specialized crawler for media assets
async function crawlMediaAssets() {
  console.log('🖼️ Crawling media assets...');
  
  const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'];
  
  for (const ext of imageExtensions) {
    await crawlDirectoryByType(PUBLIC_DIR, '', ext, async (filePath, relativePath) => {
      stats.imageFiles++;
      await storeInGraphRAG({
        path: relativePath,
        type: 'image',
        extension: ext
      });
    });
  }
}

// Specialized crawler for content hierarchy (Units → Lessons → Handouts)
async function crawlContentHierarchy() {
  console.log('📚 Crawling content hierarchy...');
  
  // Find all units
  const unitPaths = await findPathsByPattern('/units/*/index.html');
  
  for (const unitPath of unitPaths) {
    await processUnit(unitPath);
  }
  
  // Find standalone lessons
  const lessonPaths = await findPathsByPattern('/lessons/*.html');
  
  for (const lessonPath of lessonPaths) {
    await processStandaloneLesson(lessonPath);
  }
  
  // Find handouts
  const handoutPaths = await findPathsByPattern('/handouts/*.html');
  
  for (const handoutPath of handoutPaths) {
    await processHandout(handoutPath);
  }
}

// Helper function to crawl directory by file type
async function crawlDirectoryByType(dirPath, relativePath, extension, processor) {
  try {
    const items = fs.readdirSync(dirPath);
    
    for (const item of items) {
      const itemPath = path.join(dirPath, item);
      const itemRelativePath = path.join(relativePath, item);
      const stat = fs.statSync(itemPath);
      
      if (stat.isDirectory() && !IGNORED_DIRS.includes(item)) {
        await crawlDirectoryByType(itemPath, itemRelativePath, extension, processor);
      } else if (stat.isFile() && item.endsWith(extension)) {
        await processor(itemPath, itemRelativePath);
      }
    }
  } catch (error) {
    stats.errors.push(`Error crawling ${dirPath}: ${error.message}`);
  }
}

// Helper function to find paths by pattern
async function findPathsByPattern(pattern) {
  const paths = [];
  const regex = new RegExp(pattern.replace(/\*/g, '([^/]+)'));
  
  for (const [relativePath] of stats.relationships.entries()) {
    if (regex.test(relativePath)) {
      paths.push(relativePath);
    }
  }
  
  return paths;
}

// Process a unit and its lessons
async function processUnit(unitPath) {
  try {
    const unitDir = path.dirname(unitPath);
    const unitName = path.basename(unitDir);
    
    // Find lessons in this unit
    const lessonPattern = new RegExp(`^${unitDir}/lesson-[^/]+\\.html$`);
    const lessons = [];
    
    for (const [lessonPath, data] of stats.relationships.entries()) {
      if (lessonPattern.test(lessonPath)) {
        lessons.push({
          path: lessonPath,
          title: data.title || path.basename(lessonPath, '.html')
        });
      }
    }
    
    // Store unit hierarchy in GraphRAG
    await storeContentHierarchy({
      type: 'unit',
      path: unitPath,
      name: unitName,
      children: lessons,
      project_root: PROJECT_ROOT,
      crawled_at: new Date().toISOString()
    });
    
    console.log(`  Processed unit: ${unitName} with ${lessons.length} lessons`);
  } catch (error) {
    stats.errors.push(`Error processing unit ${unitPath}: ${error.message}`);
  }
}

// Process a standalone lesson
async function processStandaloneLesson(lessonPath) {
  try {
    const lessonName = path.basename(lessonPath, '.html');
    
    // Find handouts linked to this lesson
    const lessonData = stats.relationships.get(lessonPath);
    const handouts = [];
    
    if (lessonData && lessonData.internalLinks) {
      for (const link of lessonData.internalLinks) {
        if (link.includes('/handouts/')) {
          handouts.push({
            path: link,
            name: path.basename(link, '.html')
          });
        }
      }
    }
    
    // Store lesson hierarchy in GraphRAG
    await storeContentHierarchy({
      type: 'lesson',
      path: lessonPath,
      name: lessonName,
      parent: null, // Standalone lesson
      children: handouts,
      project_root: PROJECT_ROOT,
      crawled_at: new Date().toISOString()
    });
    
    console.log(`  Processed standalone lesson: ${lessonName} with ${handouts.length} handouts`);
  } catch (error) {
    stats.errors.push(`Error processing lesson ${lessonPath}: ${error.message}`);
  }
}

// Process a handout
async function processHandout(handoutPath) {
  try {
    const handoutName = path.basename(handoutPath, '.html');
    
    // Store handout in GraphRAG
    await storeContentHierarchy({
      type: 'handout',
      path: handoutPath,
      name: handoutName,
      project_root: PROJECT_ROOT,
      crawled_at: new Date().toISOString()
    });
    
    console.log(`  Processed handout: ${handoutName}`);
  } catch (error) {
    stats.errors.push(`Error processing handout ${handoutPath}: ${error.message}`);
  }
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
    stats.errors.push(`Error crawling ${dirPath}: ${error.message}`);
  }
}

// Process individual file
async function processFile(filePath, relativePath) {
  stats.totalFiles++;
  
  try {
    const ext = path.extname(filePath).toLowerCase();
    const fileName = path.basename(filePath, ext);
    
    // Update file type stats
    if (ext === '.html') {
      stats.htmlFiles++;
      await processHtmlFile(filePath, relativePath);
    } else if (ext === '.css') {
      stats.cssFiles++;
      await processCssFile(filePath, relativePath);
    } else if (ext === '.js') {
      stats.jsFiles++;
      await processJsFile(filePath, relativePath);
    } else if (['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'].includes(ext)) {
      stats.imageFiles++;
    } else {
      stats.otherFiles++;
    }
    
    // Track potential duplicates by filename
    if (!stats.duplicates[fileName]) {
      stats.duplicates[fileName] = [];
    }
    stats.duplicates[fileName].push(relativePath);
    
  } catch (error) {
    stats.errors.push(`Error processing ${filePath}: ${error.message}`);
  }
}

// Process HTML files to extract structure and relationships
async function processHtmlFile(filePath, relativePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Extract basic metadata
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    const title = titleMatch ? titleMatch[1] : '';
    
    const descriptionMatch = content.match(/<meta name="description" content="(.*?)"/i);
    const description = descriptionMatch ? descriptionMatch[1] : '';
    
    // Extract CSS links
    const cssLinks = [];
    const cssMatches = content.matchAll(/<link[^>]*rel=["']stylesheet["'][^>]*href=["']([^"']+)["'][^>]*>/gi);
    for (const match of cssMatches) {
      cssLinks.push(match[1]);
    }
    
    // Extract JS scripts
    const jsScripts = [];
    const jsMatches = content.matchAll(/<script[^>]*src=["']([^"']+)["'][^>]*>/gi);
    for (const match of jsMatches) {
      jsScripts.push(match[1]);
    }
    
    // Extract internal links
    const internalLinks = [];
    const linkMatches = content.matchAll(/<a[^>]*href=["']([^"']+)["'][^>]*>/gi);
    for (const match of linkMatches) {
      const href = match[1];
      // Only include internal links (not external)
      if (!href.startsWith('http') && !href.startsWith('//') && !href.startsWith('mailto')) {
        internalLinks.push(href);
      }
    }
    
    // Extract component includes
    const components = [];
    const componentMatches = content.matchAll(/fetch\(["']([^"']+)["']\)\.then\(r=>r\.text\(\)\)\.then\(html=>{[^}]+innerHTML=html}/gi);
    for (const match of componentMatches) {
      components.push(match[1]);
    }
    
    // Determine page type based on path and content
    const pageType = determinePageType(relativePath, content);
    
    // Store relationships
    stats.relationships.set(relativePath, {
      type: pageType,
      cssLinks,
      jsScripts,
      internalLinks,
      components
    });
    
    // Store in GraphRAG
    await storeInGraphRAG({
      path: relativePath,
      type: 'html',
      pageType,
      title,
      description,
      cssLinks,
      jsScripts,
      internalLinks,
      components,
      content: content.substring(0, 1000) // Store first 1000 chars for search
    });
    
  } catch (error) {
    stats.errors.push(`Error processing HTML ${filePath}: ${error.message}`);
  }
}

// Process CSS files
async function processCssFile(filePath, relativePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Store in GraphRAG
    await storeInGraphRAG({
      path: relativePath,
      type: 'css',
      content: content.substring(0, 1000) // Store first 1000 chars
    });
    
  } catch (error) {
    stats.errors.push(`Error processing CSS ${filePath}: ${error.message}`);
  }
}

// Process JS files
async function processJsFile(filePath, relativePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Store in GraphRAG
    await storeInGraphRAG({
      path: relativePath,
      type: 'js',
      content: content.substring(0, 1000) // Store first 1000 chars
    });
    
  } catch (error) {
    stats.errors.push(`Error processing JS ${filePath}: ${error.message}`);
  }
}

// Determine page type based on path and content
function determinePageType(relativePath, content) {
  if (relativePath.endsWith('index.html')) {
    if (relativePath === 'index.html' || relativePath === 'public/index.html') {
      return 'homepage';
    } else if (relativePath.includes('/units/')) {
      return 'unit-index';
    } else if (relativePath.includes('/lessons/')) {
      return 'lesson-index';
    } else if (relativePath.includes('/handouts/')) {
      return 'handout-index';
    }
    return 'directory-index';
  }
  
  if (relativePath.includes('/login') || relativePath.includes('/auth')) {
    return 'authentication';
  }
  
  if (relativePath.includes('/dashboard')) {
    return 'dashboard';
  }
  
  if (relativePath.includes('/units/')) {
    return 'unit';
  }
  
  if (relativePath.includes('/lessons/')) {
    return 'lesson';
  }
  
  if (relativePath.includes('/handouts/')) {
    return 'handout';
  }
  
  if (relativePath.includes('/components/')) {
    return 'component';
  }
  
  return 'page';
}

// Store data in GraphRAG
async function storeInGraphRAG(data) {
  // Skip GraphRAG storage for now and just collect the data
  // This allows us to generate the complete report without schema issues
  return;
}

// Store content hierarchy in GraphRAG
async function storeContentHierarchy(data) {
  // Skip GraphRAG storage for now and just collect the data
  // This allows us to generate the complete report without schema issues
  return;
}

// Analyze relationships between files
function analyzeRelationships() {
  console.log('🔍 Analyzing file relationships...');
  
  // This could be expanded to build a more complex relationship graph
  // For now, we're just collecting the basic relationships in processHtmlFile
}

// Find duplicate files
function findDuplicates() {
  console.log('🔍 Finding duplicate files...');
  
  const duplicates = {};
  
  for (const [fileName, paths] of Object.entries(stats.duplicates)) {
    if (paths.length > 1) {
      // Filter out common files that are expected to be duplicated
      if (!['manifest', 'robots', 'favicon'].includes(fileName.toLowerCase())) {
        duplicates[fileName] = paths;
      }
    }
  }
  
  stats.duplicates = duplicates;
}

// Generate comprehensive report
function generateReport() {
  console.log('\n📊 COMPREHENSIVE SITE CRAWL REPORT\n');
  console.log(`Total Files: ${stats.totalFiles}`);
  console.log(`HTML Files: ${stats.htmlFiles}`);
  console.log(`CSS Files: ${stats.cssFiles}`);
  console.log(`JS Files: ${stats.jsFiles}`);
  console.log(`Image Files: ${stats.imageFiles}`);
  console.log(`Other Files: ${stats.otherFiles}`);
  
  console.log('\n🔗 DUPLICATE FILES:');
  for (const [fileName, paths] of Object.entries(stats.duplicates)) {
    console.log(`  ${fileName}: ${paths.length} copies`);
    paths.forEach(p => console.log(`    - ${p}`));
  }
  
  console.log('\n📄 PAGE TYPES:');
  const pageTypes = {};
  for (const [path, data] of stats.relationships.entries()) {
    if (!pageTypes[data.type]) {
      pageTypes[data.type] = 0;
    }
    pageTypes[data.type]++;
  }
  
  for (const [type, count] of Object.entries(pageTypes)) {
    console.log(`  ${type}: ${count}`);
  }
  
  if (stats.errors.length > 0) {
    console.log('\n❌ ERRORS:');
    stats.errors.forEach(error => console.log(`  ${error}`));
  }
  
  // Save detailed report to file
  const reportData = {
    timestamp: new Date().toISOString(),
    stats,
    relationships: Object.fromEntries(stats.relationships)
  };
  
  fs.writeFileSync(
    path.join(PROJECT_ROOT, 'site-crawl-report.json'),
    JSON.stringify(reportData, null, 2)
  );
  
  console.log('\n💾 Detailed report saved to site-crawl-report.json');
}

// Run the crawler
crawlSite().catch(console.error);
