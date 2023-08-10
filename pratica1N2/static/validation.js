document.addEventListener("DOMContentLoaded", function () {
  const usernameInput = document.querySelector('input[name="username"]');
  const passwordInput = document.querySelector('input[name="password"]');
  const registerForm = document.querySelector("form");

  registerForm.addEventListener("submit", function (event) {
    if (!validateUsername(usernameInput.value)) {
      event.preventDefault();
      alert("Invalid username format. Please use only letters.");
    }

    if (!validatePassword(passwordInput.value)) {
      event.preventDefault();
      alert("Password must be at least 6 characters long.");
    }
  });

  function validateUsername(username) {
    return /^[A-Za-z]+$/.test(username);
  }

  function validatePassword(password) {
    return password.length >= 6;
  }
});
