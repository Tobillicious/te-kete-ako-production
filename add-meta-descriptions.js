#!/usr/bin/env node
/**
 * Add Meta Descriptions to AI-Generated Resources
 * Adds SEO-friendly meta descriptions to resources that are missing them
 */

const fs = require('fs');
const path = require('path');

// Files missing meta descriptions and their appropriate descriptions
const metaDescriptions = {
  // Handouts
  'biotechnology-ethics-through-māori-worldview.html': 'Explore biotechnology ethics through a Māori worldview. Handout integrating traditional knowledge with contemporary bioethics for NZ classrooms.',
  'calculus-applications-in-environmental-modeling.html': 'Learn calculus applications in environmental modeling. Handout connecting mathematical concepts with ecological systems for Years 12-13.',
  'chemistry-of-traditional-māori-medicine.html': 'Discover the chemistry of traditional Māori medicine (rongoā). Handout exploring scientific principles in indigenous healing practices.',
  'chromebook-optimized-mobile-learning-guide.html': 'Chromebook-optimized mobile learning guide. Practical tips for effective digital learning in NZ classrooms with limited bandwidth.',
  'coding-projects-inspired-by-māori-patterns.html': 'Create coding projects inspired by Māori patterns and kōwhaiwhai. Programming handout integrating cultural design with computer science.',
  'cultural-safety-checklists-for-classroom-discussions.html': 'Cultural safety checklists for classroom discussions. Guide for creating respectful, inclusive learning environments in diverse NZ classrooms.',
  'data-visualization-of-cultural-demographics.html': 'Learn data visualization of cultural demographics. Handout exploring statistics and representation with NZ Census and cultural data.',
  'financial-literacy-with-māori-economic-principles.html': 'Financial literacy through Māori economic principles. Handout integrating traditional concepts like manaakitanga with modern financial skills.',
  'global-citizenship-with-tangata-whenua-perspective.html': 'Explore global citizenship from a tangata whenua perspective. Handout connecting local indigenous knowledge with global citizenship.',
  'leadership-development-through-cultural-values.html': 'Leadership development through cultural values. Handout exploring Māori leadership principles for contemporary contexts.',
  'mathematical-modeling-of-ecological-systems.html': 'Mathematical modeling of ecological systems. Handout connecting algebra and calculus with environmental science and kaitiakitanga.',
  'ncea-level-1-literacy-and-numeracy-must-knows.html': 'NCEA Level 1 literacy and numeracy must-knows. Essential skills and strategies for success in NCEA co-requisites.',
  'te-reo-maths-glossary-key-terms-in-māori-and-english.html': 'Te Reo Māori maths glossary with key terms in Māori and English. Essential vocabulary for bilingual mathematics learning.',
  'year-9-starter-pack-essential-skills-for-high-school-success.html': 'Year 9 starter pack with essential skills for high school success. Handout covering study skills, organization, and learning strategies.',
  
  // Lessons
  'ai-ethics-through-māori-data-sovereignty-FIXED.html': 'AI ethics through Māori data sovereignty. Lesson exploring ethical AI development through indigenous data governance principles.',
  'ai-ethics-through-māori-data-sovereignty.html': 'AI ethics through Māori data sovereignty. Lesson exploring ethical AI development through indigenous data governance principles.',
  'career-pathways-in-stem-for-māori-students.html': 'Explore career pathways in STEM for Māori students. Lesson connecting cultural identity with science, technology, and innovation careers.',
  'climate-change-through-te-taiao-māori-lens.html': 'Climate change through te taiao Māori lens. Lesson integrating indigenous environmental knowledge with climate science.',
  'creative-writing-inspired-by-whakataukī.html': 'Creative writing inspired by whakataukī (Māori proverbs). Lesson using traditional wisdom as springboard for narrative and poetic writing.',
  'critical-analysis-of-historical-documents.html': 'Critical analysis of historical documents. Lesson developing source evaluation skills with Treaty of Waitangi and colonial texts.',
  'debate-skills-with-māori-oratory-traditions.html': 'Debate skills with Māori oratory traditions. Lesson integrating whaikōrero principles with contemporary argumentation techniques.',
  'digital-storytelling-with-pūrākau-framework.html': 'Digital storytelling with pūrākau framework. Lesson blending traditional Māori narrative structures with multimedia creation.',
  'genetics-and-whakapapa-scientific-and-cultural-perspectives.html': 'Genetics and whakapapa from scientific and cultural perspectives. Lesson connecting biological heredity with genealogical knowledge.',
  'health-and-wellbeing-te-whare-tapa-whā-model.html': 'Health and wellbeing through te whare tapa whā model. Lesson exploring holistic Māori health framework for personal wellness.',
  'physics-of-traditional-māori-instruments.html': 'Physics of traditional Māori instruments. Lesson exploring sound waves, resonance, and acoustics through pūtōrino, pūkāea, and pūtātara.',
  'poetry-analysis-through-māori-literary-traditions.html': 'Poetry analysis through Māori literary traditions. Lesson connecting waiata, mōteatea, and contemporary Māori poetry.',
  'renewable-energy-and-māori-innovation.html': 'Renewable energy and Māori innovation. Lesson exploring sustainable energy solutions through indigenous environmental stewardship.',
  'scientific-method-using-traditional-māori-practices.html': 'Scientific method using traditional Māori practices. Lesson connecting empirical inquiry with mātauranga Māori research methodologies.',
  'statistical-analysis-of-sports-performance.html': 'Statistical analysis of sports performance. Lesson using data from NZ sports to teach descriptive and inferential statistics.',
  'traditional-navigation-and-modern-gps-integration.html': 'Traditional navigation and modern GPS integration. Lesson connecting Polynesian wayfinding techniques with contemporary satellite technology.'
};

