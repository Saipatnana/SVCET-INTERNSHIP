function Strength(password) {
  let i = 0;
  if (password.length >= 7) {
    i++;
  }
  if (/[A-Z]/.test(password)) {
    i++;
  }
  if (/[a-z]/.test(password)) {
    i++;
  }
  if (/[0-9]/.test(password)) {
    i++;
  }
  if (/[^A-Za-z0-9]/.test(password)) {
    i++;
  }
  if (password.trim() === "") {
    return 0;
  }
  return i;
}

document.addEventListener("DOMContentLoaded", () => {
  let passwordInput = document.getElementById("your-password");
  let strengthMeter = document.getElementById("strengthMeter");
  let showButton = document.querySelector(".show");

  passwordInput.addEventListener("input", () => {
    console.log("key press");
    let password = passwordInput.value;
    let strength = Strength(password);

    strengthMeter.className = "strengthMeter"; // Reset classes
    if (strength <= 1) {
      strengthMeter.classList.add("weak");
    } else if (strength === 2) {
      strengthMeter.classList.add("moderate");
    } else {
      strengthMeter.classList.add("strong");
    }
  });

  showButton.onclick = function () {
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      showButton.textContent = "Hide";
    } else {
      passwordInput.type = "password";
      showButton.textContent = "Show";
    }
  };
});
