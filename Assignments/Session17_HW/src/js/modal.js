const $ = (selector) => document.querySelector(selector);
const body = $("body");
const modal = $(".modal-container");

const openModal = () => {
    $(".modal-container").classList.add("open");
    body.style.overflow = "hidden";
};

const closeModal = () => {
    $(".modal-container").classList.remove("open");
    body.style.overflow = "auto";
};

export { openModal, closeModal };
