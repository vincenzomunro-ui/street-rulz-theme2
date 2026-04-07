// ===== MOBILE MENU =====
const navToggle = document.getElementById('navToggle');
const mobileMenu = document.getElementById('mobileMenu');

if (navToggle && mobileMenu) {
  navToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    navToggle.classList.toggle('active');
  });
  // Close menu on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      navToggle.classList.remove('active');
    });
  });
}

// ===== ACTIVE NAV LINK =====
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPath || (currentPath === '/' && href === '/')) {
    link.classList.add('active');
  }
});

// ===== SMOOTH SCROLL FOR ANCHOR LINKS =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// ===== SCROLL ANIMATIONS =====
const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));

// ===== ANNOUNCEMENT BAR CLOSE =====
const closeAnnounce = document.getElementById('closeAnnounce');
if (closeAnnounce) {
  closeAnnounce.addEventListener('click', () => {
    closeAnnounce.closest('.announce-bar').style.display = 'none';
  });
}

// ===== ACADEMY SUBSCRIPTION WIDGET RELOCATION =====
(function() {
  if (window.location.pathname.indexOf('/pages/academy') === -1) return;
  var enrolBtn = document.querySelector('a[href*="rulz-academy-monthly"]');
  if (!enrolBtn) return;
  var container = document.createElement('div');
  container.id = 'academy-subscription-widget';
  container.style.cssText = 'margin-top:48px;max-width:700px;margin-left:auto;margin-right:auto;';
  var enrolParent = enrolBtn.parentElement;
  if (enrolParent && enrolParent.parentElement) {
    enrolParent.parentElement.insertBefore(container, enrolParent.nextSibling);
  }
  function moveWidget() {
    var appBlocks = document.querySelectorAll('.shopify-app-block');
    appBlocks.forEach(function(block) {
      if (block.closest('#academy-subscription-widget')) return;
      container.appendChild(block);
    });
  }
  setTimeout(moveWidget, 500);
  setTimeout(moveWidget, 1500);
  setTimeout(moveWidget, 3000);
  setTimeout(moveWidget, 5000);
})();
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
