// ── MOBILE NAV ──
const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav__links');
if (burger) {
  burger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

// ── REVEAL ON SCROLL ──
const revealElements = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, i * 80);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
revealElements.forEach(el => observer.observe(el));

// ── SKILL BARS ANIMATE ──
const skillFills = document.querySelectorAll('.skill-card__fill');
const barObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fill = entry.target;
      const targetWidth = fill.style.width;
      fill.style.width = '0';
      setTimeout(() => { fill.style.width = targetWidth; }, 100);
      barObserver.unobserve(fill);
    }
  });
}, { threshold: 0.5 });
skillFills.forEach(fill => barObserver.observe(fill));

// ── ACTIVE NAV HIGHLIGHT ──
const links = document.querySelectorAll('.nav__link');
links.forEach(link => {
  if (link.href === window.location.href) link.classList.add('active');
});
