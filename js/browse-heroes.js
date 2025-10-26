// browse-heroes.js
// Dynamic hero sections for subject and year level browse pages

class BrowseHeroes {
    constructor() {
        this.subjects = {
            'english': {
                icon: '📝',
                titleMi: 'Reo Pākehā',
                titleEn: 'English',
                descriptionMi: 'Tuhituhi, pānui, kōrero - ngā pūkenga reo hei whakawhitiwhiti whakaaro',
                descriptionEn: 'Writing, reading, speaking - language skills for sharing ideas and stories',
                color: '#5B8DBE',
                quickLinks: [
                    { href: 'handouts/writers-toolkit-peel-argument-handout.html', label: 'PEEL Method', icon: '📝' },
                    { href: 'toolkit.html', label: 'Writer\'s Toolkit', icon: '✍️' },
                    { href: 'handouts/media-literacy-comprehension-handout.html', label: 'Media Literacy', icon: '📰' }
                ],
                pedagogy: 'Literacy as liberation: "Reading the word and reading the world" <cite>(Freire, 1970)</cite>. Effective English teaching honors students\' home languages and cultural narratives as assets, not deficits <cite>(Paris & Alim, 2017)</cite>. Counter-storytelling challenges dominant narratives and centers marginalized voices <cite>(Delgado & Stefancic, 2001)</cite>.',
                culturalNote: 'Te reo Pākehā is taught alongside te reo Māori, recognizing bilingualism as a strength and honoring the languages of all our ākonga.'
            },
            'math': {
                icon: '🔢',
                titleMi: 'Pāngarau',
                titleEn: 'Mathematics and Statistics',
                descriptionMi: 'Whakaaro tātai, raraunga, me te whakatau rapanga',
                descriptionEn: 'Mathematical thinking, data, and problem-solving for real-world contexts',
                color: '#8B2E4E',
                quickLinks: [
                    { href: 'handouts/probability-handout.html', label: 'Probability', icon: '🎲' },
                    { href: 'curriculum-alignment.html#mathematics', label: 'Mathematics AO', icon: '📋' }
                ],
                pedagogy: 'Mathematics as cultural practice: Learning occurs through "active construction within social and cultural contexts" <cite>(Vygotsky, 1978)</cite>. Ethnomathematics recognizes that all cultures develop sophisticated mathematical systems <cite>(D\'Ambrosio, 1985)</cite>. Māori navigation, weaving patterns (tukutuku), and land management embody complex mathematical concepts.',
                culturalNote: 'Pāngarau honors mātauranga Māori mathematical knowledge systems including geometry in whakairo, statistics in whakapapa, and spatial reasoning in traditional navigation.'
            },
            'science': {
                icon: '🔬',
                titleMi: 'Pūtaiao',
                titleEn: 'Science',
                descriptionMi: 'Mātauranga Māori me te pūtaiao hou - ngā pūnaha mātai taiao',
                descriptionEn: 'Integrating mātauranga Māori and contemporary science for environmental understanding',
                color: '#1E5741',
                quickLinks: [
                    { href: 'units/unit-3-stem-matauranga.html', label: 'STEM + Mātauranga', icon: '🌊' },
                    { href: 'curriculum-alignment.html#science', label: 'Science AO', icon: '📋' }
                ],
                pedagogy: 'Two knowledge systems, one vision: "Two-eyed seeing" means learning to see from one eye with Indigenous knowledge and from the other with Western science <cite>(Bartlett et al., 2012)</cite>. Mātauranga Māori is legitimate, sophisticated scientific knowledge developed over centuries <cite>(Royal, 2009)</cite>. Rongoā Māori, mahinga kai, and environmental observation systems demonstrate rigorous scientific methodology.',
                culturalNote: 'Pūtaiao weaves mātauranga Māori and Western science together, honoring kaitiakitanga (guardianship) and whakapapa (interconnection) as foundational scientific principles.'
            },
            'social-studies': {
                icon: '🌏',
                titleMi: 'Tikanga-ā-Iwi',
                titleEn: 'Social Sciences',
                descriptionMi: 'Te ao Māori, tiriti, me te tika hapori - ako mō te ao hurihuri',
                descriptionEn: 'Te Ao Māori, Te Tiriti, and social justice - learning about our changing world',
                color: '#6B4C9A',
                quickLinks: [
                    { href: 'y8-systems-unit.html', label: 'Systems Unit (Y8)', icon: '🏛️' },
                    { href: 'units/unit-2-decolonized-history.html', label: 'Decolonized History', icon: '🔥' },
                    { href: 'handouts/treaty-of-waitangi-handout.html', label: 'Te Tiriti', icon: '📜' },
                    { href: 'curriculum-alignment.html#social-sciences', label: 'Social Sciences AO', icon: '📋' }
                ],
                pedagogy: 'Education as power-sharing: "Culturally Responsive Pedagogy of Relations" creates classrooms where Māori students experience genuine self-determination <cite>(Bishop & Berryman, 2006)</cite>. Te Tiriti o Waitangi is our nation\'s founding document, requiring partnership, protection, and participation. Critical Race Theory shows how counter-storytelling challenges dominant narratives and centers Indigenous perspectives <cite>(Delgado & Stefancic, 2001)</cite>.',
                culturalNote: 'Tikanga-ā-Iwi centers Te Tiriti, te ao Māori, and social justice. We teach history from multiple perspectives, honoring Māori voices and experiences as central, not marginal.'
            },
            'te-reo': {
                icon: '🌿',
                titleMi: 'Te Reo Māori',
                titleEn: 'Learning Languages',
                descriptionMi: 'Ko te reo te mauri o te mana Māori',
                descriptionEn: 'The language is the life force of Māori culture',
                color: '#40B5AD',
                quickLinks: [
                    { href: 'games/te-reo-wordle.html', label: 'Te Reo Wordle', icon: '🎮' },
                    { href: 'handouts/haka-comprehension-handout.html', label: 'Haka Analysis', icon: '💪' },
                    { href: 'units/unit-1-te-ao-maori.html', label: 'Te Ao Māori Unit', icon: '🌟' }
                ],
                pedagogy: 'Language revitalization as justice: "Ko te reo te mauri o te mana Māori" - the language is the life force of Māori cultural identity <cite>(Waitangi Tribunal, 1986)</cite>. Communicative competence develops through meaningful interaction in authentic, culturally grounded contexts <cite>(Krashen, 1982)</cite>. Language learning must center Indigenous sovereignty and cultural revitalization, not just linguistic skills.',
                culturalNote: 'Te reo Māori is a taonga (treasure) protected under Te Tiriti. Our teaching honors language as identity, whakapapa, and a living connection to tūpuna (ancestors).'
            },
            'arts': {
                icon: '🎨',
                titleMi: 'Ngā Toi',
                titleEn: 'The Arts',
                descriptionMi: 'Whakairo, toi ataata, puoro - ngā momo toi Māori me te ao whānui',
                descriptionEn: 'Visual arts, performing arts, music - Māori and global creative expression',
                color: '#C17A4F',
                quickLinks: [],
                pedagogy: 'Creativity as knowledge: "The arts are a way of knowing" distinct from but equal to scientific or mathematical thinking <cite>(Eisner, 2002)</cite>. Artistic expression enables cultural renewal, identity affirmation, and intergenerational connection. Toi Māori represents sophisticated knowledge systems in whakairo (carving), raranga (weaving), kapa haka, and mahi toi.',
                culturalNote: 'Ngā Toi honors toi Māori as living, evolving artistic traditions. Whakapapa, tikanga, and mātauranga are woven through all creative expression in this learning area.'
            },
            'health-pe': {
                icon: '💪',
                titleMi: 'Hauora',
                titleEn: 'Health and Physical Education',
                descriptionMi: 'Tinana, hinengaro, whānau, wairua - te hauora whānui',
                descriptionEn: 'Physical, mental, family, spiritual - holistic wellbeing',
                color: '#D64045',
                quickLinks: [],
                pedagogy: 'Holistic wellbeing: Te Whare Tapa Whā integrates four dimensions of health - taha tinana (physical), taha hinengaro (mental/emotional), taha whānau (family/social), and taha wairua (spiritual) <cite>(Durie, 1985)</cite>. Health is not individual biology but a socio-cultural construction shaped by context, identity, and relationships <cite>(Burrows & Wright, 2007)</cite>.',
                culturalNote: 'Hauora is grounded in Māori models of wellbeing. We reject deficit narratives about Māori health and center strengths-based, culturally affirming approaches to physical and mental wellness.'
            },
            'technology': {
                icon: '🔧',
                titleMi: 'Hangarau',
                titleEn: 'Technology',
                descriptionMi: 'Hangarau matihiko, hoahoa, me te mātauranga raraunga Māori',
                descriptionEn: 'Digital technologies, design, and Māori data sovereignty',
                color: '#8B6F47',
                quickLinks: [
                    { href: 'units/unit-7-digital-tech-ai-ethics.html', label: 'AI Ethics', icon: '🤖' },
                    { href: 'curriculum-alignment.html#technology', label: 'Technology AO', icon: '📋' }
                ],
                pedagogy: 'Data as taonga: Māori Data Sovereignty asserts Indigenous peoples\' rights to govern the collection, ownership, and application of data about Māori communities <cite>(Te Mana Raraunga, 2018)</cite>. Critical digital literacy questions who benefits from technology and challenges assumptions about "neutral" algorithms <cite>(Pangrazio, 2016)</cite>. Technology education must center ethics, equity, and cultural protocols.',
                culturalNote: 'Hangarau integrates tikanga Māori into digital design and innovation. We teach students to be critical creators, not passive consumers, of technology.'
            }
        };

        this.yearLevels = {
            '1': {
                stage: 'Primary / Tuatahi',
                focus: 'Building foundation skills through play, exploration, and cultural grounding',
                development: 'Ages 5-6: Developing literacy, numeracy, and social skills. Learning through hands-on experiences and storytelling.',
                pedagogy: '"Play is the work of the child" (Montessori, 1967). Zone of Proximal Development - learning occurs through supported interaction with more capable others (Vygotsky, 1978).'
            },
            '2': {
                stage: 'Primary / Tuatahi',
                focus: 'Expanding literacy and numeracy through cultural stories and real-world contexts',
                development: 'Ages 6-7: Growing independence in reading and writing. Exploring mathematical concepts through practical activities.',
                pedagogy: 'Structured play, collaborative learning, building on prior knowledge.'
            },
            '3': {
                stage: 'Primary / Tuatahi',
                focus: 'Developing critical thinking and deeper understanding across all learning areas',
                development: 'Ages 7-8: Increased reading fluency, problem-solving skills, and ability to work independently.',
                pedagogy: 'Inquiry-based learning, differentiation, connecting learning to students\' lives.'
            },
            '4': {
                stage: 'Primary / Tuatahi',
                focus: 'Building independence and exploring identity through curriculum content',
                development: 'Ages 8-9: Developing more complex thinking, beginning to question and analyze information.',
                pedagogy: 'Student agency, collaborative projects, connecting to whānau and community.'
            },
            '5': {
                stage: 'Primary / Tuatahi',
                focus: 'Preparing for intermediate with increased independence and responsibility',
                development: 'Ages 9-10: Transitioning to more abstract thinking, leadership opportunities, peer collaboration.',
                pedagogy: 'Self-directed learning, leadership development, complex problem-solving.'
            },
            '6': {
                stage: 'Primary / Tuatahi',
                focus: 'Consolidating primary learning and transitioning to intermediate challenges',
                development: 'Ages 10-11: Ready for more complex content, developing strong peer relationships, increased independence.',
                pedagogy: 'Transition planning, authentic audiences, real-world problem-solving.'
            },
            '7': {
                stage: 'Intermediate / Waenga',
                focus: 'Navigating early adolescence with cultural identity and academic challenge',
                development: 'Ages 11-12: Rapid physical and emotional changes, seeking peer acceptance, questioning identity.',
                pedagogy: '"Caring relationships and high expectations" (Bishop, 2003) - Te Kotahitanga effective teaching profile. Culturally responsive pedagogy centers student identity and voice (Gay, 2010).'
            },
            '8': {
                stage: 'Intermediate / Waenga',
                focus: 'Building critical thinking and preparing for secondary school transitions',
                development: 'Ages 12-13: Developing abstract thinking, exploring values, preparing for increased academic demands.',
                pedagogy: '"Problem-posing education" (Freire, 1970) - students as critical co-investigators. Adolescent identity formation requires authentic challenges and meaningful participation (Erikson, 1968).'
            },
            '9': {
                stage: 'Junior Secondary / Tuarua',
                focus: 'Beginning secondary education with identity exploration and academic specialization',
                development: 'Ages 13-14: New school environment, increased subject choice, developing independence and responsibility.',
                pedagogy: 'Subject specialization, assessment for learning, digital literacy, career pathways.'
            },
            '10': {
                stage: 'Junior Secondary / Tuarua',
                focus: 'Deepening subject knowledge and preparing for NCEA pathways',
                development: 'Ages 14-15: Solidifying interests, planning for senior years, developing study skills and time management.',
                pedagogy: 'Pathway planning, authentic assessment, student choice, future-focused learning.'
            },
            '11': {
                stage: 'Senior Secondary / NCEA',
                focus: 'NCEA Level 1 - Building credits and exploring post-school pathways',
                development: 'Ages 15-16: First year of NCEA, developing assessment skills, beginning to specialize in subject areas.',
                pedagogy: 'Assessment for Learning (Black & Wiliam, 1998) - feedback that moves learning forward. Culturally located assessment honors diverse ways of demonstrating knowledge (Penetito, 2010).'
            },
            '12': {
                stage: 'Senior Secondary / NCEA',
                focus: 'NCEA Level 2 - Specializing and planning for post-school transitions',
                development: 'Ages 16-17: Focused study, career planning, developing expertise in chosen areas.',
                pedagogy: 'Funds of Knowledge (Moll et al., 1992) - drawing on students\' cultural and community resources as learning assets. Self-determination theory supports autonomy in pathway choices (Ryan & Deci, 2000).'
            },
            '13': {
                stage: 'Senior Secondary / NCEA',
                focus: 'NCEA Level 3 - Final year preparation for university, polytech, or workforce',
                development: 'Ages 17-18: University entrance, scholarship opportunities, mature independent learners.',
                pedagogy: '"Conscientização" - critical consciousness (Freire, 1970). Rangatiratanga in education: Māori self-determination and leadership in learning pathways (G.H. Smith, 1997).'
            }
        };
    }

