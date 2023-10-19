function toggleDropdown() {
  const dropdown = document.querySelector('.dropdown-content');
  const overlay = document.querySelector('.overlay');

  // Check transform property to determine dropdown's visibility
  if (window.getComputedStyle(dropdown).transform === "none" || window.getComputedStyle(dropdown).transform === "matrix(1, 0, 0, 1, 0, 0)") { // Matrix representation of translateX(0%)
      dropdown.style.transform = 'translateX(100%)';
      setTimeout(() => overlay.style.opacity = '0', 100);
      setTimeout(() => {
          overlay.style.display = 'none';
      }, 300); // Hide overlay after the slide and fade out
  } else {
      dropdown.style.transform = 'translateX(0%)'; // Slide the dropdown in
      overlay.style.display = 'block';
      setTimeout(() => overlay.style.opacity = '1', 100);
  }
}

function initializeCarousel(carouselElement) {
  const carousel = carouselElement.querySelector('.carousel-inner');
  const nextBtn = carouselElement.querySelector('.next-btn');
  const prevBtn = carouselElement.querySelector('.prev-btn');

  let currentIndex = 0;

  nextBtn.addEventListener('click', function() {
    currentIndex += 100;
    if (currentIndex >= carousel.children.length * 100) {
      currentIndex = 0;
    }
    carousel.style.transform = `translateX(-${currentIndex}%)`;
  });

  prevBtn.addEventListener('click', function() {
    currentIndex -= 100;
    if (currentIndex < 0) {
      currentIndex = (carousel.children.length - 1) * 100;
    }
    carousel.style.transform = `translateX(-${currentIndex}%)`;
  });
}

// Initialize both carousels
const carousel1 = document.querySelector('.carousel-1');
initializeCarousel(carousel1);

const carousel2 = document.querySelector('.carousel-2');
initializeCarousel(carousel2);

