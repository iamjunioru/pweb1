function confirmDelete() {
  var result = confirm("Tem certeza que deseja excluir este pet?");
  if (result) {
    return true;
  } else {
    return false;
  }
}

function mostrarDataHora() {
  var dataHora = new Date();
  var data = dataHora.toLocaleDateString();
  var hora = dataHora.toLocaleTimeString();
  var elemento = document.getElementById("datetime");
  elemento.textContent = "Hoje é " + data + "\n São " + hora;
}

mostrarDataHora();