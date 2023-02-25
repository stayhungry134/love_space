let menu_btn = document.querySelector('.menu-toggle .iconfont');
let menu = document.querySelector('.mobile-nav');
let body = document.body;
menu_btn.addEventListener('click', function (){
    console.log(menu.style.left)
    if (parseInt(menu.style.left)){
        menu_btn.classList.remove('icon-shouqicaidan');
        menu_btn.classList.add('icon-zhankaicaidan');
        menu.style.left = 0;
        menu.addEventListener('touchmove', (e)=>{
            e.preventDefault();
        }, false)
    }else {
        // 取消固定 body
        menu_btn.classList.remove('icon-zhankaicaidan');
        menu_btn.classList.add('icon-shouqicaidan');
        menu.style.left = '100vw';
    }
}, {passive: false})
