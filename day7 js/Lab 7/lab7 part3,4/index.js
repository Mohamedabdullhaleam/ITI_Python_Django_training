
document.addEventListener('DOMContentLoaded', function () {
const slides = document.getElementsByClassName('slide');
let currentSlide = 0;
let slideshowInterval;

function showSlide(index) {
    for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = i === index ? 'block' : 'none';
    }
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

function startSlideshow() {
    slideshowInterval = setInterval(nextSlide, 2000); // Change slide every 2 seconds
}

function stopSlideshow() {
    clearInterval(slideshowInterval);
}

showSlide(currentSlide);

document.getElementById('prevBtn').addEventListener('click', prevSlide);
document.getElementById('nextBtn').addEventListener('click', nextSlide);
document
    .getElementById('startBtn')
    .addEventListener('click', startSlideshow);
document
    .getElementById('stopBtn')
    .addEventListener('click', stopSlideshow);
});
//Task 4


