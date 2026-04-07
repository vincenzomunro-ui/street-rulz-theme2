// CINEMATIC ANIMATIONS (Nano Banana approach)
// Isolated, safe, uses only new component classes

document.addEventListener('DOMContentLoaded', () => {
  // Fade-in on scroll for new sections
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

  // Only observe fade-in-section (new component)
  document.querySelectorAll('.fade-in-section').forEach(el => {
    observer.observe(el);
  });

  // Parallax scroll for new components only
  window.addEventListener('scroll', () => {
    document.querySelectorAll('.parallax-section').forEach(parallax => {
      const rect = parallax.getBoundingClientRect();
      const scrolled = window.pageYOffset;
      const yPos = parallax.offsetTop - scrolled * 0.5;
      parallax.style.backgroundPosition = `center ${yPos}px`;
    });
  });

  console.log('✅ Cinematic animations loaded (safe mode)');
});
