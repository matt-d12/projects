const modal = document.getElementById("modal");
const modalImage = document.getElementById("modal-image");
const modalText = document.getElementById("modal-text");
const closeBtn = document.querySelector(".close");

const projectDetails = {
  1: {
    image: "images/dicegame.png",
    text: "Detailed explanation of Project 1. Tech used, purpose, challenges, etc."
  },
  2: {
    image: "images/sql.png",
    text: "Detailed explanation of Project 2. Features, skills demonstrated, etc."
  }
};

document.querySelectorAll(".learn-more").forEach(button => {
  button.addEventListener("click", () => {
    const id = button.dataset.project;
    modalImage.src = projectDetails[id].image;
    modalText.textContent = projectDetails[id].text;
    modal.style.display = "flex";
  });
});

closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

window.addEventListener("click", e => {
  if (e.target === modal) modal.style.display = "none";
});