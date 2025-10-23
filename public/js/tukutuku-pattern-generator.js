/**
 * Tukutuku Pattern Generator - Interactive Mathematics Learning Tool
 * Te Kete Ako - Cultural STEM Education
 * 
 * This tool allows students to explore geometric transformations through traditional Māori tukutuku patterns,
 * demonstrating how advanced mathematics is embedded in cultural art forms.
 */

class TukutukuPatternGenerator {
    constructor(canvasId, controlsId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.controls = document.getElementById(controlsId);

        // Set canvas size
        this.canvas.width = 800;
        this.canvas.height = 600;

        // Enhanced features
        this.learningProgress = {
            patternsExplored: new Set(),
            transformationsUsed: new Set(),
            animationsWatched: 0,
            patternsSaved: 0,
            interactions: 0
        };

        // Pattern settings
        this.settings = {
            basePattern: 'diamond',
            transformation: 'translation',
            colorScheme: 'traditional',
            gridSize: 40,
            animationSpeed: 1,
            showGrid: true,
            showAxes: true,
            culturalInfo: true
        };

        // Traditional Māori color schemes
        this.colorSchemes = {
            traditional: {
                primary: '#8B4513',    // Traditional brown
                secondary: '#CD853F',  // Sandy brown
                accent: '#F5DEB3',     // Wheat
                background: '#FFF8DC'  // Cornsilk
            },
            modern: {
                primary: '#2E7D32',
                secondary: '#4CAF50',
                accent: '#81C784',
                background: '#E8F5E8'
            },
            ocean: {
                primary: '#1565C0',
                secondary: '#42A5F5',
                accent: '#90CAF9',
                background: '#E3F2FD'
            }
        };

        // Pattern definitions with cultural significance
        this.patterns = {
            diamond: {
                name: 'Pātikitiki',
                meaning: 'Diamond pattern representing abundance and prosperity',
                maoriWords: ['pātikitiki', 'taonga', 'whairawa', 'hua'],
                coordinates: [
                    [0, -20], [20, 0], [0, 20], [-20, 0]
                ]
            },
            triangle: {
                name: 'Niho Taniwha',
                meaning: 'Taniwha teeth pattern representing strength and protection',
                maoriWords: ['taniwha', 'mana', 'kaha', 'taupua'],
                coordinates: [
                    [0, -20], [15, 15], [-15, 15]
                ]
            },
            cross: {
                name: 'Tawhiri',
                meaning: 'Four winds pattern representing the cardinal directions and balance',
                maoriWords: ['tawhiri', 'hau', 'rangi', 'whenua'],
                coordinates: [
                    [0, -20], [5, -5], [20, 0], [5, 5], [0, 20], [-5, 5], [-20, 0], [-5, -5]
                ]
            },
            chevron: {
                name: 'Roimata Toroa',
                meaning: 'Albatross tears representing peace and tranquility',
                maoriWords: ['roimata', 'toroa', 'rangimarie', 'ataahua'],
                coordinates: [
                    [-10, -15], [0, -25], [10, -15], [10, 15], [0, 25], [-10, 15]
                ]
            }
        };

        // Transformation descriptions
        this.transformations = {
            translation: {
                name: 'Nekehanga (Translation)',
                description: 'Moving the pattern in straight lines to create repeating designs',
                maoriConcept: 'Like stars moving across the sky in predictable paths'
            },
            rotation: {
                name: 'Tawhiri (Rotation)',
                description: 'Turning the pattern around a central point',
                maoriConcept: 'Like the four winds spinning around the earth'
            },
            reflection: {
                name: 'Whakaata (Reflection)',
                description: 'Flipping the pattern across a mirror line',
                maoriConcept: 'Like seeing your reflection in still water'
            },
            scaling: {
                name: 'Whakanui (Scaling)',
                description: 'Making the pattern larger or smaller',
                maoriConcept: 'Like watching the moon grow from crescent to full'
            }
        };

        this.animationId = null;
        this.animationStep = 0;

        this.init();
    }

    init() {
        this.createControls();
        this.bindEvents();
        this.draw();
        this.updateCulturalInfo();
        
        // Initialize gamification systems
        this.initializeGamification();
    }

