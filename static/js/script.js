const btnHamburger = document.querySelector('#btnHamburger');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElems = document.querySelectorAll('.has-fade');
const body = document.querySelector('body');

btnHamburger.addEventListener('click', function(){
    if(header.classList.contains('open')){
        body.classList.remove('noscroll');
        header.classList.remove('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-in');
            element.classList.add('fade-out');
        });
    }else{
        body.classList.add('noscroll');
        header.classList.add('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
        });
    }
})

const headerUser = document.querySelector('.header__user');
const headerUsername = document.querySelector('#dropdown');
const headerDropdown = document.querySelector('.header__dropdown_user');

headerUsername.addEventListener('click', () => {
  if(headerUser.classList.contains('open')){
    headerUser.classList.remove('open');
    // headerDropdown.style.display = "none";
    headerDropdown.classList.remove('fade-in');
    headerDropdown.classList.add('fade-out');
  }else{
    headerUser.classList.add('open');
    // headerDropdown.style.display = "block";
    headerDropdown.classList.remove('fade-out');
    headerDropdown.classList.add('fade-in');
  }
})

const categoryDropdown = document.querySelector('#category-dropdown');
const categoryHeaderDropdown = document.querySelector('.header__dropdown');
const categoryContentDropdown = document.querySelector('#category-content');

categoryDropdown.addEventListener('click', () => {
  if(categoryHeaderDropdown.classList.contains('open')){
    categoryHeaderDropdown.classList.remove('open');
    categoryContentDropdown.classList.remove('fade-in');
    categoryContentDropdown.classList.add('fade-out');
  }else{
    categoryHeaderDropdown.classList.add('open');
    categoryContentDropdown.classList.remove('fade-out');
    categoryContentDropdown.classList.add('fade-in');
  }
})