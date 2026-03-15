// FAQ icons
const faqItems = document.querySelectorAll(".faq_item");

faqItems.forEach((item) => {
    const question = item.querySelector(".faq_question");

    question.addEventListener("click", () => {
        item.classList.toggle("active");
    });
});

// Show Password
const passwordInput = document.querySelector('input[type="password"]');
const showPassword = document.getElementById("showPassword");
showPassword.addEventListener("change", function () {
    if (this.checked) {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
});