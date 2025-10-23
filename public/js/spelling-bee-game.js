// Enhanced Te Reo Māori Spelling Bee Game
// Integrates with Māori Dictionary API, Gamification, and Adaptive Difficulty

// Game state
let gameState = {
    centerLetter: '',
    outerLetters: [],
    foundWords: [],
    score: 0,
    pangrams: 0,
    gameActive: false,
    wordDefinitions: new Map(),
    pronunciationEnabled: true
};

// Te Reo Māori word lists for validation and scoring
const MAORI_WORDS = [
    // 4-letter words
    'aroha', 'kaiako', 'mauri', 'tangi', 'tapu', 'tino', 'wairua', 'whenua',
    'whare', 'mana', 'papa', 'rama', 'roto', 'taha', 'taiao', 'taonga', 'whaea',
    'matua', 'tamariki', 'hapū', 'iwi', 'kura', 'ranga', 'waka', 'mata', 'nuku',
    
    // 5-letter words
    'rangatira', 'kaumātua', 'kōhanga', 'mahinga', 'whakatū', 'tāngata', 'wahine',
    'tamariki', 'mātauranga', 'whakapapa', 'manaakitanga', 'kaitiakitanga',
    
    // 6+ letter words
    'whakatōhea', 'rangatiratanga', 'manaakitanga', 'whakapapa', 'kaitiakitanga',
    'tangata', 'tamariki', 'kaumātua', 'wahine', 'tāngata', 'mātauranga'
];

// English word validation (basic list)
const ENGLISH_WORDS = [
    'area', 'tear', 'rate', 'near', 'eaten', 'enter', 'nature', 'tenant',
    'rent', 'earn', 'neat', 'treat', 'train', 'inter', 'retain', 'entire'
];

// Daily puzzle configurations
const DAILY_PUZZLES = [
    { center: 'A', outer: ['T', 'E', 'R', 'O', 'N', 'I'] },
    { center: 'E', outer: ['T', 'A', 'R', 'O', 'N', 'I'] },
    { center: 'I', outer: ['T', 'A', 'E', 'R', 'O', 'N'] },
    { center: 'O', outer: ['T', 'A', 'E', 'R', 'N', 'I'] },
    { center: 'U', outer: ['T', 'A', 'E', 'R', 'O', 'N'] }
];

// Initialize game
function initSpellingBee() {
    // Get daily puzzle
    const today = new Date();
    const dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / 86400000);
    const puzzleIndex = dayOfYear % DAILY_PUZZLES.length;
    const puzzle = DAILY_PUZZLES[puzzleIndex];
    
    gameState.centerLetter = puzzle.center;
    gameState.outerLetters = [...puzzle.outer];
    gameState.foundWords = [];
    gameState.score = 0;
    gameState.pangrams = 0;
    gameState.wordDefinitions.clear();
    
    // Render the hexagon
    renderHexagon();
    updateScore();
    
    // Initialize gamification
    if (window.gamificationSystem) {
        window.gamificationSystem.startGameSession('spelling-bee', {
            difficulty: 'medium',
            learningObjectives: ['te-reo-maori', 'spelling', 'vocabulary', 'cultural-literacy']
        });
    }
    
    // Initialize adaptive difficulty
    if (window.adaptiveDifficulty) {
        window.adaptiveDifficulty.startSession('spelling-bee');
    }
    
    // Setup event listeners
    setupEventListeners();
}

// Render the hexagon layout
function renderHexagon() {
    const centerLetterEl = document.getElementById('center-letter');
    const outerLetters = document.querySelectorAll('.hex-outer');
    
    centerLetterEl.textContent = gameState.centerLetter;
    centerLetterEl.style.backgroundColor = '#FFD700'; // Gold for center
    
    gameState.outerLetters.forEach((letter, index) => {
        if (outerLetters[index]) {
            outerLetters[index].textContent = letter;
            outerLetters[index].style.backgroundColor = '#E8F4FD';
        }
    });
}

