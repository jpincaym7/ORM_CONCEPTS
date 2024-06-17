/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,html}", // Rutas donde se utilizarán las clases de Tailwind CSS
  ],
  theme: {
    extend: {}, // Aquí puedes extender el tema predeterminado de Tailwind CSS si es necesario
  },
  plugins: [
    require('daisyui'), // Incluye el plugin de daisyui para utilizar sus componentes y utilidades
  ],
};

