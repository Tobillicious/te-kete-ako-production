// Tailwind CSS Configuration for Te Kete Ako Ultimate Beauty System
// Wait for Tailwind to load before configuring
if (typeof tailwind !== 'undefined') {
  tailwind.config = {
  theme: {
    extend: {
      colors: {
        'kete-green': '#1b4332',
        'kete-accent': '#f59e0b',
        'kete-cultural': '#a855f7',
        'kete-brain': '#ec4899',
      },
      fontFamily: {
        'inter': ['Inter', 'sans-serif'],
        'lato': ['Lato', 'sans-serif'],
        'merriweather': ['Merriweather', 'serif'],
      },
      animation: {
        'bounce-gentle': 'bounce 2s infinite',
        'pulse-slow': 'pulse 3s infinite',
        'fade-in': 'fadeIn 0.5s ease-in',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    }
  },
  safelist: [
    'bg-gradient-to-r',
    'from-purple-600',
    'to-blue-600',
    'text-white',
    'shadow-lg',
    'rounded-lg',
    'p-4',
    'mb-4',
    'animate-pulse',
    'hover:scale-105',
    'transition-all',
    'duration-300',
  ]
  }
} else {
  // Fallback if Tailwind isn't loaded yet
  console.log('🎨 Tailwind CSS not yet loaded, config will apply when ready');
}