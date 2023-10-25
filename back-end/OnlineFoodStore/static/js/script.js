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

function loginPopUp() {
  const loginPopUpForm = document.getElementById("login");
  const registerPopUpForm = document.getElementById("register");

  // Close the registration popup if it's open
  if (registerPopUpForm.style.display === "block") {
    registerPopUpForm.style.display = "none";
  }

  if (loginPopUpForm.style.display === "block") {
    loginPopUpForm.style.display = "none";
  } else {
    loginPopUpForm.style.display = "block";
  }
}

function registrationPopUp() {
  const loginPopUpForm = document.getElementById("login");
  const registerPopUpForm = document.getElementById("register");

  // Close the login popup if it's open
  if (loginPopUpForm.style.display === "block") {
    loginPopUpForm.style.display = "none";
  }

  if (registerPopUpForm.style.display === "block") {
    registerPopUpForm.style.display = "none";
  } else {
    registerPopUpForm.style.display = "block";
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


function changeQuantity(button, action) {
    var quantityElement = button.parentElement.querySelector('.quantity');
    var quantity = parseInt(quantityElement.innerText);

    if (action === 'increment') {
        quantity++;
    } else if (action === 'decrement' && quantity > 1) {
        quantity--;
    }

    quantityElement.innerText = quantity;
}
function resetQuantity(checkButton) {
    var quantityElement = checkButton.parentElement.querySelector('.quantity');
    quantityElement.innerText = '1';
}

document.getElementById('flip').addEventListener('change', function() {
  var backImage = document.querySelector('.back img');
  if (this.checked) {
    backImage.src = "{{ url_for('static', filename='Images/otherimage.png')}}";
  } else {
    backImage.src = "{{ url_for('static', filename='Images/loginimage.png')}}";
  }
});


