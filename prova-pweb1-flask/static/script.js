function confirmDelete() {
    var result = confirm("Tem certeza que deseja excluir este pet?");
    if (result) {
      return true;
    } else {
      return false;
    }
  }
  