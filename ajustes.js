// Cambiar idioma
document.querySelector("select").addEventListener("change", (e) => {
  alert("Idioma cambiado a: " + e.target.value);
});

// Confirmar cierre de sesión
document.querySelector(".btn-cerrar").addEventListener("click", () => {
  if (confirm("¿Seguro que quieres cerrar sesión?")) {
    alert("Sesión cerrada ✅");
  }
});
