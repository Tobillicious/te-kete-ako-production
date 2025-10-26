/**
 * AGENTIC INTERACTIONS REVOLUTION
 * Advanced AI-Powered Interface System for Te Kete Ako
 * Implements cutting-edge conversational AI with cultural authenticity
 */

class AgenticInteractionSystem {
    constructor() {
        this.apiKey = this.getDeepSeekAPIKey();
        this.isInitialized = false;
        this.chatContainer = null;
        this.triggerButton = null;
        this.messageHistory = [];
        this.isTyping = false;
        this.culturalContext = this.loadCulturalContext();
        this.touchTargetSize = 44; // Professional mobile standard
        this.animationDuration = 300;
        this.culturalMotifs = ['🌺', '🍃', '⭐', '🌊'];
        
        this.init();
    }
    
    getDeepSeekAPIKey() {
        // Load from environment - NEVER hardcode API keys!
        // This requires serverless function to proxy the API call
        console.error('ERROR: API key should be loaded from serverless function, not client-side');
        return null; // Removed hardcoded key for security
    }
    
    loadCulturalContext() {
        return {
            greeting: "Kia ora! I'm your AI learning assistant, here to support your educational journey with culturally authentic resources.",
            principles: [
                "Respect for Te Ao Māori perspectives",
                "Inclusive support for neurodivergent learners",
                "Evidence-based educational approaches",
                "Community-centered learning design"
            ],
            specializations: [
                "New Zealand curriculum alignment",
                "Cultural authenticity validation",
                "Adaptive learning pathways",
                "Foundational literacy and numeracy"
            ]
        };
    }
    
    async init() {
        try {
            await this.createChatInterface();
            this.setupEventListeners();
            this.initializePerformanceMonitoring();
            this.enhanceButtonInteractions();
            this.implementGestureSupport();
            this.addCulturalAnimations();
            this.deploySmartFeedback();
            this.optimizeMobileExperience();
            this.isInitialized = true;
            console.log('🤖 Agentic Interaction System initialized successfully');
        } catch (error) {
            console.error('❌ Failed to initialize Agentic Interaction System:', error);
        }
    }
    
    async createChatInterface() {
        // Create the trigger button
        this.createTriggerButton();
        
        // Create the main chat container
        this.createChatContainer();
        
        // Initialize with welcome message
        this.addWelcomeMessage();
    }
    
    createTriggerButton() {
        this.triggerButton = document.createElement('button');
        this.triggerButton.className = 'agentic-trigger';
        this.triggerButton.innerHTML = '🤖';
        this.triggerButton.setAttribute('aria-label', 'Open AI Assistant Chat');
        this.triggerButton.setAttribute('title', 'Chat with your AI learning assistant');
        
        document.body.appendChild(this.triggerButton);
    }
    
    createChatContainer() {
        this.chatContainer = document.createElement('div');
        this.chatContainer.className = 'agentic-chat-container';
        this.chatContainer.innerHTML = this.getChatHTML();
        
        document.body.appendChild(this.chatContainer);
    }
    
    getChatHTML() {
        return `
            <div class="agentic-chat-header">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div class="ai-avatar">🧠</div>
                    <div class="ai-info">
                        <h3>Te Kete Ako AI</h3>
                        <div class="ai-status">Ready to assist • Culturally aware</div>
                    </div>
                </div>
                <button class="chat-minimize" aria-label="Minimize chat">✕</button>
            </div>
            <div class="agentic-chat-messages" id="chatMessages" role="log" aria-live="polite" aria-label="Chat messages"></div>
            <div class="agentic-chat-input">
                <textarea 
                    class="chat-input-field" 
                    placeholder="Ask about lessons, resources, or Te Ao Māori content..."
                    rows="1"
                    aria-label="Type your message"
                ></textarea>
                <button class="chat-send-btn" aria-label="Send message">
                    <span>📨</span>
                </button>
            </div>
        `;
    }
    
    setupEventListeners() {
        // Trigger button click
        this.triggerButton.addEventListener('click', () => this.toggleChat());
        
        // Minimize button
        const minimizeBtn = this.chatContainer.querySelector('.chat-minimize');
        minimizeBtn.addEventListener('click', () => this.closeChat());
        
        // Input field events
        const inputField = this.chatContainer.querySelector('.chat-input-field');
        const sendBtn = this.chatContainer.querySelector('.chat-send-btn');
        
        inputField.addEventListener('keydown', (e) => this.handleInputKeydown(e));
        inputField.addEventListener('input', () => this.handleInputChange());
        sendBtn.addEventListener('click', () => this.sendMessage());
        
        // Auto-resize textarea
        inputField.addEventListener('input', () => this.autoResizeTextarea(inputField));
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => this.handleGlobalKeydown(e));
        
