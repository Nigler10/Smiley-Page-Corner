/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./products/templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light"], // pick one simple theme for now
  }
}
