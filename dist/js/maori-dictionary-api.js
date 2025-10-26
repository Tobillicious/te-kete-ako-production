// MĀORI DICTIONARY API - CULTURAL SAFETY SYSTEM
// Validates Te Reo Māori words for Wordle games with cultural authenticity

class MaoriDictionaryAPI {
    constructor() {
        this.isLoaded = false;
        this.dictionary = new Map();
        this.culturalSafetyEnabled = true;
        this.init();
    }

    async init() {
        console.log('🌺 Initializing Māori Dictionary API...');
        try {
            await this.loadBasicDictionary();
            this.isLoaded = true;
            console.log('✅ Māori Dictionary API loaded successfully');
            
            // Dispatch ready event
            window.dispatchEvent(new CustomEvent('maori-dictionary-ready', {
                detail: { dictionarySize: this.dictionary.size }
            }));
        } catch (error) {
            console.error('❌ Failed to load Māori Dictionary API:', error);
        }
    }

    async loadBasicDictionary() {
        // Essential Te Reo Māori words for Wordle (5 letters)
        const basicWords = [
            // Common 5-letter words
            'AROHA', 'ATAUA', 'AWHAI', 'HAINA', 'HAERE',
            'HAPŪ', 'HAUMIE', 'HIAHIA', 'HOHOU', 'HONGI',
            'HUNGA', 'IWHAI', 'KAIHE', 'KAORE', 'KARAKIA',
            'KATEA', 'KAURI', 'KŌHUA', 'KŌRERO', 'KUPU',
            'MĀMĀ', 'MANAAKI', 'MARAE', 'MATUA', 'MIHINI',
            'MOANA', 'MOKOPUNA', 'NGATI', 'PAPATŪĀNUKU', 'PŌWHIRI',
            'RANGATAHI', 'TAIAO', 'TAMARIKI', 'TANGATA', 'TAONGA',
            'TIKANGA', 'TIRITI', 'WAIATA', 'WAKA', 'WHAKAPAPA',
            'WHĀNAU', 'WHENUA'
        ];

        // Cultural context for each word
        const wordContexts = {
            'AROHA': { meaning: 'love, compassion', cultural: 'high', difficulty: 'beginner' },
            'ATAUA': { meaning: 'we (inclusive)', cultural: 'medium', difficulty: 'intermediate' },
            'AWHAI': { meaning: 'to pursue, follow', cultural: 'medium', difficulty: 'intermediate' },
            'HAINA': { meaning: 'to sign', cultural: 'medium', difficulty: 'intermediate' },
            'HAERE': { meaning: 'to go, come', cultural: 'high', difficulty: 'beginner' },
            'HAPŪ': { meaning: 'subtribe, pregnant', cultural: 'high', difficulty: 'intermediate' },
            'HIAHIA': { meaning: 'to want, desire', cultural: 'medium', difficulty: 'beginner' },
            'HONGI': { meaning: 'traditional greeting', cultural: 'high', difficulty: 'beginner' },
            'KAORE': { meaning: 'no, not', cultural: 'high', difficulty: 'beginner' },
            'KAURI': { meaning: 'native tree', cultural: 'high', difficulty: 'intermediate' },
            'KŌRERO': { meaning: 'to speak, story', cultural: 'high', difficulty: 'beginner' },
            'KUPU': { meaning: 'word', cultural: 'medium', difficulty: 'intermediate' },
            'MARAE': { meaning: 'ceremonial grounds', cultural: 'high', difficulty: 'beginner' },
            'MATUA': { meaning: 'parent, adult', cultural: 'high', difficulty: 'beginner' },
            'MOANA': { meaning: 'sea, ocean', cultural: 'high', difficulty: 'beginner' },
            'NGATI': { meaning: 'tribe, people of', cultural: 'high', difficulty: 'intermediate' },
            'TAIAO': { meaning: 'environment', cultural: 'high', difficulty: 'intermediate' },
            'TAONGA': { meaning: 'treasure', cultural: 'high', difficulty: 'beginner' },
            'TIKANGA': { meaning: 'customs, practices', cultural: 'high', difficulty: 'intermediate' },
            'TIRITI': { meaning: 'treaty', cultural: 'high', difficulty: 'intermediate' },
            'WAIATA': { meaning: 'song', cultural: 'high', difficulty: 'beginner' },
            'WAKA': { meaning: 'canoe, vehicle', cultural: 'high', difficulty: 'beginner' },
            'WHENUA': { meaning: 'land, placenta', cultural: 'high', difficulty: 'intermediate' },
            'WHĀNAU': { meaning: 'family', cultural: 'high', difficulty: 'beginner' }
        };

        // Load into dictionary
        basicWords.forEach(word => {
            if (word.length === 5) {
                this.dictionary.set(word.toUpperCase(), {
                    word,
                    valid: true,
                    ...wordContexts[word] || { meaning: 'Te Reo Māori word', cultural: 'medium', difficulty: 'intermediate' }
                });
            }
        });

        console.log(`📚 Loaded ${this.dictionary.size} Te Reo Māori words`);
    }

