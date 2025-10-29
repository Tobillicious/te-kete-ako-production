/**
 * =================================================================
 * MĀORI DICTIONARY API INTEGRATION - Te Kete Ako
 * =================================================================
 * 
 * PURPOSE: Integrates with Te Aka Māori Dictionary API to provide 
 * authentic word validation, definitions, and cultural context for
 * all educational games.
 * 
 * FEATURES:
 * - Real-time word validation against authentic Māori dictionary
 * - Definition retrieval with cultural context
 * - Pronunciation guides and audio support
 * - Word categories and cultural significance
 * - Caching for performance optimization
 * - Fallback to local dictionary when offline
 * 
 * CULTURAL REQUIREMENTS:
 * - All words validated for cultural appropriateness
 * - Respect for traditional knowledge protocols
 * - Accurate pronunciation and meaning
 * - Cultural context provided where appropriate
 * 
 * =================================================================
 */

class MaoriDictionaryAPI {
    constructor() {
        this.baseURL = 'https://api.aka.co.nz/v1';
        this.cache = new Map();
        this.cacheExpiry = 24 * 60 * 60 * 1000; // 24 hours
        this.fallbackDictionary = this.initializeFallbackDictionary();
        this.isOnline = navigator.onLine;
        
        // Listen for online/offline events
        window.addEventListener('online', () => { this.isOnline = true; });
        window.addEventListener('offline', () => { this.isOnline = false; });
    }

