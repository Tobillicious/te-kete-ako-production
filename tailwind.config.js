/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/**/*.{html,js}",
    "./public/components/**/*.html",
    "./public/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'kete-green': '#1a4d2e',
        'kete-gold': '#d4a574',
        'kete-earth': '#8b4513',
        'kete-sky': '#87ceeb'
      },
      fontFamily: {
        'maori': ['Inter', 'system-ui', 'sans-serif']
      }
    },
  },
  plugins: [],
}