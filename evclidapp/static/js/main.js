const swiper = new Swiper('.swiper', {
  direction: 'horizontal',
  loop: true,
	pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
		clickable: true,
  },
});







const viewport_width = document.documentElement.clientWidth;
const navMenuBar = document.querySelector('.main-menu-bar');
const barWrapMenu = document.querySelector('.bar-wrap-menu');
const headerNav = document.querySelector('.header');
const mainMenuList = document.querySelector('.main-menu_list');
const mainMenuItem = document.querySelectorAll('.main-menu__item');

let statusMenu = false;
const defoltMenu = -500;
const openMenu = 0;

navMenuBar.addEventListener('click', clickNav);
function clickNav() {
	if (statusMenu === false) {
		barWrapMenu.append(mainMenuList);
		mainMenuList.classList.add('viewMenu');
		mainMenuItem.forEach((el) => { el.classList.add('viewItem') });
		barWrapMenu.style.left = openMenu + 'px';
		statusMenu = true;
	} else {
		barWrapMenu.style.left = defoltMenu + 'px';
		mainMenuList.classList.remove('viewMenu');
		statusMenu = false;
	}
}


// code for opening the search

const wrapSrc = document.querySelector('.wrap-src');
const wrapSrcClose = document.querySelector('.wrap-src-close');
const closedSrc = document.querySelector('.closed-src');
let statusWrapSrc = false;
const defoltSrc = -500;
const openSrc = 0;

wrapSrc.addEventListener('click', clickWrapSrc);
closedSrc.addEventListener('click', clickClosedSrc);
// function open search
function clickWrapSrc() {
	if (statusWrapSrc === false) {
		wrapSrcClose.style.top = openSrc + 'px';
		wrapSrc.style.transform = 'translateX(-50px)';
		statusWrapSrc = true;
	}
}
// function closed search
function clickClosedSrc() {
	wrapSrcClose.style.top = defoltSrc + 'px';
	wrapSrc.style.transform = 'translateX(0px)';
	statusWrapSrc = false;
	console.log('defolt: ', statusWrapSrc);
}







