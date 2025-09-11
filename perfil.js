function cargarImagen(event) {
  let imgPreview = document.getElementById("previewImg");
  imgPreview.src = URL.createObjectURL(event.target.files[0]);
}