// Setup event listeners
function setupEventListeners() {
    const wordInput = document.getElementById('word-input');
    const submitBtn = document.getElementById('submit-btn');
    const deleteBtn = document.getElementById('delete-btn');
    const shuffleBtn = document.getElementById('shuffle-btn');
    
    // Letter click handlers
    document.querySelectorAll('.hex-letter').forEach(letter => {
        letter.addEventListener('click', () => {
            if (gameState.gameActive) {
                const letterText = letter.textContent;
                wordInput.value += letterText.toLowerCase();
                wordInput.focus();
            }
        });
    });
    
    // Submit word
    submitBtn.addEventListener('click', submitWord);
    
    // Delete last character
    deleteBtn.addEventListener('click', () => {
        const current = wordInput.value;
        wordInput.value = current.slice(0, -1);
    });
    
    // Shuffle outer letters
    shuffleBtn.addEventListener('click', shuffleLetters);
    
    // Enter key submission
    wordInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            submitWord();
        }
    });
}

// Enhanced word submission with API validation
async function submitWord() {
    const wordInput = document.getElementById('word-input');
    const word = wordInput.value.toLowerCase().trim();
    
    if (!word) return;
    
    // Basic validation
    if (word.length < 4) {
        showMessage('Words must be at least 4 letters long!', 'error');
        return;
    }
    
    if (foundWords.includes(word)) {
        showMessage('You already found that word!', 'error');
        wordInput.value = '';
        return;
    }
    
    // Check if word uses valid letters
    if (!isValidWord(word)) {
        showMessage('Word must include the center letter and only use available letters!', 'error');
        wordInput.value = '';
        return;
    }
    
    // Enhanced validation with Māori Dictionary API
    let isValid = false;
    let isMaori = false;
    let wordDefinition = null;
    
    // Check against predefined lists first
    isMaori = MAORI_WORDS.includes(word);
    const isEnglish = ENGLISH_WORDS.includes(word);
    
    if (isMaori || isEnglish) {
        isValid = true;
    } else if (window.maoriDictionaryAPI) {
        // Check with API for additional Māori words
        try {
            const isValidMaori = await window.maoriDictionaryAPI.validateMaoriWord(word.toUpperCase());
            if (isValidMaori) {
                isMaori = true;
                isValid = true;
                // Get definition for display
                wordDefinition = await window.maoriDictionaryAPI.getWordDefinition(word.toUpperCase());
                if (wordDefinition) {
                    gameState.wordDefinitions.set(word, wordDefinition);
                }
            }
        } catch (error) {
        }
    }
    
    if (!isValid) {
        showMessage(`"${word}" is not a valid word. Try again!`, 'error');
        wordInput.value = '';
        return;
    }
    
    // Add word to found list
    gameState.foundWords.push(word);
    
    // Calculate points
    const points = calculatePoints(word);
    gameState.score += points;
    
    // Check for pangram
    const isPangram = isPangramWord(word);
    if (isPangram) {
        gameState.pangrams++;
    }
    
    // Update display
    updateScore();
    renderFoundWord(word, points, isMaori, isPangram);
    wordInput.value = '';
    
    // Show success message
    let message;
    if (isPangram) {
        message = `🎉 PANGRAM! "${word}" uses all 7 letters - ${points} points!`;
    } else if (isMaori) {
        message = `Ka rawe! "${word}" is Te Reo Māori - ${points} points (doubled)!`;
    } else {
        message = `Great! "${word}" - ${points} points!`;
    }
    showMessage(message, 'success');
    
    // Show definition popup if available
    if (wordDefinition) {
        showDefinitionPopup(word, wordDefinition);
    }
}

// Validate word against game rules
function isValidWord(word) {
    // Must include center letter
    if (!word.includes(gameState.centerLetter.toLowerCase())) {
        return false;
    }
    
    // All letters must be from available set
    const availableLetters = [gameState.centerLetter.toLowerCase(), ...gameState.outerLetters.map(l => l.toLowerCase())];
    for (let letter of word) {
        if (!availableLetters.includes(letter)) {
            return false;
        }
    }
    
    return true;
}

// Calculate points for a word
function calculatePoints(word) {
    let points = 0;
    
    if (word.length === 4) points = 1;
    else if (word.length === 5) points = 2;
    else if (word.length === 6) points = 3;
    else if (word.length === 7) points = 5;
    else if (word.length >= 8) points = 8;
    
    // Double points for Māori words
    if (MAORI_WORDS.includes(word) || gameState.wordDefinitions.has(word)) {
        points *= 2;
    }
    
    // Pangram bonus
    if (isPangramWord(word)) {
        points += 7; // Bonus for using all letters
    }
    
    return points;
}

