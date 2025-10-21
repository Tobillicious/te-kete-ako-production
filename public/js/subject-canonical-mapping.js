/**
 * CANONICAL SUBJECT MAPPING - Te Kete Ako
 * Updated: 2025-10-21
 * 
 * Maps all subject variations to 11 canonical values
 * synchronized with GraphRAG database normalization
 */

const CANONICAL_SUBJECTS = {
    'Mathematics': {
        canonical: 'Mathematics',
        aliases: ['maths', 'math', 'mathematics'],
        icon: '🔢',
        color: '#3b82f6',
        slug: 'mathematics'
    },
    'English': {
        canonical: 'English',
        aliases: ['english', 'literacy', 'reading', 'writing'],
        icon: '📚',
        color: '#8b5cf6',
        slug: 'english'
    },
    'Science': {
        canonical: 'Science',
        aliases: ['science', 'biology', 'chemistry', 'physics', 'ecology'],
        icon: '🔬',
        color: '#10b981',
        slug: 'science'
    },
    'Social Studies': {
        canonical: 'Social Studies',
        aliases: ['social studies', 'history', 'geography'],
        icon: '🌍',
        color: '#f59e0b',
        slug: 'social-studies'
    },
    'Te Ao Māori': {
        canonical: 'Te Ao Māori',
        aliases: ['te ao māori', 'te reo māori', 'māori culture'],
        icon: '🌿',
        color: '#059669',
        slug: 'te-ao-maori'
    },
    'Digital Technologies': {
        canonical: 'Digital Technologies',
        aliases: ['digital technologies', 'technology', 'coding'],
        icon: '💻',
        color: '#6366f1',
        slug: 'digital-technologies'
    },
    'Health & PE': {
        canonical: 'Health & PE',
        aliases: ['health & pe', 'health', 'physical education'],
        icon: '🏃',
        color: '#ec4899',
        slug: 'health-pe'
    },
    'The Arts': {
        canonical: 'The Arts',
        aliases: ['arts', 'the arts', 'visual arts', 'music', 'drama'],
        icon: '🎨',
        color: '#a855f7',
        slug: 'the-arts'
    },
    'Cross-Curricular': {
        canonical: 'Cross-Curricular',
        aliases: ['cross-curricular'],
        icon: '🔗',
        color: '#14b8a6',
        slug: 'cross-curricular'
    },
    'Platform Infrastructure': {
        canonical: 'Platform Infrastructure',
        aliases: ['platform infrastructure'],
        icon: '⚙️',
        color: '#64748b',
        slug: 'platform-infrastructure'
    },
    'Languages': {
        canonical: 'Languages',
        aliases: ['languages'],
        icon: '🗣️',
        color: '#f97316',
        slug: 'languages'
    }
};

/**
 * Get canonical subject from any variation
 * @param {string} subject - Subject string (any variation)
 * @returns {string|null} - Canonical subject name or null
 */
function getCanonicalSubject(subject) {
    if (!subject) return null;
    const normalized = subject.toLowerCase().trim();
    
    for (const [canonical, config] of Object.entries(CANONICAL_SUBJECTS)) {
        if (config.aliases.includes(normalized)) {
            return canonical;
        }
    }
    
    return subject; // Return original if no mapping found
}

/**
 * Get subject metadata
 * @param {string} subject - Subject string (canonical or alias)
 * @returns {object} - Subject config with icon, color, slug
 */
function getSubjectMeta(subject) {
    const canonical = getCanonicalSubject(subject);
    return CANONICAL_SUBJECTS[canonical] || {
        canonical: subject,
        icon: '📄',
        color: '#64748b',
        slug: subject?.toLowerCase().replace(/[^a-z0-9]+/g, '-')
    };
}

/**
 * Get all canonical subjects (for filters/dropdowns)
 * @returns {array} - Array of canonical subject names
 */
function getAllCanonicalSubjects() {
    return Object.keys(CANONICAL_SUBJECTS);
}

/**
 * Generate subject badge HTML
 * @param {string} subject - Subject string
 * @returns {string} - HTML for subject badge
 */
function generateSubjectBadge(subject) {
    const meta = getSubjectMeta(subject);
    return `
        <span class="subject-badge" style="background: ${meta.color}; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem; font-weight: 600;">
            ${meta.icon} ${meta.canonical}
        </span>
    `;
}

// Export for ES modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        CANONICAL_SUBJECTS,
        getCanonicalSubject,
        getSubjectMeta,
        getAllCanonicalSubjects,
        generateSubjectBadge
    };
}

