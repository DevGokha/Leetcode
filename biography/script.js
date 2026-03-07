/* ===== Navigation active state on scroll ===== */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

function setActiveNav() {
  const scrollY = window.scrollY + 100;
  sections.forEach(section => {
    const top    = section.offsetTop;
    const height = section.offsetHeight;
    const id     = section.getAttribute('id');
    if (scrollY >= top && scrollY < top + height) {
      navLinks.forEach(a => a.classList.remove('active'));
      const active = document.querySelector(`.nav-links a[href="#${id}"]`);
      if (active) active.classList.add('active');
    }
  });
}

/* ===== Scroll reveal ===== */
const revealEls = document.querySelectorAll('.reveal');

function reveal() {
  revealEls.forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight - 80) {
      el.classList.add('visible');
    }
  });
}

/* ===== Skill bar animation ===== */
const bars = document.querySelectorAll('.bar-fill');
let barsAnimated = false;

function animateBars() {
  if (barsAnimated) return;
  const section = document.getElementById('skills');
  if (!section) return;
  const rect = section.getBoundingClientRect();
  if (rect.top < window.innerHeight - 50) {
    bars.forEach(bar => {
      bar.style.width = bar.dataset.width;
    });
    barsAnimated = true;
  }
}

window.addEventListener('scroll', () => {
  setActiveNav();
  reveal();
  animateBars();
});

/* run on load */
reveal();
animateBars();
