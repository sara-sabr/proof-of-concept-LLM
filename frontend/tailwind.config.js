/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "gray-0": '#f7f7f7',
        "gray-20": "#f2f3ed",
        "gray-50": "#8f908b",
        "gray-100": "#6f7872",
        "gray-500": "#060606",
        "primary-100": "#bfd58d",
        "primary-200": "#7cab74",
        "primary-300": "#6da670",
        "primary-500": "#507754",
        "secondary-400": "#e8db8c",
        "secondary-500": "#a6966d",
      },
      backgroundImage: (theme) => ({
      }),
      fontFamily: {
        dmsans: ["DM Sans", "sans-serif"],
        montserrat: ["Montserrat", "sans-serif"],
      },
      content: {
      },
    },
    screens: {
      xs: "480px",
      sm: "768px",
      md: "1060px",
    },
  },
  plugins: [],
};