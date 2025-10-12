// GraphRAG Activation for Intelligent Collaboration
const fs = require('fs');
const path = require('path');

class GraphRAGCoordinator {
    constructor() {
        this.knowledgeGraphPath = './te_kete_knowledge_graph.json';
        this.resourceDatabasePath = './graphrag_resource_database.js';
        this.mcpEndpoint = 'http://localhost:3001';
        this.conflictDetection = true;
        this.smartRecommendations = true;
    }

    async activate() {
        console.log('🧠 Activating GraphRAG for Intelligent Collaboration...');
        
        try {
            // Load knowledge graph
            const knowledgeGraph = this.loadKnowledgeGraph();
            console.log(`📊 Loaded ${knowledgeGraph.nodes?.length || 0} knowledge nodes`);
            
            // Load resource database
            const resourceDatabase = this.loadResourceDatabase();
            console.log(`📚 Loaded ${resourceDatabase.resources?.length || 0} resources`);
            
            // Detect CSS conflicts
            const conflicts = this.detectConflicts();
            console.log(`⚠️  Detected ${conflicts.length} conflicts`);
            
            // Generate smart recommendations
            const recommendations = this.generateRecommendations(conflicts);
            console.log(`💡 Generated ${recommendations.length} recommendations`);
            
            // Update MCP with intelligence
            await this.updateMCPWithIntelligence(conflicts, recommendations);
            
            console.log('✅ GraphRAG activation complete - Intelligent collaboration enabled!');
            return { conflicts, recommendations };
            
        } catch (error) {
            console.error('❌ GraphRAG activation failed:', error);
            return null;
        }
    }

    loadKnowledgeGraph() {
        try {
            const content = fs.readFileSync(this.knowledgeGraphPath, 'utf8');
            return JSON.parse(content);
        } catch (error) {
            console.log('📝 Knowledge graph not found, creating basic structure...');
            return { nodes: [], edges: [] };
        }
    }

    loadResourceDatabase() {
        try {
            const content = fs.readFileSync(this.resourceDatabasePath, 'utf8');
            // Extract resources from JS file
            const match = content.match(/const resources = (\[[\s\S]*?\]);/);
            if (match) {
                return eval(match[0]); // Safe in this controlled context
            }
            return { resources: [] };
        } catch (error) {
            console.log('📝 Resource database not found, creating basic structure...');
            return { resources: [] };
        }
    }

    detectConflicts() {
        const conflicts = [];
        
        // Check for CSS conflicts
        const cssFiles = this.findFiles('./public', '.css');
        const cssConflicts = this.analyzeCSSConflicts(cssFiles);
        conflicts.push(...cssConflicts);
        
        // Check for navigation inconsistencies
        const htmlFiles = this.findFiles('./public', '.html');
        const navConflicts = this.analyzeNavigationConflicts(htmlFiles);
        conflicts.push(...navConflicts);
        
        // Check for styling inconsistencies
        const styleConflicts = this.analyzeStyleConflicts(htmlFiles);
        conflicts.push(...styleConflicts);
        
        return conflicts;
    }

    findFiles(dir, extension) {
        const files = [];
        
        function traverse(currentDir) {
            const items = fs.readdirSync(currentDir);
            
            for (const item of items) {
                const fullPath = path.join(currentDir, item);
                const stat = fs.statSync(fullPath);
                
                if (stat.isDirectory() && !item.includes('node_modules')) {
                    traverse(fullPath);
                } else if (item.endsWith(extension)) {
                    files.push(fullPath);
                }
            }
        }
        
        traverse(dir);
        return files;
    }

    analyzeCSSConflicts(cssFiles) {
        const conflicts = [];
        
        // Check for multiple CSS files in HTML
        const htmlFiles = this.findFiles('./public', '.html');
        for (const htmlFile of htmlFiles) {
            const content = fs.readFileSync(htmlFile, 'utf8');
            const cssMatches = content.match(/<link[^>]*\.css[^>]*>/g) || [];
            
            if (cssMatches.length > 2) {
                conflicts.push({
                    type: 'css-overload',
                    file: htmlFile,
                    severity: 'high',
                    description: `Too many CSS files (${cssMatches.length}) causing conflicts`,
                    recommendation: 'Consolidate to single design system'
                });
            }
        }
        
        return conflicts;
    }

