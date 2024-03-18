const menuOpen = document.getElementById('menu-open');
const menuClose = document.getElementById('menu-close');
const sideBar = document.querySelector('.container .left-section');
const sidebarItems = document.querySelectorAll('.container .left-section .sidebar .item');
const mainContentIframe = document.getElementById('main-content'); // 确保你已经在HTML中添加了这个ID的iframe

menuOpen.addEventListener('click', () => {
    sideBar.style.top = '0';
});

menuClose.addEventListener('click', () => {
    sideBar.style.top = '-60vh';
});

let activeItem = sidebarItems[0]; // 假设第一个项目默认是激活状态

sidebarItems.forEach(element => {
    const link = element.querySelector('a'); // 获取当前项中的链接
    element.addEventListener('click', (event) => {
        event.preventDefault(); // 阻止链接默认的跳转行为

        // 处理激活状态的变化
        if (activeItem) {
            activeItem.removeAttribute('id');
        }
        element.setAttribute('id', 'active');
        activeItem = element;

        // 改变iframe的src属性来加载新内容
        if(link) {
            mainContentIframe.src = link.getAttribute('href');
        }
    });
});