    initializeGamification() {
        // Initialize gamification system if available
        if (window.gamificationSystem) {
            window.gamificationSystem.startGameSession('tukutuku-explorer', {
                difficulty: 'medium',
                learningObjectives: ['geometry', 'transformations', 'cultural-mathematics', 'pattern-recognition']
            });
        }
        
        // Initialize adaptive difficulty if available
        if (window.adaptiveDifficulty) {
            window.adaptiveDifficulty.startSession('tukutuku-explorer');
        }
        
        this.startTime = Date.now();
    }

    createControls() {
        this.controls.innerHTML = `
            <div class="pattern-controls">
                <div class="control-section">
                    <h3>🎨 Pattern Selection</h3>
                    <label for="basePattern">Choose Base Pattern:</label>
                    <select id="basePattern">
                        ${Object.keys(this.patterns).map(key =>
            `<option value="${key}">${this.patterns[key].name}</option>`
        ).join('')}
                    </select>
                </div>
                
                <div class="control-section">
                    <h3>🔄 Transformation</h3>
                    <label for="transformation">Mathematical Transformation:</label>
                    <select id="transformation">
                        ${Object.keys(this.transformations).map(key =>
            `<option value="${key}">${this.transformations[key].name}</option>`
        ).join('')}
                    </select>
                </div>
                
                <div class="control-section">
                    <h3>🎨 Visual Settings</h3>
                    <label for="colorScheme">Color Scheme:</label>
                    <select id="colorScheme">
                        <option value="traditional">Traditional Māori</option>
                        <option value="modern">Modern Green</option>
                        <option value="ocean">Ocean Blue</option>
                    </select>
                    
                    <label for="gridSize">Pattern Size:</label>
                    <input type="range" id="gridSize" min="20" max="80" value="40">
                    <span id="gridSizeValue">40</span>
                    
                    <label for="animationSpeed">Animation Speed:</label>
                    <input type="range" id="animationSpeed" min="0.1" max="3" step="0.1" value="1">
                    <span id="animationSpeedValue">1</span>
                </div>
                
                <div class="control-section">
                    <h3>📏 Display Options</h3>
                    <label>
                        <input type="checkbox" id="showGrid" checked> Show Grid Lines
                    </label>
                    <label>
                        <input type="checkbox" id="showAxes" checked> Show Coordinate Axes
                    </label>
                    <label>
                        <input type="checkbox" id="culturalInfo" checked> Show Cultural Information
                    </label>
                </div>
                
                <div class="control-section">
                    <h3>🎮 Actions</h3>
                    <button id="animate">▶️ Animate Transformation</button>
                    <button id="stopAnimation">⏹️ Stop Animation</button>
                    <button id="resetView">🔄 Reset View</button>
                    <button id="savePattern">💾 Save Pattern</button>
                </div>
            </div>
            
            <div class="cultural-info" id="culturalInfo">
                <h3>🌿 Cultural Knowledge</h3>
                <div id="patternMeaning"></div>
                <div id="transformationMeaning"></div>
                <div id="mathematicalConnection"></div>
            </div>
        `;
    }

    bindEvents() {
        // Pattern and transformation selection
        document.getElementById('basePattern').addEventListener('change', (e) => {
            this.settings.basePattern = e.target.value;
            this.learningProgress.patternsExplored.add(e.target.value);
            this.learningProgress.interactions++;
            this.draw();
            this.updateCulturalInfo();
            this.updateProgressDisplay();
        });

        document.getElementById('transformation').addEventListener('change', (e) => {
            this.settings.transformation = e.target.value;
            this.learningProgress.transformationsUsed.add(e.target.value);
            this.learningProgress.interactions++;
            this.draw();
            this.updateCulturalInfo();
            this.updateProgressDisplay();
        });

        // Visual settings
        document.getElementById('colorScheme').addEventListener('change', (e) => {
            this.settings.colorScheme = e.target.value;
            this.draw();
        });

        document.getElementById('gridSize').addEventListener('input', (e) => {
            this.settings.gridSize = parseInt(e.target.value);
            document.getElementById('gridSizeValue').textContent = e.target.value;
            this.draw();
        });

        document.getElementById('animationSpeed').addEventListener('input', (e) => {
            this.settings.animationSpeed = parseFloat(e.target.value);
            document.getElementById('animationSpeedValue').textContent = e.target.value;
        });

        // Display options
        document.getElementById('showGrid').addEventListener('change', (e) => {
            this.settings.showGrid = e.target.checked;
            this.draw();
        });

        document.getElementById('showAxes').addEventListener('change', (e) => {
            this.settings.showAxes = e.target.checked;
            this.draw();
        });

        document.getElementById('culturalInfo').addEventListener('change', (e) => {
            this.settings.culturalInfo = e.target.checked;
            document.getElementById('culturalInfo').style.display = e.target.checked ? 'block' : 'none';
        });

        // Action buttons
        document.getElementById('animate').addEventListener('click', () => this.startAnimation());
        document.getElementById('stopAnimation').addEventListener('click', () => this.stopAnimation());
        document.getElementById('resetView').addEventListener('click', () => this.resetView());
        document.getElementById('savePattern').addEventListener('click', () => this.savePattern());

        // Canvas interaction
        this.canvas.addEventListener('click', (e) => this.handleCanvasClick(e));
    }

