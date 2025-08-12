document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".menu");
  const navList = document.querySelector("nav ul");

  menuButton.addEventListener("click", () => {
    navList.classList.toggle("hide");
  });

  //Modal
  const modal = document.getElementById("modal");
  const modalImg = document.getElementById("modal-img");
  const closeModal = document.querySelector(".close-viewer");
  const galleryImages = document.querySelectorAll(".gallery img");

  galleryImages.forEach((img) => {
    img.addEventListener("click", () => {
      modal.style.display = "block";
      modalImg.src = img.src;
      modalImg.alt = img.alt;
    });
  });

  closeModal.addEventListener("click", () => {
    modal.style.display = "none";
  });
});
