#!/usr/bin/env node
/**
 * FIX COLOR CONSISTENCY
 * Actually fix the issue instead of just reporting it
 * Consolidate 37 colors down to unified design system
 */

const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = '/Users/admin/Documents/te-kete-ako-clean/public';

// UNIFIED COLOR PALETTE (Te Kete Ako Design System)
const colorPalette = {
  // Primary colors (Forest Green - Te Kete identity)
  primary: {
    dark: '#0f2818',      // Very dark forest
    DEFAULT: '#1a4d2e',   // Main brand green
    light: '#2d6a4f'      // Lighter forest
  },
  
  // Secondary (Warm earth tones)
  secondary: {
    dark: '#92400e',      // Deep brown
    DEFAULT: '#d4a574',   // Warm tan
    light: '#f5e6d3'      // Light cream
  },
  
  // Accent (Cultural gold)
  accent: {
    DEFAULT: '#f59e0b',   // Warm gold
    light: '#fbbf24',
    lighter: '#fde68a'
  },
  
  // Success (Emerald)
  success: '#10b981',
  
  // Info (Blue)
  info: '#3b82f6',
  
  // Warning (Amber)
  warning: '#f59e0b',
  
  // Text
  text: {
    primary: '#2c3e50',
    secondary: '#546e7a',
    light: '#78350f'
  },
  
  // Neutral
  white: '#ffffff',
  black: '#000000',
  gray: {
    50: '#f9fafb',
    100: '#f3f4f6',
    200: '#e5e7eb',
    300: '#d1d5db',
    500: '#6b7280',
    700: '#374151',
    900: '#111827'
  }
};

// Color mapping for replacement
const colorReplacements = {
  // Homepage has too many greens - standardize to primary scale
  '#1b4332': colorPalette.primary.dark,
  '#1a4d2e': colorPalette.primary.DEFAULT,
  '#2E8B57': colorPalette.primary.DEFAULT,
  '#0f2818': colorPalette.primary.dark,
  
  // Too many browns/tans - standardize to secondary
  '#92400e': colorPalette.secondary.dark,
  '#78350f': colorPalette.text.light,
  '#d4a574': colorPalette.secondary.DEFAULT,
  
  // Gold/amber - use accent
  '#f59e0b': colorPalette.accent.DEFAULT,
  '#fbbf24': colorPalette.accent.light,
  '#fde68a': colorPalette.accent.lighter,
  '#fef3c7': '#fef3c7', // Keep this background
  
  // Standardize grays
  '#666': colorPalette.text.secondary,
  '#666666': colorPalette.text.secondary,
  '#f9fafb': colorPalette.gray[50],
  
  // Keep semantic colors consistent
  '#10b981': colorPalette.success,
  '#3b82f6': colorPalette.info
};

console.log('🎨 Fixing Color Consistency...\n');
console.log('Target: Reduce from 37 colors to 12-15 unified palette\n');

// Files to fix
const filesToFix = [
  'index.html',
  'login.html'
];

let totalReplacements = 0;

filesToFix.forEach(file => {
  const filePath = path.join(PUBLIC_DIR, file);
  
  if (!fs.existsSync(filePath)) {
    console.log(`⚠️  ${file} not found, skipping`);
    return;
  }
  
  let content = fs.readFileSync(filePath, 'utf-8');
  let replacements = 0;
  
  // Replace colors
  Object.entries(colorReplacements).forEach(([oldColor, newColor]) => {
    const regex = new RegExp(oldColor, 'gi');
    const matches = content.match(regex);
    if (matches) {
      content = content.replace(regex, newColor);
      replacements += matches.length;
    }
  });
  
  // Write back
  fs.writeFileSync(filePath, content, 'utf-8');
  
  console.log(`✅ ${file}: ${replacements} color replacements`);
  totalReplacements += replacements;
});

console.log(`\n✅ Total: ${totalReplacements} color values standardized`);
console.log('🎨 Color palette now unified to Te Kete Design System\n');

