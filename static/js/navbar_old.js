updateScroll = function () {
    const scrollPosition = window.scrollY;
    const header = document.querySelector('header')

    if (scrollPosition > 50) {
        header.classList.add('scrolled-nav')
    } else {
        header.classList.remove('scrolled-nav')
    }
}

checkScreen = function () {
    const iconNavbar = document.querySelector("#iconNavId");
    const linksDesktop = document.querySelector('#navId')
    let windowWidth = window.innerWidth;

    if (windowWidth < 768) {
        //Hide the links of navbar desktop
        linksDesktop.classList.add('navigationHidden');
        linksDesktop.classList.remove('navigation');
        //Show the icon Navbar Menu
        iconNavbar.classList.remove('iconNavbarHidden');
        iconNavbar.classList.add('iconNavbar');

        if (!iconNavbar.classList.contains('icon-active')) {

        }
        // iconNavbar.classList.add("mobile")
        // iconNavbar.classList.add("menuMobile")
    } else {
        //Show the links of navbar desktop
        linksDesktop.classList.remove('navigationHidden');
        linksDesktop.classList.add('navigation');
        //Hide the icon navbar menu
        iconNavbar.classList.add('iconNavbarHidden');
        iconNavbar.classList.remove('iconNavbar');
        //Hide the mobile navbar

        // iconNavbar.classList.remove("mobile")
        // iconNavbar.classList.remove("menuMobile")
    }
}

toggleMenuMobile = function () {
    const iconNavbar = document.querySelector(".iconNavbar");
    const iconActive = document.querySelector('.icon-active');
    const mobileNavbar = document.querySelector("#mobileNavId")

    if (iconActive) {
        console.log('out')
        iconNavbar.classList.remove('icon-active')
    } else {
        console.log('in')
        iconNavbar.classList.add('icon-active');
    }
}




const iconNavbar = document.querySelector(".iconNavbar");

window.addEventListener('scroll', updateScroll);
window.addEventListener('resize', checkScreen);
window.addEventListener('load', checkScreen);
iconNavbar.addEventListener('click', toggleMenuMobile);