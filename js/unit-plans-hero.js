// unit-plans-hero.js
// Ultimate Unit Plans Hero - Interactive Command Center
// Created: Oct 28, 2025

class UnitPlansHero {
    constructor() {
        this.units = [];
        this.filteredUnits = [];
        this.currentView = 'timeline';
        
        // NZC Subject Colors (consistent across the site)
        this.subjectColors = {
            'english': '#5B8DBE',
            'te-ao-maori': '#40B5AD',
            'mathematics': '#E67E22',
            'science': '#1E5741',
            'social-studies': '#6B4C9A',
            'technology': '#8B6F47',
            'arts': '#D35D6E',
            'health-pe': '#52B788',
            'cross-curricular': '#40B5AD'
        };
    }

    async init() {
        console.log('[Unit Plans Hero] Initializing...');
        await this.loadUnits();
        this.setupEventListeners();
        this.renderNetwork();
        this.animateStats();
        console.log('[Unit Plans Hero] Initialized successfully!');
    }

    async loadUnits() {
        // Load units from the page's resource cards
        const unitCards = document.querySelectorAll('.resource-card.unit-card');
        this.units = Array.from(unitCards).map((card, index) => {
            const title = card.querySelector('.resource-card-title')?.textContent.trim() || '';
            const description = card.querySelector('.resource-card-description')?.textContent.trim() || '';
            const yearBadge = card.querySelector('.year-badge')?.textContent.trim() || '';
            const meta = card.querySelector('.unit-meta')?.textContent.trim() || '';
            const href = card.getAttribute('href') || '#';
            
            // Extract subject from meta text and border color
            let subject = 'cross-curricular'; // default
            
            // Parse subject from .unit-meta text (e.g., "6-8 weeks • Te Ao Māori")
            if (meta.toLowerCase().includes('te ao māori') || meta.toLowerCase().includes('te ao maori')) {
                subject = 'te-ao-maori';
            } else if (meta.toLowerCase().includes('social studies') || meta.toLowerCase().includes('tikanga-ā-iwi')) {
                subject = 'social-studies';
            } else if (meta.toLowerCase().includes('english') || meta.toLowerCase().includes('reo pākehā')) {
                subject = 'english';
            } else if (meta.toLowerCase().includes('science') || meta.toLowerCase().includes('pūtaiao')) {
                subject = 'science';
            } else if (meta.toLowerCase().includes('stem')) {
                subject = 'science';
            } else if (meta.toLowerCase().includes('mathematics') || meta.toLowerCase().includes('pāngarau')) {
                subject = 'mathematics';
            } else if (meta.toLowerCase().includes('technology') || meta.toLowerCase().includes('hangarau')) {
                subject = 'technology';
            } else if (meta.toLowerCase().includes('arts') || meta.toLowerCase().includes('toi')) {
                subject = 'arts';
            } else if (meta.toLowerCase().includes('health') || meta.toLowerCase().includes('pe')) {
                subject = 'health-pe';
            }
            
            // Fallback: try to match border color
            const borderColor = card.style.borderLeft;
            if (subject === 'cross-curricular' && borderColor) {
                for (const [subj, color] of Object.entries(this.subjectColors)) {
                    if (borderColor.includes(color.toLowerCase()) || borderColor.includes(color.toUpperCase())) {
                        subject = subj;
                        break;
                    }
                }
            }
            
            // Parse year levels
            const yearMatch = yearBadge.match(/Y?(\d+)(-(\d+))?/);
            let yearLevels = [];
            if (yearMatch) {
                const start = parseInt(yearMatch[1]);
                const end = yearMatch[3] ? parseInt(yearMatch[3]) : start;
                yearLevels = Array.from({length: end - start + 1}, (_, i) => start + i);
            }
            
            // Extract duration from meta (2-3 weeks = short, 4-6 = medium, 8-10 = long)
            let duration = 'medium';
            if (meta.includes('2-3') || meta.includes('4-6') || meta.includes('5 weeks')) {
                duration = 'short';
            } else if (meta.includes('8-10') || meta.includes('10 weeks')) {
                duration = 'long';
            }
            
            return {
                id: `unit-${index + 1}`,
                title,
                description,
                subject,
                yearLevels,
                duration,
                href,
                meta,
                x: 0,
                y: 0
            };
        });
        
        this.filteredUnits = [...this.units];
        console.log(`[Unit Plans Hero] Loaded ${this.units.length} units`);
    }

