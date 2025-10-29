// school-autocomplete.js
// Reusable NZ Schools Autocomplete Component
// Self-growing database that adds new schools to Supabase + GraphRAG

class SchoolAutocomplete {
    constructor(inputId, suggestionsId, options = {}) {
        this.inputId = inputId;
        this.suggestionsId = suggestionsId;
        this.schoolsCache = [];
        this.debounceTimer = null;
        this.onSelect = options.onSelect || null;
        this.onAddNew = options.onAddNew || null;
        this.autoAddToGraphRAG = options.autoAddToGraphRAG !== false; // Default true
        
        this.init();
    }

    async init() {
        // Wait for Supabase
        if (typeof supabase === 'undefined') {
            setTimeout(() => this.init(), 100);
            return;
        }

        await this.loadSchools();
        this.setupEventListeners();
    }

    async loadSchools() {
        try {
            const { data, error } = await supabase
                .from('nz_schools')
                .select('name, location, region, school_type, authority')
                .order('name');
            
            if (error) throw error;
            this.schoolsCache = data || [];
            console.log(`✅ School Autocomplete: Loaded ${this.schoolsCache.length} NZ schools`);
        } catch (error) {
            console.error('Error loading schools:', error);
            this.schoolsCache = [];
        }
    }

    setupEventListeners() {
        const input = document.getElementById(this.inputId);
        if (!input) {
            console.error(`Input element #${this.inputId} not found`);
            return;
        }

        // Input event for searching
        input.addEventListener('input', (e) => {
            this.searchSchools(e.target.value);
        });

        // Hide suggestions when clicking outside
        document.addEventListener('click', (e) => {
            const wrapper = input.closest('.school-search-wrapper');
            if (!e.target.closest('.school-search-wrapper') || e.target === input) {
                // Don't hide immediately, wait a bit for clicks
            } else {
                this.hideSuggestions();
            }
        });

        // Keyboard navigation (future enhancement)
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hideSuggestions();
            }
        });
    }

    searchSchools(query) {
        clearTimeout(this.debounceTimer);
        
        if (!query || query.length < 2) {
            this.hideSuggestions();
            return;
        }
        
        this.debounceTimer = setTimeout(() => {
            this.showSuggestions(query);
        }, 300);
    }

    showSuggestions(query) {
        const suggestionsDiv = document.getElementById(this.suggestionsId);
        if (!suggestionsDiv) return;

        const filtered = this.schoolsCache.filter(school => 
            school.name.toLowerCase().includes(query.toLowerCase())
        );
        
        if (filtered.length === 0) {
            // No matches - show "Add new" only
            suggestionsDiv.innerHTML = this.renderAddNewItem(query, 'No schools found');
        } else {
            // Show matches + "Add new" option
            const matchesHtml = filtered.slice(0, 5).map(school => 
                this.renderSchoolItem(school)
            ).join('');
            
            const addNewHtml = this.renderAddNewItem(query, 'Not in the list? Click to add');
            
            suggestionsDiv.innerHTML = matchesHtml + addNewHtml;
        }
        
        suggestionsDiv.classList.add('show');
    }

    renderSchoolItem(school) {
        const escapedName = this.escapeHtml(school.name);
        const region = school.region || 'Unknown region';
        const type = school.school_type || 'School';
        // Map State → Public for display clarity, keep others as-is
        const displayAuthority = school.authority === 'State' ? 'Public' : school.authority;
        const authority = displayAuthority ? ` • ${displayAuthority}` : '';
        
        return `
            <div class="suggestion-item" data-school-name="${escapedName}">
                <div class="suggestion-name">${escapedName}</div>
                <div class="suggestion-meta">${region} • ${type}${authority}</div>
            </div>
        `;
    }

    renderAddNewItem(query, subtitle) {
        const escapedQuery = this.escapeHtml(query);
        return `
            <div class="suggestion-item suggestion-new" data-new-school="${escapedQuery}">
                <div class="suggestion-name">➕ Add "${escapedQuery}" as new school</div>
                <div class="suggestion-meta">${subtitle}</div>
            </div>
        `;
    }

    setupSuggestionClickHandlers() {
        const suggestionsDiv = document.getElementById(this.suggestionsId);
        if (!suggestionsDiv) return;

        // Use event delegation for efficiency
        suggestionsDiv.addEventListener('click', async (e) => {
            const item = e.target.closest('.suggestion-item');
            if (!item) return;

            if (item.hasAttribute('data-new-school')) {
                // Add new school
                const schoolName = item.getAttribute('data-new-school');
                await this.addNewSchool(schoolName);
            } else if (item.hasAttribute('data-school-name')) {
                // Select existing school
                const schoolName = item.getAttribute('data-school-name');
                const school = this.schoolsCache.find(s => s.name === schoolName);
                if (school) {
                    this.selectSchool(school);
                }
            }
        });
    }

    selectSchool(school) {
        const input = document.getElementById(this.inputId);
        if (input) {
            input.value = school.name;
        }
        
        this.hideSuggestions();
        
        // Callback
        if (this.onSelect) {
            this.onSelect(school);
        }
    }

    async addNewSchool(schoolName) {
        try {
            const input = document.getElementById(this.inputId);
            if (input) {
                input.value = schoolName;
            }
            
            this.hideSuggestions();
            
            // Check if already exists (prevent duplicates)
            const exists = this.schoolsCache.find(s => 
                s.name.toLowerCase() === schoolName.toLowerCase()
            );
            
            if (exists) {
                console.log('School already exists, using existing entry');
                if (this.onAddNew) {
                    this.onAddNew(exists, false);
                }
                return exists;
            }
            
            // Insert into nz_schools table
            const { data, error } = await supabase
                .from('nz_schools')
                .insert({
                    name: schoolName,
                    location: 'To be confirmed',
                    region: null,
                    school_type: null,
                    decile: null
                })
                .select()
                .single();
            
            if (error) {
                console.error('Error adding school:', error);
                return null;
            }
            
            // Add to cache
            this.schoolsCache.push(data);
            this.schoolsCache.sort((a, b) => a.name.localeCompare(b.name));
            
            console.log('✅ New school added to database:', schoolName);
            
            // Add to GraphRAG if enabled
            if (this.autoAddToGraphRAG) {
                await this.addSchoolToGraphRAG(data);
            }
            
            // Callback
            if (this.onAddNew) {
                this.onAddNew(data, true);
            }
            
            return data;
        } catch (error) {
            console.error('Error adding new school:', error);
            return null;
        }
    }

    async addSchoolToGraphRAG(school) {
        try {
            const { error } = await supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `/schools/${school.name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '')}`,
                    resource_type: 'school',
                    title: school.name,
                    metadata: {
                        location: school.location,
                        region: school.region,
                        school_type: school.school_type,
                        decile: school.decile,
                        added_by: 'user',
                        auto_created: true,
                        created_at: new Date().toISOString()
                    },
                    subject: 'Platform Infrastructure',
                    year_level: 'All',
                    quality_score: 50
                });
            
            if (error) {
                console.error('Error adding to GraphRAG:', error);
            } else {
                console.log('✅ School added to GraphRAG:', school.name);
            }
        } catch (error) {
            console.error('Error in addSchoolToGraphRAG:', error);
        }
    }

    hideSuggestions() {
        const suggestionsDiv = document.getElementById(this.suggestionsId);
        if (suggestionsDiv) {
            suggestionsDiv.classList.remove('show');
        }
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Public method to refresh cache
    async refresh() {
        await this.loadSchools();
    }

    // Public method to get cached schools
    getSchools() {
        return this.schoolsCache;
    }
}

// Export for use in other scripts
if (typeof window !== 'undefined') {
    window.SchoolAutocomplete = SchoolAutocomplete;
}

