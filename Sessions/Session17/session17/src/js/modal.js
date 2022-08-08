// 📁 modal.js
// 모달 관련 함수들을 정의하고 내보낸다.
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
