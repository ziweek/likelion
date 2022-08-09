const $ = (selector) => document.querySelector(selector);

import { openModal, closeModal } from "./modal.js";
// import { setCookie, getCookie } from "./cookie.js";


function App() {
    this.init = () => {
        if (getCookie("modalClose") === "true") {
            closeModal();
            return;
        }
        openModal();
    };
}

const app = new App();
app.init();

$(".modal-container").addEventListener("click", (event) => {
    if (event.target === $(".modal-container")) {
        closeModal();
    }
});

$(".modal-stop-button").addEventListener("click", () => {
    setCookie("modalClose", "true", 1);
    closeModal();
});

$(".modal-close").addEventListener("click", () => {
    closeModal();
});

$(".btn-open-modal").addEventListener("click", () => {
    openModal();
});


document.querySelector(".modal-close").addEventListener("click", () => {
    closeModal();
});