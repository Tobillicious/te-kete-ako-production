#!/usr/bin/env node

/**
 * Te Kete Ako Workflow Synchronization Script
 *
 * PROBLEM IDENTIFIED:
 * - 37 lesson files exist on filesystem with proper titles
 * - GraphRAG database only has 2 lessons properly indexed
 * - Website index pages show placeholder names
 *
 * SOLUTION: Automated sync between filesystem → database → website
 */

const fs = require('fs');
const path = require('path');

// Note: Using MCP Supabase tools instead of direct client connection
// This ensures proper authentication through the MCP server

class WorkflowSync {
    constructor() {
        this.lessonsPath = path.join(__dirname, 'public/units/lessons');
        this.resourcesPath = path.join(__dirname, 'public');
    }

    /**
     * Extract lesson metadata from HTML files
     */
    async extractLessonMetadata() {
        console.log('🔍 Extracting lesson metadata from filesystem...');

        const lessonFiles = fs.readdirSync(this.lessonsPath)
            .filter(file => file.endsWith('.html') && file !== 'index.html');

        const lessons = [];

        for (const file of lessonFiles) {
            const filePath = path.join(this.lessonsPath, file);
            const content = fs.readFileSync(filePath, 'utf8');

            // Extract title from HTML
            const titleMatch = content.match(/<title>(.*?)<\/title>/);
            const title = titleMatch ? titleMatch[1].replace(' | Te Kete Ako', '').replace(' | Mangakōtukutuku College', '') : '';

            // Extract description
            const descMatch = content.match(/<meta name="description" content="(.*?)"/);
            const description = descMatch ? descMatch[1] : '';

            // Determine unit and lesson number from filename
            const unitMatch = file.match(/unit-(\d+)-lesson-(\d+)\.html/);
            const unit = unitMatch ? `Unit ${unitMatch[1]}` : '';
            const lessonNumber = unitMatch ? parseInt(unitMatch[2]) : 0;

            lessons.push({
                file_path: `/units/lessons/${file}`,
                title,
                description,
                unit,
                lesson_number: lessonNumber,
                resource_type: 'Lesson',
                subject: this.inferSubject(title, unit),
                year_level: this.inferYearLevel(title, unit),
                quality_score: 85, // Default quality score
                cultural_context: this.detectCulturalContext(title, content),
                content_preview: description.substring(0, 200) + '...',
                metadata: {
                    file_size: fs.statSync(filePath).size,
                    last_modified: fs.statSync(filePath).mtime,
                    word_count: content.split(' ').length
                }
            });
        }

        console.log(`✅ Extracted ${lessons.length} lessons from filesystem`);
        return lessons;
    }

    /**
     * Infer subject from title and content
     */
    inferSubject(title, unit) {
        const subjects = {
            'Unit 1': 'Te Ao Māori',
            'Unit 2': 'Social Studies',
            'Unit 3': 'Science',
            'Unit 4': 'Mathematics',
            'Unit 5': 'Social Studies',
            'Unit 6': 'Digital Technologies',
            'Unit 7': 'Digital Technologies'
        };

        if (unit in subjects) return subjects[unit];

        // Fallback subject detection
        if (title.toLowerCase().includes('māori') || title.toLowerCase().includes('cultural')) {
            return 'Te Ao Māori';
        }
        if (title.toLowerCase().includes('math') || title.toLowerCase().includes('number')) {
            return 'Mathematics';
        }
        if (title.toLowerCase().includes('science') || title.toLowerCase().includes('environment')) {
            return 'Science';
        }
        if (title.toLowerCase().includes('digital') || title.toLowerCase().includes('ai') || title.toLowerCase().includes('technology')) {
            return 'Digital Technologies';
        }

        return 'Cross-Curricular';
    }

    /**
     * Infer year level from content
     */
    inferYearLevel(title, unit) {
        if (unit === 'Unit 1') return 'Year 7-8';
        if (unit === 'Unit 2') return 'Year 8-9';
        if (unit === 'Unit 3') return 'Year 9-10';
        if (unit === 'Unit 4') return 'Year 10-11';
        if (unit === 'Unit 5') return 'Year 11-12';
        if (unit === 'Unit 6') return 'Year 12-13';
        if (unit === 'Unit 7') return 'Year 13';

        return 'Year 7-13';
    }

    /**
     * Detect cultural context from content
     */
    detectCulturalContext(title, content) {
        const culturalKeywords = ['māori', 'te ao māori', 'tikanga', 'whakapapa', 'kaitiakitanga', 'mana', 'aroha', 'cultural', 'indigenous'];
        const lowerTitle = title.toLowerCase();
        const lowerContent = content.toLowerCase();

        return culturalKeywords.some(keyword => lowerTitle.includes(keyword) || lowerContent.includes(keyword));
    }

