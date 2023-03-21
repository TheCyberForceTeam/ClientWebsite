const showPasswordCheckbox = document.getElementById("show-password");
const passwordInput = document.getElementById("password");
const StaffAccess = document.getElementById("staff");

showPasswordCheckbox.addEventListener("change", function() {
    if (this.checked) {
        passwordInput.setAttribute("type", "text");
    } else {
        passwordInput.setAttribute("type", "password");
    }
});

window.onload = function() {
    const consentPopup = document.getElementById("cookie-consent");
    const acceptBtn = document.getElementById("accept-cookies");
    const loginButton = document.getElementById("login-button");
    const loginContainer = document.getElementById("login-container");

    StaffAccess.style.display = "none";

    if (!localStorage.getItem("cookiesAccepted")) {
        consentPopup.style.display = "block";
    }

    // check if the user is already logged in
    const username = sessionStorage.getItem('username');
    if (username) {
        // disable the login button and replace its text with the username
        loginButton.disabled = true;
        loginButton.textContent = username;
    }

    acceptBtn.addEventListener("click", function() {
        localStorage.setItem("cookiesAccepted", true);
        consentPopup.style.display = "none";
    });

    loginButton.addEventListener("click", function() {
        const form = document.querySelector("form");
        form.style.opacity = 1;
      });
      
}