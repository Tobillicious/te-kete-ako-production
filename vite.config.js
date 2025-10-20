import { resolve } from 'path';
import { defineConfig } from 'vite';
import { glob } from 'glob';

export default defineConfig({
  root: resolve(__dirname, 'public'),
  build: {
    outDir: resolve(__dirname, 'dist'),
    rollupOptions: {
      input: {
        // Core pages
        main: resolve(__dirname, 'public/index.html'),
        auth: resolve(__dirname, 'public/auth-test.html'),

        // Enhanced pages with world-class features
        units: resolve(__dirname, 'public/units/index.html'),
        lessons: resolve(__dirname, 'public/lessons.html'),
        handouts: resolve(__dirname, 'public/handouts.html'),
        'teacher-dashboard': resolve(__dirname, 'public/teachers/dashboard.html'),

        // AI-Generated resources
        'generated-resources': resolve(__dirname, 'public/generated-resources-alpha/index.html'),
        'generated-handouts': resolve(__dirname, 'public/generated-resources-alpha/handouts/index.html'),
        'generated-lessons': resolve(__dirname, 'public/generated-resources-alpha/lessons/index.html'),

        // Additional enhanced pages
        'curriculum-index': resolve(__dirname, 'public/curriculum-index.html'),
        'resource-hub': resolve(__dirname, 'public/resource-hub.html'),
        'site-map': resolve(__dirname, 'public/site-map.html'),

        // Include ALL HTML files for deployment
        ...Object.fromEntries(
          glob.sync('public/**/*.html').map(file => [
            file.replace('public/', '').replace('.html', ''),
            resolve(__dirname, file)
          ])
        ),
      },
    },
  },
  server: {
    port: 3000,
    open: true,
  },
  preview: {
    port: 4173,
  },
});
