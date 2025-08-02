/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        mahjong: {
          red: '#dc2626',
          green: '#059669',
          blue: '#2563eb',
          yellow: '#ca8a04',
          gray: '#6b7280',
        }
      },
      fontFamily: {
        'mahjong': ['Arial', 'sans-serif'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
} 