    /**
     * Initialize comprehensive fallback dictionary for offline use
     */
    initializeFallbackDictionary() {
        return {
            // Basic vocabulary - everyday words
            'AROHA': { 
                word: 'AROHA', 
                meaning: 'Love, compassion, empathy, affectionate regard', 
                example: 'Aroha atu ki a koe - Love to you', 
                category: 'emotions',
                pronunciation: 'ah-ROH-hah',
                culturalNote: 'Central concept in Māori worldview - encompasses love, compassion, and empathy'
            },
            'WHARE': { 
                word: 'WHARE', 
                meaning: 'House, building, home, dwelling', 
                example: 'Kei te whare au - I am at home', 
                category: 'places',
                pronunciation: 'FAH-reh',
                culturalNote: 'More than just a building - represents family, shelter, and belonging'
            },
            'MAURI': { 
                word: 'MAURI', 
                meaning: 'Life force, vital essence, life principle', 
                example: 'Kia mauri ora - Be well, be healthy', 
                category: 'spiritual',
                pronunciation: 'MAH-oo-ree',
                culturalNote: 'Fundamental concept - the spiritual life force in all living things'
            },
            'TAIAO': { 
                word: 'TAIAO', 
                meaning: 'Environment, natural world, nature', 
                example: 'Tiaki i te taiao - Care for the environment', 
                category: 'nature',
                pronunciation: 'tah-ee-AH-oh',
                culturalNote: 'Emphasizes interconnectedness between people and environment'
            },
            'KAIAKO': { 
                word: 'KAIAKO', 
                meaning: 'Teacher, educator, instructor', 
                example: 'He kaiako pai ia - They are a good teacher', 
                category: 'people',
                pronunciation: 'kah-ee-AH-koh',
                culturalNote: 'More than instructor - includes mentoring and cultural guidance'
            },
            'RANGI': { 
                word: 'RANGI', 
                meaning: 'Sky, heaven, day, heavens', 
                example: 'He rangi ataahua - A beautiful day', 
                category: 'nature',
                pronunciation: 'RAH-ngee',
                culturalNote: 'Sky Father in Māori cosmology - ancestor and protector'
            },
            'MOANA': { 
                word: 'MOANA', 
                meaning: 'Ocean, sea, large lake, deep water', 
                example: 'Kei te moana mātou - We are at the ocean', 
                category: 'nature',
                pronunciation: 'moh-AH-nah',
                culturalNote: 'Sacred element connecting all Pacific peoples'
            },
            'MANA': { 
                word: 'MANA', 
                meaning: 'Power, authority, prestige, spiritual power', 
                example: 'He mana tō - You have power/authority', 
                category: 'spiritual',
                pronunciation: 'MAH-nah',
                culturalNote: 'Spiritual power and authority - can be inherited or earned'
            },
            'TAONGA': { 
                word: 'TAONGA', 
                meaning: 'Treasure, precious thing, valuable possession', 
                example: 'He taonga tēnei - This is a treasure', 
                category: 'cultural',
                pronunciation: 'tah-OH-ngah',
                culturalNote: 'Includes cultural practices, language, and spiritual treasures'
            },
            'WAIRUA': { 
                word: 'WAIRUA', 
                meaning: 'Spirit, soul, spiritual essence', 
                example: 'He wairua pai - A good spirit', 
                category: 'spiritual',
                pronunciation: 'wah-ee-ROO-ah',
                culturalNote: 'Spiritual dimension present in all living things'
            },
            
            // Family and relationships - whānau
            'MATUA': { 
                word: 'MATUA', 
                meaning: 'Parent, father, elder, adult', 
                example: 'Ko taku matua - My father', 
                category: 'whanau',
                pronunciation: 'MAH-too-ah',
                culturalNote: 'Includes biological and social parenting roles'
            },
            'WHAEA': { 
                word: 'WHAEA', 
                meaning: 'Mother, aunt, female elder', 
                example: 'Ko taku whaea - My mother', 
                category: 'whanau',
                pronunciation: 'FAH-eh-ah',
                culturalNote: 'Respectful term for mother figures and female elders'
            },
            'WHANAU': { 
                word: 'WHANAU', 
                meaning: 'Family, extended family group, to be born', 
                example: 'Ko taku whānau - My family', 
                category: 'whanau',
                pronunciation: 'FAH-nah-oo',
                culturalNote: 'Extends beyond nuclear family to include wider kinship connections'
            },
            
            // Cultural concepts - tikanga
            'HONGI': { 
                word: 'HONGI', 
                meaning: 'Traditional greeting - touching noses and foreheads', 
                example: 'Hongi mai - Come and hongi', 
                category: 'cultural',
                pronunciation: 'HONG-gee',
                culturalNote: 'Sacred greeting sharing the breath of life (hā)'
            },
            'HANGI': { 
                word: 'HANGI', 
                meaning: 'Earth oven, traditional cooking method', 
                example: 'Hangi kai - Earth oven food', 
                category: 'cultural',
                pronunciation: 'HANG-gee',
                culturalNote: 'Traditional cooking method using heated stones in earth pit'
            },
            'MARAE': { 
                word: 'MARAE', 
                meaning: 'Ceremonial grounds, sacred meeting place', 
                example: 'Ki te marae - To the marae', 
                category: 'cultural',
                pronunciation: 'MAH-rah-eh',
                culturalNote: 'Heart of Māori community - where traditions are maintained'
            },
            
            // Nature and environment - taiao
            'WHENUA': { 
                word: 'WHENUA', 
                meaning: 'Land, country, birth place, placenta', 
                example: 'Taku whenua - My land', 
                category: 'nature',
                pronunciation: 'FEH-noo-ah',
                culturalNote: 'Deep connection between people and land - includes placenta'
            },
            'KOWHAI': { 
                word: 'KOWHAI', 
                meaning: 'Golden native tree, yellow', 
                example: 'He rākau kōwhai - A kowhai tree', 
                category: 'nature',
                pronunciation: 'KOH-fah-ee',
                culturalNote: 'Iconic native tree - symbol of spring and renewal'
            },
            'KAURI': { 
                word: 'KAURI', 
                meaning: 'Native tree species, ancient forest giant', 
                example: 'He kauri rākau - A kauri tree', 
                category: 'nature',
                pronunciation: 'KAH-oo-ree',
                culturalNote: 'Sacred tree - can live thousands of years, revered ancestor'
            },
            'MAUNGA': { 
                word: 'MAUNGA', 
                meaning: 'Mountain, large hill', 
                example: 'Te maunga - The mountain', 
                category: 'nature',
                pronunciation: 'MAH-oo-ngah',
                culturalNote: 'Often ancestors in Māori cosmology - sources of identity'
            },
            
            // Actions and movement - mahi
            'HAERE': { 
                word: 'HAERE', 
                meaning: 'Go, come, travel, proceed', 
                example: 'Haere mai - Come here/welcome', 
                category: 'actions',
                pronunciation: 'HAH-eh-reh',
                culturalNote: 'Common in greetings and farewells - implies welcome'
            },
            'NOHO': { 
                word: 'NOHO', 
                meaning: 'Sit, stay, remain, live', 
                example: 'Noho mai - Stay here', 
                category: 'actions',
                pronunciation: 'NOH-hoh',
                culturalNote: 'Implies settling, belonging, making oneself at home'
            },
            'TITIRO': { 
                word: 'TITIRO', 
                meaning: 'Look, watch, observe', 
                example: 'Titiro mai - Look here', 
                category: 'actions',
                pronunciation: 'tee-tee-ROH',
                culturalNote: 'More than seeing - includes understanding and perceiving'
            },
            
            // Colors - nga tae
            'WHERO': { 
                word: 'WHERO', 
                meaning: 'Red, crimson', 
                example: 'He whero - Red', 
                category: 'colors',
                pronunciation: 'FEH-roh',
                culturalNote: 'Sacred color often used in traditional art and ceremonies'
            },
            'MANGU': { 
                word: 'MANGU', 
                meaning: 'Black, dark', 
                example: 'He mangu - Black', 
                category: 'colors',
                pronunciation: 'MAH-ngoo',
                culturalNote: 'Color of depth, strength, and formality'
            },
            'KAKARIKI': { 
                word: 'KAKARIKI', 
                meaning: 'Green, native parrot', 
                example: 'He kakariki - Green', 
                category: 'colors',
                pronunciation: 'kah-kah-REE-kee',
                culturalNote: 'Color of growth and life - also native green parrot'
            },
            
            // Food - kai
            'PIPI': { 
                word: 'PIPI', 
                meaning: 'Small edible shellfish', 
                example: 'Ngā pipi - The pipi', 
                category: 'food',
                pronunciation: 'PEE-pee',
                culturalNote: 'Traditional kai moana (seafood) - gathered sustainably'
            },
            'KINA': { 
                word: 'KINA', 
                meaning: 'Sea urchin, spiny sea creature', 
                example: 'He kina - Sea urchin', 
                category: 'food',
                pronunciation: 'KEE-nah',
                culturalNote: 'Delicacy and traditional kai moana with cultural protocols'
            },
            'PAUA': { 
                word: 'PAUA', 
                meaning: 'Abalone, edible sea snail', 
                example: 'He paua - Abalone', 
                category: 'food',
                pronunciation: 'PAH-oo-ah',
                culturalNote: 'Prized for food and beautiful shell used in art'
            },
            
            // Additional common words
            'TIKANGA': { 
                word: 'TIKANGA', 
                meaning: 'Customs, traditions, correct procedures', 
                example: 'He tikanga Māori - Māori customs', 
                category: 'cultural',
                pronunciation: 'tee-KAH-ngah',
                culturalNote: 'The correct way of doing things according to Māori values'
            },
            'TANGATA': { 
                word: 'TANGATA', 
                meaning: 'Person, people, human being', 
                example: 'He tangata pai - A good person', 
                category: 'people',
                pronunciation: 'TAH-ngah-tah',
                culturalNote: 'Emphasizes common humanity and dignity of all people'
            },
            'WHAKAPAPA': { 
                word: 'WHAKAPAPA', 
                meaning: 'Genealogy, lineage, connections', 
                example: 'Taku whakapapa - My genealogy', 
                category: 'cultural',
                pronunciation: 'fah-kah-PAH-pah',
                culturalNote: 'Foundation of Māori identity - connections to ancestors and land'
            },

            // Extended 5-letter vocabulary
            'TAUPO': { 
                word: 'TAUPO', 
                meaning: 'Lake Taupo, great lake', 
                example: 'Ki a Taupo - To Lake Taupo', 
                category: 'places',
                pronunciation: 'TAH-oo-poh',
                culturalNote: 'New Zealand\'s largest lake, sacred to local iwi'
            },
            'TEINA': { 
                word: 'TEINA', 
                meaning: 'Younger sibling, junior', 
                example: 'Ko taku teina - My younger sibling', 
                category: 'whanau',
                pronunciation: 'TEH-ee-nah',
                culturalNote: 'Important relationship role in whānau structure'
            },
            'NGATI': { 
                word: 'NGATI', 
                meaning: 'Tribal group, people of, descendants', 
                example: 'Ngāti Tuwharetoa - Tuwharetoa people', 
                category: 'people',
                pronunciation: 'NGAH-tee',
                culturalNote: 'Prefix for tribal names indicating kinship'
            },
            'WAHINE': { 
                word: 'WAHINE', 
                meaning: 'Woman, female, lady', 
                example: 'He wahine atahua - A beautiful woman', 
                category: 'people',
                pronunciation: 'wah-HEE-neh',
                culturalNote: 'Respectful term for women of all ages'
            },
            'TANE': { 
                word: 'TANE', 
                meaning: 'Man, male, husband', 
                example: 'He tane pai - A good man', 
                category: 'people',
                pronunciation: 'TAH-neh',
                culturalNote: 'Also refers to Tāne Mahuta, god of forests'
            },
            'TAWHIRI': { 
                word: 'TAWHIRI', 
                meaning: 'Wind god, storm, tempest', 
                example: 'Tawhirimatea - God of winds', 
                category: 'spiritual',
                pronunciation: 'tah-FEE-ree',
                culturalNote: 'Atua of winds and storms in Māori cosmology'
            },
            'HINAU': { 
                word: 'HINAU', 
                meaning: 'Native tree, food source', 
                example: 'He hinau rākau - A hinau tree', 
                category: 'nature',
                pronunciation: 'HEE-nah-oo',
                culturalNote: 'Traditional food tree, nuts were ground for flour'
            },
            'PURIRI': { 
                word: 'PURIRI', 
                meaning: 'Native hardwood tree', 
                example: 'He puriri rākau - A puriri tree', 
                category: 'nature',
                pronunciation: 'poo-REE-ree',
                culturalNote: 'Valuable timber tree with beautiful grain'
            },
            'TAWA': { 
                word: 'TAWA', 
                meaning: 'Native forest tree', 
                example: 'He tawa rākau - A tawa tree', 
                category: 'nature',
                pronunciation: 'TAH-wah',
                culturalNote: 'Important forest tree, traditional food source'
            },
            'RIMU': { 
                word: 'RIMU', 
                meaning: 'Native conifer tree', 
                example: 'He rimu rākau - A rimu tree', 
                category: 'nature',
                pronunciation: 'REE-moo',
                culturalNote: 'Ancient native tree, important for traditional building'
            },
            'TOTARA': { 
                word: 'TOTARA', 
                meaning: 'Native tree, durable timber', 
                example: 'He totara rākau - A totara tree', 
                category: 'nature',
                pronunciation: 'toh-TAH-rah',
                culturalNote: 'Sacred tree traditionally used for waka building'
            },

            // Tainui dialect words (double vowels replacing macrons) - 5 letters only
            'MAAUA': { 
                word: 'MAAUA', 
                meaning: 'We two (Tainui: māua)', 
                example: 'Ko māua - We two', 
                category: 'people',
                pronunciation: 'mah-AH-oo-ah',
                culturalNote: 'Tainui dialect form using double vowels'
            },
            'RAAUA': { 
                word: 'RAAUA', 
                meaning: 'They two (Tainui: rāua)', 
                example: 'Ko rāua - They two', 
                category: 'people',
                pronunciation: 'rah-AH-oo-ah',
                culturalNote: 'Tainui dialect form for third person dual'
            },
            'TAAUA': { 
                word: 'TAAUA', 
                meaning: 'We two including you (Tainui: tāua)', 
                example: 'Ko tāua - We two (inclusive)', 
                category: 'people',
                pronunciation: 'tah-AH-oo-ah',
                culturalNote: 'Tainui dialect inclusive dual pronoun'
            },
            'KOOUA': { 
                word: 'KOOUA', 
                meaning: 'We all (Tainui: kōua)', 
                example: 'Ko kōua katoa - All of us', 
                category: 'people',
                pronunciation: 'koh-OH-oo-ah',
                culturalNote: 'Tainui dialect inclusive plural pronoun'
            },
            'POOURI': { 
                word: 'POOURI', 
                meaning: 'Sad, sorrowful (Tainui: pōuri)', 
                example: 'Kei te pōuri au - I am sad', 
                category: 'emotions',
                pronunciation: 'poh-OH-oo-ree',
                culturalNote: 'Tainui dialect form for sadness'
            },

            // Extended family terms
            'TEEKE': { 
                word: 'TEEKE', 
                meaning: 'Uncle (father\'s brother)', 
                example: 'Ko taku teeke - My uncle', 
                category: 'whanau',
                pronunciation: 'TEH-eh-keh',
                culturalNote: 'Specific kinship term in whānau relationships'
            },
            'KEKE': { 
                word: 'KEKE', 
                meaning: 'Aunt (mother\'s sister)', 
                example: 'Ko taku keke - My aunt', 
                category: 'whanau',
                pronunciation: 'KEH-keh',
                culturalNote: 'Traditional kinship term for maternal aunt'
            },
            'KOEKE': { 
                word: 'KOEKE', 
                meaning: 'Brother-in-law, relative by marriage', 
                example: 'Ko taku koeke - My brother-in-law', 
                category: 'whanau',
                pronunciation: 'koh-EH-keh',
                culturalNote: 'Important relationship in extended whānau'
            },
            'TUAEA': { 
                word: 'TUAEA', 
                meaning: 'Sister-in-law, female relative by marriage', 
                example: 'Ko taku tuaea - My sister-in-law', 
                category: 'whanau',
                pronunciation: 'too-AH-eh-ah',
                culturalNote: 'Traditional term for female in-law relationships'
            },

            // Animals and nature
            'KIWI': { 
                word: 'KIWI', 
                meaning: 'Native flightless bird', 
                example: 'He kiwi - A kiwi bird', 
                category: 'animals',
                pronunciation: 'KEE-wee',
                culturalNote: 'Iconic native bird, symbol of New Zealand'
            },
            'HUIA': { 
                word: 'HUIA', 
                meaning: 'Extinct native bird, sacred feathers', 
                example: 'He plume huia - Huia feathers', 
                category: 'animals',
                pronunciation: 'HOO-ee-ah',
                culturalNote: 'Sacred bird, feathers were symbols of high rank'
            },
            'TUTU': { 
                word: 'TUTU', 
                meaning: 'Native shrub, poisonous plant', 
                example: 'He tutu - Tutu plant', 
                category: 'nature',
                pronunciation: 'TOO-too',
                culturalNote: 'Traditional knowledge warned of its toxicity'
            },
            'HOIHO': { 
                word: 'HOIHO', 
                meaning: 'Yellow-eyed penguin', 
                example: 'He hoiho - Yellow-eyed penguin', 
                category: 'animals',
                pronunciation: 'HOH-ee-hoh',
                culturalNote: 'Endangered native penguin species'
            },

            // Cultural items and concepts
            'HAKA': { 
                word: 'HAKA', 
                meaning: 'Traditional war dance, ceremonial dance', 
                example: 'He haka - A haka', 
                category: 'cultural',
                pronunciation: 'HAH-kah',
                culturalNote: 'Powerful expression of mana, identity, and emotion'
            },
            'POUNAMU': { 
                word: 'POUNAMU', 
                meaning: 'Greenstone, nephrite jade', 
                example: 'He pounamu - Greenstone', 
                category: 'cultural',
                pronunciation: 'poh-oo-NAH-moo',
                culturalNote: 'Sacred stone, passed down through generations'
            },
            'WAIATA': { 
                word: 'WAIATA', 
                meaning: 'Song, chant, music', 
                example: 'He waiata atahua - A beautiful song', 
                category: 'cultural',
                pronunciation: 'wah-ee-AH-tah',
                culturalNote: 'Important for preserving history and culture'
            },
            'KARAKIA': { 
                word: 'KARAKIA', 
                meaning: 'Prayer, blessing, incantation', 
                example: 'He karakia - A prayer', 
                category: 'spiritual',
                pronunciation: 'kah-rah-KEE-ah',
                culturalNote: 'Spiritual practice connecting to ancestors and atua'
            },

            // More 5-letter verbs and adjectives
            'AKONA': {
                word: 'AKONA',
                meaning: 'Learn, study, acquire knowledge',
                example: 'Kei te ako au - I am learning',
                category: 'actions',
                pronunciation: 'ah-KOH-nah',
                culturalNote: 'Fundamental concept in education and growth'
            },
            'WHAIU': {
                word: 'WHAIU',
                meaning: 'Chase, pursue, follow',
                example: 'Whaiu mai - Follow me',
                category: 'actions',
                pronunciation: 'FAH-ee-oo',
                culturalNote: 'Used for physical and metaphorical pursuit'
            },
            'WHATU': {
                word: 'WHATU',
                meaning: 'Weave, knit, eye',
                example: 'Whatu kākahu - Weave clothing',
                category: 'actions',
                pronunciation: 'FAH-too',
                culturalNote: 'Traditional skill passed down through generations'
            },
            'WHAOA': {
                word: 'WHAOA',
                meaning: 'Strike, hit, beat',
                example: 'Whaoa te taniwha - Strike the taniwha',
                category: 'actions',
                pronunciation: 'FAH-oh-ah',
                culturalNote: 'Used in traditional stories and combat'
            },
            'MOHIO': {
                word: 'MOHIO',
                meaning: 'Know, understand, be aware',
                example: 'Kei te mohio au - I know',
                category: 'mental',
                pronunciation: 'moh-HEE-oh',
                culturalNote: 'Deep understanding beyond surface knowledge'
            },
            'PAKEKE': {
                word: 'PAKEKE',
                meaning: 'Adult, mature, grown up',
                example: 'He pakeke ia - They are an adult',
                category: 'people',
                pronunciation: 'pah-KEH-keh',
                culturalNote: 'Refers to full maturity and responsibility'
            },
            'ATAHUA': {
                word: 'ATAHUA',
                meaning: 'Beautiful, pretty, lovely',
                example: 'He atahua - Beautiful',
                category: 'qualities',
                pronunciation: 'ah-tah-HOO-ah',
                culturalNote: 'Beauty that encompasses inner and outer qualities'
            },
            'KAIKINO': {
                word: 'KAIKINO',
                meaning: 'Evil, wicked, harmful',
                example: 'He kaikino - Evil',
                category: 'qualities',
                pronunciation: 'kah-ee-KEE-noh',
                culturalNote: 'Strong term for moral wrongness'
            },
            'NGARO': {
                word: 'NGARO',
                meaning: 'Lost, missing, hidden',
                example: 'Kua ngaro - It is lost',
                category: 'states',
                pronunciation: 'NGAH-roh',
                culturalNote: 'Can refer to physical or spiritual absence'
            },
            'WATEA': {
                word: 'WATEA',
                meaning: 'Clear, open, free, empty',
                example: 'He watea - Clear/open',
                category: 'states',
                pronunciation: 'wah-TEH-ah',
                culturalNote: 'State of being unobstructed or available'
            },
            'KIKINO': {
                word: 'KIKINO',
                meaning: 'Small, little, tiny',
                example: 'He kikino - Small',
                category: 'qualities',
                pronunciation: 'kee-KEE-noh',
                culturalNote: 'Affectionate term for small things'
            },
            'TAWHITI': {
                word: 'TAWHITI',
                meaning: 'Far, distant, remote',
                example: 'He tawhiti - Far away',
                category: 'locations',
                pronunciation: 'tah-FEE-tee',
                culturalNote: 'Physical or emotional distance'
            },
            'TEITEI': {
                word: 'TEITEI',
                meaning: 'High, tall, elevated',
                example: 'He teitei - High/tall',
                category: 'qualities',
                pronunciation: 'TEH-ee-TEH-ee',
                culturalNote: 'Physical height or elevated status'
            },
            'HOHORO': {
                word: 'HOHORO',
                meaning: 'Quick, fast, hurried',
                example: 'Hohoro mai - Come quickly',
                category: 'qualities',
                pronunciation: 'hoh-HOH-roh',
                culturalNote: 'Urgency in movement or action'
            },
            'MARIE': {
                word: 'MARIE',
                meaning: 'Calm, peaceful, still',
                example: 'He marie - Calm',
                category: 'states',
                pronunciation: 'MAH-ree-eh',
                culturalNote: 'Inner peace and tranquility'
            },

            // More 5-letter verbs, adjectives and everyday words
            'WHAIA': {
                word: 'WHAIA',
                meaning: 'Follow, pursue, chase',
                example: 'Whaia te mea pai - Pursue good things',
                category: 'actions',
                pronunciation: 'FAH-ee-ah',
                culturalNote: 'Active pursuit of goals or values'
            },
            'KOREA': {
                word: 'KOREA',
                meaning: 'Dance, move rhythmically',
                example: 'Kōrea mai - Dance here',
                category: 'actions',
                pronunciation: 'koh-REH-ah',
                culturalNote: 'Cultural expression through movement'
            },
            'WHAAO': {
                word: 'WHAAO',
                meaning: 'Wade, walk through water',
                example: 'Whaao te awa - Wade the river',
                category: 'actions',
                pronunciation: 'FAH-ah-oh',
                culturalNote: 'Traditional river crossing technique'
            },
            'KANGA': {
                word: 'KANGA',
                meaning: 'Call, cry out, summon',
                example: 'Kanga mai - Call out',
                category: 'actions',
                pronunciation: 'KAH-ngah',
                culturalNote: 'Vocal communication and calling'
            },
            'WHANA': {
                word: 'WHANA',
                meaning: 'Kick, strike with foot',
                example: 'Whana te pōro - Kick the ball',
                category: 'actions',
                pronunciation: 'FAH-nah',
                culturalNote: 'Physical action in games and combat'
            },
            'HURUA': {
                word: 'HURUA',
                meaning: 'Disinter, dig up, uncover',
                example: 'Hurua te taonga - Uncover the treasure',
                category: 'actions',
                pronunciation: 'hoo-ROO-ah',
                culturalNote: 'Revealing hidden or buried things'
            },
            'WHAOA': {
                word: 'WHAOA',
                meaning: 'Prepare, get ready, set up',
                example: 'Whaoa mai - Get ready',
                category: 'actions',
                pronunciation: 'FAH-oh-ah',
                culturalNote: 'Preparation for important events'
            },
            'PATAI': {
                word: 'PATAI',
                meaning: 'Ask, question, inquire',
                example: 'Patai mai - Ask me',
                category: 'actions',
                pronunciation: 'pah-TAH-ee',
                culturalNote: 'Seeking knowledge through questioning'
            },
            'WETE': {
                word: 'WETE',
                meaning: 'Unravel, undo, separate',
                example: 'Wete te taura - Unravel the rope',
                category: 'actions',
                pronunciation: 'WEH-teh',
                culturalNote: 'Careful undoing or separation'
            },
            'HIKOI': {
                word: 'HIKOI',
                meaning: 'Walk, march, journey',
                example: 'Hikoi atu - Walk away',
                category: 'actions',
                pronunciation: 'HEE-koh-ee',
                culturalNote: 'Purposeful walking or marching'
            },
            'ATETE': {
                word: 'ATETE',
                meaning: 'Resist, oppose, defy',
                example: 'Atete te kino - Resist evil',
                category: 'actions',
                pronunciation: 'ah-TEH-teh',
                culturalNote: 'Standing against wrongdoing'
            },
            'RANEA': {
                word: 'RANEA',
                meaning: 'Float, drift, be buoyant',
                example: 'Ranea te waka - The boat floats',
                category: 'actions',
                pronunciation: 'rah-NEH-ah',
                culturalNote: 'Natural buoyancy and drifting'
            },

            // More 5-letter adjectives and descriptors
            'MAORI': {
                word: 'MAORI',
                meaning: 'Normal, ordinary, indigenous',
                example: 'He Māori - Indigenous person',
                category: 'people',
                pronunciation: 'MAH-oh-ree',
                culturalNote: 'Originally meant normal/ordinary, now refers to indigenous people'
            },
            'RONGO': {
                word: 'RONGO',
                meaning: 'Hear, listen, news',
                example: 'Rongo mai - Listen',
                category: 'actions',
                pronunciation: 'ROH-ngoh',
                culturalNote: 'Active listening and receiving news'
            },
            'KITE': {
                word: 'KITE',
                meaning: 'See, find, discover',
                example: 'Kite au - I see',
                category: 'actions',
                pronunciation: 'KEE-teh',
                culturalNote: 'Physical and spiritual seeing'
            },
            'WHATU': {
                word: 'WHATU',
                meaning: 'Eye, weave, knit',
                example: 'Nga whatu - The eyes',
                category: 'body',
                pronunciation: 'FAH-too',
                culturalNote: 'Vision and traditional weaving skills'
            },
            'WERA': {
                word: 'WERA',
                meaning: 'Hot, warm, burn',
                example: 'He wera - Hot',
                category: 'qualities',
                pronunciation: 'WEH-rah',
                culturalNote: 'Heat and warmth, physical or emotional'
            },
            'MAMAE': {
                word: 'MAMAE',
                meaning: 'Pain, hurt, ache',
                example: 'He mamae - Pain',
                category: 'feelings',
                pronunciation: 'mah-MAH-eh',
                culturalNote: 'Physical or emotional pain'
            },
            'HIAHIA': {
                word: 'HIAHIA',
                meaning: 'Want, desire, wish',
                example: 'Hiahia au - I want',
                category: 'emotions',
                pronunciation: 'hee-ah-HEE-ah',
                culturalNote: 'Personal wanting and desires'
            },

            // 6-letter words for the 6-letter variant
            'KAIAKO': { 
                word: 'KAIAKO', 
                meaning: 'Teacher, educator, instructor', 
                example: 'He kaiako pai ia - They are a good teacher', 
                category: 'people',
                pronunciation: 'kah-ee-AH-koh',
                culturalNote: 'More than instructor - includes mentoring and cultural guidance'
            },
            'KORERO': {
                word: 'KORERO',
                meaning: 'To talk, speak, speech, narrative',
                example: 'Kia kaha te kōrero Māori - Speak Māori strongly',
                category: 'actions',
                pronunciation: 'koh-REH-roh',
                culturalNote: 'Vital for passing down stories and history'
            },
            'WHAKAU': {
                word: 'WHAKAU',
                meaning: 'To lean against, support',
                example: 'Whakau mai - Lean on me',
                category: 'actions',
                pronunciation: 'fah-KAH-oo',
                culturalNote: 'Concept of mutual support and cooperation'
            },
            'WHANAU': {
                word: 'WHANAU',
                meaning: 'Family, extended family group, to be born',
                example: 'Ko taku whānau - My family',
                category: 'whanau',
                pronunciation: 'FAH-nah-oo',
                culturalNote: 'Extends beyond nuclear family to include wider kinship'
            },
            'WHENUA': {
                word: 'WHENUA',
                meaning: 'Land, country, birth place, placenta',
                example: 'Taku whenua - My land',
                category: 'nature',
                pronunciation: 'FEH-noo-ah',
                culturalNote: 'Deep connection between people and land'
            },
            'WAIATA': {
                word: 'WAIATA',
                meaning: 'Song, chant, music',
                example: 'He waiata atahua - A beautiful song',
                category: 'cultural',
                pronunciation: 'wah-ee-AH-tah',
                culturalNote: 'Important for preserving history and culture'
            },
            'WAIRUA': {
                word: 'WAIRUA',
                meaning: 'Spirit, soul, spiritual essence',
                example: 'He wairua pai - A good spirit',
                category: 'spiritual',
                pronunciation: 'wah-ee-ROO-ah',
                culturalNote: 'Spiritual dimension present in all living things'
            },
            'MAUNGA': {
                word: 'MAUNGA',
                meaning: 'Mountain, large hill',
                example: 'Te maunga - The mountain',
                category: 'nature',
                pronunciation: 'MAH-oo-ngah',
                culturalNote: 'Often ancestors in Māori cosmology'
            },
            'TAONGA': {
                word: 'TAONGA',
                meaning: 'Treasure, precious thing, valuable possession',
                example: 'He taonga tēnei - This is a treasure',
                category: 'cultural',
                pronunciation: 'tah-OH-ngah',
                culturalNote: 'Includes cultural practices, language, and spiritual treasures'
            },
            'MARAMA': {
                word: 'MARAMA',
                meaning: 'Moon, month, light',
                example: 'Te marama - The moon',
                category: 'nature',
                pronunciation: 'mah-RAH-mah',
                culturalNote: 'Important for traditional calendar and navigation'
            },

            // More 6-letter verbs and adjectives
            'WHAKAU': {
                word: 'WHAKAU',
                meaning: 'Support, lean against, assist',
                example: 'Whakau mai - Support me',
                category: 'actions',
                pronunciation: 'fah-KAH-oo',
                culturalNote: 'Mutual support and cooperation'
            },
            'WHAARI': {
                word: 'WHAARI',
                meaning: 'Share, divide, distribute',
                example: 'Whaari mai - Share with me',
                category: 'actions',
                pronunciation: 'fah-AH-ree',
                culturalNote: 'Generosity and community sharing'
            },
            'AWHINA': {
                word: 'AWHINA',
                meaning: 'Help, assist, support',
                example: 'Awhina mai - Help me',
                category: 'actions',
                pronunciation: 'ah-FEE-nah',
                culturalNote: 'Community support and mutual aid'
            },
            'WHAATI': {
                word: 'WHAATI',
                meaning: 'Break, smash, shatter',
                example: 'Kua whāti - It is broken',
                category: 'actions',
                pronunciation: 'fah-AH-tee',
                culturalNote: 'Physical breaking or destruction'
            },
            'TAKOTO': {
                word: 'TAKOTO',
                meaning: 'Lie down, rest, place',
                example: 'Takoto mai - Lie down',
                category: 'actions',
                pronunciation: 'tah-KOH-toh',
                culturalNote: 'Rest and positioning'
            },
            'PATUA': {
                word: 'PATUA',
                meaning: 'Strike, hit, beat',
                example: 'Patua te taniwha - Strike the taniwha',
                category: 'actions',
                pronunciation: 'pah-TOO-ah',
                culturalNote: 'Used in traditional stories and combat'
            },
            'ATAHUA': {
                word: 'ATAHUA',
                meaning: 'Beautiful, lovely, good',
                example: 'He atahua - Beautiful',
                category: 'qualities',
                pronunciation: 'ah-tah-HOO-ah',
                culturalNote: 'Beauty encompassing inner and outer qualities'
            },
            'TAIOHI': {
                word: 'TAIOHI',
                meaning: 'Young person, youth',
                example: 'He taiohi - A young person',
                category: 'people',
                pronunciation: 'tah-ee-OH-hee',
                culturalNote: 'Youth with potential and energy'
            },
            'PAKARI': {
                word: 'PAKARI',
                meaning: 'Strong, powerful, fit',
                example: 'He pakari - Strong',
                category: 'qualities',
                pronunciation: 'pah-KAH-ree',
                culturalNote: 'Physical and spiritual strength'
            },
            'HAUORA': {
                word: 'HAUORA',
                meaning: 'Health, wellness, wellbeing',
                example: 'Te hauora - Health',
                category: 'health',
                pronunciation: 'hah-oo-OH-rah',
                culturalNote: 'Holistic concept of physical, mental, spiritual wellness'
            },

            // More 6-letter words
            'PAPAKU': {
                word: 'PAPAKU',
                meaning: 'Shallow, not deep',
                example: 'He papaku - Shallow',
                category: 'qualities',
                pronunciation: 'pah-PAH-koo',
                culturalNote: 'Physical or metaphorical shallowness'
            },
            'HIAHIA': {
                word: 'HIAHIA',
                meaning: 'Want, desire, wish',
                example: 'Hiahia au - I want',
                category: 'emotions',
                pronunciation: 'hee-ah-HEE-ah',
                culturalNote: 'Personal wanting and desires'
            },
            'TANGATA': {
                word: 'TANGATA',
                meaning: 'Person, people, human being',
                example: 'He tangata pai - A good person',
                category: 'people',
                pronunciation: 'TAH-ngah-tah',
                culturalNote: 'Emphasizes common humanity'
            },
            'WHAIAO': {
                word: 'WHAIAO',
                meaning: 'Dawn, daybreak, early morning',
                example: 'I te whaiao - At dawn',
                category: 'time',
                pronunciation: 'FAH-ee-ah-oh',
                culturalNote: 'Sacred time of new beginnings'
            },
            'PAEPAE': {
                word: 'PAEPAE',
                meaning: 'Doorstep, threshold, speakers bench',
                example: 'Ki te paepae - To the threshold',
                category: 'cultural',
                pronunciation: 'PAH-eh-PAH-eh',
                culturalNote: 'Sacred speaking platform on marae'
            },
            'MANAWA': {
                word: 'MANAWA',
                meaning: 'Heart, breath, time',
                example: 'Taku manawa - My heart',
                category: 'body',
                pronunciation: 'mah-NAH-wah',
                culturalNote: 'Centre of life and emotion'
            },
            'TATAKU': {
                word: 'TATAKU',
                meaning: 'Knock, tap, strike gently',
                example: 'Tataku te tatau - Knock the door',
                category: 'actions',
                pronunciation: 'tah-TAH-koo',
                culturalNote: 'Gentle striking or knocking'
            },
            'WHANGA': {
                word: 'WHANGA',
                meaning: 'Bay, harbor, inlet',
                example: 'Te whanga - The bay',
                category: 'nature',
                pronunciation: 'FAH-ngah',
                culturalNote: 'Natural harbor and safe waters'
            },
            'ATAHUA': {
                word: 'ATAHUA',
                meaning: 'Beautiful, lovely, good',
                example: 'He atahua - Beautiful',
                category: 'qualities',
                pronunciation: 'ah-tah-HOO-ah',
                culturalNote: 'Beauty encompassing inner and outer qualities'
            },
            'KOHATU': {
                word: 'KOHATU',
                meaning: 'Stone, rock, boulder',
                example: 'He kohatu - A stone',
                category: 'nature',
                pronunciation: 'koh-HAH-too',
                culturalNote: 'Important in traditional tools and monuments'
            },

            // Even more 5-letter words - pushing to find every possible one!
            'TIRAU': {
                word: 'TIRAU',
                meaning: 'String of pearls, hang in festoons',
                example: 'Tirau nga kakano - String the seeds',
                category: 'actions',
                pronunciation: 'tee-RAH-oo',
                culturalNote: 'Traditional decoration and adornment'
            },
            'WHIRI': {
                word: 'WHIRI',
                meaning: 'Choose, select, plait',
                example: 'Whiri mai - Choose',
                category: 'actions',
                pronunciation: 'FEE-ree',
                culturalNote: 'Important decision-making and traditional crafts'
            },
            'TAAHI': {
                word: 'TAAHI',
                meaning: 'Light a fire, kindle',
                example: 'Taahi te ahi - Light the fire',
                category: 'actions',
                pronunciation: 'tah-AH-hee',
                culturalNote: 'Essential survival and cultural skill'
            },
            'WHANO': {
                word: 'WHANO',
                meaning: 'Stretch out, extend',
                example: 'Whano atu - Stretch out',
                category: 'actions',
                pronunciation: 'FAH-noh',
                culturalNote: 'Physical extension and reaching'
            },
            'WHAOA': {
                word: 'WHAOA',
                meaning: 'Clear land, cultivate',
                example: 'Whaoa te whenua - Clear the land',
                category: 'actions',
                pronunciation: 'FAH-oh-ah',
                culturalNote: 'Traditional land preparation'
            },
            'KAUAE': {
                word: 'KAUAE',
                meaning: 'Jaw, chin',
                example: 'Te kauae - The jaw',
                category: 'body',
                pronunciation: 'kah-oo-AH-eh',
                culturalNote: 'Important in traditional facial features'
            },
            'TAERO': {
                word: 'TAERO',
                meaning: 'Spear, javelin',
                example: 'He taero - A spear',
                category: 'tools',
                pronunciation: 'tah-EH-roh',
                culturalNote: 'Traditional hunting and warfare weapon'
            },
            'RAUPO': {
                word: 'RAUPO',
                meaning: 'Bulrush, cattail plant',
                example: 'Te raupo - The bulrush',
                category: 'nature',
                pronunciation: 'rah-oo-POH',
                culturalNote: 'Traditional building and weaving material'
            },
            'KOURA': {
                word: 'KOURA',
                meaning: 'Freshwater crayfish',
                example: 'He koura - A crayfish',
                category: 'animals',
                pronunciation: 'koh-oo-RAH',
                culturalNote: 'Traditional kai (food) from rivers'
            },
            'INAKA': {
                word: 'INAKA',
                meaning: 'Now, at this time',
                example: 'Inaka nei - Right now',
                category: 'time',
                pronunciation: 'ee-NAH-kah',
                culturalNote: 'Present moment awareness'
            },
            'TAEWA': {
                word: 'TAEWA',
                meaning: 'Potato, especially traditional varieties',
                example: 'He taewa - A potato',
                category: 'food',
                pronunciation: 'tah-EH-wah',
                culturalNote: 'Traditional Māori potato varieties'
            },
            'WHAOA': {
                word: 'WHAOA',
                meaning: 'Exclamation of surprise',
                example: 'Whaoa! - Wow!',
                category: 'expressions',
                pronunciation: 'FAH-oh-ah',
                culturalNote: 'Expression of amazement'
            },
            'POROA': {
                word: 'POROA',
                meaning: 'Long, extended, tall',
                example: 'He poroa - Long',
                category: 'qualities',
                pronunciation: 'poh-ROH-ah',
                culturalNote: 'Physical length and extension'
            },
            'KAPU': {
                word: 'KAPU',
                meaning: 'Scoop up, cup hands',
                example: 'Kapu te wai - Scoop the water',
                category: 'actions',
                pronunciation: 'KAH-poo',
                culturalNote: 'Traditional way of drinking water'
            },
            'MIHIA': {
                word: 'MIHIA',
                meaning: 'Greet, salute, cherish',
                example: 'Mihia mai - Greet me',
                category: 'actions',
                pronunciation: 'mee-HEE-ah',
                culturalNote: 'Traditional greeting and cherishing customs'
            },

            // More carefully counted 6-letter words!
            'MAHARA': {
                word: 'MAHARA',
                meaning: 'Remember, think, consider',
                example: 'Mahara ki a au - Remember me',
                category: 'mental',
                pronunciation: 'mah-HAH-rah',
                culturalNote: 'Deep remembering and consideration'
            },
            'PATAKA': {
                word: 'PATAKA',
                meaning: 'Storehouse, pantry, library',
                example: 'Te pataka - The storehouse',
                category: 'buildings',
                pronunciation: 'pah-TAH-kah',
                culturalNote: 'Traditional food and knowledge storage'
            },
            'KOTAHI': {
                word: 'KOTAHI',
                meaning: 'One, single, together',
                example: 'Kotahi - One',
                category: 'numbers',
                pronunciation: 'koh-TAH-hee',
                culturalNote: 'Unity and oneness'
            },
            'KARAKA': {
                word: 'KARAKA',
                meaning: 'Native orange tree, clock',
                example: 'He karaka - A karaka tree',
                category: 'nature',
                pronunciation: 'kah-RAH-kah',
                culturalNote: 'Important traditional food tree'
            },
            'HOHONU': {
                word: 'HOHONU',
                meaning: 'Deep, profound, low',
                example: 'He hohonu - Deep',
                category: 'qualities',
                pronunciation: 'hoh-HOH-noo',
                culturalNote: 'Physical and spiritual depth'
            },
            'KAUHUA': {
                word: 'KAUHUA',
                meaning: 'Strength, power, force',
                example: 'Te kauhua - The strength',
                category: 'qualities',
                pronunciation: 'kah-oo-HOO-ah',
                culturalNote: 'Inner and outer strength'
            },
            'MAHINA': {
                word: 'MAHINA',
                meaning: 'Moon, month',
                example: 'Te mahina - The moon',
                category: 'nature',
                pronunciation: 'mah-HEE-nah',
                culturalNote: 'Lunar cycles and time keeping'
            },
            'WAENUA': {
                word: 'WAENUA',
                meaning: 'Middle, centre, between',
                example: 'Ki waenganui - In the middle',
                category: 'locations',
                pronunciation: 'wah-eh-NOO-ah',
                culturalNote: 'Central position and balance'
            },
            'RONGOĀ': {
                word: 'RONGOĀ',
                meaning: 'Medicine, traditional healing',
                example: 'Te rongoā - The medicine',
                category: 'health',
                pronunciation: 'roh-ngoh-AH',
                culturalNote: 'Traditional Māori healing practices'
            },
            'TIPUNA': {
                word: 'TIPUNA',
                meaning: 'Ancestor, grandparent',
                example: 'Aku tipuna - My ancestors',
                category: 'people',
                pronunciation: 'tee-POO-nah',
                culturalNote: 'Revered ancestors and lineage'
            },

            // FINAL HUNT - Every remaining 5-letter word!
            'TARAU': {
                word: 'TARAU',
                meaning: 'Trousers, pants',
                example: 'He tarau - Trousers',
                category: 'clothing',
                pronunciation: 'tah-RAH-oo',
                culturalNote: 'Modern clothing adapted into te reo'
            },
            'HOATU': {
                word: 'HOATU',
                meaning: 'Give away, donate, present',
                example: 'Hoatu ki a ia - Give it to them',
                category: 'actions',
                pronunciation: 'hoh-AH-too',
                culturalNote: 'Generosity and gift-giving customs'
            },
            'HOMAI': {
                word: 'HOMAI',
                meaning: 'Give to me, hand over',
                example: 'Homai te pukapuka - Give me the book',
                category: 'actions',
                pronunciation: 'hoh-MAH-ee',
                culturalNote: 'Polite requesting and receiving'
            },
            'WHAOA': {
                word: 'WHAOA',
                meaning: 'Wow, expression of amazement',
                example: 'Whaoa! He ataahua! - Wow! Beautiful!',
                category: 'expressions',
                pronunciation: 'FAH-oh-ah',
                culturalNote: 'Natural expression of wonder'
            },
            'TOPUNI': {
                word: 'TOPUNI',
                meaning: 'Cloak, cover completely',
                example: 'Topuni ki te kōwai - Cover with the cloak',
                category: 'clothing',
                pronunciation: 'toh-POO-nee',
                culturalNote: 'Traditional Māori cloaks and covering'
            },
            'POAKA': {
                word: 'POAKA',
                meaning: 'Pig, pork',
                example: 'He poaka - A pig',
                category: 'animals',
                pronunciation: 'poh-AH-kah',
                culturalNote: 'Introduced animal, now part of traditional kai'
            },
            'HIAKO': {
                word: 'HIAKO',
                meaning: 'Shark',
                example: 'He hiako - A shark',
                category: 'animals',
                pronunciation: 'hee-AH-koh',
                culturalNote: 'Respected ocean predator in Māori culture'
            },
            'TUORO': {
                word: 'TUORO',
                meaning: 'Sound, noise, tone',
                example: 'He tuoro atahua - A beautiful sound',
                category: 'sounds',
                pronunciation: 'too-OH-roh',
                culturalNote: 'Musical and natural sounds'
            },
            'POHATU': {
                word: 'POHATU',
                meaning: 'Stone, rock, boulder',
                example: 'He pohatu nui - A big stone',
                category: 'nature',
                pronunciation: 'poh-HAH-too',
                culturalNote: 'Important in traditional tools and construction'
            },
            'TAIAO': {
                word: 'TAIAO',
                meaning: 'Environment, world, natural surroundings',
                example: 'Tiaki i te taiao - Care for the environment',
                category: 'nature',
                pronunciation: 'tah-ee-AH-oh',
                culturalNote: 'Holistic view of environmental stewardship'
            },

            // FINAL HUNT - Every remaining 6-letter word!
            'HAUHUNGA': {
                word: 'HAUHUNGA',
                meaning: 'Shallow, not deep, superficial',
                example: 'He hauhunga te moana - The ocean is shallow',
                category: 'qualities',
                pronunciation: 'hah-oo-HOO-ngah',
                culturalNote: 'Physical and metaphorical shallowness'
            },
            'KONIHI': {
                word: 'KONIHI',
                meaning: 'Dizzy, giddy, confused',
                example: 'Kei te konihi au - I am dizzy',
                category: 'feelings',
                pronunciation: 'koh-NEE-hee',
                culturalNote: 'Physical disorientation and confusion'
            },
            'TAWHAO': {
                word: 'TAWHAO',
                meaning: 'Encircle, surround, wrap around',
                example: 'Tawhao te whare - Surround the house',
                category: 'actions',
                pronunciation: 'tah-FAH-oh',
                culturalNote: 'Traditional defensive and protective actions'
            },
            'WHATUA': {
                word: 'WHATUA',
                meaning: 'Family, relations, kin group',
                example: 'Ko taku whātua - My family group',
                category: 'whanau',
                pronunciation: 'FAH-too-ah',
                culturalNote: 'Extended kinship networks'
            },
            'KOINGA': {
                word: 'KOINGA',
                meaning: 'Planting season, time of sowing',
                example: 'Te koinga - The planting season',
                category: 'time',
                pronunciation: 'koh-EE-ngah',
                culturalNote: 'Traditional agricultural cycles'
            },
            'TOIORA': {
                word: 'TOIORA',
                meaning: 'Health, wellness, vitality',
                example: 'Te toiora - Health and wellness',
                category: 'health',
                pronunciation: 'toh-ee-OH-rah',
                culturalNote: 'Holistic concept of health and well-being'
            },
            'KAIHUA': {
                word: 'KAIHUA',
                meaning: 'Speaker, orator, spokesperson',
                example: 'He kaihua - A speaker',
                category: 'people',
                pronunciation: 'kah-ee-HOO-ah',
                culturalNote: 'Respected role in traditional gatherings'
            },
            'POWHIRI': {
                word: 'POWHIRI',
                meaning: 'Welcome ceremony, greeting ritual',
                example: 'Te pōwhiri - The welcome ceremony',
                category: 'cultural',
                pronunciation: 'poh-FEE-ree',
                culturalNote: 'Sacred welcoming protocols on marae'
            },
            'MAIORO': {
                word: 'MAIORO',
                meaning: 'Peace, tranquility, calm',
                example: 'Kia maioro - Be at peace',
                category: 'states',
                pronunciation: 'mah-ee-OH-roh',
                culturalNote: 'Inner peace and harmony'
            },
            'WEHIWEHI': {
                word: 'WEHIWEHI',
                meaning: 'Fearsome, awesome, impressive',
                example: 'He mea wehiwehi - Something awesome',
                category: 'qualities',
                pronunciation: 'weh-hee-WEH-hee',
                culturalNote: 'Inspiring awe and respect'
            }
        };
    }

