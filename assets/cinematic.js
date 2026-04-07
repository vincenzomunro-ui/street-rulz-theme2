// ===== STREET RULZ FOOTBALL — CINEMATIC V5 ANIMATIONS =====

// Fade-in on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe all fade-in elements
document.querySelectorAll('.fade-in').forEach(el => {
  observer.observe(el);
});

// Add fade-in class to cards and sections
document.querySelectorAll('.card, .round-card, .section').forEach(el => {
  el.classList.add('fade-in');
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Parallax scroll effect
window.addEventListener('scroll', () => {
  document.querySelectorAll('.parallax').forEach(parallax => {
    let scrollPosition = window.pageYOffset;
    let elementPosition = parallax.offsetTop;
    let windowHeight = window.innerHeight;
    
    if (scrollPosition + windowHeight > elementPosition) {
      parallax.style.backgroundPosition = `center ${(scrollPosition - elementPosition) * 0.5}px`;
    }
  });
});

console.log('🎬 Street Rulz Cinematic Design v5 activated');
