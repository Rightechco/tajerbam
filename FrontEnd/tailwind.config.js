/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0ea5e9',
      },
      fontFamily: {
        // فونت وزیرمتن به عنوان اولویت اول قرار گرفت
        sans: ['Vazirmatn', 'Tahoma', 'Arial', 'sans-serif'], 
      }
    },
  },
  plugins: [],
}