// Function to add meta description to a file
function addMetaDescription(filePath, description) {
  try {
    let content = fs.readFileSync(filePath, 'utf-8');
    
    // Check if meta description already exists
    if (content.includes('<meta name="description"')) {
      console.log(`⏭️  Skipped: ${path.basename(filePath)} (already has meta description)`);
      return false;
    }
    
    // Find the title tag and add meta description after it
    const titleMatch = content.match(/(<title>.*?<\/title>)/);
    if (!titleMatch) {
      console.log(`⚠️  Warning: No title tag found in ${path.basename(filePath)}`);
      return false;
    }
    
    const titleTag = titleMatch[1];
    const metaTag = `\n    <meta name="description" content="${description}">`;
    
    // Insert meta description after title tag
    content = content.replace(titleTag, titleTag + metaTag);
    
    // Write back to file
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`✅ Added: ${path.basename(filePath)}`);
    return true;
    
  } catch (error) {
    console.error(`❌ Error processing ${filePath}:`, error.message);
    return false;
  }
}

// Main execution
function main() {
  const handoutsDir = '/Users/admin/Documents/te-kete-ako-clean/public/generated-resources-alpha/handouts';
  const lessonsDir = '/Users/admin/Documents/te-kete-ako-clean/public/generated-resources-alpha/lessons';
  
  let successCount = 0;
  let skipCount = 0;
  let errorCount = 0;
  
  console.log('\n🚀 Adding meta descriptions to AI-generated resources...\n');
  console.log('📄 Processing handouts...\n');
  
  // Process each file
  for (const [filename, description] of Object.entries(metaDescriptions)) {
    let filePath;
    
    // Determine if it's a handout or lesson
    if (filename.includes('handout') || 
        ['biotechnology-ethics', 'calculus-applications', 'chemistry-of', 'chromebook-optimized',
         'coding-projects', 'cultural-safety', 'data-visualization', 'financial-literacy',
         'global-citizenship', 'leadership-development', 'mathematical-modeling', 'ncea-level',
         'te-reo-maths', 'year-9-starter'].some(pattern => filename.includes(pattern))) {
      filePath = path.join(handoutsDir, filename);
    } else {
      filePath = path.join(lessonsDir, filename);
    }
    
    if (!fs.existsSync(filePath)) {
      console.log(`⚠️  File not found: ${filename}`);
      errorCount++;
      continue;
    }
    
    const result = addMetaDescription(filePath, description);
    if (result === true) {
      successCount++;
    } else if (result === false && !fs.readFileSync(filePath, 'utf-8').includes('<meta name="description"')) {
      errorCount++;
    } else {
      skipCount++;
    }
  }
  
  console.log('\n' + '='.repeat(60));
  console.log('📊 Summary:');
  console.log(`✅ Successfully added: ${successCount}`);
  console.log(`⏭️  Skipped (already exists): ${skipCount}`);
  console.log(`❌ Errors: ${errorCount}`);
  console.log('='.repeat(60) + '\n');
  
  if (successCount > 0) {
    console.log('🎉 Meta descriptions added successfully!');
    console.log('💡 Tip: Run the test-resources-integrity.js script to verify all resources now pass.\n');
  }
}

main();

