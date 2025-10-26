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
                pedagogy: 'Literacy as liberation: "Reading the word and reading the world" <cite>(<a href="https://en.wikipedia.org/wiki/Pedagogy_of_the_Oppressed" target="_blank" rel="noopener">Freire, 1970</a>)</cite>. Effective English teaching honors students\' home languages and cultural narratives as assets, not deficits <cite>(<a href="https://doi.org/10.4324/9781315458908" target="_blank" rel="noopener">Paris & Alim, 2017</a>)</cite>. Counter-storytelling challenges dominant narratives and centers marginalized voices <cite>(<a href="https://www.jstor.org/stable/j.ctt7sns7" target="_blank" rel="noopener">Delgado & Stefancic, 2001</a>)</cite>.',
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
                pedagogy: 'Mathematics as cultural practice: Learning occurs through "active construction within social and cultural contexts" <cite>(<a href="https://www.marxists.org/archive/vygotsky/works/mind/index.htm" target="_blank" rel="noopener">Vygotsky, 1978</a>)</cite>. Ethnomathematics recognizes that all cultures develop sophisticated mathematical systems <cite>(<a href="https://doi.org/10.1007/BF00302346" target="_blank" rel="noopener">D\'Ambrosio, 1985</a>)</cite>. Māori navigation, weaving patterns (tukutuku), and land management embody complex mathematical concepts.',
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
                pedagogy: 'Two knowledge systems, one vision: "Two-eyed seeing" means learning to see from one eye with Indigenous knowledge and from the other with Western science <cite>(<a href="https://www.iwk.nshealth.ca/sites/default/files/integrative_science.pdf" target="_blank" rel="noopener">Bartlett et al., 2012</a>)</cite>. Mātauranga Māori is legitimate, sophisticated scientific knowledge developed over centuries <cite>(<a href="https://doi.org/10.1080/03036758.2009.9523429" target="_blank" rel="noopener">Royal, 2009</a>)</cite>. Rongoā Māori, mahinga kai, and environmental observation systems demonstrate rigorous scientific methodology.',
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
                pedagogy: 'Education as power-sharing: "Culturally Responsive Pedagogy of Relations" creates classrooms where Māori students experience genuine self-determination <cite>(<a href="https://doi.org/10.18296/set.0452" target="_blank" rel="noopener">Bishop & Berryman, 2006</a>)</cite>. Te Tiriti o Waitangi is our nation\'s founding document, requiring partnership, protection, and participation. Critical Race Theory shows how counter-storytelling challenges dominant narratives and centers Indigenous perspectives <cite>(<a href="https://www.jstor.org/stable/j.ctt7sns7" target="_blank" rel="noopener">Delgado & Stefancic, 2001</a>)</cite>.',
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
                pedagogy: 'Language revitalization as justice: "Ko te reo te mauri o te mana Māori" - the language is the life force of Māori cultural identity <cite>(<a href="https://forms.justice.govt.nz/search/Documents/WT/wt_DOC_68482156/Report%20on%20the%20Te%20Reo%20Maori%20Claim.pdf" target="_blank" rel="noopener">Waitangi Tribunal, 1986</a>)</cite>. Communicative competence develops through meaningful interaction in authentic, culturally grounded contexts <cite>(<a href="https://www.sdkrashen.com/content/books/principles_and_practice.pdf" target="_blank" rel="noopener">Krashen, 1982</a>)</cite>. Language learning must center Indigenous sovereignty and cultural revitalization, not just linguistic skills.',
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
                pedagogy: 'Creativity as knowledge: "The arts are a way of knowing" distinct from but equal to scientific or mathematical thinking <cite>(<a href="https://doi.org/10.4324/9780203466452" target="_blank" rel="noopener">Eisner, 2002</a>)</cite>. Artistic expression enables cultural renewal, identity affirmation, and intergenerational connection. Toi Māori represents sophisticated knowledge systems in whakairo (carving), raranga (weaving), kapa haka, and mahi toi.',
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
                pedagogy: 'Holistic wellbeing: Te Whare Tapa Whā integrates four dimensions of health - taha tinana (physical), taha hinengaro (mental/emotional), taha whānau (family/social), and taha wairua (spiritual) <cite>(<a href="https://www.health.govt.nz/our-work/populations/maori-health/maori-health-models/maori-health-models-te-whare-tapa-wha" target="_blank" rel="noopener">Durie, 1985</a>)</cite>. Health is not individual biology but a socio-cultural construction shaped by context, identity, and relationships <cite>(<a href="https://doi.org/10.1080/17408980701345733" target="_blank" rel="noopener">Burrows & Wright, 2007</a>)</cite>.',
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
                pedagogy: 'Data as taonga: Māori Data Sovereignty asserts Indigenous peoples\' rights to govern the collection, ownership, and application of data about Māori communities <cite>(<a href="https://www.temanararaunga.maori.nz/nga-rauemi" target="_blank" rel="noopener">Te Mana Raraunga, 2018</a>)</cite>. Critical digital literacy questions who benefits from technology and challenges assumptions about "neutral" algorithms <cite>(<a href="https://doi.org/10.1080/17439884.2016.1142504" target="_blank" rel="noopener">Pangrazio, 2016</a>)</cite>. Technology education must center ethics, equity, and cultural protocols.',
                culturalNote: 'Hangarau integrates tikanga Māori into digital design and innovation. We teach students to be critical creators, not passive consumers, of technology.'
            }
        };

        this.yearLevels = {
            '1': {
                stage: 'Primary / Tuatahi',
                focus: 'Building foundation skills through play, exploration, and cultural grounding',
                development: 'Ages 5-6: Developing literacy, numeracy, and social skills. Learning through hands-on experiences and storytelling.',
                pedagogy: 'Play as foundation: "Play is the work of the child" <cite>(<a href="https://amshq.org/About-Montessori/Inside-the-Classroom/Play" target="_blank" rel="noopener">Montessori, 1967</a>)</cite>. Zone of Proximal Development shows learning occurs through supported interaction with more capable others <cite>(<a href="https://www.marxists.org/archive/vygotsky/works/mind/index.htm" target="_blank" rel="noopener">Vygotsky, 1978</a>)</cite>.',
                ministryLink: { href: 'https://nzcurriculum.tki.org.nz/The-New-Zealand-Curriculum', label: 'NZC: The New Zealand Curriculum' }
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
                pedagogy: 'Responsive relationships: "Caring relationships and high expectations" define effective teaching <cite>(<a href="https://doi.org/10.18296/set.0452" target="_blank" rel="noopener">Bishop, 2003</a>)</cite>. Culturally responsive pedagogy centers student identity and voice, not deficit narratives <cite>(<a href="https://doi.org/10.4324/9780203594391" target="_blank" rel="noopener">Gay, 2010</a>)</cite>.',
                ministryLink: { href: 'https://www.education.govt.nz/school/student-support/wellbeing-in-schools/', label: 'Ministry: Student Wellbeing' }
            },
            '8': {
                stage: 'Intermediate / Waenga',
                focus: 'Building critical thinking and preparing for secondary school transitions',
                development: 'Ages 12-13: Developing abstract thinking, exploring values, preparing for increased academic demands.',
                pedagogy: 'Critical consciousness: "Problem-posing education" frames students as critical co-investigators, not passive recipients <cite>(<a href="https://en.wikipedia.org/wiki/Pedagogy_of_the_Oppressed" target="_blank" rel="noopener">Freire, 1970</a>)</cite>. Adolescent identity formation requires authentic challenges and meaningful participation <cite>(<a href="https://www.verywellmind.com/erik-eriksons-stages-of-psychosocial-development-2795740" target="_blank" rel="noopener">Erikson, 1968</a>)</cite>.',
                ministryLink: { href: 'https://www.education.govt.nz/school/running-a-school/curriculum/transition-from-primary-to-secondary/', label: 'Ministry: Primary to Secondary Transition' }
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
                pedagogy: 'Assessment as learning: Feedback that moves learning forward, not just measures it <cite>(<a href="https://doi.org/10.1177/003172171009200119" target="_blank" rel="noopener">Black & Wiliam, 1998</a>)</cite>. Culturally located assessment honors diverse ways of demonstrating knowledge beyond Western written exams <cite>(<a href="https://nzareblog.wordpress.com/2010/06/16/wally-penetito/" target="_blank" rel="noopener">Penetito, 2010</a>)</cite>.',
                ministryLink: { href: 'https://www.nzqa.govt.nz/ncea/', label: 'NZQA: NCEA Information' }
            },
            '12': {
                stage: 'Senior Secondary / NCEA',
                focus: 'NCEA Level 2 - Specializing and planning for post-school transitions',
                development: 'Ages 16-17: Focused study, career planning, developing expertise in chosen areas.',
                pedagogy: 'Cultural assets as strength: Funds of Knowledge draws on students\' cultural and community resources as learning assets, not deficits <cite>(<a href="https://doi.org/10.1177/003172170109200605" target="_blank" rel="noopener">Moll et al., 1992</a>)</cite>. Self-determination theory shows autonomy supports motivation and achievement <cite>(<a href="https://psycnet.apa.org/doi/10.1037/0003-066X.55.1.68" target="_blank" rel="noopener">Ryan & Deci, 2000</a>)</cite>.',
                ministryLink: { href: 'https://www.careers.govt.nz/', label: 'Careers NZ: Pathway Planning' }
            },
            '13': {
                stage: 'Senior Secondary / NCEA',
                focus: 'NCEA Level 3 - Final year preparation for university, polytech, or workforce',
                development: 'Ages 17-18: University entrance, scholarship opportunities, mature independent learners.',
                pedagogy: 'Liberation and leadership: "Conscientização" (critical consciousness) empowers students to read and transform their world <cite>(<a href="https://en.wikipedia.org/wiki/Pedagogy_of_the_Oppressed" target="_blank" rel="noopener">Freire, 1970</a>)</cite>. Rangatiratanga in education means Māori self-determination and leadership in learning pathways <cite>(<a href="https://doi.org/10.1080/0161956970180202" target="_blank" rel="noopener">G.H. Smith, 1997</a>)</cite>.',
                ministryLink: { href: 'https://www.nzqa.govt.nz/qualifications-standards/awards/university-entrance/', label: 'NZQA: University Entrance' }
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
                </div>
            </div>
        `;

        main.insertBefore(hero, main.firstChild);
        
        // Add pedagogy section separately after the hero
        if (subject.pedagogy) {
            const pedagogyBox = document.createElement('div');
            pedagogyBox.className = 'hero-pedagogy-box';
            pedagogyBox.innerHTML = `
                <div class="hero-pedagogy">
                    <strong>Research-Based Pedagogy</strong>
                    <p>${subject.pedagogy}</p>
                    ${subject.culturalNote ? `<p class="cultural-note"><strong>Cultural Responsiveness:</strong> ${subject.culturalNote}</p>` : ''}
                </div>
            `;
            main.insertBefore(pedagogyBox, hero.nextSibling);
        }
        
        console.log(`[Browse Heroes] Rendered subject hero for ${subjectKey}`);
    }

    renderYearHero(yearLevel) {
        const year = this.yearLevels[yearLevel];
        const main = document.querySelector('main.content-area');
        if (!main) return;

        // Rainbow color progression for years 1-13 (evenly spaced across spectrum)
        const yearColors = {
            '1': { start: '#D1477A', mid: '#E56B9A', end: '#F5A5C4' },  // Bright Pink
            '2': { start: '#B84E8E', mid: '#D172AC', end: '#EBA5D1' },  // Pink-Purple
            '3': { start: '#9755A3', mid: '#B879C7', end: '#D9ACEB' },  // Purple
            '4': { start: '#7660B7', mid: '#9884D1', end: '#C4B7EB' },  // Blue-Purple
            '5': { start: '#556BC7', mid: '#778FDB', end: '#AABCF0' },  // Blue
            '6': { start: '#3476CF', mid: '#5693DD', end: '#93C0F0' },  // Sky Blue
            '7': { start: '#2B8AAA', mid: '#4DA8C7', end: '#8DD1E8' },  // Cyan
            '8': { start: '#2A9B7E', mid: '#4CB99E', end: '#8DDDC8' },  // Teal-Green
            '9': { start: '#3FA856', mid: '#62C478', end: '#9DE8B4' },  // Green
            '10': { start: '#7AB83A', mid: '#9BD65E', end: '#C8F090' }, // Yellow-Green
            '11': { start: '#C2B43A', mid: '#DDD25E', end: '#F5EB90' }, // Yellow
            '12': { start: '#DB8E3A', mid: '#EFAD5E', end: '#FFD090' }, // Orange
            '13': { start: '#D85A3A', mid: '#EF7E5E', end: '#FFB090' }  // Orange-Red
        };

        const colors = yearColors[yearLevel] || yearColors['5'];

        const hero = document.createElement('div');
        hero.className = 'year-hero';
        hero.style.setProperty('--year-color-start', colors.start);
        hero.style.setProperty('--year-color-mid', colors.mid);
        hero.style.setProperty('--year-color-end', colors.end);
        
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
                    ${year.ministryLink ? `
                        <div class="ministry-resource">
                            <a href="${year.ministryLink.href}" target="_blank" rel="noopener" class="ministry-link">
                                <span class="ministry-icon">🏛️</span>
                                ${year.ministryLink.label}
                            </a>
                        </div>
                    ` : ''}
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

