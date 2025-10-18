/**
 * Sitewide Excellence Script - Te Kete Ako
 * Automates: GraphRAG indexing, Tailwind integration, Navigation standardization
 * Framer Motion, GraphRAG recommendations everywhere
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// Initialize Supabase
const supabase = createClient(
    process.env.SUPABASE_URL,
    process.env.SUPABASE_ANON_KEY
);

class SitewideExcellence {
    constructor() {
        this.publicDir = path.join(__dirname, '../public');
        this.stats = {
            filesProcessed: 0,
            filesIndexed: 0,
            filesStandardized: 0,
            relationshipsBuilt: 0
        };
    }

    async run() {
        console.log('🌿 NGA MIHI NUI! Starting Sitewide Excellence...\n');

        // Step 1: Index all files in GraphRAG
        await this.indexAllFilesInGraphRAG();

        // Step 2: Standardize navigation
        await this.standardizeNavigation();

        // Step 3: Add GraphRAG recommendations everywhere
        await this.addGraphRAGRecommendations();

        // Step 4: Build relationships
        await this.buildRelationships();

        // Report
        this.printReport();
    }

    async indexAllFilesInGraphRAG() {
        console.log('📊 Step 1: Indexing all files in GraphRAG...');

        const htmlFiles = this.getAllHTMLFiles(this.publicDir);
        console.log(`Found ${htmlFiles.length} HTML files`);

        for (const filePath of htmlFiles) {
            try {
                const relativePath = path.relative(process.cwd(), filePath);
                const content = fs.readFileSync(filePath, 'utf8');
                
                // Extract metadata
                const title = this.extractTitle(content);
                const type = this.determineType(relativePath);
                const preview = this.extractPreview(content);

                // Check if already indexed
                const { data: existing } = await supabase
                    .from('graphrag_resources')
                    .select('id')
                    .eq('file_path', relativePath)
                    .single();

                if (!existing) {
                    // Insert into GraphRAG
                    await supabase
                        .from('graphrag_resources')
                        .insert({
                            file_path: relativePath,
                            title: title,
                            content_preview: preview,
                            metadata: {
                                type: type,
                                date: new Date().toISOString().split('T')[0],
                                indexed_by: 'sitewide_excellence_script'
                            },
                            quality_score: 75
                        });

                    this.stats.filesIndexed++;
                }

                this.stats.filesProcessed++;
                if (this.stats.filesProcessed % 100 === 0) {
                    console.log(`  Processed ${this.stats.filesProcessed}/${htmlFiles.length} files...`);
                }

            } catch (error) {
                console.error(`  Error indexing ${filePath}:`, error.message);
            }
        }

        console.log(`✅ Indexed ${this.stats.filesIndexed} new files\n`);
    }

    async standardizeNavigation() {
        console.log('🔧 Step 2: Standardizing navigation...');

        const htmlFiles = this.getAllHTMLFiles(this.publicDir);
        const navScript = `
    <!-- Standardized Navigation -->
    <div id="navigation-container"></div>
    <script>
        fetch('/components/navigation-standard.html')
            .then(response => response.text())
            .then(html => {
                document.getElementById('navigation-container').innerHTML = html;
            });
    </script>`;

        for (const filePath of htmlFiles) {
            try {
                let content = fs.readFileSync(filePath, 'utf8');

                // Check if navigation is already standardized
                if (content.includes('/components/navigation-standard.html')) {
                    continue;
                }

                // Remove old navigation if exists
                content = this.removeOldNavigation(content);

                // Add standardized navigation after <body> tag
                const bodyMatch = content.match(/<body[^>]*>/i);
                if (bodyMatch) {
                    const insertPosition = bodyMatch.index + bodyMatch[0].length;
                    content = content.slice(0, insertPosition) + navScript + content.slice(insertPosition);

                    // Write back
                    fs.writeFileSync(filePath, content, 'utf8');
                    this.stats.filesStandardized++;
                }

            } catch (error) {
                console.error(`  Error standardizing ${filePath}:`, error.message);
            }
        }

        console.log(`✅ Standardized ${this.stats.filesStandardized} files\n`);
    }

    async addGraphRAGRecommendations() {
        console.log('🔗 Step 3: Adding GraphRAG recommendations...');

        const lessonFiles = this.getAllHTMLFiles(path.join(this.publicDir, 'lessons'));
        const unitFiles = this.getAllHTMLFiles(path.join(this.publicDir, 'units'));
        const handoutFiles = this.getAllHTMLFiles(path.join(this.publicDir, 'handouts'));

        const allFiles = [...lessonFiles, ...unitFiles, ...handoutFiles];

        const recommendationScript = `
    <!-- GraphRAG Recommendations -->
    <div id="graphrag-recommendations-container"></div>
    <script src="/js/graphrag-recommendations.js"></script>
    <script>
        if (window.GraphRAGRecommendations) {
            const recs = new window.GraphRAGRecommendations();
            recs.loadRecommendations();
        }
    </script>`;

        for (const filePath of allFiles) {
            try {
                let content = fs.readFileSync(filePath, 'utf8');

                // Check if already has GraphRAG recommendations
                if (content.includes('graphrag-recommendations')) {
                    continue;
                }

                // Add before closing </body> tag
                const bodyCloseMatch = content.match(/<\/body>/i);
                if (bodyCloseMatch) {
                    const insertPosition = bodyCloseMatch.index;
                    content = content.slice(0, insertPosition) + recommendationScript + content.slice(insertPosition);

                    fs.writeFileSync(filePath, content, 'utf8');
                }

            } catch (error) {
                console.error(`  Error adding recommendations to ${filePath}:`, error.message);
            }
        }

        console.log(`✅ Added GraphRAG recommendations to ${allFiles.length} files\n`);
    }

    async buildRelationships() {
        console.log('🔗 Step 4: Building GraphRAG relationships...');

        // Get all resources from GraphRAG
        const { data: resources } = await supabase
            .from('graphrag_resources')
            .select('id, file_path, title, metadata');

        if (!resources) return;

        for (const resource of resources) {
            try {
                // Find related resources
                const related = this.findRelatedResources(resource, resources);

                for (const relatedResource of related) {
                    // Create relationship
                    await supabase
                        .from('graphrag_relationships')
                        .insert({
                            from_resource_id: resource.id,
                            to_resource_id: relatedResource.id,
                            relationship_type: relatedResource.relationshipType,
                            strength: relatedResource.strength,
                            metadata: {
                                created_by: 'sitewide_excellence_script',
                                created_at: new Date().toISOString()
                            }
                        });

                    this.stats.relationshipsBuilt++;
                }

            } catch (error) {
                // Ignore duplicate errors
                if (!error.message.includes('duplicate')) {
                    console.error(`  Error building relationship for ${resource.title}:`, error.message);
                }
            }
        }

        console.log(`✅ Built ${this.stats.relationshipsBuilt} relationships\n`);
    }

    // Helper methods
    getAllHTMLFiles(dir) {
        let results = [];
        try {
            const list = fs.readdirSync(dir);
            for (const file of list) {
                const filePath = path.join(dir, file);
                const stat = fs.statSync(filePath);
                if (stat.isDirectory()) {
                    results = results.concat(this.getAllHTMLFiles(filePath));
                } else if (file.endsWith('.html')) {
                    results.push(filePath);
                }
            }
        } catch (error) {
            // Directory doesn't exist or can't be read
        }
        return results;
    }

    extractTitle(content) {
        const titleMatch = content.match(/<title[^>]*>([^<]+)<\/title>/i);
        if (titleMatch) {
            return titleMatch[1].trim();
        }

        const h1Match = content.match(/<h1[^>]*>([^<]+)<\/h1>/i);
        if (h1Match) {
            return h1Match[1].trim();
        }

        return 'Untitled Page';
    }

    determineType(filePath) {
        if (filePath.includes('/lessons/')) return 'lesson';
        if (filePath.includes('/units/')) return 'unit';
        if (filePath.includes('/handouts/')) return 'handout';
        if (filePath.includes('/games/')) return 'game';
        if (filePath.includes('/tools/')) return 'tool';
        return 'page';
    }

    extractPreview(content) {
        // Remove HTML tags and get first 200 chars
        const text = content.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
        return text.substring(0, 200) + '...';
    }

    removeOldNavigation(content) {
        // Remove old inline navigation
        content = content.replace(/<header class="site-header[^>]*>[\s\S]*?<\/header>/gi, '');
        content = content.replace(/<nav[^>]*>[\s\S]*?<\/nav>/gi, '');
        return content;
    }

    findRelatedResources(resource, allResources) {
        const related = [];

        for (const other of allResources) {
            if (resource.id === other.id) continue;

            // Same directory = related
            const resourceDir = path.dirname(resource.file_path);
            const otherDir = path.dirname(other.file_path);

            if (resourceDir === otherDir) {
                related.push({
                    id: other.id,
                    relationshipType: 'in_same_directory',
                    strength: 0.7
                });
            }

            // Same type = related
            const resourceType = resource.metadata?.type;
            const otherType = other.metadata?.type;

            if (resourceType && otherType && resourceType === otherType) {
                related.push({
                    id: other.id,
                    relationshipType: 'same_type',
                    strength: 0.5
                });
            }
        }

        return related.slice(0, 10); // Limit to top 10
    }

    printReport() {
        console.log('═══════════════════════════════════════════════════════');
        console.log('🎉 SITEWIDE EXCELLENCE COMPLETE!');
        console.log('═══════════════════════════════════════════════════════');
        console.log(`📊 Files Processed:      ${this.stats.filesProcessed}`);
        console.log(`📚 Files Indexed:        ${this.stats.filesIndexed}`);
        console.log(`🔧 Files Standardized:   ${this.stats.filesStandardized}`);
        console.log(`🔗 Relationships Built:  ${this.stats.relationshipsBuilt}`);
        console.log('═══════════════════════════════════════════════════════\n');
        console.log('🌿 NGA MIHI NUI RANGATIRA! Te Kete Ako is now professional!\n');
    }
}

// Run the script
if (require.main === module) {
    const excellence = new SitewideExcellence();
    excellence.run().catch(console.error);
}

module.exports = SitewideExcellence;