// Check if word is a pangram (uses all 7 letters)
function isPangramWord(word) {
    const allLetters = [gameState.centerLetter.toLowerCase(), ...gameState.outerLetters.map(l => l.toLowerCase())];
    const wordLetters = [...new Set(word.toLowerCase())];
    
    return allLetters.every(letter => wordLetters.includes(letter));
}

// Update score display
function updateScore() {
    document.getElementById('words-count').textContent = gameState.foundWords.length;
    document.getElementById('score').textContent = gameState.score;
    document.getElementById('pangrams-count').textContent = gameState.pangrams;
    
    // Update rank
    updateRank();
}

// Update player rank based on score
function updateRank() {
    const rankName = document.getElementById('rank-name');
    const rankDescription = document.getElementById('rank-description');
    
    let rank, description;
    
    if (gameState.score >= 100) {
        rank = 'Māori Master';
        description = 'Outstanding! You truly understand Te Reo Māori!';
    } else if (gameState.score >= 75) {
        rank = 'Language Leader';
        description = 'Excellent work! Keep exploring Māori words!';
    } else if (gameState.score >= 50) {
        rank = 'Word Warrior';
        description = 'Great progress! You\'re building strong vocabulary!';
    } else if (gameState.score >= 25) {
        rank = 'Letter Learner';
        description = 'Good start! Keep discovering new words!';
    } else {
        rank = 'Beginner';
        description = 'Keep finding words to advance!';
    }
    
    rankName.textContent = rank;
    rankDescription.textContent = description;
}

// Render found word in the grid
function renderFoundWord(word, points, isMaori, isPangram) {
    const wordsGrid = document.getElementById('words-grid');
    const wordDiv = document.createElement('div');
    
    wordDiv.className = 'found-word';
    if (isMaori) wordDiv.classList.add('maori-word');
    if (isPangram) wordDiv.classList.add('pangram-word');
    
    wordDiv.innerHTML = `
        <span class="word-text">${word}</span>
        <span class="word-points">${points}</span>
        ${isMaori ? '<span class="maori-badge">Māori</span>' : ''}
        ${isPangram ? '<span class="pangram-badge">Pangram!</span>' : ''}
    `;
    
    // Add click handler for definition
    wordDiv.addEventListener('click', () => {
        if (gameState.wordDefinitions.has(word)) {
            showDefinitionPopup(word, gameState.wordDefinitions.get(word));
        }
    });
    
    wordsGrid.appendChild(wordDiv);
}

// Shuffle outer letters
function shuffleLetters() {
    const shuffled = [...gameState.outerLetters];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    gameState.outerLetters = shuffled;
    renderHexagon();
}

