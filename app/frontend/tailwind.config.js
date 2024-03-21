/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.vue',
    './vueform.config.js',
    './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/@vueform/vueform/themes/tailwind/**/*.js',
  ],
  theme: {
    fontFamily: {
      sans: ['Noto Sans', 'sans-serif'],
    },
    extend: {
      boxShadow: {
        deep: '0 0 8px rgba(0,0,0,0.8)',
      },
      colors: {
        primary: '#04A8B5',
        secondary: '#2B2F42',
        plain: {
          typography: '#515051',
          lighter: '#FFFFFF',
          medium: '#F9F8F9',
          darker: '#F4F3F4',
        },
      },
    },
  },
  plugins: [],
};
