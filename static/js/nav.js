const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-menu a');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('open');
});

navLinks.forEach((link) => {
    link.addEventListener('click', () => navMenu.classList.remove('open'));
});

const sections = ['home', 'education', 'skills', 'experience', 'projects'];

window.addEventListener('scroll', () => {
    let current = 'home';

    for (const id of sections) {
        const section = document.getElementById(id);
        if (section && window.scrollY >= section.offsetTop - 100) {
            current = id;
        }
    }

    navLinks.forEach((link) => {
        link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });
});
