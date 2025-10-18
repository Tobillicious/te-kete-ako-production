/**
 * Content Hierarchy Automation - GraphRAG Powered
 * Auto-organizes Units → Lessons → Handouts using relationship data
 * Modernized version of legacy content-hierarchy.js
 */

class ContentHierarchyAuto {
    constructor() {
        this.supabase = null;
        this.hierarchy = {};
    }

    async init() {
        const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
        
        this.supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
        await this.buildHierarchy();
    }

    /**
     * Build complete content hierarchy from GraphRAG relationships
     */
    async buildHierarchy() {
        try {
            // Get all unit→lesson relationships (12,829 in GraphRAG!)
            const { data: unitLessons } = await this.supabase
                .from('graphrag_relationships')
                .select('source_path, target_path')
                .eq('relationship_type', 'unit_contains_lesson');

            // Get all lesson→handout relationships (602 in GraphRAG!)
            const { data: lessonHandouts } = await this.supabase
                .from('graphrag_relationships')
                .select('source_path, target_path')
                .eq('relationship_type', 'has_handout');

            // Build hierarchy structure
            this.hierarchy = {};
            
            unitLessons?.forEach(rel => {
                const unit = rel.source_path;
                const lesson = rel.target_path;
                
                if (!this.hierarchy[unit]) {
                    this.hierarchy[unit] = { lessons: [], handouts: {} };
                }
                this.hierarchy[unit].lessons.push(lesson);
                this.hierarchy[unit].handouts[lesson] = [];
            });

            // Add handouts to lessons
            lessonHandouts?.forEach(rel => {
                const lesson = rel.source_path;
                const handout = rel.target_path;
                
                // Find which unit this lesson belongs to
                for (const unit in this.hierarchy) {
                    if (this.hierarchy[unit].lessons.includes(lesson)) {
                        this.hierarchy[unit].handouts[lesson].push(handout);
                    }
                }
            });

            console.log('✅ Content hierarchy built from GraphRAG');
            console.log(`📊 ${Object.keys(this.hierarchy).length} units organized`);
            
        } catch (error) {
            console.error('Error building hierarchy:', error);
        }
    }

    /**
     * Get all lessons for a unit
     */
    getLessons(unitPath) {
        return this.hierarchy[unitPath]?.lessons || [];
    }

    /**
     * Get all handouts for a lesson
     */
    getHandouts(lessonPath) {
        for (const unit in this.hierarchy) {
            if (this.hierarchy[unit].handouts[lessonPath]) {
                return this.hierarchy[unit].handouts[lessonPath];
            }
        }
        return [];
    }

    /**
     * Auto-generate unit index page HTML
     */
    async generateUnitPage(unitPath) {
        const lessons = this.getLessons(unitPath);
        
        if (lessons.length === 0) return null;

        // Get lesson details from GraphRAG
        const { data: lessonDetails } = await this.supabase
            .from('graphrag_resources')
            .select('*')
            .in('file_path', lessons);

        let html = `
            <section class="unit-lessons-auto" style="background: white; border-radius: 16px; padding: 2rem; margin: 2rem 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color: #1f2937; margin-top: 0;">
                    📚 Lessons in This Unit
                    <span style="background: linear-gradient(135deg, #a855f7, #ec4899); color: white; font-size: 0.75rem; padding: 0.25rem 0.75rem; border-radius: 12px; margin-left: 0.5rem;">Auto-Generated</span>
                </h2>
                <div style="display: grid; gap: 1rem;">
        `;

        lessonDetails?.forEach((lesson, index) => {
            const handouts = this.getHandouts(lesson.file_path);
            html += `
                <div style="background: #f9fafb; border-radius: 12px; padding: 1.5rem; border-left: 4px solid #3b82f6;">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <h3 style="margin: 0 0 0.5rem 0; color: #1f2937; font-size: 1.125rem;">
                                ${index + 1}. ${lesson.title || 'Lesson'}
                            </h3>
                            <p style="margin: 0; color: #6b7280; font-size: 0.875rem;">${lesson.file_path}</p>
                        </div>
                        <div style="text-align: right;">
                            ${lesson.quality_score ? `<div style="background: #10b981; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 700; font-size: 0.875rem;">⭐ ${lesson.quality_score}</div>` : ''}
                        </div>
                    </div>
                    
                    ${handouts.length > 0 ? `
                        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 2px solid #e5e7eb;">
                            <strong style="color: #374151; font-size: 0.875rem;">📄 Handouts (${handouts.length}):</strong>
                            <ul style="margin: 0.5rem 0 0 1.5rem; color: #6b7280; font-size: 0.875rem;">
                                ${handouts.slice(0, 3).map(h => `<li>${h.split('/').pop()}</li>`).join('')}
                                ${handouts.length > 3 ? `<li><em>...and ${handouts.length - 3} more</em></li>` : ''}
                            </ul>
                        </div>
                    ` : ''}
                </div>
            `;
        });

        html += `
                </div>
                <p style="margin-top: 1.5rem; text-align: center; color: #6b7280; font-size: 0.875rem;">
                    🧠 Auto-generated from ${lessons.length} lesson relationships and ${lessonDetails?.reduce((sum, l) => sum + this.getHandouts(l.file_path).length, 0)} handout links in GraphRAG
                </p>
            </section>
        `;

        return html;
    }

    /**
     * Render hierarchy for current page (if it's a unit page)
     */
    async renderForCurrentPage(containerId = 'auto-hierarchy') {
        await this.init();
        
        const currentPath = window.location.pathname.replace('/public/', '');
        const container = document.getElementById(containerId);
        
        if (!container) return;

        // Check if current page is a unit
        const isUnit = currentPath.includes('/units/') && currentPath.includes('index.html');
        
        if (!isUnit) return;

        const html = await this.generateUnitPage(currentPath);
        
        if (html) {
            container.innerHTML = html;
        }
    }
}

// Initialize global instance
window.ContentHierarchyAuto = new ContentHierarchyAuto();

// Auto-render if container exists
window.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('auto-hierarchy');
    if (container) {
        await window.ContentHierarchyAuto.renderForCurrentPage();
    }
});

