/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/**/*.{html,js}",
    "./src/**/*.{html,js}",
    "./components/**/*.{html,js}"
  ],
  theme: {
    extend: {
      colors: {
        // Authentic Te Ao Māori Color Palette
        'pounamu': {
          green: '#059669',
          light: '#d1fae5',
          DEFAULT: '#059669'
        },
        'kahurangi': {
          blue: '#0284c7',
          DEFAULT: '#0284c7'
        },
        'whenua': {
          light: '#f5f1eb',
          DEFAULT: '#f5f1eb'
        },
        'ocean': {
          light: '#e0f2fe',
          DEFAULT: '#e0f2fe'
        },
        'sunrise': {
          yellow: '#fef3c7',
          DEFAULT: '#fef3c7'
        },
        // Cultural significance colors
        'cultural': {
          primary: '#059669',
          secondary: '#0284c7',
          accent: '#fef3c7',
          background: '#f5f1eb',
          highlight: '#e0f2fe'
        }
      },
      fontFamily: {
        'primary': ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        'cultural': ['Noto Sans Maori', 'Inter', 'sans-serif']
      },
      spacing: {
        'xs': '0.25rem',
        'sm': '0.5rem',
        'md': '1rem',
        'lg': '1.5rem',
        'xl': '2rem',
        '2xl': '3rem',
        '3xl': '4rem'
      },
      borderRadius: {
        'sm': '0.375rem',
        'md': '0.5rem',
        'lg': '0.75rem',
        'xl': '1rem'
      },
      boxShadow: {
        'cultural': '0 4px 6px -1px rgba(5, 150, 105, 0.1)',
        'cultural-lg': '0 10px 15px -3px rgba(5, 150, 105, 0.1)'
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.4s ease-out'
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        },
        slideUp: {
          '0%': { transform: 'translateY(30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        }
      }
    }
  },
  plugins: [
    // A4 Print optimization plugin
    function({ addUtilities }) {
      const printUtilities = {
        '.print-hide': {
          '@media print': {
            display: 'none !important'
          }
        },
        '.print-show': {
          '@media print': {
            display: 'block !important'
          }
        },
        '.print-a4': {
          '@media print': {
            width: '210mm',
            height: '297mm'
          }
        },
        '.print-break-inside-avoid': {
          '@media print': {
            'break-inside': 'avoid',
            'page-break-inside': 'avoid'
          }
        }
      }
      addUtilities(printUtilities)
    }
  ]
}

