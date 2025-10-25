/**
 * NZ Curriculum Tagger
 * Links lessons to official Te Mātaiaho progress outcomes
 */

class CurriculumTagger {
    constructor() {
        this.curriculumData = null;
        this.supabase = null;
    }

    async init() {
        const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
        
        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
        
        // Load Te Mātaiaho curriculum data
        try {
            const response = await fetch('/data/temataiaho.json');
            this.curriculumData = await response.json();
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
            this.curriculumData = this.getFallbackData();
        }
    }

    /**
     * Get curriculum outcomes for a specific subject and phase
     */
    getOutcomes(subject, phase) {
        if (!this.curriculumData) return [];
        
        const subjectData = this.curriculumData.subjects?.find(s => 
            s.name.toLowerCase() === subject.toLowerCase()
        );
        
        if (!subjectData) return [];
        
        const phaseData = subjectData.learning_phases?.find(p => p.phase === phase);
        return phaseData?.progress_outcomes || [];
    }

    /**
     * Display curriculum alignment on a lesson page
     */
    async displayAlignment(containerId, lessonPath) {
        await this.init();
        
        const container = document.getElementById(containerId);
        if (!container) return;

        try {
            // Get lesson metadata from GraphRAG
            const { data: lesson } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', lessonPath)
                .single();

            if (!lesson) {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
                return;
            }

            // Determine phase from year level
            const phase = this.getPhaseFromYearLevel(lesson.year_level);
            
            // Get relevant outcomes
            const outcomes = this.getOutcomes(lesson.subject, phase);

            if (outcomes.length === 0) {
                container.innerHTML = this.renderGenericAlignment(lesson);
                return;
            }

            container.innerHTML = this.renderAlignment(outcomes, lesson, phase);

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
        }
    }

    getPhaseFromYearLevel(yearLevel) {
        if (!yearLevel) return 3; // Default to Phase 3 (Y7-8)
        
        const yearMatch = yearLevel.match(/\d+/);
        const year = yearMatch ? parseInt(yearMatch[0]) : 7;
        
        if (year <= 2) return 1;
        if (year <= 4) return 2;
        if (year <= 8) return 3;
        if (year <= 10) return 4;
        return 5; // Y11-13
    }

    renderAlignment(outcomes, lesson, phase) {
        return `
            <div style="background: linear-gradient(135deg, #f0fdf4, #dcfce7); padding: 2rem; border-radius: 16px; margin: 2rem 0; border-left: 4px solid #10b981;">
                <h3 style="color: #065f46; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span>📋</span>
                    <span>NZ Curriculum Alignment | Te Mātaiaho</span>
                </h3>
                <p style="color: #047857; margin-bottom: 1.5rem;">
                    <strong>Phase ${phase}</strong> (Years ${this.getYearsForPhase(phase)}) • ${lesson.subject}
                </p>
                
                <div style="display: grid; gap: 1rem;">
                    ${outcomes.slice(0, 3).map(outcome => `
                        <div style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981;">
                            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                                <span style="background: #10b981; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">${outcome.id}</span>
                                <span style="color: #059669; font-weight: 600; font-size: 0.875rem;">${outcome.type}</span>
                            </div>
                            <p style="margin: 0; color: #1f2937; line-height: 1.6;">${outcome.statement}</p>
                        </div>
                    `).join('')}
                    
                    ${outcomes.length > 3 ? `
                        <p style="margin: 1rem 0 0 0; color: #047857; font-size: 0.875rem; text-align: center;">
                            ...and ${outcomes.length - 3} more progress outcomes
                            <a href="/curriculum-${lesson.subject.toLowerCase().replace(/ /g, '-')}.html" style="color: #059669; font-weight: 600; text-decoration: none;">
                                View full curriculum →
                            </a>
                        </p>
                    ` : ''}
                </div>

                <p style="margin-top: 1.5rem; font-size: 0.875rem; color: #065f46; text-align: center;">
                    <strong>🧠 GraphRAG Powered:</strong> Curriculum alignment automatically detected from lesson content and metadata
                </p>
            </div>
        `;
    }

    renderGenericAlignment(lesson) {
        return `
            <div style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 16px; margin: 2rem 0; border-left: 4px solid #0284c7;">
                <h3 style="color: #075985; margin-top: 0;">📋 NZ Curriculum Alignment</h3>
                <p style="color: #0c4a6e; margin-bottom: 1rem;">
                    <strong>Subject:</strong> ${lesson.subject}<br>
                    <strong>Year Level:</strong> ${lesson.year_level}
                </p>
                <p style="margin: 0; color: #0369a1; font-size: 0.875rem;">
                    This resource aligns with New Zealand Curriculum standards for ${lesson.subject} at ${lesson.year_level}.
                    <a href="/curriculum-${lesson.subject.toLowerCase()}.html" style="color: #0284c7; font-weight: 600;">
                        View full curriculum framework →
                    </a>
                </p>
            </div>
        `;
    }

    getYearsForPhase(phase) {
        const phases = {
            1: '1-2',
            2: '3-4',
            3: '7-8',
            4: '9-10',
            5: '11-13'
        };
        return phases[phase] || '7-8';
    }

    getFallbackData() {
        // Simplified curriculum structure for when temataiaho.json isn't available
        return {
            curriculum: "Te Mātaiaho",
            subjects: [
                {
                    name: "Social Studies",
                    learning_phases: [
                        {
                            phase: 3,
                            years: "7-8",
                            progress_outcomes: [
                                {
                                    id: "TM-SS-3-U1",
                                    type: "Understand",
                                    statement: "Systems shape how people and groups organise themselves"
                                }
                            ]
                        }
                    ]
                }
            ]
        };
    }
}

// Initialize global instance
window.CurriculumTagger = new CurriculumTagger();

// Auto-render if container exists
window.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('curriculum-alignment');
    if (container && window.location.pathname) {
        await window.CurriculumTagger.displayAlignment('curriculum-alignment', window.location.pathname);
    }
});

