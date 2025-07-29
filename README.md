# Te Kete Ako | The Basket of Knowledge

**"Whaowhia te kete mātauranga"** - *Fill the basket of knowledge*

Te Kete Ako is a collection of high-quality educational resources for teachers and students in Aotearoa, with a focus on honoring Te Ao Māori and aligning with the New Zealand Curriculum.

This repository represents a clean, production-ready version of the website, optimized for stable and easy deployment.

## ✨ Key Features

*   **📚 Comprehensive Resources:** A wide range of materials including Unit Plans, Lesson Plans, Handouts, and "Do Now" activities.
*   **🎮 Interactive Games:** Engaging learning games like Te Reo Māori Wordle, Spelling Bee, and Countdown.
*   **📋 NZ Curriculum Aligned:** Resources are mapped to the NZ Curriculum, with an interactive browser to explore achievement objectives.
*   **🌿 Te Ao Māori Focus:** Content is designed to integrate and honor Māori perspectives, knowledge, and language.
*   **📺 Multimedia Integration:** Curated YouTube video resources and activities.
*   **📱 PWA Ready:** The site is a Progressive Web App, allowing for offline access and installation on devices.

## 🚀 Deployment

This site is designed for simple, static deployment. The recommended method is Netlify.

**Netlify Drag & Drop (Recommended)**
1.  Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
2.  Drag the entire `te-kete-ako-clean` folder onto the page.
3.  The site will be live in seconds!

The `netlify.toml` file in this repository contains all the necessary configuration for redirects and headers.

## 📂 Project Structure

The repository is organized into the following main directories:

```
/
├── css/              # Main stylesheets
├── data/             # JSON data for curriculum frameworks
├── games/            # HTML and JS for interactive games
├── handouts/         # Printable and digital student handouts
├── js/               # Core JavaScript files for interactivity
├── units/            # Complete unit and lesson plans
├── y8-systems/       # Specific unit for Year 8 Social Studies
├── *.html            # Top-level pages (Home, About, etc.)
└── netlify.toml      # Deployment configuration
```

## 🤖 Working with AI Agents

To effectively contribute to this project, an AI agent should:
1.  **Analyze Existing Conventions:** Before adding new content, review existing `.html` files in the relevant directory (e.g., `handouts/` or `units/`) to understand the established structure, class names, and layout.
2.  **Use Shared Components:** The `js/shared-components.js` script likely handles common elements like headers and footers. New pages should be built to work with this script.
3.  **Maintain the Style:** Adhere to the visual style defined in `css/main.css`.
4.  **Update Navigation:** When adding new top-level pages or resources, consider if updates are needed to navigation menus in the main `.html` files.
PREVIEWS FOLDER REMOVED - Tue Jul 29 23:25:03 NZST 2025
