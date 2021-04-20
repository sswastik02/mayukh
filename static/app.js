const mobileMenu= document.querySelector('#mobile-menu')
const Menu= document.querySelector('.menu')
const logo=document.querySelector('.navbar_logo')
//const links=document.querySelector('.navbar_links')  didn't work
const link_home=document.querySelector('#home-page')
const link_about=document.querySelector('#about-page')
const link_courses=document.querySelector('#courses-page')
const toggleMenu = () => {
    Menu.classList.toggle('active')
    mobileMenu.classList.toggle('is-active')
}

mobileMenu.addEventListener('click',toggleMenu)

const navmenu_clicked = () => {
    const mob= document.querySelector('.is-active')
    if(window.innerWidth <= 960 && mob) // if window width<960px and mob is active (mob might be active without width being < 960px)
    {
        mobileMenu.classList.toggle('is-active')
        Menu.classList.remove('active')
    }

}
link_home.addEventListener('click',navmenu_clicked)
link_about.addEventListener('click',navmenu_clicked)
link_courses.addEventListener('click',navmenu_clicked)
logo.addEventListener('click',navmenu_clicked)