    setupEventListeners() {
        // Search input
        const searchInput = document.getElementById('hero-search');
        if (searchInput) {
            searchInput.addEventListener('input', () => this.handleSearch());
        }

        // Filters
        const yearFilter = document.getElementById('hero-year-filter');
        const subjectFilter = document.getElementById('hero-subject-filter');
        const durationFilter = document.getElementById('hero-duration-filter');

        [yearFilter, subjectFilter, durationFilter].forEach(filter => {
            if (filter) {
                filter.addEventListener('change', () => this.handleFilters());
            }
        });

        // Quick tags
        document.querySelectorAll('.quick-tag').forEach(tag => {
            tag.addEventListener('click', (e) => this.handleQuickTag(e));
        });

        // Network view buttons
        document.querySelectorAll('.network-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchNetworkView(e));
        });

        // Stat cards animation on hover
        document.querySelectorAll('.stat-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-4px) scale(1.05)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) scale(1)';
            });
        });
    }

    handleSearch() {
        const searchTerm = document.getElementById('hero-search')?.value.toLowerCase() || '';
        this.applyFilters();
    }

    handleFilters() {
        this.applyFilters();
    }

    applyFilters() {
        const searchTerm = document.getElementById('hero-search')?.value.toLowerCase() || '';
        const yearFilter = document.getElementById('hero-year-filter')?.value || '';
        const subjectFilter = document.getElementById('hero-subject-filter')?.value || '';
        const durationFilter = document.getElementById('hero-duration-filter')?.value || '';

        this.filteredUnits = this.units.filter(unit => {
            // Search filter
            const matchesSearch = !searchTerm || 
                unit.title.toLowerCase().includes(searchTerm) ||
                unit.description.toLowerCase().includes(searchTerm) ||
                unit.subject.toLowerCase().includes(searchTerm);

            // Year level filter
            let matchesYear = !yearFilter;
            if (yearFilter === 'primary') matchesYear = unit.yearLevels.some(y => y >= 1 && y <= 6);
            else if (yearFilter === 'intermediate') matchesYear = unit.yearLevels.some(y => y >= 7 && y <= 8);
            else if (yearFilter === 'junior-secondary') matchesYear = unit.yearLevels.some(y => y >= 9 && y <= 10);
            else if (yearFilter === 'senior-secondary') matchesYear = unit.yearLevels.some(y => y >= 11 && y <= 13);

            // Subject filter
            const matchesSubject = !subjectFilter || unit.subject === subjectFilter;

            // Duration filter
            const matchesDuration = !durationFilter || unit.duration === durationFilter;

            return matchesSearch && matchesYear && matchesSubject && matchesDuration;
        });

        this.renderNetwork();
        this.highlightMatchingCards();
    }

    handleQuickTag(e) {
        const tag = e.target.dataset.tag;
        const searchInput = document.getElementById('hero-search');
        if (searchInput) {
            searchInput.value = tag;
            this.handleSearch();
        }
    }

    switchNetworkView(e) {
        const btn = e.target;
        const view = btn.dataset.view;
        
        // Update active button
        document.querySelectorAll('.network-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        this.currentView = view;
        this.renderNetwork();
    }

    renderNetwork() {
        const canvas = document.getElementById('unit-network-canvas');
        if (!canvas) return;

        const units = this.filteredUnits.length > 0 ? this.filteredUnits : this.units;
        
        if (this.currentView === 'timeline') {
            this.renderTimelineView(canvas, units);
        } else if (this.currentView === 'subjects') {
            this.renderSubjectsView(canvas, units);
        }
    }

    renderTimelineView(canvas, units) {
        // Group units by year level range
        const yearGroups = {
            'Primary (Y1-6)': units.filter(u => u.yearLevels.some(y => y >= 1 && y <= 6)),
            'Intermediate (Y7-8)': units.filter(u => u.yearLevels.some(y => y >= 7 && y <= 8)),
            'Junior Secondary (Y9-10)': units.filter(u => u.yearLevels.some(y => y >= 9 && y <= 10)),
            'Senior Secondary (Y11-13)': units.filter(u => u.yearLevels.some(y => y >= 11 && y <= 13))
        };
        
        let html = `<div class="timeline-view">`;
        
        Object.entries(yearGroups).forEach(([stage, stageUnits]) => {
            if (stageUnits.length === 0) return;
            
            html += `
                <div class="timeline-stage">
                    <h3 class="timeline-stage-title">
                        ${stage} <span class="stage-count">(${stageUnits.length} units)</span>
                    </h3>
                    <div class="timeline-stage-scroll">
            `;
            
            // Split units into two rows (alternating)
            const row1Units = stageUnits.filter((_, index) => index % 2 === 0);
            const row2Units = stageUnits.filter((_, index) => index % 2 === 1);
            
            // Render Row 1
            html += `<div class="timeline-row">`;
            row1Units.forEach(unit => {
                const color = this.subjectColors[unit.subject] || '#6B4C9A';
                const opacity = '25'; // 25% opacity for color-coding
                
                html += `
                    <div class="timeline-unit" 
                         onclick="window.location.href='${unit.href}'"
                         style="background: ${color}${opacity}; border-left: 4px solid ${color};"
                         data-subject="${unit.subject}"
                         data-duration="${unit.duration}">
                        <div class="timeline-unit-header">
                            <span class="unit-emoji">${this.getUnitEmoji(unit.title)}</span>
                            <span class="unit-title">${unit.title}</span>
                        </div>
                        <div class="timeline-unit-meta">${unit.meta}</div>
                    </div>
                `;
            });
            html += `</div>`;
            
            // Render Row 2
            html += `<div class="timeline-row">`;
            row2Units.forEach(unit => {
                const color = this.subjectColors[unit.subject] || '#6B4C9A';
                const opacity = '25'; // 25% opacity for color-coding
                
                html += `
                    <div class="timeline-unit" 
                         onclick="window.location.href='${unit.href}'"
                         style="background: ${color}${opacity}; border-left: 4px solid ${color};"
                         data-subject="${unit.subject}"
                         data-duration="${unit.duration}">
                        <div class="timeline-unit-header">
                            <span class="unit-emoji">${this.getUnitEmoji(unit.title)}</span>
                            <span class="unit-title">${unit.title}</span>
                        </div>
                        <div class="timeline-unit-meta">${unit.meta}</div>
                    </div>
                `;
            });
            html += `</div>`;
            
            html += `</div></div>`;
        });
        
        html += '</div>';
        canvas.innerHTML = html;
        
        // Add hover effects
        canvas.querySelectorAll('.timeline-unit').forEach(unit => {
            const subject = unit.dataset.subject;
            const color = this.subjectColors[subject] || '#6B4C9A';
            
            unit.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-4px)';
                this.style.boxShadow = '0 6px 16px rgba(0,0,0,0.15)';
                this.style.background = `${color}35`; // Increase opacity on hover
            });
            unit.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = 'var(--shadow-light)';
                this.style.background = `${color}25`; // Back to original opacity
            });
        });
    }

    renderSubjectsView(canvas, units) {
        const width = canvas.offsetWidth;
        const height = 400;
        
        // Group units by subject
        const subjectGroups = {};
        units.forEach(unit => {
            if (!subjectGroups[unit.subject]) {
                subjectGroups[unit.subject] = [];
            }
            subjectGroups[unit.subject].push(unit);
        });
        
        let html = `<div class="subjects-view" style="padding: 2rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">`;
        
        Object.entries(subjectGroups).forEach(([subject, subjectUnits]) => {
            const color = this.subjectColors[subject] || '#6B4C9A';
            const subjectName = this.formatSubjectName(subject);
            
            html += `
                <div class="subject-group" style="background: white; border-radius: 12px; 
                                                   padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                                                   border-top: 4px solid ${color};">
                    <h3 style="font-size: 1.1rem; margin-bottom: 1rem; color: ${color}; display: flex; align-items: center; gap: 0.5rem;">
                        ${this.getSubjectEmoji(subject)}
                        <span>${subjectName}</span>
                        <span style="margin-left: auto; font-size: 0.9rem; opacity: 0.7;">${subjectUnits.length}</span>
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
            `;
            
            subjectUnits.forEach(unit => {
                html += `
                    <a href="${unit.href}" 
                       style="padding: 0.75rem; background: ${color}08; border-radius: 6px; 
                              text-decoration: none; color: var(--color-text-primary);
                              transition: all 0.2s ease; display: block;"
                       class="subject-unit-link">
                        <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem;">
                            ${this.getUnitEmoji(unit.title)} ${unit.title}
                        </div>
                        <div style="font-size: 0.8rem; color: var(--color-text-secondary);">
                            ${unit.meta}
                        </div>
                    </a>
                `;
            });
            
            html += `</div></div>`;
        });
        
        html += '</div>';
        canvas.innerHTML = html;
        
        // Add hover effects
        canvas.querySelectorAll('.subject-unit-link').forEach(link => {
            link.addEventListener('mouseenter', function() {
                this.style.transform = 'translateX(4px)';
                this.style.background = this.style.background.replace('08', '15');
            });
            link.addEventListener('mouseleave', function() {
                this.style.transform = 'translateX(0)';
                this.style.background = this.style.background.replace('15', '08');
            });
        });
    }

    highlightMatchingCards() {
        const allCards = document.querySelectorAll('.resource-card.unit-card');
        const matchingIds = new Set(this.filteredUnits.map(u => u.id));
        
        allCards.forEach((card, index) => {
            const unitId = `unit-${index + 1}`;
            if (this.filteredUnits.length === this.units.length) {
                // No filter applied - show all
                card.style.opacity = '1';
                card.style.filter = 'none';
            } else if (matchingIds.has(unitId)) {
                // Matches filter
                card.style.opacity = '1';
                card.style.filter = 'none';
            } else {
                // Doesn't match filter
                card.style.opacity = '0.3';
                card.style.filter = 'grayscale(0.8)';
            }
        });
    }

    animateStats() {
        document.querySelectorAll('.stat-number').forEach(stat => {
            const target = parseInt(stat.textContent);
            const duration = 1500;
            const increment = target / (duration / 16);
            let current = 0;
            
            const animate = () => {
                current += increment;
                if (current < target) {
                    stat.textContent = Math.floor(current);
                    requestAnimationFrame(animate);
                } else {
                    stat.textContent = target;
                }
            };
            
            animate();
        });
    }

    getUnitEmoji(title) {
        const t = title.toLowerCase();
        if (t.includes('te ao māori') || t.includes('cultural')) return '🌟';
        if (t.includes('decoloni') || t.includes('history')) return '🔥';
        if (t.includes('stem') || t.includes('science')) return '🌊';
        if (t.includes('economic') || t.includes('justice')) return '💰';
        if (t.includes('global') || t.includes('media')) return '🌏';
        if (t.includes('rangatiratanga') || t.includes('future')) return '🚀';
        if (t.includes('ai') || t.includes('digital') || t.includes('tech')) return '🤖';
        if (t.includes('system')) return '⚙️';
        if (t.includes('writer') || t.includes('toolkit')) return '✍️';
        return '📚';
    }

    getSubjectEmoji(subject) {
        const emojis = {
            'english': '📝',
            'te-ao-maori': '🌿',
            'science': '🔬',
            'social-studies': '🌏',
            'technology': '💻',
            'mathematics': '🔢',
            'arts': '🎨',
            'health-pe': '💪',
            'cross-curricular': '🌈'
        };
        return emojis[subject] || '📚';
    }

    formatSubjectName(subject) {
        const names = {
            'english': 'English / Reo Pākehā',
            'te-ao-maori': 'Te Ao Māori',
            'science': 'Science / Pūtaiao',
            'social-studies': 'Social Studies / Tikanga-ā-Iwi',
            'technology': 'Technology / Hangarau',
            'mathematics': 'Mathematics / Pāngarau',
            'arts': 'The Arts / Ngā Toi',
            'health-pe': 'Health & PE / Hauora',
            'cross-curricular': 'Cross-Curricular'
        };
        return names[subject] || subject.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const hero = new UnitPlansHero();
    hero.init();
});

