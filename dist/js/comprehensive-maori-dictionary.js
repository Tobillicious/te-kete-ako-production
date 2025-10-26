// COMPREHENSIVE MĀORI DICTIONARY - EXTENDED WORD COLLECTION
// Extended Te Reo Māori vocabulary for advanced Wordle gameplay

class ComprehensiveMaoriDictionary {
    constructor() {
        this.extendedWords = new Map();
        this.loadExtendedVocabulary();
    }

    loadExtendedVocabulary() {
        // Extended 5-letter Te Reo Māori words with cultural context
        const extendedVocabulary = [
            // Nature & Environment
            { word: 'ĀKAU', meaning: 'shore, coast', cultural: 'high', category: 'nature' },
            { word: 'HAUHU', meaning: 'wind', cultural: 'medium', category: 'nature' },
            { word: 'MAUNGA', meaning: 'mountain', cultural: 'high', category: 'nature' },
            { word: 'NGAHERE', meaning: 'forest', cultural: 'high', category: 'nature' },
            { word: 'RAUMATI', meaning: 'summer', cultural: 'medium', category: 'nature' },
            { word: 'TAKURUA', meaning: 'winter', cultural: 'medium', category: 'nature' },

            // Body & Health
            { word: 'MATA', meaning: 'face, eye', cultural: 'medium', category: 'body' },
            { word: 'RINGA', meaning: 'hand, arm', cultural: 'medium', category: 'body' },
            { word: 'WAEWAE', meaning: 'foot, leg', cultural: 'medium', category: 'body' },
            { word: 'HAUORA', meaning: 'health', cultural: 'high', category: 'wellbeing' },

            // Cultural Concepts
            { word: 'MANA', meaning: 'power, prestige', cultural: 'high', category: 'cultural' },
            { word: 'TAPU', meaning: 'sacred', cultural: 'high', category: 'cultural' },
            { word: 'NOA', meaning: 'free from tapu', cultural: 'high', category: 'cultural' },
            { word: 'MAURI', meaning: 'life force', cultural: 'high', category: 'cultural' },
            { word: 'WAIRUA', meaning: 'spirit', cultural: 'high', category: 'cultural' },

            // Actions & Verbs
            { word: 'KŌHĪ', meaning: 'to gather', cultural: 'medium', category: 'action' },
            { word: 'MAHI', meaning: 'work', cultural: 'high', category: 'action' },
            { word: 'NOHO', meaning: 'to sit, stay', cultural: 'medium', category: 'action' },
            { word: 'RONGO', meaning: 'to hear, feel', cultural: 'medium', category: 'action' },
            { word: 'TITIRO', meaning: 'to look', cultural: 'medium', category: 'action' },

            // Numbers
            { word: 'KOTAHI', meaning: 'one', cultural: 'medium', category: 'number' },
            { word: 'RUA', meaning: 'two', cultural: 'medium', category: 'number' },
            { word: 'TORU', meaning: 'three', cultural: 'medium', category: 'number' },
            { word: 'WHĀ', meaning: 'four', cultural: 'medium', category: 'number' },
            { word: 'RIMA', meaning: 'five', cultural: 'medium', category: 'number' },

            // Directions
            { word: 'RARO', meaning: 'below, down', cultural: 'medium', category: 'direction' },
            { word: 'RUNGA', meaning: 'above, up', cultural: 'medium', category: 'direction' },
            { word: 'MURI', meaning: 'behind, back', cultural: 'medium', category: 'direction' },
            { word: 'MUA', meaning: 'front, before', cultural: 'medium', category: 'direction' },

            // Time
            { word: 'NEI', meaning: 'now, here', cultural: 'medium', category: 'time' },
            { word: 'INANAHI', meaning: 'yesterday', cultural: 'medium', category: 'time' },
            { word: 'ĀPŌPŌ', meaning: 'tomorrow', cultural: 'medium', category: 'time' },

            // Colors
            { word: 'KIRI', meaning: 'skin, bark', cultural: 'medium', category: 'color' },
            { word: 'MA', meaning: 'white, clean', cultural: 'medium', category: 'color' },
            { word: 'MANGU', meaning: 'black', cultural: 'medium', category: 'color' }
        ];

        // Process and store extended vocabulary
        extendedVocabulary.forEach(entry => {
            if (entry.word.length === 5) {
                this.extendedWords.set(entry.word.toUpperCase(), {
                    ...entry,
                    difficulty: this.calculateDifficulty(entry),
                    frequency: this.calculateFrequency(entry.category)
                });
            }
        });

        console.log(`📖 Loaded ${this.extendedWords.size} extended Te Reo Māori words`);
    }

