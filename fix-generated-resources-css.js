const fs = require('fs');
const path = require('path');

// Directory containing generated resources
const resourcesDir = path.join(__dirname, 'public/generated-resources-alpha');

// Function to fix CSS paths in a file
function fixCssPaths(filePath) {
  try {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Replace absolute CSS paths with relative paths
    content = content.replace(/href="\/css\//g, 'href="css/');
    content = content.replace(/src="\/js\//g, 'src="js/');
    
    // Ensure te-kete-professional.css is included
    if (!content.includes('te-kete-professional.css') && content.includes('print.css')) {
      content = content.replace(
        /<link rel="stylesheet" href="css\/print\.css" media="print">/,
        '<link rel="stylesheet" href="css/te-kete-professional.css">\n    <link rel="stylesheet" href="css/print.css" media="print">'
      );
    }
    
    fs.writeFileSync(filePath, content);
    console.log(`Fixed: ${filePath}`);
    return true;
  } catch (error) {
    console.error(`Error fixing ${filePath}:`, error);
    return false;
  }
}

// Function to recursively find and fix HTML files
function fixDirectory(dir) {
  const files = fs.readdirSync(dir);
  let fixedCount = 0;
  
  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isDirectory()) {
      fixedCount += fixDirectory(filePath);
    } else if (path.extname(file) === '.html') {
      if (fixCssPaths(filePath)) {
        fixedCount++;
      }
    }
  });
  
  return fixedCount;
}

// Start fixing
console.log('Fixing CSS paths in generated-resources-alpha...');
const totalFixed = fixDirectory(resourcesDir);
console.log(`\nComplete! Fixed ${totalFixed} files.`);
