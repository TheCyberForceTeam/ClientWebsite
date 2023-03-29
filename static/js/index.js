// Wait for the DOM to load before executing the code inside the function
document.addEventListener('DOMContentLoaded', function() {

    // Define variables to reference DOM elements
    //Cookie consent popup
    const consentPopup = document.getElementById("cookie-consent");
    const acceptBtn = document.getElementById("accept-cookies");
    //Login form
    const username = sessionStorage.getItem("username");
    const password = sessionStorage.getItem("password");
    const loginButton = document.getElementById("Login-button");
    const passwordInput = document.getElementById("login-password");
    const showPasswordLogin = document.getElementById("show-password-login");
    const loginContainer = document.querySelector(".login-container");
    //Signup form
    const signupButton = document.getElementById("signup-button");
    const signupForm = document.querySelector(".signup-form");
    const showPasswordSignup = document.getElementById("show-password-signup");
    //Staff access button
    const staffAccess = document.getElementById("Staff-button");
    //Close buttons
    const closeBtnLogin = document.getElementById("close-button-login");
    const closeBtnSignup = document.getElementById("close-button-signup");
    const closeBtnEmailUs = document.getElementById("close-button-emailUS");
    //Email us button
    const emailUSbutton = document.getElementById("email-form");
    const emailform = document.querySelector(".emailUS-form");
    
    //--------------------------------------------------------------------------------
    // Define a function to close a modal by setting opacity and pointerEvents to 0 and none respectively
    const closeModal = (modal) => {
      modal.style.display = "none";
      modal.style.pointerEvents = "none";
    };
    
    //--------------------------------------------------------------------------------
    // Add an event listener to the accept cookies button to save cookiesAccepted in local storage and close the consent popup
    acceptBtn.addEventListener("click", () => {
      localStorage.setItem("cookiesAccepted", true);
      consentPopup.style.display = "none";
    });

    //--------------------------------------------------------------------------------
    // If cookies have not been accepted, show the cookie consent popup
    if (!localStorage.getItem("cookiesAccepted")) {
      consentPopup.style.display = "block";
    }
    //--------------------------------------------------------------------------------
    // Hide the staff access button by default
    staffAccess.style.display = "none";
    //--------------------------------------------------------------------------------
    // If a username is saved in session storage, disable the login button and display the username
    if (username) {
        loginButton.disabled = true;
        loginButton.textContent = username;
        loginButton.innerHTML = username;
        loginButton.innerText = username;
      }
    //--------------------------------------------------------------------------------
    // If the user is logged in, show the staff access button
    if (username === "staff") {
        staffAccess.style.display = "block";
    }

    //--------------------------------------------------------------------------------
    // If the innerhtml of the login button is "Staff" or "Admin", set the staffAccess.style.display = "block"
    if (loginButton.innerHTML === "Staff" || loginButton.innerHTML === "Admin") {
        staffAccess.style.display = "block";
    }

    //--------------------------------------------------------------------------------
    // Add an event listener to the staff access button to redirect the browser to the staff access page
    staffAccess.addEventListener("click", () => {
        window.location.href = "/staff";
    });
  
    //--------------------------------------------------------------------------------
    // Add an event listener to the show password checkbox to show/hide the password IN THE LOGIN FORM
    showPasswordLogin.addEventListener("change", () => {
        passwordInput.type = showPasswordLogin.checked ? "text" : "password";
    });
    // Add an event listener to the show password checkbox to show/hide the password IN THE SIGNUP FORM
    showPasswordSignup.addEventListener("change", () => {
        passwordInput.type = showPasswordSignup.checked ? "text" : "password";
      });
    
    //--------------------------------------------------------------------------------
    // Add an event listener to the login button to show the login form on click
    loginButton.addEventListener("click", () => {
      const form = document.querySelector("form");
      loginContainer.style.display = "block";
      loginContainer.style.opacity = "1";
      signupForm.style.pointerEvents = "auto";
    });
  
    //--------------------------------------------------------------------------------
    // Add an event listener to the signup button to close the login container and show the signup form on click
    signupButton.addEventListener("click", () => {
      closeModal(loginContainer);
      signupForm.style.display = "block";
      signupForm.style.pointerEvents = "auto";
    });

    //--------------------------------------------------------------------------------
    // Add an event listener to the email us button to show the email form
    emailUSbutton.addEventListener("click", () => {
        emailform.style.display = "block";
        emailform.style.pointerEvents = "auto";
    });
  
    //--------------------------------------------------------------------------------
    // Add event listeners to all close buttons to close their parent modals when clicked
    //--------------------------------------------------------------------------------
    // Close the login container
    closeBtnLogin.addEventListener("click", () => {
        closeModal(loginContainer);
        loginContainer.style.opacity = "0";
        loginContainer.style.display = "none";
        loginContainer.style.pointerEvents = "none";
    });
    //--------------------------------------------------------------------------------
    // Close the signup form
    closeBtnSignup.addEventListener("click", () => {
        closeModal(signupForm);
        signupForm.style.opacity = "0";
        signupForm.style.display = "none";
        signupForm.style.pointerEvents = "none";
    });
    //--------------------------------------------------------------------------------
    // Close the email form
    closeBtnEmailUs.addEventListener("click", () => {
        closeModal(emailform);
        emailform.style.opacity = "0";
        emailform.style.display = "none";
        emailform.style.pointerEvents = "none";
    });
    //--------------------------------------------------------------------------------
  });
  