        // Accessibility improvements
        this.setupAccessibilityFeatures();
    }
    
    setupAccessibilityFeatures() {
        // Focus management
        this.chatContainer.addEventListener('focusin', () => {
            this.chatContainer.setAttribute('data-focused', 'true');
        });
        
        this.chatContainer.addEventListener('focusout', () => {
            setTimeout(() => {
                if (!this.chatContainer.contains(document.activeElement)) {
                    this.chatContainer.removeAttribute('data-focused');
                }
            }, 100);
        });
        
        // Screen reader announcements
        this.announceToScreenReader = (message) => {
            const announcement = document.createElement('div');
            announcement.setAttribute('aria-live', 'assertive');
            announcement.setAttribute('aria-atomic', 'true');
            announcement.className = 'sr-only';
            announcement.textContent = message;
            announcement.style.cssText = `
                position: absolute;
                width: 1px;
                height: 1px;
                padding: 0;
                margin: -1px;
                overflow: hidden;
                clip: rect(0, 0, 0, 0);
                white-space: nowrap;
                border: 0;
            `;
            document.body.appendChild(announcement);
            
            setTimeout(() => {
                document.body.removeChild(announcement);
            }, 1000);
        };
    }
    
    toggleChat() {
        const isActive = this.chatContainer.classList.contains('active');
        
        if (isActive) {
            this.closeChat();
        } else {
            this.openChat();
        }
    }
    
    openChat() {
        this.chatContainer.classList.add('active');
        this.triggerButton.classList.add('hidden');
        
        // Focus on input field
        setTimeout(() => {
            const inputField = this.chatContainer.querySelector('.chat-input-field');
            inputField.focus();
        }, 400);
        
        // Analytics
        this.trackEvent('chat_opened');
        
        // Screen reader announcement
        this.announceToScreenReader('AI assistant chat opened');
    }
    
    closeChat() {
        this.chatContainer.classList.remove('active');
        this.triggerButton.classList.remove('hidden');
        
        // Analytics
        this.trackEvent('chat_closed');
        
        // Screen reader announcement
        this.announceToScreenReader('AI assistant chat closed');
    }
    
    handleInputKeydown(e) {
        const inputField = e.target;
        
        // Send message on Enter (but not Shift+Enter)
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            this.sendMessage();
        }
        
        // Close chat on Escape
        if (e.key === 'Escape') {
            this.closeChat();
        }
    }
    
    handleInputChange() {
        const inputField = this.chatContainer.querySelector('.chat-input-field');
        const sendBtn = this.chatContainer.querySelector('.chat-send-btn');
        
        // Enable/disable send button based on input
        const hasContent = inputField.value.trim().length > 0;
        sendBtn.disabled = !hasContent || this.isTyping;
        sendBtn.style.opacity = hasContent && !this.isTyping ? '1' : '0.5';
    }
    
    autoResizeTextarea(textarea) {
        textarea.style.height = 'auto';
        const maxHeight = 120;
        const newHeight = Math.min(textarea.scrollHeight, maxHeight);
        textarea.style.height = newHeight + 'px';
    }
    
    handleGlobalKeydown(e) {
        // Toggle chat with Ctrl+/ or Cmd+/
        if ((e.ctrlKey || e.metaKey) && e.key === '/') {
            e.preventDefault();
            this.toggleChat();
        }
    }
    
    async sendMessage() {
        const inputField = this.chatContainer.querySelector('.chat-input-field');
        const message = inputField.value.trim();
        
        if (!message || this.isTyping) return;
        
        // Clear input and reset height
        inputField.value = '';
        inputField.style.height = 'auto';
        this.handleInputChange();
        
        // Add user message to chat
        this.addMessage('user', message);
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            // Get AI response
            const response = await this.getAIResponse(message);
            
            // Hide typing indicator
            this.hideTypingIndicator();
            
            // Add AI response to chat
            this.addMessage('ai', response);
            
            // Analytics
            this.trackEvent('message_sent', { message_length: message.length });
            
        } catch (error) {
            console.error('Failed to get AI response:', error);
            
            // Hide typing indicator
            this.hideTypingIndicator();
            
            // Show error message
            this.addMessage('ai', 'Aroha mai, I encountered an issue. Please try again or contact support if the problem persists.', 'error');
            
            // Analytics
            this.trackEvent('ai_response_error', { error: error.message });
        }
    }
    
    addWelcomeMessage() {
        const welcomeMessage = `${this.culturalContext.greeting}

I can help you with:
• Finding educational resources
• Understanding Te Ao Māori content
• Adaptive learning support
• Curriculum alignment

How can I assist you today?`;
        
        setTimeout(() => {
            this.addMessage('ai', welcomeMessage, 'welcome');
        }, 1000);
    }
    
    addMessage(sender, content, type = 'normal') {
        const messagesContainer = document.getElementById('chatMessages');
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-message';
        
        const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const isAI = sender === 'ai';
        
        messageElement.innerHTML = `
            <div class="message-avatar ${sender}">
                ${isAI ? '🤖' : '👤'}
            </div>
            <div class="message-content ${sender}">
                <div class="message-text">${this.formatMessage(content)}</div>
                <div class="message-time">${timestamp}</div>
            </div>
        `;
        
        // Add cultural verification badge for AI messages about Te Ao Māori
        if (isAI && this.containsCulturalContent(content)) {
            messageElement.querySelector('.message-content').classList.add('cultural-verified');
        }
        
        messagesContainer.appendChild(messageElement);
        
        // Store in history
        this.messageHistory.push({
            sender,
            content,
            timestamp: Date.now(),
            type
        });
        
        // Scroll to bottom
        this.scrollToBottom();
        
        // Screen reader announcement for new AI messages
        if (isAI) {
            this.announceToScreenReader(`AI assistant says: ${content.substring(0, 100)}${content.length > 100 ? '...' : ''}`);
        }
    }
    
    formatMessage(content) {
        // Convert newlines to <br>
        content = content.replace(/\n/g, '<br>');
        
        // Format bullet points
        content = content.replace(/• /g, '<span style="color: var(--color-accent); font-weight: bold;">• </span>');
        
        // Format Te Reo Māori terms (basic detection)
        const maoriTerms = ['kia ora', 'te ao māori', 'whakatauki', 'aroha', 'mātauranga', 'whakapapa', 'tikanga', 'marae', 'whānau'];
        maoriTerms.forEach(term => {
            const regex = new RegExp(`\\b${term}\\b`, 'gi');
            content = content.replace(regex, `<span lang="mi" style="font-style: italic; color: var(--color-cultural); font-weight: 500;">${term}</span>`);
        });
        
        return content;
    }
    
    containsCulturalContent(content) {
        const culturalKeywords = [
            'māori', 'maori', 'te ao māori', 'te reo', 'whakatauki', 'tikanga', 
            'mātauranga', 'whakapapa', 'marae', 'whānau', 'indigenous', 'cultural'
        ];
        
        return culturalKeywords.some(keyword => 
            content.toLowerCase().includes(keyword.toLowerCase())
        );
    }
    
    showTypingIndicator() {
        this.isTyping = true;
        this.handleInputChange();
        
        const messagesContainer = document.getElementById('chatMessages');
        const typingElement = document.createElement('div');
        typingElement.className = 'typing-indicator';
        typingElement.id = 'typingIndicator';
        typingElement.innerHTML = `
            <div class="message-avatar ai">🤖</div>
            <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1rem; background: #f8f9fa; border-radius: 1rem;">
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
                <span style="font-size: 0.85rem; color: #666;">AI is thinking...</span>
            </div>
        `;
        
        messagesContainer.appendChild(typingElement);
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.isTyping = false;
        this.handleInputChange();
        
        const typingElement = document.getElementById('typingIndicator');
        if (typingElement) {
            typingElement.remove();
        }
    }
    
    async getAIResponse(userMessage) {
        const endpoint = '/.netlify/functions/deepseek-agent';
        
        // Prepare context-rich prompt
        const systemPrompt = this.buildSystemPrompt();
        const contextualMessage = this.buildContextualMessage(userMessage);
        
        const requestBody = {
            message: contextualMessage,
            system_prompt: systemPrompt,
            use_graphrag: true,
            cultural_validation: true,
            conversation_history: this.getRecentHistory()
        };
        
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody)
        });
        
        if (!response.ok) {
            throw new Error(`AI service error: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (!data.success) {
            throw new Error(data.error || 'Unknown AI service error');
        }
        
        return data.response || 'I apologize, but I couldn\\'t generate a proper response. Please try rephrasing your question.';
    }
    
    buildSystemPrompt() {
        return `You are the AI learning assistant for Te Kete Ako, New Zealand's premier cultural-educational platform. You embody the following characteristics:

🌿 CULTURAL AUTHENTICITY
- Deep respect for Te Ao Māori worldviews and practices
- Accurate representation of indigenous knowledge systems
- Culturally appropriate language and concepts

📚 EDUCATIONAL EXCELLENCE
- Aligned with New Zealand Curriculum standards
- Support for foundational literacy and numeracy
- Inclusive design for neurodivergent learners (ADHD, dyslexia, autism)
- Evidence-based pedagogical approaches

🤝 COMMUNITY-CENTERED APPROACH
- Emphasis on whānau and community engagement
- Collaborative and relationship-based learning
- Trauma-informed educational practices

💡 ADAPTIVE INTELLIGENCE
- Personalized responses based on individual learning needs
- Recognition of diverse learning styles and preferences
- Scaffolded support appropriate to developmental levels

When responding:
1. Always prioritize cultural authenticity and respect
2. Provide practical, actionable educational guidance
3. Include relevant Te Reo Māori terms with translations when appropriate
4. Consider accessibility and inclusive design principles
5. Reference the 467+ resources available on Te Kete Ako when relevant
6. Maintain a warm, encouraging, and supportive tone

Your responses should feel like guidance from a knowledgeable kaiako (teacher) who understands both traditional wisdom and modern educational research.`;
    }
    
    buildContextualMessage(userMessage) {
        // Analyze the message for intent and context
        const context = this.analyzeMessageContext(userMessage);
        
        let contextualPrefix = '';
        
        if (context.isAboutResources) {
            contextualPrefix = '[RESOURCE REQUEST] ';
        } else if (context.isAboutCulture) {
            contextualPrefix = '[CULTURAL INQUIRY] ';
        } else if (context.isAboutLearning) {
            contextualPrefix = '[LEARNING SUPPORT] ';
        }
        
        return contextualPrefix + userMessage;
    }
    
    analyzeMessageContext(message) {
        const lowerMessage = message.toLowerCase();
        
        return {
            isAboutResources: /\b(resource|handout|lesson|activity|worksheet|material)\b/.test(lowerMessage),
            isAboutCulture: /\b(māori|maori|cultural|te ao|te reo|tikanga|whakatauki)\b/.test(lowerMessage),
            isAboutLearning: /\b(learn|teach|study|understand|help|support|struggle|difficulty)\b/.test(lowerMessage),
            isAboutCurriculum: /\b(curriculum|standard|objective|assessment|year level)\b/.test(lowerMessage)
        };
    }
    
    getRecentHistory(limit = 5) {
        return this.messageHistory.slice(-limit).map(msg => ({
            role: msg.sender === 'ai' ? 'assistant' : 'user',
            content: msg.content
        }));
    }
    
    scrollToBottom() {
        const messagesContainer = document.getElementById('chatMessages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    // Enhanced Button Interactions
    enhanceButtonInteractions() {
        // Professional button enhancements
        document.querySelectorAll('button, .btn, .cta-button').forEach(btn => {
            if (!btn.classList.contains('agentic-enhanced')) {
                btn.classList.add('agentic-enhanced');
                
                // Add ripple effect
                btn.addEventListener('click', (e) => this.createRipple(e, btn));
                
                // Add hover elevation
                btn.addEventListener('mouseenter', () => this.elevateElement(btn));
                btn.addEventListener('mouseleave', () => this.resetElement(btn));
                
                // Ensure touch target size
                this.ensureTouchTarget(btn);
            }
        });
    }
    
    createRipple(event, element) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple-animation 0.6s ease-out;
            pointer-events: none;
            z-index: 1000;
        `;

        // Ensure parent is positioned
        if (getComputedStyle(element).position === 'static') {
            element.style.position = 'relative';
        }

        element.appendChild(ripple);

        // Add animation keyframes if not exists
        this.addRippleStyles();

        // Remove ripple after animation
        setTimeout(() => ripple.remove(), 600);
    }
    
    addRippleStyles() {
        if (!document.getElementById('agentic-ripple-styles')) {
            const style = document.createElement('style');
            style.id = 'agentic-ripple-styles';
            style.textContent = `
                @keyframes ripple-animation {
                    to {
                        transform: scale(4);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    elevateElement(element) {
        element.style.transform = 'translateY(-2px)';
        element.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)';
        element.style.transition = `all ${this.animationDuration}ms ease`;
    }
    
    resetElement(element) {
        element.style.transform = 'translateY(0)';
        element.style.boxShadow = '';
    }
    
    ensureTouchTarget(element) {
        const rect = element.getBoundingClientRect();
        if (rect.width < this.touchTargetSize || rect.height < this.touchTargetSize) {
            element.style.minWidth = `${this.touchTargetSize}px`;
            element.style.minHeight = `${this.touchTargetSize}px`;
            element.style.display = 'inline-flex';
            element.style.alignItems = 'center';
            element.style.justifyContent = 'center';
        }
    }
    
    // Gesture Support
    implementGestureSupport() {
        // Add swipe gesture for mobile navigation
        let startX, startY, startTime;
        
        document.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            startY = e.touches[0].clientY;
            startTime = Date.now();
        });

        document.addEventListener('touchend', (e) => {
            if (!startX || !startY) return;
            
            const endX = e.changedTouches[0].clientX;
            const endY = e.changedTouches[0].clientY;
            const endTime = Date.now();
            
            const deltaX = endX - startX;
            const deltaY = endY - startY;
            const deltaTime = endTime - startTime;
            
            // Quick swipe detection
            if (deltaTime < 300 && Math.abs(deltaX) > 50) {
                this.handleSwipeGesture(deltaX > 0 ? 'right' : 'left');
            }
        });
    }
    
    handleSwipeGesture(direction) {
        console.log(`🌊 Cultural swipe gesture detected: ${direction}`);
        // Add visual feedback
        this.showGestureFeedback(direction);
        
        // Trigger navigation or interactions
        if (direction === 'right') {
            this.triggerBackNavigation();
        } else if (direction === 'left') {
            this.triggerForwardNavigation();
        }
    }
    
    showGestureFeedback(direction) {
        const motif = this.culturalMotifs[Math.floor(Math.random() * this.culturalMotifs.length)];
        const feedback = document.createElement('div');
        feedback.className = 'gesture-feedback';
        feedback.innerHTML = motif;
        feedback.style.cssText = `
            position: fixed;
            top: 50%;
            ${direction === 'right' ? 'left: 20px' : 'right: 20px'};
            font-size: 2rem;
            z-index: 10000;
            animation: gesture-fade 1s ease-out;
            pointer-events: none;
        `;

        document.body.appendChild(feedback);

        // Add gesture animation styles
        this.addGestureStyles();

        setTimeout(() => feedback.remove(), 1000);
    }
    
    addGestureStyles() {
        if (!document.getElementById('agentic-gesture-styles')) {
            const style = document.createElement('style');
            style.id = 'agentic-gesture-styles';
            style.textContent = `
                @keyframes gesture-fade {
                    0% { transform: translateY(-50%) scale(0.8); opacity: 0; }
                    50% { transform: translateY(-50%) scale(1.2); opacity: 1; }
                    100% { transform: translateY(-50%) scale(1); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    // Cultural Animations
    addCulturalAnimations() {
        // Scroll-triggered cultural motif animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateElement(entry.target);
                }
            });
        }, { threshold: 0.3 });

        // Observe key elements
        document.querySelectorAll('.stat-item, .trust-item, .resource-card, h1, h2, h3').forEach(el => {
            if (!el.classList.contains('agentic-observed')) {
                el.classList.add('agentic-observed');
                observer.observe(el);
            }
        });
    }
    
    animateElement(element) {
        element.style.cssText += `
            animation: cultural-entrance 0.6s ease-out;
            animation-fill-mode: both;
        `;

        // Add cultural animation styles
        this.addCulturalStyles();
    }
    
    addCulturalStyles() {
        if (!document.getElementById('agentic-cultural-styles')) {
            const style = document.createElement('style');
            style.id = 'agentic-cultural-styles';
            style.textContent = `
                @keyframes cultural-entrance {
                    0% { 
                        opacity: 0; 
                        transform: translateY(30px) rotate(-2deg);
                    }
                    100% { 
                        opacity: 1; 
                        transform: translateY(0) rotate(0deg);
                    }
                }
                .agentic-enhanced {
                    overflow: hidden;
                    position: relative;
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    // Smart Feedback System
    deploySmartFeedback() {
        // Success/error feedback system
        window.agenticFeedback = (type, message) => {
            const feedback = document.createElement('div');
            feedback.className = `agentic-feedback ${type}`;
            feedback.innerHTML = `
                <span class="feedback-icon">${this.getFeedbackIcon(type)}</span>
                <span class="feedback-message">${message}</span>
            `;
            feedback.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 12px 16px;
                border-radius: 8px;
                color: white;
                font-weight: 500;
                z-index: 10000;
                animation: feedback-slide 0.3s ease-out;
                background: ${this.getFeedbackColor(type)};
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            `;

            document.body.appendChild(feedback);
            this.addFeedbackStyles();

            setTimeout(() => {
                feedback.style.animation = 'feedback-slide 0.3s ease-in reverse';
                setTimeout(() => feedback.remove(), 300);
            }, 3000);
        };
    }
    
    getFeedbackIcon(type) {
        const icons = {
            'success': '✅',
            'error': '❌',
            'info': 'ℹ️',
            'warning': '⚠️'
        };
        return icons[type] || icons.info;
    }

    getFeedbackColor(type) {
        const colors = {
            'success': 'linear-gradient(135deg, #2C5F41, #4CAF50)',
            'error': 'linear-gradient(135deg, #d32f2f, #f44336)',
            'info': 'linear-gradient(135deg, #00b0b9, #2196F3)',
            'warning': 'linear-gradient(135deg, #f57c00, #ff9800)'
        };
        return colors[type] || colors.info;
    }

    addFeedbackStyles() {
        if (!document.getElementById('agentic-feedback-styles')) {
            const style = document.createElement('style');
            style.id = 'agentic-feedback-styles';
            style.textContent = `
                @keyframes feedback-slide {
                    0% { transform: translateX(100%); opacity: 0; }
                    100% { transform: translateX(0); opacity: 1; }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    // Mobile Experience Optimization
    optimizeMobileExperience() {
        // Mobile-specific optimizations
        if (window.innerWidth <= 768) {
            // Increase touch targets
            document.querySelectorAll('a, button, input, select').forEach(el => {
                this.ensureTouchTarget(el);
            });

            // Add mobile-specific interactions
            this.addMobileScrollEffects();
        }
    }
    
    addMobileScrollEffects() {
        let ticking = false;
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    this.handleMobileScroll();
                    ticking = false;
                });
                ticking = true;
            }
        });
    }
    
    handleMobileScroll() {
        const scrolled = window.pageYOffset;
        const header = document.querySelector('header, .hero-section');
        
        if (header && scrolled > 100) {
            header.style.transform = `translateY(-${Math.min(scrolled * 0.1, 20)}px)`;
            header.style.opacity = Math.max(1 - scrolled * 0.001, 0.8);
        }
    }
    
    triggerBackNavigation() {
        if (window.history.length > 1) {
            window.history.back();
        }
    }

    triggerForwardNavigation() {
        // Implement forward navigation logic
        console.log('🚀 Forward navigation triggered');
    }
    
    // Performance Monitoring
    initializePerformanceMonitoring() {
        this.performanceMetrics = {
            responseStartTime: null,
            averageResponseTime: [],
            errorCount: 0,
            interactionCount: 0
        };
        
        // Monitor response times
        this.originalSendMessage = this.sendMessage;
        this.sendMessage = async (...args) => {
            this.performanceMetrics.responseStartTime = performance.now();
            this.performanceMetrics.interactionCount++;
            
            try {
                await this.originalSendMessage.apply(this, args);
                
                if (this.performanceMetrics.responseStartTime) {
                    const responseTime = performance.now() - this.performanceMetrics.responseStartTime;
                    this.performanceMetrics.averageResponseTime.push(responseTime);
                    
                    // Keep only last 10 response times
                    if (this.performanceMetrics.averageResponseTime.length > 10) {
                        this.performanceMetrics.averageResponseTime.shift();
                    }
                }
            } catch (error) {
                this.performanceMetrics.errorCount++;
                throw error;
            } finally {
                this.performanceMetrics.responseStartTime = null;
            }
        };
    }
    
    // Analytics and Tracking
    trackEvent(eventName, properties = {}) {
        const eventData = {
            event: eventName,
            timestamp: Date.now(),
            page: window.location.pathname,
            user_agent: navigator.userAgent,
            viewport: {
                width: window.innerWidth,
                height: window.innerHeight
            },
            ...properties
        };
        
        // In production, this would send to analytics service
        console.log('🔍 Analytics Event:', eventData);
        
        // Store locally for debugging
        const events = JSON.parse(localStorage.getItem('agentic_events') || '[]');
        events.push(eventData);
        
        // Keep only last 100 events
        if (events.length > 100) {
            events.splice(0, events.length - 100);
        }
        
        localStorage.setItem('agentic_events', JSON.stringify(events));
    }
    
    // Public API for external integrations
    getPerformanceMetrics() {
        const avgResponseTime = this.performanceMetrics.averageResponseTime.length > 0
            ? this.performanceMetrics.averageResponseTime.reduce((a, b) => a + b) / this.performanceMetrics.averageResponseTime.length
            : 0;
        
        return {
            ...this.performanceMetrics,
            averageResponseTime: Math.round(avgResponseTime),
            successRate: this.performanceMetrics.interactionCount > 0 
                ? ((this.performanceMetrics.interactionCount - this.performanceMetrics.errorCount) / this.performanceMetrics.interactionCount) * 100
                : 100
        };
    }
    
    // Export conversation history
    exportConversation() {
        const exportData = {
            timestamp: new Date().toISOString(),
            platform: 'Te Kete Ako',
            conversation: this.messageHistory,
            metrics: this.getPerformanceMetrics()
        };
        
        const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `te-kete-ako-conversation-${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
}

// Enhanced Search Integration
class AgenticSearchSystem {
    constructor(interactionSystem) {
        this.interactionSystem = interactionSystem;
        this.setupSearchEnhancements();
    }
    
    setupSearchEnhancements() {
        // Find existing search inputs and enhance them
        const searchInputs = document.querySelectorAll('input[type="search"], input[placeholder*="search"], .search-input');
        
        searchInputs.forEach(input => this.enhanceSearchInput(input));
        
        // Create smart search suggestions
        this.createSearchSuggestions();
    }
    
    enhanceSearchInput(input) {
        const container = input.parentElement;
        container.classList.add('agentic-search-container');
        input.classList.add('agentic-search-input');
        
        // Add AI search button
        const aiButton = document.createElement('button');
        aiButton.className = 'search-ai-button';
        aiButton.innerHTML = '🧠';
        aiButton.setAttribute('aria-label', 'AI-powered search');
        aiButton.title = 'Get AI-powered search suggestions';
        
        container.appendChild(aiButton);
        
        // AI search functionality
        aiButton.addEventListener('click', () => {
            const query = input.value.trim();
            if (query) {
                this.performAISearch(query);
            }
        });
        
        // Enhanced input behavior
        input.addEventListener('input', (e) => {
            this.handleSearchInput(e, input);
        });
    }
    
    async performAISearch(query) {
        try {
            // Use the interaction system to get AI-powered search results
            const aiQuery = `Please help me find resources related to: "${query}". Show me the most relevant educational materials and explain why they might be useful.`;
            
            // Open the AI chat if not already open
            if (!this.interactionSystem.chatContainer.classList.contains('active')) {
                this.interactionSystem.openChat();
            }
            
            // Add the search query to the chat
            const inputField = this.interactionSystem.chatContainer.querySelector('.chat-input-field');
            inputField.value = aiQuery;
            
            // Trigger the search
            await this.interactionSystem.sendMessage();
            
        } catch (error) {
            console.error('AI search failed:', error);
            this.showSearchError();
        }
    }
    
    handleSearchInput(event, input) {
        const query = input.value.trim();
        
        if (query.length > 2) {
            this.showSearchSuggestions(query, input);
        } else {
            this.hideSearchSuggestions();
        }
    }
    
    showSearchSuggestions(query, input) {
        // This would integrate with the GraphRAG system for intelligent suggestions
        const suggestions = this.generateSmartSuggestions(query);
        
        let suggestionsContainer = document.getElementById('ai-search-suggestions');
        if (!suggestionsContainer) {
            suggestionsContainer = this.createSuggestionsContainer(input);
        }
        
        this.renderSuggestions(suggestions, suggestionsContainer);
    }
    
    generateSmartSuggestions(query) {
        // This would be powered by the GraphRAG system in production
        const baseSuggestions = {
            'māori': [
                { title: 'Te Ao Māori Resources', description: 'Cultural learning materials and authentic content', icon: '🌿' },
                { title: 'Te Reo Māori Games', description: 'Interactive language learning activities', icon: '🎮' },
                { title: 'Cultural Assessment Tools', description: 'Culturally responsive evaluation methods', icon: '📊' }
            ],
            'literacy': [
                { title: 'Foundational Reading', description: 'Core literacy skills development', icon: '📖' },
                { title: 'Writing Toolkit', description: 'Comprehensive writing skill resources', icon: '✍️' },
                { title: 'Phonics Games', description: 'Interactive sound-based learning', icon: '🔊' }
            ],
            'numeracy': [
                { title: 'Math Fundamentals', description: 'Essential numeracy skill building', icon: '🔢' },
                { title: 'Problem Solving', description: 'Critical thinking math activities', icon: '🧮' },
                { title: 'Real-world Math', description: 'Practical mathematical applications', icon: '💰' }
            ]
        };
        
        const lowerQuery = query.toLowerCase();
        
        for (const [key, suggestions] of Object.entries(baseSuggestions)) {
            if (lowerQuery.includes(key)) {
                return suggestions;
            }
        }
        
        // Default suggestions
        return [
            { title: 'AI-Powered Search', description: `Find resources about "${query}" with AI assistance`, icon: '🤖' },
            { title: 'Browse All Resources', description: 'Explore our complete educational library', icon: '📚' },
            { title: 'Ask AI Assistant', description: 'Get personalized recommendations', icon: '💬' }
        ];
    }
    
    createSuggestionsContainer(input) {
        const container = document.createElement('div');
        container.id = 'ai-search-suggestions';
        container.className = 'agentic-suggestions';
        
        input.parentElement.appendChild(container);
        
        return container;
    }
    
    renderSuggestions(suggestions, container) {
        container.innerHTML = suggestions.map(suggestion => `
            <div class="suggestion-item" data-suggestion="${suggestion.title}">
                <div class="suggestion-icon">${suggestion.icon}</div>
                <div class="suggestion-text">
                    <div class="suggestion-title">${suggestion.title}</div>
                    <div class="suggestion-description">${suggestion.description}</div>
                </div>
            </div>
        `).join('');
        
        container.classList.add('visible');
        
        // Add click handlers
        container.querySelectorAll('.suggestion-item').forEach(item => {
            item.addEventListener('click', () => {
                const suggestion = item.dataset.suggestion;
                this.handleSuggestionClick(suggestion);
            });
        });
    }
    
    handleSuggestionClick(suggestion) {
        // Handle different types of suggestions
        if (suggestion.includes('AI')) {
            this.interactionSystem.openChat();
        } else {
            // Navigate to relevant page or perform search
            window.location.href = this.getSuggestionURL(suggestion);
        }
        
        this.hideSearchSuggestions();
    }
    
    getSuggestionURL(suggestion) {
        const urlMap = {
            'Te Ao Māori Resources': '/te-ao-maori.html',
            'Te Reo Māori Games': '/games.html',
            'Foundational Reading': '/foundational-literacy-platform.html',
            'Writing Toolkit': '/lessons/writers-toolkit/',
            'Math Fundamentals': '/maori-numeracy-adventures.html',
            'Browse All Resources': '/handouts.html'
        };
        
        return urlMap[suggestion] || '/search.html';
    }
    
    hideSearchSuggestions() {
        const container = document.getElementById('ai-search-suggestions');
        if (container) {
            container.classList.remove('visible');
        }
    }
    
    showSearchError() {
        // Show user-friendly error message
        const errorContainer = document.createElement('div');
        errorContainer.className = 'ai-response-card warning';
        errorContainer.innerHTML = `
            <strong>Search temporarily unavailable</strong>
            <p>Please try again in a moment, or browse our resources directly.</p>
        `;
        
        document.body.appendChild(errorContainer);
        
        setTimeout(() => {
            errorContainer.remove();
        }, 5000);
    }
}

// Initialize the system when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Check if we should initialize the agentic system
    const shouldInitialize = !document.body.classList.contains('no-agentic') && 
                            !document.querySelector('[data-disable-ai]');
    
    if (shouldInitialize) {
        try {
            const agenticSystem = new AgenticInteractionSystem();
            const agenticSearch = new AgenticSearchSystem(agenticSystem);
            
            // Make available globally for debugging and integration
            window.TeKeteAkoAI = {
                interaction: agenticSystem,
                search: agenticSearch,
                version: '2.0.0-revolutionary'
            };
            
            console.log('🚀 Te Kete Ako AI Systems initialized successfully');
            
        } catch (error) {
            console.error('❌ Failed to initialize Te Kete Ako AI Systems:', error);
        }
    } else {
        console.log('ℹ️ Agentic AI system disabled for this page');
    }
});

// Handle page visibility changes for better performance
document.addEventListener('visibilitychange', () => {
    if (window.TeKeteAkoAI && document.visibilityState === 'hidden') {
        // Pause any ongoing operations when page is not visible
        window.TeKeteAkoAI.interaction.trackEvent('page_hidden');
    } else if (window.TeKeteAkoAI && document.visibilityState === 'visible') {
        // Resume operations when page becomes visible
        window.TeKeteAkoAI.interaction.trackEvent('page_visible');
    }
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { AgenticInteractionSystem, AgenticSearchSystem };
}
if (typeof window !== 'undefined') {
    window.AgenticInteractionSystem = AgenticInteractionSystem;
    window.AgenticSearchSystem = AgenticSearchSystem;
}