    draw() {
        // Clear canvas
        this.ctx.fillStyle = this.colorSchemes[this.settings.colorScheme].background;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw grid if enabled
        if (this.settings.showGrid) {
            this.drawGrid();
        }

        // Draw axes if enabled
        if (this.settings.showAxes) {
            this.drawAxes();
        }

        // Draw the pattern with transformations
        this.drawPattern();

        // Draw transformation indicators
        this.drawTransformationIndicators();
    }

    drawGrid() {
        const colors = this.colorSchemes[this.settings.colorScheme];
        this.ctx.strokeStyle = colors.accent;
        this.ctx.lineWidth = 0.5;
        this.ctx.globalAlpha = 0.3;

        const gridSpacing = this.settings.gridSize / 2;

        // Vertical lines
        for (let x = 0; x <= this.canvas.width; x += gridSpacing) {
            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.canvas.height);
            this.ctx.stroke();
        }

        // Horizontal lines
        for (let y = 0; y <= this.canvas.height; y += gridSpacing) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
    }

    drawAxes() {
        const colors = this.colorSchemes[this.settings.colorScheme];
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        this.ctx.strokeStyle = colors.primary;
        this.ctx.lineWidth = 2;
        this.ctx.globalAlpha = 0.7;

        // X-axis
        this.ctx.beginPath();
        this.ctx.moveTo(0, centerY);
        this.ctx.lineTo(this.canvas.width, centerY);
        this.ctx.stroke();

        // Y-axis
        this.ctx.beginPath();
        this.ctx.moveTo(centerX, 0);
        this.ctx.lineTo(centerX, this.canvas.height);
        this.ctx.stroke();

        // Add axis labels
        this.ctx.fillStyle = colors.primary;
        this.ctx.font = '14px Arial';
        this.ctx.fillText('X', this.canvas.width - 20, centerY - 10);
        this.ctx.fillText('Y', centerX + 10, 20);

        this.ctx.globalAlpha = 1;
    }

    drawPattern() {
        const pattern = this.patterns[this.settings.basePattern];
        const colors = this.colorSchemes[this.settings.colorScheme];
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        // Calculate how many patterns to draw based on transformation
        const repetitions = this.getRepetitions();

        for (let i = 0; i < repetitions.length; i++) {
            const rep = repetitions[i];

            this.ctx.save();

            // Apply transformation
            this.ctx.translate(centerX + rep.translateX, centerY + rep.translateY);
            this.ctx.rotate(rep.rotation);
            this.ctx.scale(rep.scaleX, rep.scaleY);

            // Draw the pattern
            this.ctx.fillStyle = i === 0 ? colors.primary : colors.secondary;
            this.ctx.strokeStyle = colors.primary;
            this.ctx.lineWidth = 2;

            this.ctx.beginPath();
            const coords = pattern.coordinates;
            this.ctx.moveTo(coords[0][0], coords[0][1]);

            for (let j = 1; j < coords.length; j++) {
                this.ctx.lineTo(coords[j][0], coords[j][1]);
            }

            this.ctx.closePath();
            this.ctx.fill();
            this.ctx.stroke();

            this.ctx.restore();
        }
    }

    getRepetitions() {
        const transformation = this.settings.transformation;
        const gridSize = this.settings.gridSize;
        const step = this.animationStep;

        switch (transformation) {
            case 'translation':
                return this.getTranslationRepetitions(gridSize, step);
            case 'rotation':
                return this.getRotationRepetitions(step);
            case 'reflection':
                return this.getReflectionRepetitions();
            case 'scaling':
                return this.getScalingRepetitions(step);
            default:
                return [{ translateX: 0, translateY: 0, rotation: 0, scaleX: 1, scaleY: 1 }];
        }
    }

    getTranslationRepetitions(gridSize, animationStep) {
        const repetitions = [];
        const maxReps = 8;

        for (let i = -maxReps / 2; i <= maxReps / 2; i++) {
            for (let j = -maxReps / 2; j <= maxReps / 2; j++) {
                if (Math.abs(i) + Math.abs(j) <= maxReps / 2) {
                    repetitions.push({
                        translateX: i * gridSize,
                        translateY: j * gridSize,
                        rotation: 0,
                        scaleX: 1,
                        scaleY: 1
                    });
                }
            }
        }

        return repetitions;
    }

    getRotationRepetitions(animationStep) {
        const repetitions = [];
        const angles = [0, Math.PI / 2, Math.PI, 3 * Math.PI / 2];

        for (let angle of angles) {
            repetitions.push({
                translateX: 0,
                translateY: 0,
                rotation: angle + (animationStep * 0.02),
                scaleX: 1,
                scaleY: 1
            });
        }

        return repetitions;
    }

    getReflectionRepetitions() {
        return [
            { translateX: 0, translateY: 0, rotation: 0, scaleX: 1, scaleY: 1 },
            { translateX: 0, translateY: 0, rotation: 0, scaleX: -1, scaleY: 1 },
            { translateX: 0, translateY: 0, rotation: 0, scaleX: 1, scaleY: -1 },
            { translateX: 0, translateY: 0, rotation: 0, scaleX: -1, scaleY: -1 }
        ];
    }

    getScalingRepetitions(animationStep) {
        const scale = 0.5 + Math.sin(animationStep * 0.05) * 0.3;
        return [
            { translateX: -50, translateY: -50, rotation: 0, scaleX: scale, scaleY: scale },
            { translateX: 0, translateY: 0, rotation: 0, scaleX: 1, scaleY: 1 },
            { translateX: 50, translateY: 50, rotation: 0, scaleX: 1.5, scaleY: 1.5 }
        ];
    }

    drawTransformationIndicators() {
        if (!this.animationId) return;

        const colors = this.colorSchemes[this.settings.colorScheme];
        const transformation = this.settings.transformation;

        // Draw transformation-specific indicators
        this.ctx.strokeStyle = colors.accent;
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);

        if (transformation === 'rotation') {
            // Draw rotation center
            const centerX = this.canvas.width / 2;
            const centerY = this.canvas.height / 2;

            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 5, 0, 2 * Math.PI);
            this.ctx.stroke();

            // Draw rotation arc
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 60, 0, (this.animationStep * 0.02) % (2 * Math.PI));
            this.ctx.stroke();
        }

        this.ctx.setLineDash([]);
    }

    updateCulturalInfo() {
        const pattern = this.patterns[this.settings.basePattern];
        const transformation = this.transformations[this.settings.transformation];

        document.getElementById('patternMeaning').innerHTML = `
            <h4>Pattern: ${pattern.name}</h4>
            <p>${pattern.meaning}</p>
        `;

        document.getElementById('transformationMeaning').innerHTML = `
            <h4>Transformation: ${transformation.name}</h4>
            <p>${transformation.description}</p>
            <p><em>Traditional Connection:</em> ${transformation.maoriConcept}</p>
        `;

        document.getElementById('mathematicalConnection').innerHTML = `
            <h4>📐 Mathematical Learning</h4>
            <p>This pattern demonstrates how traditional Māori artisans intuitively understood and applied complex geometric principles:</p>
            <ul>
                <li><strong>Symmetry:</strong> Both patterns show mathematical precision in their balance and proportion</li>
                <li><strong>Repetition:</strong> Understanding of tessellations and how patterns tile across space</li>
                <li><strong>Transformation:</strong> Practical application of geometric transformations for aesthetic and symbolic purposes</li>
                <li><strong>Coordinate Systems:</strong> Implicit understanding of spatial relationships and positioning</li>
            </ul>
            <h4>🌿 Related Māori Words</h4>
            <div class="maori-words-display">
                ${this.displayPatternWords(pattern)}
            </div>
        `;
    }

    startAnimation() {
        if (this.animationId) return;

        this.learningProgress.animationsWatched++;
        this.learningProgress.interactions++;
        this.updateProgressDisplay();

        const animate = () => {
            this.animationStep += this.settings.animationSpeed;
            this.draw();
            this.animationId = requestAnimationFrame(animate);
        };

        animate();
    }

    stopAnimation() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }

    resetView() {
        this.stopAnimation();
        this.animationStep = 0;
        this.settings.gridSize = 40;
        this.settings.animationSpeed = 1;

        // Reset UI controls
        document.getElementById('gridSize').value = 40;
        document.getElementById('gridSizeValue').textContent = '40';
        document.getElementById('animationSpeed').value = 1;
        document.getElementById('animationSpeedValue').textContent = '1';

        this.draw();
    }

    savePattern() {
        // Create download link for the canvas
        const link = document.createElement('a');
        link.download = `tukutuku-${this.settings.basePattern}-${this.settings.transformation}.png`;
        link.href = this.canvas.toDataURL();
        link.click();

        // Track progress
        this.learningProgress.patternsSaved++;
        this.learningProgress.interactions++;
        this.updateProgressDisplay();

        // Also save pattern details as JSON
        const patternData = {
            pattern: this.settings.basePattern,
            transformation: this.settings.transformation,
            colorScheme: this.settings.colorScheme,
            gridSize: this.settings.gridSize,
            culturalInfo: {
                patternName: this.patterns[this.settings.basePattern].name,
                patternMeaning: this.patterns[this.settings.basePattern].meaning,
                transformationName: this.transformations[this.settings.transformation].name,
                transformationDescription: this.transformations[this.settings.transformation].description
            },
            learningProgress: {
                patternsExplored: Array.from(this.learningProgress.patternsExplored),
                transformationsUsed: Array.from(this.learningProgress.transformationsUsed),
                animationsWatched: this.learningProgress.animationsWatched,
                patternsSaved: this.learningProgress.patternsSaved,
                interactions: this.learningProgress.interactions
            },
            timestamp: new Date().toISOString()
        };

        // Save JSON data
        const jsonLink = document.createElement('a');
        jsonLink.download = `tukutuku-data-${Date.now()}.json`;
        jsonLink.href = 'data:application/json,' + encodeURIComponent(JSON.stringify(patternData, null, 2));
        jsonLink.click();

        // Track with gamification
        if (window.gamificationSystem) {
            window.gamificationSystem.recordAchievement('pattern-creator', {
                patternType: this.settings.basePattern,
                transformation: this.settings.transformation,
                culturalSignificance: this.patterns[this.settings.basePattern].meaning
            });
        }

        // Show success message
        this.showMessage('Pattern saved! You can use this in your mathematics portfolio.', 'success');
    }

    handleCanvasClick(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        // Convert to mathematical coordinates
        const mathX = x - this.canvas.width / 2;
        const mathY = this.canvas.height / 2 - y;

        this.showMessage(`Clicked at coordinates: (${Math.round(mathX)}, ${Math.round(mathY)})`, 'info');
    }

    showMessage(message, type = 'info') {
        // Create or update message display
        let messageDiv = document.getElementById('messageDisplay');
        if (!messageDiv) {
            messageDiv = document.createElement('div');
            messageDiv.id = 'messageDisplay';
            messageDiv.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 1rem;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                z-index: 1000;
                max-width: 300px;
            `;
            document.body.appendChild(messageDiv);
        }

        // Set background color based on type
        const colors = {
            success: '#4CAF50',
            error: '#F44336',
            info: '#2196F3',
            warning: '#FF9800'
        };

        messageDiv.style.backgroundColor = colors[type] || colors.info;
        messageDiv.textContent = message;
        messageDiv.style.display = 'block';

        // Auto-hide after 3 seconds
        setTimeout(() => {
            messageDiv.style.display = 'none';
        }, 3000);
    }

    updateProgressDisplay() {
        const progressDiv = document.querySelector('.progress-indicator');
        if (progressDiv) {
            const completionPercentage = Math.round(
                ((this.learningProgress.patternsExplored.size / 4) * 25) +
                ((this.learningProgress.transformationsUsed.size / 4) * 25) +
                (Math.min(this.learningProgress.animationsWatched / 5, 1) * 25) +
                (Math.min(this.learningProgress.patternsSaved / 3, 1) * 25)
            );

            progressDiv.innerHTML = `
                <h4>🏆 Learning Progress: ${completionPercentage}%</h4>
                <div style="background: #ddd; border-radius: 10px; height: 20px; margin: 0.5rem 0;">
                    <div style="background: var(--color-accent); height: 100%; width: ${completionPercentage}%; border-radius: 10px; transition: width 0.3s ease;"></div>
                </div>
                <p>Patterns explored: ${this.learningProgress.patternsExplored.size}/4 | Transformations used: ${this.learningProgress.transformationsUsed.size}/4 | Animations watched: ${this.learningProgress.animationsWatched} | Patterns saved: ${this.learningProgress.patternsSaved}</p>
                <p><strong>💡 Tip:</strong> Click on the canvas to see coordinates! Try different combinations of patterns and transformations to discover mathematical relationships.</p>
            `;
        }

        // Track with adaptive difficulty
        if (window.adaptiveDifficulty) {
            window.adaptiveDifficulty.recordProgress({
                gameType: 'tukutuku-explorer',
                patternsExplored: this.learningProgress.patternsExplored.size,
                transformationsUsed: this.learningProgress.transformationsUsed.size,
                animationsWatched: this.learningProgress.animationsWatched,
                patternsSaved: this.learningProgress.patternsSaved,
                interactions: this.learningProgress.interactions,
                timeSpent: Date.now() - this.startTime
            });
        }
    }

    endSession() {
        // Track final session data with gamification
        if (window.gamificationSystem) {
            window.gamificationSystem.endGameSession({
                patternsExplored: this.learningProgress.patternsExplored.size,
                transformationsUsed: this.learningProgress.transformationsUsed.size,
                animationsWatched: this.learningProgress.animationsWatched,
                patternsSaved: this.learningProgress.patternsSaved,
                interactions: this.learningProgress.interactions,
                timeSpent: Date.now() - this.startTime,
                achievements: this.calculateAchievements()
            });
        }

        // Track with adaptive difficulty
        if (window.adaptiveDifficulty) {
            window.adaptiveDifficulty.recordPerformance({
                gameType: 'tukutuku-explorer',
                completionRate: (this.learningProgress.patternsExplored.size + this.learningProgress.transformationsUsed.size) / 8,
                engagementLevel: this.learningProgress.interactions,
                creativityScore: this.learningProgress.patternsSaved,
                difficulty: 'medium'
            });
        }
    }

    calculateAchievements() {
        const achievements = [];
        
        if (this.learningProgress.patternsExplored.size >= 4) achievements.push('pattern-explorer');
        if (this.learningProgress.transformationsUsed.size >= 4) achievements.push('transformation-master');
        if (this.learningProgress.animationsWatched >= 5) achievements.push('visual-learner');
        if (this.learningProgress.patternsSaved >= 3) achievements.push('creative-mathematician');
        if (this.learningProgress.interactions >= 20) achievements.push('engaged-explorer');
        
        return achievements;
    }

    // Display Māori words related to the current pattern
    displayPatternWords(pattern) {
        if (!pattern.maoriWords) return '<p>No related words available.</p>';
        
        const words = pattern.maoriWords.map(word => {
            return `
                <span class="maori-word-item" style="
                    display: inline-block;
                    background: var(--color-secondary);
                    color: white;
                    padding: 0.3rem 0.8rem;
                    margin: 0.2rem;
                    border-radius: 15px;
                    font-size: 0.9rem;
                    cursor: pointer;
                    transition: transform 0.2s ease;
                " 
                onclick="patternGenerator.showWordDefinition('${word}')"
                onmouseover="this.style.transform='scale(1.05)'"
                onmouseout="this.style.transform='scale(1)'"
                title="Click to hear pronunciation and see definition">
                    ${word}
                </span>
            `;
        }).join('');
        
        return `<div style="margin-top: 1rem;">${words}</div>`;
    }

    // Show word definition and pronunciation
    async showWordDefinition(word) {
        if (window.maoriDictionaryAPI) {
            try {
                const definition = await window.maoriDictionaryAPI.getWordDefinition(word.toUpperCase());
                if (definition) {
                    this.showDefinitionPopup(word, definition);
                } else {
                    this.showMessage(`Word "${word}" found in pattern context, but no detailed definition available.`, 'info');
                }
            } catch (error) {
                this.showMessage(`Word "${word}" is related to this pattern. Try the Māori Dictionary API for more details.`, 'info');
            }
        } else {
            this.showMessage(`"${word}" - a Māori word related to this traditional pattern.`, 'info');
        }
    }

    // Enhanced definition popup for pattern words
    showDefinitionPopup(word, definition) {
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
                    <button onclick="patternGenerator.speakMaoriWord('${word}', '${definition.pronunciation || ''}')"
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
                        <strong>🌟 Pattern Connection:</strong> This word is culturally connected to the ${this.patterns[this.settings.basePattern].name} pattern, showing how language and art are intertwined in Māori culture.
                    </p>
                </div>
            </div>
            <button onclick="patternGenerator.closeDefinitionPopup()" 
                    style="background: var(--color-primary); color: white; border: none; border-radius: 6px; padding: 0.8rem 1.5rem; cursor: pointer; font-size: 1rem;">
                Ka rawe! (Awesome!)
            </button>
        `;
        
        document.body.appendChild(popup);
        
        // Close on background click
        popup.addEventListener('click', (e) => {
            if (e.target === popup) {
                this.closeDefinitionPopup();
            }
        });
    }

    // Close definition popup
    closeDefinitionPopup() {
        const popup = document.querySelector('.definition-popup');
        if (popup) {
            popup.remove();
        }
    }

    // Māori pronunciation using Web Speech API
    speakMaoriWord(word, pronunciation) {
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
}

// Utility functions for mathematical analysis
class PatternAnalyzer {
    static analyzeSymmetry(pattern) {
        // Analyze the symmetries present in a pattern
        const coords = pattern.coordinates;

        return {
            hasVerticalSymmetry: this.checkVerticalSymmetry(coords),
            hasHorizontalSymmetry: this.checkHorizontalSymmetry(coords),
            hasRotationalSymmetry: this.checkRotationalSymmetry(coords),
            symmetryOrder: this.getSymmetryOrder(coords)
        };
    }

    static checkVerticalSymmetry(coords) {
        return coords.every(([x, y]) =>
            coords.some(([x2, y2]) => x2 === -x && y2 === y)
        );
    }

    static checkHorizontalSymmetry(coords) {
        return coords.every(([x, y]) =>
            coords.some(([x2, y2]) => x2 === x && y2 === -y)
        );
    }

    static checkRotationalSymmetry(coords) {
        // Check for 180-degree rotational symmetry
        return coords.every(([x, y]) =>
            coords.some(([x2, y2]) => x2 === -x && y2 === -y)
        );
    }

    static getSymmetryOrder(coords) {
        // Determine the order of rotational symmetry
        for (let n = 2; n <= 8; n++) {
            const angle = (2 * Math.PI) / n;
            if (this.hasRotationalSymmetryOfOrder(coords, angle)) {
                return n;
            }
        }
        return 1;
    }

    static hasRotationalSymmetryOfOrder(coords, angle) {
        const tolerance = 1;

        return coords.every(([x, y]) => {
            const rotatedX = x * Math.cos(angle) - y * Math.sin(angle);
            const rotatedY = x * Math.sin(angle) + y * Math.cos(angle);

            return coords.some(([x2, y2]) =>
                Math.abs(x2 - rotatedX) < tolerance &&
                Math.abs(y2 - rotatedY) < tolerance
            );
        });
    }

    static calculatePerimeter(coords) {
        let perimeter = 0;
        for (let i = 0; i < coords.length; i++) {
            const [x1, y1] = coords[i];
            const [x2, y2] = coords[(i + 1) % coords.length];
            perimeter += Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
        }
        return perimeter;
    }

    static calculateArea(coords) {
        // Using shoelace formula for polygon area
        let area = 0;
        for (let i = 0; i < coords.length; i++) {
            const [x1, y1] = coords[i];
            const [x2, y2] = coords[(i + 1) % coords.length];
            area += x1 * y2 - x2 * y1;
        }
        return Math.abs(area) / 2;
    }
}

// Export for use in HTML pages
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { TukutukuPatternGenerator, PatternAnalyzer };
}