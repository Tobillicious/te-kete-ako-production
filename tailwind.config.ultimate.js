/** @type {import('tailwindcss').Config} */
/**
 * 🎨 TE KETE AKO ULTIMATE DESIGN SYSTEM
 * HEGELIAN SYNTHESIS: Kehinde Wiley + Silicon Valley + Te Ao Māori
 * 
 * THESIS: Bold cultural authenticity (Kehinde Wiley + BMAD)
 * ANTITHESIS: Modern performance excellence (Tailwind + Silicon Valley)
 * SYNTHESIS: Te Kete Ako Ultimate Beauty - Beautiful beyond belief
 */

module.exports = {
  content: [
    "./public/**/*.{html,js}",
    "./src/**/*.{html,js}",
    "./components/**/*.{html,js}"
  ],
  
  theme: {
    extend: {
      // ===================================================================
      // ULTIMATE COLOR SYSTEM - Kehinde Wiley Saturation + Tailwind Scales
      // ===================================================================
      colors: {
        // POUNAMU (Greenstone) - Sacred Guardian Color
        pounamu: {
          50: '#f0fdf4',    // Morning mist
          100: '#dcfce7',   // New growth
          200: '#bbf7d0',   // Fresh leaves
          300: '#86efac',   // Vibrant jade
          400: '#4ade80',   // Bright greenstone
          500: '#1B7F5A',   // Sacred pounamu (Kehinde Wiley bold)
          600: '#059669',   // Deep jade
          700: '#047857',   // Forest depth
          800: '#065f46',   // Ancient stone
          900: '#064e3b',   // Taonga depth
          DEFAULT: '#059669',
          light: '#d1fae5',
          glow: 'rgba(27, 127, 90, 0.15)'
        },
        
        // MOANA (Ocean) - Journey & Discovery Color
        moana: {
          50: '#f0f9ff',    // Dawn reflection
          100: '#e0f2fe',   // Morning tide
          200: '#bae6fd',   // Shallow water
          300: '#7dd3fc',   // Bright ocean
          400: '#38bdf8',   // Deep blue
          500: '#006994',   // Ocean depth (Kehinde Wiley royal)
          600: '#0284c7',   // Kahurangi blue
          700: '#0369a1',   // Deep current
          800: '#075985',   // Abyss
          900: '#0c4a6e',   // Tangaroa's realm
          DEFAULT: '#0284c7',
          light: '#e0f2fe',
          royal: '#003366'  // Kehinde Wiley royal blue
        },
        
        // KŌWHAI (Golden Yellow) - Growth & Wisdom Color
        kowhai: {
          50: '#fffbeb',    // First light
          100: '#fef3c7',   // Sunrise
          200: '#fde68a',   // Morning glow
          300: '#fcd34d',   // Warm gold
          400: '#fbbf24',   // Bright bloom
          500: '#F5D915',   // Kōwhai flower (Kehinde Wiley gold)
          600: '#f59e0b',   // Rich honey
          700: '#d97706',   // Sunset
          800: '#b45309',   // Amber depth
          900: '#92400e',   // Burnt gold
          DEFAULT: '#fbbf24',
          light: '#fef3c7',
          pure: '#FFD700'   // Kehinde Wiley pure gold
        },
        
        // WHENUA (Earth) - Foundation & Stability Color
        whenua: {
          50: '#fafaf9',    // Pale earth
          100: '#f5f1eb',   // Light soil
          200: '#e7e5e4',   // Sand
          300: '#d6d3d1',   // Clay
          400: '#a8a29e',   // Rich earth
          500: '#78716c',   // Deep soil
          600: '#6B4E3D',   // Whenua (Kehinde Wiley earth brown)
          700: '#57534e',   // Dark earth
          800: '#44403c',   // Ancient soil
          900: '#292524',   // Primordial earth
          DEFAULT: '#f5f1eb',
          rich: '#8B4513'   // Kauri brown
        },
        
        // KUMARA (Orange/Red) - Vitality & Passion Color
        kumara: {
          50: '#fff7ed',    // Pale skin
          100: '#ffedd5',   // Light flesh
          200: '#fed7aa',   // Warm orange
          300: '#fdba74',   // Bright kumara
          400: '#fb923c',   // Vibrant orange
          500: '#FF6B35',   // Kumara red (Kehinde Wiley)
          600: '#ea580c',   // Deep orange
          700: '#c2410c',   // Fire orange
          800: '#9a3412',   // Burnt orange
          900: '#7c2d12',   // Ember
          DEFAULT: '#fb923c',
          fire: '#FF4500'   // Ahi (fire)
        },
        
        // CULTURAL SEMANTIC COLORS
        cultural: {
          primary: '#059669',      // Pounamu green
          secondary: '#0284c7',    // Kahurangi blue
          accent: '#fbbf24',       // Kōwhai gold
          background: '#f5f1eb',   // Whenua light
          highlight: '#e0f2fe',    // Ocean light
          regal: '#003366',        // Royal blue (Kehinde Wiley)
          bold: '#FFD700',         // Pure gold (Kehinde Wiley)
          wisdom: '#4B0082'        // Deep purple (Kehinde Wiley)
        }
      },
      
      // ===================================================================
      // TYPOGRAPHY - Regal + Modern + Cultural
      // ===================================================================
      fontFamily: {
        // Kehinde Wiley Display (Regal headlines)
        display: ['Playfair Display', 'Georgia', 'Times New Roman', 'serif'],
        // Silicon Valley Modern (Body text)
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        // Cultural Authenticity (Te Reo Māori)
        cultural: ['Noto Sans Maori', 'Inter', 'sans-serif'],
        // Cultural Accents (Quotes & poetry)
        accent: ['Crimson Text', 'Georgia', 'serif'],
        // Code (if needed)
        mono: ['SF Mono', 'Monaco', 'Consolas', 'monospace']
      },
      
      // ===================================================================
      // TYPOGRAPHY SCALE - Kehinde Wiley Bold Presence
      // ===================================================================
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '1' }],
        '6xl': ['3.75rem', { lineHeight: '1' }],
        '7xl': ['4.5rem', { lineHeight: '1' }],      // Kehinde Wiley hero
        '8xl': ['6rem', { lineHeight: '1' }],
        '9xl': ['8rem', { lineHeight: '1' }],
        // Cultural-specific sizes
        'wiley-hero': ['clamp(3rem, 8vw, 4.5rem)', { lineHeight: '1.1' }],
        'wiley-title': ['clamp(2rem, 5vw, 3.5rem)', { lineHeight: '1.2' }],
        'cultural-quote': ['clamp(1.25rem, 3vw, 1.5rem)', { lineHeight: '1.4' }]
      },
      
      // ===================================================================
      // SPACING - Generous & Intentional (Kehinde Wiley)
      // ===================================================================
      spacing: {
        'px': '1px',
        '0': '0',
        '0.5': '0.125rem',
        '1': '0.25rem',
        '1.5': '0.375rem',
        '2': '0.5rem',
        '2.5': '0.625rem',
        '3': '0.75rem',
        '3.5': '0.875rem',
        '4': '1rem',
        '5': '1.25rem',
        '6': '1.5rem',
        '7': '1.75rem',
        '8': '2rem',
        '9': '2.25rem',
        '10': '2.5rem',
        '11': '2.75rem',
        '12': '3rem',
        '14': '3.5rem',
        '16': '4rem',
        '20': '5rem',
        '24': '6rem',        // Kehinde Wiley generous spacing
        '28': '7rem',
        '32': '8rem',
        '36': '9rem',
        '40': '10rem',       // Kehinde Wiley dramatic spacing
        '44': '11rem',
        '48': '12rem',
        '52': '13rem',
        '56': '14rem',
        '60': '15rem',
        '64': '16rem',
        '72': '18rem',
        '80': '20rem',
        '96': '24rem'
      },
      
      // ===================================================================
      // BORDER RADIUS - Organic Forms + Picture Frames
      // ===================================================================
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',
        'DEFAULT': '0.25rem',
        'md': '0.375rem',
        'lg': '0.5rem',
        'xl': '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
        'full': '9999px',
        // Kehinde Wiley inspired
        'organic': '1.5rem 0.5rem 1.5rem 0.5rem',
        'frame': '20px',        // Picture frame aesthetic
        'cultural': '12px'      // Natural flowing
      },
      
      // ===================================================================
      // BOX SHADOW - Depth, Elevation & Cultural Glow
      // ===================================================================
      boxShadow: {
        'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'DEFAULT': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        'inner': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
        'none': 'none',
        // Cultural & Artistic Shadows
        'cultural': '0 4px 6px -1px rgba(5, 150, 105, 0.1), 0 2px 4px -1px rgba(5, 150, 105, 0.06)',
        'cultural-lg': '0 10px 15px -3px rgba(5, 150, 105, 0.1), 0 4px 6px -2px rgba(5, 150, 105, 0.05)',
        'cultural-xl': '0 20px 40px -12px rgba(27, 127, 90, 0.3)',
        'pounamu-glow': '0 0 20px rgba(27, 127, 90, 0.3), 0 0 40px rgba(27, 127, 90, 0.1)',
        'kowhai-glow': '0 0 20px rgba(241, 143, 1, 0.3), 0 0 40px rgba(241, 143, 1, 0.1)',
        'wiley-gallery': '0 10px 30px rgba(0,0,0,0.1), 0 1px 8px rgba(0,0,0,0.1)',
        'wiley-lifted': '0 20px 40px rgba(0,0,0,0.15), 0 1px 8px rgba(0,0,0,0.1)',
        'wiley-cultural': '0 15px 35px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.8)',
        'glass': '0 8px 32px rgba(0, 0, 0, 0.1)',
        'glass-lg': '0 20px 60px rgba(0, 0, 0, 0.15)'
      },
      
      // ===================================================================
      // ANIMATIONS - Cultural Motion Language
      // ===================================================================
      animation: {
        // Standard animations
        'spin': 'spin 1s linear infinite',
        'ping': 'ping 1s cubic-bezier(0, 0, 0.2, 1) infinite',
        'pulse': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'bounce': 'bounce 1s infinite',
        
        // Cultural animations (Framer Motion inspired)
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.4s ease-out',
        'slide-down': 'slideDown 0.4s ease-out',
        'slide-left': 'slideLeft 0.5s ease-out',
        'slide-right': 'slideRight 0.5s ease-out',
        
        // Koru (unfurling fern) animations
        'koru-unfurl': 'koruUnfurl 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)',
        'koru-spiral': 'koruSpiral 20s linear infinite',
        
        // Whakapapa (genealogical) animations
        'whakapapa-expand': 'whakapapaExpand 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)',
        'whakapapa-cascade': 'whakapapaCascade 1s ease-out',
        
        // Pōwhiri (welcome) animations
        'powhiri-enter': 'powhiriEnter 1.5s ease-out',
        'powhiri-reveal': 'powhiriReveal 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)',
        
        // Hariru (handshake/interaction) animations
        'hariru-hover': 'hariruHover 0.3s ease-out',
        'hariru-press': 'hariruPress 0.2s ease-in-out',
        
        // Shimmer & glow effects
        'shimmer': 'shimmer 3s linear infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite',
        'cultural-pulse': 'culturalPulse 3s ease-in-out infinite'
      },
      
      // ===================================================================
      // KEYFRAMES - Cultural Motion Patterns
      // ===================================================================
      keyframes: {
        // Standard
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        },
        slideUp: {
          '0%': { transform: 'translateY(30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        slideDown: {
          '0%': { transform: 'translateY(-30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        slideLeft: {
          '0%': { transform: 'translateX(30px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideRight: {
          '0%': { transform: 'translateX(-30px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        
        // Koru animations (unfurling fern frond)
        koruUnfurl: {
          '0%': { 
            transform: 'scale(0.1) rotate(-180deg)', 
            opacity: '0',
            transformOrigin: 'center center'
          },
          '60%': { transform: 'scale(1.1) rotate(10deg)', opacity: '1' },
          '100%': { transform: 'scale(1) rotate(0deg)', opacity: '1' }
        },
        koruSpiral: {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' }
        },
        
        // Whakapapa animations (genealogical revelation)
        whakapapaExpand: {
          '0%': { 
            transform: 'scale(0.8)', 
            opacity: '0',
            filter: 'blur(10px)'
          },
          '100%': { 
            transform: 'scale(1)', 
            opacity: '1',
            filter: 'blur(0px)'
          }
        },
        whakapapaCascade: {
          '0%': { transform: 'translateY(-100%)', opacity: '0' },
          '20%': { opacity: '1' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        
        // Pōwhiri animations (welcoming ceremony)
        powhiriEnter: {
          '0%': { 
            transform: 'scale(0.9) translateY(50px)', 
            opacity: '0' 
          },
          '50%': { 
            transform: 'scale(1.02) translateY(-5px)' 
          },
          '100%': { 
            transform: 'scale(1) translateY(0)', 
            opacity: '1' 
          }
        },
        powhiriReveal: {
          '0%': { 
            transform: 'translateX(-100%) skew(10deg)', 
            opacity: '0' 
          },
          '60%': { transform: 'translateX(10px) skew(-5deg)' },
          '100%': { 
            transform: 'translateX(0) skew(0deg)', 
            opacity: '1' 
          }
        },
        
        // Hariru animations (handshake/hover)
        hariruHover: {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.05)' },
          '100%': { transform: 'scale(1.02)' }
        },
        hariruPress: {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(0.95)' },
          '100%': { transform: 'scale(1)' }
        },
        
        // Shimmer & glow (Kehinde Wiley richness)
        shimmer: {
          '0%': { backgroundPosition: '-200% center' },
          '100%': { backgroundPosition: '200% center' }
        },
        glowPulse: {
          '0%, 100%': { 
            boxShadow: '0 0 20px rgba(255, 215, 0, 0.3)',
            filter: 'brightness(1)'
          },
          '50%': { 
            boxShadow: '0 0 40px rgba(255, 215, 0, 0.6)',
            filter: 'brightness(1.1)'
          }
        },
        culturalPulse: {
          '0%, 100%': { 
            boxShadow: '0 0 20px rgba(27, 127, 90, 0.2)' 
          },
          '50%': { 
            boxShadow: '0 0 40px rgba(27, 127, 90, 0.4)' 
          }
        }
      },
      
      // ===================================================================
      // BACKGROUND IMAGES - Cultural Pattern Library
      // ===================================================================
      backgroundImage: {
        // Gradients - Rich & Sophisticated
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        
        // Cultural gradients
        'gradient-pounamu': 'linear-gradient(135deg, #1B7F5A 0%, #059669 100%)',
        'gradient-moana': 'linear-gradient(135deg, #006994 0%, #0284c7 100%)',
        'gradient-kowhai': 'linear-gradient(135deg, #F5D915 0%, #fbbf24 100%)',
        'gradient-cultural': 'linear-gradient(135deg, #059669 0%, #fbbf24 50%, #0284c7 100%)',
        'gradient-hero': 'linear-gradient(135deg, #1B4332 0%, #1B7F5A 25%, #006994 100%)',
        
        // Kehinde Wiley ornate gradients
        'gradient-wiley-royal': 'linear-gradient(135deg, #003366 0%, #006A4E 100%)',
        'gradient-wiley-regal': 'linear-gradient(135deg, #4B0082 0%, #FFD700 100%)',
        'gradient-wiley-ornate': 'linear-gradient(135deg, #FFFFF0 0%, rgba(255, 255, 240, 0.95) 100%)',
        
        // Glass morphism
        'glass': 'linear-gradient(145deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%)',
        'glass-dark': 'linear-gradient(145deg, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.05) 100%)',
        
        // Pattern overlays (performance-optimized SVG data URIs)
        'pattern-koru': 'url("data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M30 10 Q 40 20 40 30 Q 40 40 30 40 Q 20 40 20 30 Q 20 25 23 22\' stroke=\'rgba(26,77,46,0.08)\' fill=\'none\' stroke-width=\'1.5\'/%3E%3C/svg%3E")',
        'pattern-taniko': 'url("data:image/svg+xml,%3Csvg width=\'40\' height=\'40\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M0 20 L10 10 L20 20 L10 30 Z M20 20 L30 10 L40 20 L30 30 Z\' fill=\'rgba(26,77,46,0.06)\'/%3E%3C/svg%3E")',
        'pattern-whakairo': 'url("data:image/svg+xml,%3Csvg width=\'80\' height=\'80\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M40 10 Q 50 20 50 30 Q 50 40 40 50 Q 30 40 30 30 Q 30 20 40 10\' stroke=\'rgba(212,165,116,0.1)\' fill=\'none\' stroke-width=\'2\'/%3E%3Ccircle cx=\'40\' cy=\'30\' r=\'8\' fill=\'rgba(212,165,116,0.06)\'/%3E%3C/svg%3E")'
      },
      
      // ===================================================================
      // BACKDROP BLUR - Glass Morphism Effects
      // ===================================================================
      backdropBlur: {
        xs: '2px',
        sm: '4px',
        DEFAULT: '8px',
        md: '12px',
        lg: '16px',
        xl: '24px',
        '2xl': '40px',
        '3xl': '64px'
      },
      
      // ===================================================================
      // TRANSITIONS - Smooth Cultural Motion
      // ===================================================================
      transitionDuration: {
        '75': '75ms',
        '100': '100ms',
        '150': '150ms',
        '200': '200ms',
        '300': '300ms',
        '500': '500ms',
        '700': '700ms',
        '1000': '1000ms',
        'fast': '150ms',
        'normal': '300ms',
        'slow': '500ms',
        'slower': '750ms',
        'cultural': '400ms'  // Perfect for cultural animations
      },
      
      transitionTimingFunction: {
        'linear': 'linear',
        'in': 'cubic-bezier(0.4, 0, 1, 1)',
        'out': 'cubic-bezier(0, 0, 0.2, 1)',
        'in-out': 'cubic-bezier(0.4, 0, 0.2, 1)',
        // Cultural easing functions
        'whakapapa': 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',  // Genealogical flow
        'cultural': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)', // Cultural bounce
        'hariru': 'cubic-bezier(0.34, 1.56, 0.64, 1)',        // Handshake spring
        'powhiri': 'cubic-bezier(0.22, 0.61, 0.36, 1)'        // Welcome ceremony
      },
      
      // ===================================================================
      // Z-INDEX - Layer Management
      // ===================================================================
      zIndex: {
        '0': '0',
        '10': '10',
        '20': '20',
        '30': '30',
        '40': '40',
        '50': '50',
        'auto': 'auto',
        'dropdown': '1000',
        'sticky': '1020',
        'banner': '1030',
        'fixed': '1030',
        'modal-backdrop': '1040',
        'modal': '1050',
        'popover': '1060',
        'tooltip': '1070',
        'toast': '1080'
      }
    }
  },
  
  // ===================================================================
  // PLUGINS - Custom Utilities & Components
  // ===================================================================
  plugins: [
    // A4 Print Optimization
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
    },
    
    // Cultural Pattern Utilities
    function({ addComponents }) {
      const culturalComponents = {
        // Kehinde Wiley inspired components
        '.wiley-hero': {
          fontFamily: 'Playfair Display, serif',
          fontSize: 'clamp(3rem, 8vw, 4.5rem)',
          fontWeight: '900',
          lineHeight: '1.1',
          letterSpacing: '-0.02em',
          textShadow: '2px 2px 4px rgba(0,0,0,0.3)'
        },
        '.wiley-ornate-border': {
          border: '3px solid #FFD700',
          borderRadius: '20px',
          padding: '2rem',
          background: 'linear-gradient(135deg, #FFFFF0 0%, rgba(255, 255, 240, 0.95) 100%)',
          position: 'relative',
          boxShadow: '0 10px 30px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.8)'
        },
        
        // Cultural components
        '.cultural-opening': {
          background: 'linear-gradient(135deg, #e0f2fe, #f5f1eb)',
          padding: '2rem',
          borderRadius: '0.75rem',
          marginTop: '1rem',
          marginBottom: '1rem',
          borderLeft: '4px solid #059669',
          position: 'relative',
          overflow: 'hidden'
        },
        '.whakatauki': {
          fontFamily: 'Noto Sans Maori, Inter, sans-serif',
          fontSize: '1.25rem',
          fontStyle: 'italic',
          color: '#059669',
          margin: '1rem 0',
          lineHeight: '1.4'
        },
        
        // Glass morphism cards
        '.glass-card': {
          background: 'rgba(255, 255, 255, 0.95)',
          backdropFilter: 'blur(10px)',
          borderRadius: '24px',
          border: '1px solid rgba(255, 255, 255, 0.6)',
          boxShadow: '0 20px 60px rgba(26, 77, 46, 0.08)',
          padding: '3rem'
        },
        
        // Cultural gradient text
        '.gradient-text-cultural': {
          backgroundImage: 'linear-gradient(135deg, #059669 0%, #fbbf24 100%)',
          WebkitBackgroundClip: 'text',
          backgroundClip: 'text',
          WebkitTextFillColor: 'transparent'
        }
      }
      addComponents(culturalComponents)
    },
    
    // Cultural Animation Utilities
    function({ addUtilities }) {
      const animationUtilities = {
        '.animate-on-scroll': {
          opacity: '0',
          transform: 'translateY(30px)',
          transition: 'all 0.6s cubic-bezier(0.22, 0.61, 0.36, 1)'
        },
        '.animate-on-scroll.is-visible': {
          opacity: '1',
          transform: 'translateY(0)'
        },
        '.hover-lift': {
          transition: 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease',
          '&:hover': {
            transform: 'translateY(-8px)',
            boxShadow: '0 20px 40px rgba(0,0,0,0.15)'
          }
        },
        '.hover-glow': {
          transition: 'box-shadow 0.3s ease',
          '&:hover': {
            boxShadow: '0 0 30px rgba(27, 127, 90, 0.4)'
          }
        }
      }
      addUtilities(animationUtilities)
    }
  ]
}