    analyzeNavigationConflicts(htmlFiles) {
        const conflicts = [];
        const navPatterns = {};
        
        for (const htmlFile of htmlFiles) {
            const content = fs.readFileSync(htmlFile, 'utf8');
            const navMatch = content.match(/<nav[^>]*>[\s\S]*?<\/nav>/g);
            
            if (navMatch) {
                const navHash = this.hashString(navMatch[0]);
                if (!navPatterns[navHash]) {
                    navPatterns[navHash] = [];
                }
                navPatterns[navHash].push(htmlFile);
            }
        }
        
        // Check for too many different navigation patterns
        const navPatternCount = Object.keys(navPatterns).length;
        if (navPatternCount > 3) {
            conflicts.push({
                type: 'navigation-inconsistency',
                severity: 'medium',
                description: `${navPatternCount} different navigation patterns found`,
                recommendation: 'Standardize to single navigation component'
            });
        }
        
        return conflicts;
    }

    analyzeStyleConflicts(htmlFiles) {
        const conflicts = [];
        
        for (const htmlFile of htmlFiles) {
            const content = fs.readFileSync(htmlFile, 'utf8');
            
            // Check for inline styles
            const inlineStyles = content.match(/style="[^"]*"/g) || [];
            if (inlineStyles.length > 10) {
                conflicts.push({
                    type: 'inline-style-overuse',
                    file: htmlFile,
                    severity: 'medium',
                    description: `${inlineStyles.length} inline styles found`,
                    recommendation: 'Move to CSS classes'
                });
            }
            
            // Check for conflicting color schemes
            const colorMatches = content.match(/#[0-9a-fA-F]{6}/g) || [];
            if (colorMatches.length > 20) {
                conflicts.push({
                    type: 'color-inconsistency',
                    file: htmlFile,
                    severity: 'low',
                    description: `${colorMatches.length} different color codes`,
                    recommendation: 'Use CSS variables for consistency'
                });
            }
        }
        
        return conflicts;
    }

    generateRecommendations(conflicts) {
        const recommendations = [];
        
        // Group conflicts by type
        const conflictTypes = {};
        for (const conflict of conflicts) {
            if (!conflictTypes[conflict.type]) {
                conflictTypes[conflict.type] = [];
            }
            conflictTypes[conflict.type].push(conflict);
        }
        
        // Generate recommendations for each type
        for (const [type, conflicts] of Object.entries(conflictTypes)) {
            switch (type) {
                case 'css-overload':
                    recommendations.push({
                        priority: 'high',
                        action: 'Consolidate CSS files',
                        description: 'Reduce to single design system (te-kete-professional.css)',
                        affectedFiles: conflicts.map(c => c.file)
                    });
                    break;
                    
                case 'navigation-inconsistency':
                    recommendations.push({
                        priority: 'medium',
                        action: 'Standardize navigation',
                        description: 'Implement single navigation component via header.html',
                        affectedFiles: conflicts.map(c => c.file)
                    });
                    break;
                    
                case 'inline-style-overuse':
                    recommendations.push({
                        priority: 'medium',
                        action: 'Convert inline styles to CSS classes',
                        description: 'Move inline styles to CSS for consistency',
                        affectedFiles: conflicts.map(c => c.file)
                    });
                    break;
                    
                case 'color-inconsistency':
                    recommendations.push({
                        priority: 'low',
                        action: 'Standardize color palette',
                        description: 'Use CSS variables for consistent colors',
                        affectedFiles: conflicts.map(c => c.file)
                    });
                    break;
            }
        }
        
        return recommendations;
    }

    async updateMCPWithIntelligence(conflicts, recommendations) {
        const intelligence = {
            timestamp: new Date().toISOString(),
            conflicts: conflicts,
            recommendations: recommendations,
            smartMode: true,
            graphragActive: true
        };
        
        try {
            const response = await fetch(`${this.mcpEndpoint}/update-progress`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    agent: 'GraphRAG',
                    page: 'Intelligence Analysis',
                    status: 'ACTIVE',
                    notes: `GraphRAG activated: ${conflicts.length} conflicts detected, ${recommendations.length} recommendations generated`
                })
            });
            
            return response.ok;
        } catch (error) {
            console.log('MCP update failed, but GraphRAG is still active');
            return false;
        }
    }

    hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32-bit integer
        }
        return hash.toString();
    }
}

// Activate GraphRAG
const graphrag = new GraphRAGCoordinator();
graphrag.activate().then(result => {
    if (result) {
        console.log('🎯 GraphRAG intelligence ready for collaborative agents!');
    }
}).catch(error => {
    console.error('GraphRAG activation failed:', error);
});
