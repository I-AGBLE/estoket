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