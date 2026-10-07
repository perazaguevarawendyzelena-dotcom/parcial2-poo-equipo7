// Muestra un mensaje cuando el usuario selecciona un material para préstamo.
const botones = document.querySelectorAll(".boton-prestamo");
const mensaje = document.getElementById("mensaje");

botones.forEach((boton) => {
  boton.addEventListener("click", () => {
    const titulo = boton.dataset.titulo;
    mensaje.textContent = `Has seleccionado "${titulo}" para préstamo.`;
    mensaje.classList.add("visible");
  });
});
