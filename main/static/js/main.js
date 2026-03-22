// FAQ icons
const faqItems = document.querySelectorAll(".faq_item");

faqItems.forEach((item) => {
    const question = item.querySelector(".faq_question");

    question.addEventListener("click", () => {
        item.classList.toggle("active");
    });
});

// Show Password
const password = document.getElementById("id_password");
const confirmPassword = document.getElementById("id_confirm_password");
const showPassword = document.getElementById("showPassword");

showPassword.addEventListener("change", function () {
    const type = this.checked ? "text" : "password";
    password.type = type;
    confirmPassword.type = type;
});

// Floating Field Account Login Display
const emailBtn = document.getElementById("emailSignIn");
const socialAuth = document.querySelector(".social_auth");
const accountAuth = document.querySelector(".account_auth");

emailBtn.addEventListener("click", function (e) {
    e.preventDefault(); // prevent page reload

    socialAuth.style.display = "none";
    accountAuth.style.display = "block";
});

// Back to Social Button
const backBtn = document.getElementById("backToSocial");
backBtn.addEventListener("click", function () {
    accountAuth.style.display = "none";
    socialAuth.style.display = "block";
});