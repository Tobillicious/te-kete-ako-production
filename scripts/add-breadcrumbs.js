#!/usr/bin/env node
/**
 * Add Breadcrumb Navigation to Orphaned Pages
 * Systematically adds breadcrumb navigation to generated resources
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const BREADCRUMB_TEMPLATE = `
    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumbs no-print" aria-label="Breadcrumb" style="padding: 1rem 0; margin-bottom: 1rem;">
        <a href="/index.html">🏠 Home</a> → 
        <a href="/handouts.html">📄 Handouts</a> → 
        <span>{{PAGE_TITLE}}</span>
    </nav>
`;

const LESSON_BREADCRUMB_TEMPLATE = `
    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumbs no-print" aria-label="Breadcrumb" style="padding: 1rem 0; margin-bottom: 1rem;">
        <a href="/index.html">🏠 Home</a> → 
        <a href="/lessons.html">📖 Lessons</a> → 
        <span>{{PAGE_TITLE}}</span>
    </nav>
`;

function extractTitle(htmlContent) {
    const match = htmlContent.match(/<title>(.*?)<\/title>/);
    return match ? match[1].replace(' | Te Kete Ako', '').trim() : 'Resource';
}

function addBreadcrumbs(filePath, isLesson = false) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Skip if already has breadcrumbs
        if (content.includes('breadcrumb') || content.includes('Breadcrumb')) {
            console.log(`⏭️  Skipping (has breadcrumbs): ${path.basename(filePath)}`);
            return false;
        }
        
        const title = extractTitle(content);
        const template = isLesson ? LESSON_BREADCRUMB_TEMPLATE : BREADCRUMB_TEMPLATE;
        const breadcrumb = template.replace('{{PAGE_TITLE}}', title);
        
        // Insert after <body> tag or first header
        if (content.includes('<body')) {
            content = content.replace(/(<body[^>]*>)/i, `$1${breadcrumb}`);
        } else if (content.includes('<header')) {
            content = content.replace(/(<header[^>]*>)/i, `${breadcrumb}$1`);
        } else {
            // Fallback: add at beginning of content
            content = breadcrumb + content;
        }
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Added breadcrumbs: ${path.basename(filePath)}`);
        return true;
    } catch (error) {
        console.error(`❌ Error processing ${filePath}:`, error.message);
        return false;
    }
}

function processDirectory(dirPath, isLesson = false) {
    const files = fs.readdirSync(dirPath);
    let count = 0;
    
    files.forEach(file => {
        if (file.endsWith('.html')) {
            const filePath = path.join(dirPath, file);
            if (addBreadcrumbs(filePath, isLesson)) {
                count++;
            }
        }
    });
    
    return count;
}

// Main execution
console.log('🧭 Adding Breadcrumbs to Generated Resources\n');

const handoutsDir = path.join(__dirname, '../public/generated-resources-alpha/handouts');
const lessonsDir = path.join(__dirname, '../public/generated-resources-alpha/lessons');

console.log('Processing handouts...');
const handoutsCount = processDirectory(handoutsDir, false);

console.log('\nProcessing lessons...');
const lessonsCount = processDirectory(lessonsDir, true);

console.log(`\n✅ Complete! Added breadcrumbs to ${handoutsCount + lessonsCount} files`);
console.log(`   - Handouts: ${handoutsCount}`);
console.log(`   - Lessons: ${lessonsCount}`);