    isValidWord(word) {
        if (!this.isLoaded) {
            console.warn('⚠️ Dictionary not yet loaded');
            return false;
        }

        const upperWord = word.toUpperCase();
        const entry = this.dictionary.get(upperWord);
        
        if (entry) {
            console.log(`✅ Valid Te Reo word: ${word} (${entry.meaning})`);
            return true;
        }
        
        console.log(`❌ Not found in Te Reo dictionary: ${word}`);
        return false;
    }

    getWordInfo(word) {
        if (!this.isLoaded) {
            return null;
        }

        const upperWord = word.toUpperCase();
        return this.dictionary.get(upperWord) || null;
    }

    getRandomWord(difficulty = 'any') {
        if (!this.isLoaded) {
            return null;
        }

        const words = Array.from(this.dictionary.values());
        const filteredWords = difficulty === 'any' 
            ? words 
            : words.filter(entry => entry.difficulty === difficulty);
            
        if (filteredWords.length === 0) {
            return null;
        }

        const randomIndex = Math.floor(Math.random() * filteredWords.length);
        return filteredWords[randomIndex];
    }

    getAllWords() {
        if (!this.isLoaded) {
            return [];
        }

        return Array.from(this.dictionary.keys());
    }

    getCulturalContext(word) {
        const info = this.getWordInfo(word);
        if (!info) {
            return 'Not found in dictionary';
        }

        return {
            meaning: info.meaning,
            culturalLevel: info.cultural,
            difficulty: info.difficulty,
            usage: this.getUsageExample(word)
        };
    }

    getUsageExample(word) {
        const examples = {
            'AROHA': 'Aroha mai - please forgive me',
            'HAERE': 'Haere mai - welcome',
            'HONGI': 'The hongi is a traditional Māori greeting',
            'KAORE': 'Kāore au i te mohio - I don\'t know',
            'KŌRERO': 'He kōrero pai - a good story',
            'MARAE': 'We gathered at the marae',
            'TAONGA': 'Te reo Māori is a taonga',
            'WAIATA': 'Let\'s sing a waiata',
            'WHĀNAU': 'My whānau is important to me'
        };

        return examples[word.toUpperCase()] || `${word} is a Te Reo Māori word`;
    }

    // Cultural safety check
    validateCulturalSafety(word) {
        if (!this.culturalSafetyEnabled) {
            return true;
        }

        const info = this.getWordInfo(word);
        if (!info) {
            return false; // Unknown words are not culturally safe
        }

        // All words in our dictionary are culturally appropriate
        return true;
    }

    // Stats for analytics
    getStats() {
        if (!this.isLoaded) {
            return null;
        }

        const words = Array.from(this.dictionary.values());
        return {
            total: words.length,
            byDifficulty: {
                beginner: words.filter(w => w.difficulty === 'beginner').length,
                intermediate: words.filter(w => w.difficulty === 'intermediate').length,
                advanced: words.filter(w => w.difficulty === 'advanced').length
            },
            byCultural: {
                high: words.filter(w => w.cultural === 'high').length,
                medium: words.filter(w => w.cultural === 'medium').length,
                low: words.filter(w => w.cultural === 'low').length
            }
        };
    }
}

// Initialize global instance
window.maoriDictionary = new MaoriDictionaryAPI();

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MaoriDictionaryAPI;
}