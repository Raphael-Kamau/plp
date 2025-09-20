const heroSection = document.querySelector('.hero-section');
const images = [
  '/assets/beach.png',
  '/assets/mountain.png',
  '/assets/bay.png',
  '/assets/safari.png'
];

let currentIndex = 0;

function changeBackground() {
  heroSection.style.backgroundImage = `url(${images[currentIndex]})`;
  currentIndex = (currentIndex + 1) % images.length;
}

changeBackground();
setInterval(changeBackground, 5000);

// Navbar toggle
const toggleBtn = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

toggleBtn.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Contact form submission
const form = document.querySelector('.contact-form');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    name: form.name.value,
    email: form.email.value,
    message: form.message.value
  };

  try {
    form.querySelector('.submit-button').disabled = true;

    const res = await fetch('http://localhost:5000/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    form.querySelector('.submit-button').disabled = false;

    if (result.success) {
      alert('Message sent! Thank you for contacting us.');
      form.reset();
    } else {
      alert('Error: ' + (result.error || 'Try again later.'));
    }
  } catch (err) {
    alert('Network error. Please try again later.');
    form.querySelector('.submit-button').disabled = false;
  }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});