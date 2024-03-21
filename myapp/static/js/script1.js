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

document.addEventListener('DOMContentLoaded', function () {
    // 初始设置iframe加载第一个项目的内容
    if (sidebarItems.length > 0) {
        const firstItemLink = sidebarItems[0].querySelector('a'); // 获取第一个项目中的链接
        if (firstItemLink) {
            mainContentIframe.src = firstItemLink.getAttribute('href');
            // 确保第一个项目被标记为激活状态
            sidebarItems[0].setAttribute('id', 'active');
            activeItem = sidebarItems[0]; // 更新当前激活的项目变量
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('logoutLink').addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('click');
        window.top.location.href = '/logout/';
    });
});
