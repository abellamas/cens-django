updateScroll = function () {
    const scrollPosition = window.scrollY;
    const header = document.querySelector('header')

    if (scrollPosition > 50) {
        header.classList.add('scrolled-nav')
    } else {
        header.classList.remove('scrolled-nav')
    }
}

window.addEventListener('scroll', updateScroll)