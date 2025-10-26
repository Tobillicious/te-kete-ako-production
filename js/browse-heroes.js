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
                color: '#d83c3e',
                quickLinks: [
                    { href: 'handouts/writers-toolkit-peel-argument-handout.html', label: 'PEEL Method', icon: '📝' },
                    { href: 'toolkit.html', label: 'Writer\'s Toolkit', icon: '✍️' },
                    { href: 'handouts/media-literacy-comprehension-handout.html', label: 'Media Literacy', icon: '📰' }
                ],
                pedagogy: '"Reading the word and reading the world" (Freire, 1970) - literacy as a tool for critical consciousness and social transformation through culturally sustaining practices (Paris & Alim, 2017).'
            },
            'math': {
                icon: '🔢',
                titleMi: 'Pāngarau',
                titleEn: 'Mathematics',
                descriptionMi: 'Whakaaro tātai, raraunga, me te whakatau rapanga',
                descriptionEn: 'Mathematical thinking, data, and problem-solving for real-world contexts',
                color: '#00b0b9',
                quickLinks: [
                    { href: 'handouts/probability-handout.html', label: 'Probability', icon: '🎲' },
                    { href: 'curriculum-alignment.html#mathematics', label: 'Mathematics AO', icon: '📋' }
                ],
                pedagogy: '"Mathematics learning occurs through active construction within social and cultural contexts" (Vygotsky, 1978). Ethnomathematics honors Indigenous ways of mathematical knowing (D\'Ambrosio, 1985).'
            },
            'science': {
                icon: '🔬',
                titleMi: 'Pūtaiao',
                titleEn: 'Science',
                descriptionMi: 'Mātauranga Māori me te pūtaiao hou - ngā pūnaha mātai taiao',
                descriptionEn: 'Integrating mātauranga Māori and contemporary science for environmental understanding',
                color: '#2c5f41',
                quickLinks: [
                    { href: 'units/unit-3-stem-matauranga.html', label: 'STEM + Mātauranga', icon: '🌊' },
                    { href: 'curriculum-alignment.html#science', label: 'Science AO', icon: '📋' }
                ],
                pedagogy: '"Two-eyed seeing" (Bartlett et al., 2012) - learning to see from one eye with Indigenous knowledge and the other with Western science. Mātauranga Māori as legitimate, sophisticated scientific knowledge (Royal, 2009).'
            },
            'social-studies': {
                icon: '🌏',
                titleMi: 'Tikanga-ā-Iwi',
                titleEn: 'Social Studies',
                descriptionMi: 'Te ao Māori, tiriti, me te tika hapori - ako mō te ao hurihuri',
                descriptionEn: 'Te Ao Māori, Te Tiriti, and social justice - learning about our changing world',
                color: '#8b6f47',
                quickLinks: [
                    { href: 'y8-systems-unit.html', label: 'Systems Unit (Y8)', icon: '🏛️' },
                    { href: 'units/unit-2-decolonized-history.html', label: 'Decolonized History', icon: '🔥' },
                    { href: 'handouts/treaty-of-waitangi-handout.html', label: 'Te Tiriti', icon: '📜' },
                    { href: 'curriculum-alignment.html#social-sciences', label: 'Social Sciences AO', icon: '📋' }
                ],
                pedagogy: '"Culturally Responsive Pedagogy of Relations" (Bishop & Berryman, 2006) - power-sharing relationships where Māori students experience self-determination. Counter-storytelling challenges dominant narratives (Delgado & Stefancic, 2001).'
            },
            'te-reo': {
                icon: '🌿',
                titleMi: 'Te Reo Māori',
                titleEn: 'Māori Language',
                descriptionMi: 'Ko te reo te mauri o te mana Māori',
                descriptionEn: 'The language is the life force of Māori culture',
                color: '#2c5f41',
                quickLinks: [
                    { href: 'games/te-reo-wordle.html', label: 'Te Reo Wordle', icon: '🎮' },
                    { href: 'handouts/haka-comprehension-handout.html', label: 'Haka Analysis', icon: '💪' },
                    { href: 'units/unit-1-te-ao-maori.html', label: 'Te Ao Māori Unit', icon: '🌟' }
                ],
                pedagogy: '"Ko te reo te mauri o te mana Māori" - language is the life force of Māori identity (Waitangi Tribunal, 1986). Communicative competence develops through meaningful interaction in authentic contexts (Krashen, 1982).'
            },
            'arts': {
                icon: '🎨',
                titleMi: 'Ngā Toi',
                titleEn: 'The Arts',
                descriptionMi: 'Whakairo, toi ataata, puoro - ngā momo toi Māori me te ao whānui',
                descriptionEn: 'Visual arts, performing arts, music - Māori and global creative expression',
                color: '#f5a623',
                quickLinks: [],
                pedagogy: '"The arts are a way of knowing" (Eisner, 2002). Creative expression as cultural renewal and identity affirmation, honoring toi Māori as sophisticated artistic knowledge systems (Mead, 2003).'
            },
            'health-pe': {
                icon: '💪',
                titleMi: 'Hauora',
                titleEn: 'Health & Physical Education',
                descriptionMi: 'Tinana, hinengaro, whānau, wairua - te hauora whānui',
                descriptionEn: 'Physical, mental, family, spiritual - holistic wellbeing',
                color: '#40e0d0',
                quickLinks: [],
                pedagogy: 'Te Whare Tapa Whā (Durie, 1985) - holistic Māori health model integrating physical, mental, family, and spiritual dimensions. Health as socio-cultural construct (Burrows & Wright, 2007).'
            },
            'technology': {
                icon: '🔧',
                titleMi: 'Hangarau',
                titleEn: 'Technology',
                descriptionMi: 'Hangarau matihiko, hoahoa, me te mātauranga raraunga Māori',
                descriptionEn: 'Digital technologies, design, and Māori data sovereignty',
                color: '#1a1a1a',
                quickLinks: [
                    { href: 'units/unit-7-digital-tech-ai-ethics.html', label: 'AI Ethics', icon: '🤖' },
                    { href: 'curriculum-alignment.html#technology', label: 'Technology AO', icon: '📋' }
                ],
                pedagogy: 'Māori Data Sovereignty principles (Te Mana Raraunga, 2018) - Indigenous peoples\' rights to govern collection and use of data about them. Critical digital literacy (Pangrazio, 2016).'
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
                <h1 class="hero-title">
                    <span class="hero-title-mi">${subject.titleMi}</span>
                    <span class="hero-title-en">${subject.titleEn}</span>
                </h1>
                <p class="hero-description-mi" lang="mi">${subject.descriptionMi}</p>
                <p class="hero-description-en">${subject.descriptionEn}</p>
                ${subject.quickLinks.length > 0 ? `
                    <div class="hero-quick-links">
                        <span class="quick-links-label">Quick Access:</span>
                        ${subject.quickLinks.map(link => `
                            <a href="${link.href}" class="quick-link">
                                <span class="quick-link-icon">${link.icon}</span>
                                <span class="quick-link-label">${link.label}</span>
                            </a>
                        `).join('')}
                    </div>
                ` : ''}
                <p class="hero-pedagogy"><strong>Teaching Approach:</strong> ${subject.pedagogy}</p>
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
                <p class="hero-focus"><strong>Learning Focus:</strong> ${year.focus}</p>
                <p class="hero-development"><strong>Developmental Stage:</strong> ${year.development}</p>
                <p class="hero-pedagogy"><strong>Teaching Approach:</strong> ${year.pedagogy}</p>
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

