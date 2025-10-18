#!/usr/bin/env node
/**
 * Batch add missing meta descriptions to generated-resources-alpha files
 * Improves SEO and social media sharing
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Files missing meta descriptions from resource-integrity-report.json
const filesToFix = [
    'biotechnology-ethics-through-māori-worldview.html',
    'calculus-applications-in-environmental-modeling.html',
    'chemistry-of-traditional-māori-medicine.html',
    'chromebook-optimized-mobile-learning-guide.html',
    'coding-projects-inspired-by-māori-patterns.html',
    'cultural-safety-checklists-for-classroom-discussions.html',
    'data-visualization-of-cultural-demographics.html',
    'financial-literacy-with-māori-economic-principles.html',
    'global-citizenship-with-tangata-whenua-perspective.html',
    'leadership-development-through-cultural-values.html',
    'mathematical-modeling-of-ecological-systems.html',
    'ncea-level-1-literacy-and-numeracy-must-knows.html',
    'te-reo-maths-glossary-key-terms-in-māori-and-english.html',
    'year-9-starter-pack-essential-skills-for-high-school-success.html'
];

const lessonFilesToFix = [
    'ai-ethics-through-māori-data-sovereignty-FIXED.html',
    'ai-ethics-through-māori-data-sovereignty.html',
    'career-pathways-in-stem-for-māori-students.html',
    'climate-change-through-te-taiao-māori-lens.html',
    'creative-writing-inspired-by-whakataukī.html',
    'critical-analysis-of-historical-documents.html',
    'debate-skills-with-māori-oratory-traditions.html',
    'digital-storytelling-with-pūrākau-framework.html',
    'genetics-and-whakapapa-scientific-and-cultural-perspectives.html',
    'health-and-wellbeing-te-whare-tapa-whā-model.html',
    'physics-of-traditional-māori-instruments.html',
    'poetry-analysis-through-māori-literary-traditions.html',
    'renewable-energy-and-māori-innovation.html',
    'scientific-method-using-traditional-māori-practices.html',
    'statistical-analysis-of-sports-performance.html',
    'traditional-navigation-and-modern-gps-integration.html'
];

function generateDescription(filename, type) {
    // Extract meaningful description from filename
    const name = filename.replace('.html', '').split('-').join(' ');
    const capitalizedName = name.charAt(0).toUpperCase() + name.slice(1);
    
    if (type === 'handout') {
        return `${capitalizedName} - Print-ready educational handout integrating mātauranga Māori with NZ curriculum (Years 7-13) | Te Kete Ako`;
    } else {
        return `${capitalizedName} - Complete lesson plan with cultural integration for NZ classrooms (Years 9-13) | Te Kete Ako`;
    }
}

function addMetaDescription(filePath, description) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Check if meta description already exists
        if (content.includes('<meta name="description"')) {
            console.log(`✓ Already has description: ${path.basename(filePath)}`);
            return false;
        }
        
        // Find the title tag and add description after it
        const titleMatch = content.match(/(<title>.*?<\/title>)/);
        if (titleMatch) {
            const metaTag = `\n    <meta name="description" content="${description}">`;
            content = content.replace(titleMatch[0], titleMatch[0] + metaTag);
            
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✓ Added description: ${path.basename(filePath)}`);
            return true;
        } else {
            console.log(`✗ No title tag found: ${path.basename(filePath)}`);
            return false;
        }
    } catch (err) {
        console.error(`✗ Error processing ${filePath}: ${err.message}`);
        return false;
    }
}

// Process handouts
console.log('\n📄 Processing Handouts...\n');
let handoutCount = 0;
filesToFix.forEach(filename => {
    const filePath = path.join(__dirname, '../public/generated-resources-alpha/handouts', filename);
    if (fs.existsSync(filePath)) {
        const description = generateDescription(filename, 'handout');
        if (addMetaDescription(filePath, description)) {
            handoutCount++;
        }
    } else {
        console.log(`✗ File not found: ${filename}`);
    }
});

// Process lessons
console.log('\n🎓 Processing Lessons...\n');
let lessonCount = 0;
lessonFilesToFix.forEach(filename => {
    const filePath = path.join(__dirname, '../public/generated-resources-alpha/lessons', filename);
    if (fs.existsSync(filePath)) {
        const description = generateDescription(filename, 'lesson');
        if (addMetaDescription(filePath, description)) {
            lessonCount++;
        }
    } else {
        console.log(`✗ File not found: ${filename}`);
    }
});

console.log(`\n✅ Complete! Added ${handoutCount} handout descriptions and ${lessonCount} lesson descriptions.`);
console.log(`📊 Total: ${handoutCount + lessonCount} files updated.\n`);