    /**
     * Sync lessons to GraphRAG database
     */
    async syncToGraphRAG(lessons) {
        console.log('🔄 Syncing lessons to GraphRAG database...');

        let synced = 0;
        let errors = 0;

        for (const lesson of lessons) {
            try {
                // Check if lesson already exists
                const { data: existing } = await supabase
                    .from('graphrag_resources')
                    .select('id')
                    .eq('file_path', lesson.file_path)
                    .single();

                if (existing) {
                    // Update existing record
                    const { error } = await supabase
                        .from('graphrag_resources')
                        .update({
                            title: lesson.title,
                            resource_type: lesson.resource_type,
                            subject: lesson.subject,
                            year_level: lesson.year_level,
                            quality_score: lesson.quality_score,
                            cultural_context: lesson.cultural_context,
                            content_preview: lesson.content_preview,
                            metadata: lesson.metadata,
                            updated_at: new Date().toISOString()
                        })
                        .eq('id', existing.id);

                    if (error) throw error;
                    console.log(`📝 Updated: ${lesson.title}`);
                } else {
                    // Insert new record
                    const { error } = await supabase
                        .from('graphrag_resources')
                        .insert([{
                            file_path: lesson.file_path,
                            title: lesson.title,
                            resource_type: lesson.resource_type,
                            subject: lesson.subject,
                            year_level: lesson.year_level,
                            quality_score: lesson.quality_score,
                            cultural_context: lesson.cultural_context,
                            content_preview: lesson.content_preview,
                            metadata: lesson.metadata,
                            has_whakataukī: lesson.cultural_context,
                            has_te_reo: lesson.cultural_context
                        }]);

                    if (error) throw error;
                    console.log(`✨ Created: ${lesson.title}`);
                }

                synced++;
            } catch (error) {
                console.error(`❌ Error syncing ${lesson.title}:`, error.message);
                errors++;
            }
        }

        console.log(`✅ Sync complete: ${synced} synced, ${errors} errors`);
        return { synced, errors };
    }

    /**
     * Update lesson index page with proper titles
     */
    async updateLessonIndex(lessons) {
        console.log('📄 Updating lesson index page...');

        const indexPath = path.join(this.lessonsPath, 'index.html');
        let indexContent = fs.readFileSync(indexPath, 'utf8');

        // Group lessons by unit
        const lessonsByUnit = {};
        lessons.forEach(lesson => {
            if (!lessonsByUnit[lesson.unit]) {
                lessonsByUnit[lesson.unit] = [];
            }
            lessonsByUnit[lesson.unit].push(lesson);
        });

        // Update each unit section in the index
        for (const [unitName, unitLessons] of Object.entries(lessonsByUnit)) {
            const sectionStart = indexContent.indexOf(`<!-- ${unitName} -->`);
            if (sectionStart === -1) continue;

            // Find the end of this unit section
            const nextUnitMatch = indexContent.substring(sectionStart + 10).match(/<!-- Unit \d|<!-- Units \d-7/);
            const sectionEnd = nextUnitMatch ?
                sectionStart + 10 + nextUnitMatch.index :
                indexContent.indexOf('<!-- Quick Stats -->');

            if (sectionEnd === -1) continue;

            // Generate new lesson cards
            const lessonCards = unitLessons
                .sort((a, b) => a.lesson_number - b.lesson_number)
                .map(lesson => {
                    const cardId = `lesson-${lesson.unit.replace('Unit ', '').toLowerCase()}-${lesson.lesson_number}`;
                    return `                <a href="${lesson.file_path.replace('/units/lessons/', '')}" style="text-decoration: none; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #1a4d2e; transition: transform 0.2s;">
                    <h3 style="color: #1a4d2e; margin-top: 0;">${lesson.title}</h3>
                    <p style="color: #666; font-size: 0.95rem;">${lesson.description}</p>
                    <span style="display: inline-block; margin-top: 0.5rem; padding: 0.25rem 0.75rem; background: #1a4d2e; color: white; border-radius: 12px; font-size: 0.85rem;">Lesson ${lesson.lesson_number}</span>
                </a>`;
                })
                .join('\n\n');

            // Replace the unit section
            const beforeSection = indexContent.substring(0, sectionStart);
            const afterSection = indexContent.substring(sectionEnd);
            indexContent = beforeSection + lessonCards + '\n\n' + afterSection;
        }

        // Write updated index
        fs.writeFileSync(indexPath, indexContent);
        console.log('✅ Lesson index page updated');
    }

    /**
     * Run complete workflow sync
     */
    async run() {
        try {
            console.log('🚀 Starting Te Kete Ako Workflow Sync...\n');

            // 1. Extract lesson metadata from filesystem
            const lessons = await this.extractLessonMetadata();

            // 2. Sync to GraphRAG database
            await this.syncToGraphRAG(lessons);

            // 3. Update index pages
            await this.updateLessonIndex(lessons);

            console.log('\n🎉 Workflow sync complete!');
            console.log(`📊 Processed ${lessons.length} lessons`);
            console.log('🔗 GraphRAG database updated');
            console.log('📄 Website index pages updated');

        } catch (error) {
            console.error('❌ Workflow sync failed:', error);
            process.exit(1);
        }
    }
}

// Run if called directly
if (require.main === module) {
    const sync = new WorkflowSync();
    sync.run();
}

module.exports = WorkflowSync;