// Enhanced definition popup with pronunciation
function showDefinitionPopup(word, definition) {
    const popup = document.createElement('div');
    popup.className = 'definition-popup';
    popup.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        border: 2px solid var(--color-primary);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        z-index: 1000;
        max-width: 500px;
        width: 90%;
        text-align: center;
    `;
    
    popup.innerHTML = `
        <div style="margin-bottom: 1rem;">
            <h3 style="margin: 0 0 1rem 0; color: var(--color-primary); font-size: 1.5rem; display: flex; align-items: center; justify-content: center; gap: 1rem;">
                <span>${word.toUpperCase()}</span>
                <button onclick="speakMaoriWord('${word}', '${definition.pronunciation || ''}')"
                        style="background: var(--color-secondary); color: white; border: none; border-radius: 20px; padding: 0.5rem 1rem; cursor: pointer;"
                        title="Listen to pronunciation">
                    🔊 Whakarongo
                </button>
            </h3>
            <p style="margin: 0 0 1rem 0; font-size: 1.1rem;"><strong>Meaning:</strong> ${definition.meaning}</p>
            ${definition.example ? `<p style="margin: 0 0 1rem 0; font-style: italic;"><strong>Example:</strong> ${definition.example}</p>` : ''}
            ${definition.pronunciation ? `<p style="margin: 0 0 1rem 0; color: var(--color-secondary); font-style: italic;"><strong>Pronunciation:</strong> ${definition.pronunciation}</p>` : ''}
            <div style="margin-top: 1rem; padding: 1rem; background: rgba(184, 134, 11, 0.1); border-radius: 6px; border-left: 4px solid var(--color-secondary);">
                <p style="margin: 0; font-style: italic; color: var(--color-secondary);">
                    <strong>🌟 Cultural Note:</strong> Every Te Reo Māori word carries deeper cultural meaning and connects to the rich history and worldview of Māori people.
                </p>
            </div>
        </div>
        <button onclick="closeDefinitionPopup()" 
                style="background: var(--color-primary); color: white; border: none; border-radius: 6px; padding: 0.8rem 1.5rem; cursor: pointer; font-size: 1rem;">
            Ka rawe! (Awesome!)
        </button>
    `;
    
    document.body.appendChild(popup);
    
    // Close on background click
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            closeDefinitionPopup();
        }
    });
}

// Close definition popup
function closeDefinitionPopup() {
    const popup = document.querySelector('.definition-popup');
    if (popup) {
        popup.remove();
    }
}

// Māori pronunciation using Web Speech API
function speakMaoriWord(word, pronunciation) {
    if (!gameState.pronunciationEnabled) return;
    
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = 'mi-NZ'; // Māori language code
        utterance.rate = 0.7; // Slower for learning
        utterance.pitch = 1.0;
        
        // Try to find a Māori voice if available
        const voices = speechSynthesis.getVoices();
        const maoriVoice = voices.find(voice => 
            voice.lang.includes('mi') || 
            voice.name.toLowerCase().includes('maori') ||
            voice.name.toLowerCase().includes('māori')
        );
        
        if (maoriVoice) {
            utterance.voice = maoriVoice;
        }
        
        speechSynthesis.speak(utterance);
    } else {
    }
}

// Show message to user
function showMessage(text, type = 'info') {
    const messageDiv = document.getElementById('message');
    messageDiv.innerHTML = `<div class="message ${type}">${text}</div>`;
    
    if (type === 'error' || type === 'success') {
        setTimeout(() => {
            messageDiv.innerHTML = '';
        }, 3000);
    }
}

// Start game
function startGame() {
    gameState.gameActive = true;
    initSpellingBee();
}

// End game with enhanced tracking
function endGame() {
    gameState.gameActive = false;
    
    // Calculate enhanced stats
    const maoriWordsFound = gameState.foundWords.filter(word => 
        MAORI_WORDS.includes(word) || gameState.wordDefinitions.has(word)
    ).length;
    const pangramsFound = gameState.pangrams;
    
    // Track with gamification system
    if (window.gamificationSystem) {
        window.gamificationSystem.endGameSession({
            score: gameState.score,
            wordsFound: gameState.foundWords.length,
            maoriWordsFound: maoriWordsFound,
            pangramsFound: pangramsFound,
            timeSpent: Date.now() - gameState.startTime,
            achievements: calculateAchievements()
        });
    }
    
    // Track with adaptive difficulty
    if (window.adaptiveDifficulty) {
        window.adaptiveDifficulty.recordPerformance({
            gameType: 'spelling-bee',
            score: gameState.score,
            accuracy: gameState.foundWords.length / Math.max(1, gameState.foundWords.length + 3),
            wordsFound: gameState.foundWords.length,
            difficulty: 'medium'
        });
    }
}

// Calculate achievements
function calculateAchievements() {
    const achievements = [];
    
    if (gameState.foundWords.length >= 20) achievements.push('word-collector');
    if (gameState.score >= 100) achievements.push('high-scorer');
    if (gameState.pangrams >= 3) achievements.push('pangram-master');
    if (gameState.foundWords.filter(word => MAORI_WORDS.includes(word) || gameState.wordDefinitions.has(word)).length >= 10) {
        achievements.push('maori-expert');
    }
    
    return achievements;
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    // Add enhanced dependencies
    const script1 = document.createElement('script');
    script1.src = '/js/maori-dictionary-api.js';
    document.head.appendChild(script1);
    
    const script2 = document.createElement('script');
    script2.src = '/js/gamification-system.js';
    document.head.appendChild(script2);
    
    const script3 = document.createElement('script');
    script3.src = '/js/adaptive-difficulty-system.js';
    document.head.appendChild(script3);
    
    // Initialize game after dependencies load
    setTimeout(() => {
        initSpellingBee();
        gameState.startTime = Date.now();
    }, 1000);
});
