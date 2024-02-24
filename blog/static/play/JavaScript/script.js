const openMenu = document.querySelector("#openMenu");
const closeMenu = document.querySelector("#closeMenu");
const navLinks = document.querySelector("#nav_links");

openMenu.addEventListener("click", () => {
  navLinks.style.top = "0";
});

closeMenu.addEventListener("click", () => {
  navLinks.style.top = "-400px";
});
