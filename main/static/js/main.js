// FAQ icons
const faqItems = document.querySelectorAll(".faq_item");

faqItems.forEach((item) => {
    const question = item.querySelector(".faq_question");

    question.addEventListener("click", () => {
        item.classList.toggle("active");
    });
});