    calculateDifficulty(entry) {
        // Determine difficulty based on cultural complexity and common usage
        if (entry.cultural === 'high' && ['cultural', 'wellbeing'].includes(entry.category)) {
            return 'advanced';
        }
        if (entry.category === 'number' || entry.category === 'direction') {
            return 'beginner';
        }
        return 'intermediate';
    }

    calculateFrequency(category) {
        const frequencyMap = {
            'cultural': 'high',
            'nature': 'high',
            'action': 'medium',
            'body': 'medium',
            'number': 'high',
            'direction': 'medium',
            'time': 'medium',
            'color': 'low',
            'wellbeing': 'medium'
        };
        return frequencyMap[category] || 'medium';
    }

    isValidWord(word) {
        const upperWord = word.toUpperCase();
        return this.extendedWords.has(upperWord);
    }

    getWordInfo(word) {
        const upperWord = word.toUpperCase();
        return this.extendedWords.get(upperWord) || null;
    }

    getWordsByCategory(category) {
        const words = Array.from(this.extendedWords.values());
        return words.filter(entry => entry.category === category);
    }

    getWordsByDifficulty(difficulty) {
        const words = Array.from(this.extendedWords.values());
        return words.filter(entry => entry.difficulty === difficulty);
    }

    getAllExtendedWords() {
        return Array.from(this.extendedWords.keys());
    }

    combineWithBasicDictionary() {
        // Merge with basic dictionary if available
        if (window.maoriDictionary && window.maoriDictionary.isLoaded) {
            const basicWords = window.maoriDictionary.getAllWords();
            const extendedWords = this.getAllExtendedWords();
            return [...new Set([...basicWords, ...extendedWords])];
        }
        return this.getAllExtendedWords();
    }

    getRandomWordByCategory(category) {
        const categoryWords = this.getWordsByCategory(category);
        if (categoryWords.length === 0) {
            return null;
        }
        const randomIndex = Math.floor(Math.random() * categoryWords.length);
        return categoryWords[randomIndex];
    }

    getCategories() {
        const words = Array.from(this.extendedWords.values());
        const categories = [...new Set(words.map(entry => entry.category))];
        return categories.sort();
    }

    getCategoryStats() {
        const words = Array.from(this.extendedWords.values());
        const stats = {};
        
        words.forEach(entry => {
            if (!stats[entry.category]) {
                stats[entry.category] = {
                    count: 0,
                    difficulties: { beginner: 0, intermediate: 0, advanced: 0 },
                    cultural: { high: 0, medium: 0, low: 0 }
                };
            }
            stats[entry.category].count++;
            stats[entry.category].difficulties[entry.difficulty]++;
            stats[entry.category].cultural[entry.cultural]++;
        });

        return stats;
    }

    // Enhanced word validation with cultural context
    validateWordWithContext(word, gameLevel = 'intermediate') {
        const info = this.getWordInfo(word);
        if (!info) {
            return { valid: false, reason: 'Not in dictionary' };
        }

        // Check if word is appropriate for game level
        const levelMap = { beginner: 1, intermediate: 2, advanced: 3 };
        const wordLevel = levelMap[info.difficulty];
        const gameLevel_num = levelMap[gameLevel];

        if (wordLevel > gameLevel_num + 1) {
            return { 
                valid: true, 
                appropriate: false, 
                reason: 'Word may be too advanced for current level',
                suggestion: 'Consider easier words first'
            };
        }

        return { 
            valid: true, 
            appropriate: true, 
            info: info 
        };
    }
}

// Initialize global comprehensive dictionary
window.comprehensiveMaoriDictionary = new ComprehensiveMaoriDictionary();

// Extend the basic dictionary if it exists
if (window.maoriDictionary) {
    // Add method to check both dictionaries
    window.maoriDictionary.isValidWordExtended = function(word) {
        return this.isValidWord(word) || window.comprehensiveMaoriDictionary.isValidWord(word);
    };

    // Add method to get comprehensive word info
    window.maoriDictionary.getWordInfoExtended = function(word) {
        return this.getWordInfo(word) || window.comprehensiveMaoriDictionary.getWordInfo(word);
    };
}

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ComprehensiveMaoriDictionary;
}