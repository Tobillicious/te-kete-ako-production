/**
 * ANSWER KEY SYSTEM - P2-16
 * Teacher-only access to assessment answer keys
 * Priority Score: 0.60 | Impact: 12% users (teachers with assessments)
 */

class AnswerKeySystem {
    constructor() {
        this.init();
    }
    
    init() {
        // Add answer key toggles to assessment pages
        this.addAnswerKeyToggles();
    }
    
    addAnswerKeyToggles() {
        // Check if this is an assessment page
        const isAssessment = window.location.pathname.includes('assessment') || 
                            document.querySelector('[data-resource-type="assessment"]');
        
        if (!isAssessment) return;
        
        // Add answer key section (initially hidden)
        this.createAnswerKeySection();
    }
    
    createAnswerKeySection() {
        const answerKeyHTML = `
            <div class="answer-key-container" style="margin-top: 3rem; border-top: 3px solid #dc2626; padding-top: 2rem;">
                <div class="teacher-only-banner" style="background: #fef2f2; border: 2px solid #dc2626; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem;">
                    <h3 style="color: #991b1b; font-size: 1.5rem; margin-bottom: 0.5rem;">
                        🔒 Teacher-Only Answer Key
                    </h3>
                    <p style="color: #7f1d1d;">
                        This section contains assessment answers and is for verified teachers only.
                    </p>
                    <button class="btn btn-primary mt-3" onclick="window.AnswerKeySystem.revealAnswers()" id="reveal-btn">
                        🔓 I'm a Teacher - Show Answers
                    </button>
                </div>
                
                <div id="answer-key-content" class="hidden">
                    <h3 class="text-2xl font-bold mb-4">✅ Answer Key & Marking Rubric</h3>
                    
                    <div class="answer-section bg-gray-50 p-6 rounded-lg">
                        <h4 class="font-bold text-lg mb-3">Assessment Solutions:</h4>
                        <div id="answers-list">
                            <!-- Dynamically loaded or manually added by content team -->
                            <p class="text-gray-600 italic">
                                Answer keys are being developed for all assessments. 
                                <a href="/contact.html" class="text-blue-600 hover:underline">Request priority access</a> for specific assessments.
                            </p>
                        </div>
                    </div>
                    
                    <div class="marking-guide bg-blue-50 p-6 rounded-lg mt-4">
                        <h4 class="font-bold text-lg mb-3">Marking Guide:</h4>
                        <ul class="space-y-2 text-gray-700">
                            <li>✓ Review cultural appropriateness of student responses</li>
                            <li>✓ Award credit for alternative culturally valid answers</li>
                            <li>✓ Consider te reo Māori proficiency levels</li>
                            <li>✓ Use rubric for consistent marking</li>
                        </ul>
                    </div>
                </div>
            </div>
        `;
        
        // Find main content area and append
        const mainContent = document.querySelector('main, article, .content');
        if (mainContent) {
            mainContent.insertAdjacentHTML('beforeend', answerKeyHTML);
        }
    }
    
    async revealAnswers() {
        // In production, this would verify teacher login
        // For now, simple confirmation
        const confirmed = confirm('This content is for teachers only. Are you a verified teacher?');
        
        if (confirmed) {
            document.getElementById('answer-key-content').classList.remove('hidden');
            document.getElementById('reveal-btn').disabled = true;
            document.getElementById('reveal-btn').textContent = '✅ Answers Revealed';
            
            // Track analytics
            if (window.posthog) {
                posthog.capture('answer_key_revealed', {
                    resource: window.location.pathname
                });
            }
        }
    }
}

// CSS
const answerKeyCSS = `
<style>
.answer-key-container {
    background: #fffbeb;
    padding: 2rem;
    border-radius: 12px;
}

.hidden {
    display: none;
}

.answer-section, .marking-guide {
    margin-top: 1rem;
}

@media print {
    /* Teachers can choose to print with or without answers */
    .teacher-only-banner button {
        display: none;
    }
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', answerKeyCSS);

// Auto-initialize
if (typeof window !== 'undefined') {
    window.AnswerKeySystem = new AnswerKeySystem();
}

