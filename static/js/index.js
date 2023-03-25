window.onload = function() {
    const consentPopup = document.getElementById("cookie-consent");
    const acceptBtn = document.getElementById("accept-cookies");

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
      
}

document.addEventListener("DOMContentLoaded", function() {
    const StaffAccess = document.getElementById("staff-button");
    StaffAccess.style.display = "none";
    const showPasswordCheckbox = document.querySelector("input[type=checkbox]");
    const passwordInput = document.getElementById("login-password");
    const loginButton = document.getElementById("login-button");
    const loginContainer = document.getElementById("login-container");
    const closeBtn = document.getElementById("close-button");
    const signupButton = document.getElementById("signup-button");
    const signupForm = document.querySelector("signup");

    closeBtn.addEventListener("click", function() {
        loginContainer.style.opacity = 0;
    });

    signupButton.addEventListener("click", function() {
        loginContainer.style.opacity = 0;
        signupForm.style.opacity = 1;
    });

    //closeSignup.addEventListener("click", function() { });




    showPasswordCheckbox.addEventListener("change", function() {
        if (this.checked) {
            passwordInput.setAttribute("type", "text");
        } else {
            passwordInput.setAttribute("type", "password");
        }
    });

    loginButton.addEventListener("click", function() {
        const form = document.querySelector("form");
        form.style.opacity = 1;
      });

  });