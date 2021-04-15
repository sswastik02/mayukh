const mobileMenu= document.querySelector('#mobile-menu')
const Menu= document.querySelector('.menu')

const toggleMenu = () => {
    Menu.classList.toggle('active')
    mobileMenu.classList.toggle('is-active')
}

mobileMenu.addEventListener('click',toggleMenu)