    init() {
        const urlParams = new URLSearchParams(window.location.search);
        const subject = urlParams.get('subject');
        const year = urlParams.get('year');

        if (subject && this.subjects[subject]) {
            this.renderSubjectHero(subject);
        } else if (year && this.yearLevels[year]) {
            this.renderYearHero(year);
        }
    }

    renderSubjectHero(subjectKey) {
        const subject = this.subjects[subjectKey];
        const main = document.querySelector('main.content-area');
        if (!main) return;

        const hero = document.createElement('div');
        hero.className = 'subject-hero';
        hero.style.setProperty('--subject-color', subject.color);
        
        hero.innerHTML = `
            <div class="hero-icon">${subject.icon}</div>
            <div class="hero-content">
                <div class="hero-main">
                    <h1 class="hero-title">
                        <span class="hero-title-mi">${subject.titleMi}</span>
                        <span class="hero-title-en">${subject.titleEn}</span>
                    </h1>
                    <p class="hero-description-mi" lang="mi">${subject.descriptionMi}</p>
                    <p class="hero-description-en">${subject.descriptionEn}</p>
                </div>
                <div class="hero-sidebar">
                    ${subject.quickLinks.length > 0 ? `
                        <div class="hero-quick-links">
                            <span class="quick-links-label">Quick Access</span>
                            ${subject.quickLinks.map(link => `
                                <a href="${link.href}" class="quick-link">
                                    <span class="quick-link-icon">${link.icon}</span>
                                    <span class="quick-link-label">${link.label}</span>
                                </a>
                            `).join('')}
                        </div>
                    ` : ''}
                    <div class="hero-pedagogy">
                        <strong>Research-Based Pedagogy</strong>
                        <p>${subject.pedagogy}</p>
                        ${subject.culturalNote ? `<p class="cultural-note"><strong>Cultural Responsiveness:</strong> ${subject.culturalNote}</p>` : ''}
                    </div>
                </div>
            </div>
        `;

        main.insertBefore(hero, main.firstChild);
        console.log(`[Browse Heroes] Rendered subject hero for ${subjectKey}`);
    }

    renderYearHero(yearLevel) {
        const year = this.yearLevels[yearLevel];
        const main = document.querySelector('main.content-area');
        if (!main) return;

        const hero = document.createElement('div');
        hero.className = 'year-hero';
        
        hero.innerHTML = `
            <div class="hero-year-badge">
                <span class="year-number">Year ${yearLevel}</span>
                <span class="year-stage">${year.stage}</span>
            </div>
            <div class="hero-content">
                <h1 class="hero-title">Year ${yearLevel} Resources</h1>
                <div class="hero-info-grid">
                    <div class="hero-focus">
                        <strong>Ako Focus</strong>
                        <p>${year.focus}</p>
                    </div>
                    <div class="hero-development">
                        <strong>Ākonga Development</strong>
                        <p>${year.development}</p>
                    </div>
                </div>
                <div class="hero-pedagogy">
                    <strong>Research-Based Pedagogy</strong>
                    <p>${year.pedagogy}</p>
                </div>
            </div>
        `;

        main.insertBefore(hero, main.firstChild);
        console.log(`[Browse Heroes] Rendered year hero for Year ${yearLevel}`);
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const browseHeroes = new BrowseHeroes();
    browseHeroes.init();
});

