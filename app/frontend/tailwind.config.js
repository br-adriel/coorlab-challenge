/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.vue'],
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
