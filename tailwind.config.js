/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //template from project level
    "./**/templates/**/*.html", //template from app level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