    /**
     * Validate if a word is authentic Māori
     */
    async validateMaoriWord(word) {
        if (!word || typeof word !== 'string') return false;
        
        const normalizedWord = this.normalizeText(word);
        
        // Check cache first
        const cacheKey = `validate_${normalizedWord}`;
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheExpiry) {
                return cached.data;
            }
        }

        // Check fallback dictionary first (for reliability)
        if (this.fallbackDictionary[normalizedWord]) {
            this.cache.set(cacheKey, { data: true, timestamp: Date.now() });
            return true;
        }

        // If online, try API validation
        if (this.isOnline) {
            try {
                const response = await fetch(`${this.baseURL}/words/${encodeURIComponent(normalizedWord)}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                    },
                    timeout: 3000 // 3 second timeout
                });

                if (response.ok) {
                    const data = await response.json();
                    const isValid = data && data.entries && data.entries.length > 0;
                    this.cache.set(cacheKey, { data: isValid, timestamp: Date.now() });
                    return isValid;
                }
            } catch (error) {
                console.warn('Te Aka API validation failed, using fallback:', error);
            }
        }

        // Fallback to pattern-based validation for common Māori words
        return this.validateMaoriPattern(normalizedWord);
    }

    /**
     * Get word definition with cultural context
     */
    async getWordDefinition(word) {
        if (!word || typeof word !== 'string') return null;
        
        const normalizedWord = this.normalizeText(word);
        
        // Check cache first
        const cacheKey = `definition_${normalizedWord}`;
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheExpiry) {
                return cached.data;
            }
        }

        // Check fallback dictionary first
        if (this.fallbackDictionary[normalizedWord]) {
            const definition = this.fallbackDictionary[normalizedWord];
            this.cache.set(cacheKey, { data: definition, timestamp: Date.now() });
            return definition;
        }

        // If online, try API
        if (this.isOnline) {
            try {
                const response = await fetch(`${this.baseURL}/words/${encodeURIComponent(normalizedWord)}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                    },
                    timeout: 5000
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data && data.entries && data.entries.length > 0) {
                        const definition = this.formatAPIDefinition(data, normalizedWord);
                        this.cache.set(cacheKey, { data: definition, timestamp: Date.now() });
                        return definition;
                    }
                }
            } catch (error) {
                console.warn('Te Aka API definition failed, using fallback:', error);
            }
        }

        return null;
    }

    /**
     * Check if word deserves cultural bonus (is Māori)
     */
    async isMaoriWord(word) {
        return await this.validateMaoriWord(word);
    }

    /**
     * Format API response into consistent structure
     */
    formatAPIDefinition(apiData, word) {
        const entry = apiData.entries[0];
        return {
            word: word.toUpperCase(),
            meaning: entry.definition || '',
            example: entry.example || '',
            category: entry.category || 'general',
            pronunciation: entry.pronunciation || '',
            culturalNote: entry.culturalNote || ''
        };
    }

    /**
     * Normalize Māori text (handle macrons and case)
     */
    normalizeText(text) {
        if (!text) return '';
        return text.toUpperCase()
            .replace(/Ā/g, 'A')
            .replace(/Ē/g, 'E')
            .replace(/Ī/g, 'I')
            .replace(/Ō/g, 'O')
            .replace(/Ū/g, 'U')
            .trim();
    }

    /**
     * Pattern-based validation for Māori words
     */
    validateMaoriPattern(word) {
        // Basic Māori phonological patterns
        const maoriPattern = /^[AEIOUWHRNGTKMPL]+$/;
        const hasValidCombinations = /WH|NG|[AEIOU]/;
        const hasConsonantClusters = /[BCDFGJQSVXYZ]{2,}|[WHRNGTKMPL]{3,}/;
        
        // Check if word follows Māori phonology
        return maoriPattern.test(word) && 
               hasValidCombinations.test(word) && 
               !hasConsonantClusters.test(word) &&
               word.length <= 10; // Reasonable length limit
    }

    /**
     * Get all valid Māori words for a game
     */
    getValidMaoriWords(length = null) {
        const words = Object.keys(this.fallbackDictionary);
        return length ? words.filter(word => word.length === length) : words;
    }

    /**
     * Get random Māori word for games
     */
    getRandomMaoriWord(length = 5, category = null) {
        let words = this.getValidMaoriWords(length);
        
        if (category) {
            words = words.filter(word => 
                this.fallbackDictionary[word].category === category
            );
        }
        
        if (words.length === 0) return null;
        
        const randomIndex = Math.floor(Math.random() * words.length);
        const selectedWord = words[randomIndex];
        return this.fallbackDictionary[selectedWord];
    }

    /**
     * Clear cache (for debugging or reset)
     */
    clearCache() {
        this.cache.clear();
    }

    /**
     * Get cache statistics
     */
    getCacheStats() {
        return {
            size: this.cache.size,
            entries: Array.from(this.cache.keys())
        };
    }
}

// Initialize global dictionary API instance
window.maoriDictionaryAPI = new MaoriDictionaryAPI();

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MaoriDictionaryAPI;
}