const images = [
  "/static/images/nail1.jpg",
  "/static/images/nail2.jpg",
  "/static/images/nail3.jpg",
  "/static/images/nail4.jpg",
];

let index = 0;

function changeBackground() {
  const carousel = document.querySelector(".carousel");
  carousel.style.backgroundImage = `url(${images[index]})`;

  index++;

  if (index >= images.length) {
    index = 0;
  }
}

setInterval(changeBackground, 4000);

changeBackground();
