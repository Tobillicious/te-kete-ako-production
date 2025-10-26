// daily-whakatauki.js
// Displays a rotating daily whakataukī in the sidebar

class DailyWhakatauki {
    constructor() {
        this.whakatauki = [
            {
                mi: "He aha te mea nui o te ao? He tangata, he tangata, he tangata.",
                en: "What is the most important thing in the world? It is people, it is people, it is people."
            },
            {
                mi: "Whāia te mātauranga hei oranga mō koutou.",
                en: "Seek after learning for the sake of your wellbeing."
            },
            {
                mi: "He waka eke noa.",
                en: "We are all in this together."
            },
            {
                mi: "Mā te kōrero, ka mōhio; mā te mōhio, ka mārama; mā te mārama, ka mātau; mā te mātau, ka ora.",
                en: "Through discussion comes awareness; through awareness comes understanding; through understanding comes knowledge; through knowledge comes life."
            },
            {
                mi: "Poipoia te kakano kia puawai.",
                en: "Nurture the seed and it will blossom."
            },
            {
                mi: "Kia kaha, kia māia, kia manawanui.",
                en: "Be strong, be brave, be steadfast."
            },
            {
                mi: "Whaowhia te kete mātauranga.",
                en: "Fill the basket of knowledge."
            },
            {
                mi: "Ehara taku toa i te toa takitahi, engari he toa takitini.",
                en: "My strength is not that of an individual, but that of the collective."
            },
            {
                mi: "Mā pango, mā whero, ka oti te mahi.",
                en: "With red and black (collaboration), the work will be complete."
            },
            {
                mi: "Hutia te rito o te harakeke, kei hea te kōmako e kō?",
                en: "If you pluck the heart of the flax, where will the bellbird sing?"
            },
            {
                mi: "Nāu te rourou, nāku te rourou, ka ora ai te iwi.",
                en: "With your food basket and my food basket, the people will thrive."
            },
            {
                mi: "Ko te pae tawhiti, whāia kia tata. Ko te pae tata, whakamaua kia tina.",
                en: "Seek out distant horizons and cherish those you attain."
            },
            {
                mi: "He kai kei aku ringa.",
                en: "There is food at the end of my hands (I have the ability to provide)."
            },
            {
                mi: "Kia hora te marino, kia whakapapa pounamu te moana.",
                en: "May peace be widespread, may the sea glisten like greenstone."
            },
            {
                mi: "Tūturu whakamaua kia tina! Haumi e, hui e, tāiki e!",
                en: "Stand fast, be determined! Join together, gather as one!"
            }
        ];
    }

    // Get today's whakataukī based on day of year (changes daily)
    getTodaysWhakatauki() {
        const dayOfYear = this.getDayOfYear();
        const index = dayOfYear % this.whakatauki.length;
        return this.whakatauki[index];
    }

    // Calculate day of year (1-365/366)
    getDayOfYear() {
        const now = new Date();
        const start = new Date(now.getFullYear(), 0, 0);
        const diff = now - start;
        const oneDay = 1000 * 60 * 60 * 24;
        return Math.floor(diff / oneDay);
    }

    // Render the whakataukī widget in the sidebar
    render() {
        const sidebar = document.querySelector('.left-sidebar');
        if (!sidebar) {
            console.log('[Daily Whakataukī] Sidebar not found on this page');
            return;
        }

        const todaysWhakatauki = this.getTodaysWhakatauki();
        
        // Create the widget HTML
        const widget = document.createElement('div');
        widget.className = 'sidebar-widget whakatauki-widget';
        widget.innerHTML = `
            <h3 class="sidebar-widget-title">
                <span class="sidebar-icon">💭</span>
                <span class="sidebar-title-text">
                    <span class="sidebar-mi">Whakataukī o te Rā</span>
                    <span class="sidebar-en">Proverb of the Day</span>
                </span>
            </h3>
            <div class="whakatauki-content">
                <p class="whakatauki-mi" lang="mi">${todaysWhakatauki.mi}</p>
                <p class="whakatauki-en">${todaysWhakatauki.en}</p>
            </div>
        `;

        // Insert at the top of the sidebar
        sidebar.insertBefore(widget, sidebar.firstChild);
        
        console.log('[Daily Whakataukī] Rendered successfully');
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const dailyWhakatauki = new DailyWhakatauki();
    dailyWhakatauki.render();
});

