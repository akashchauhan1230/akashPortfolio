// sidebar toggle variables
const menuToggler = document.querySelector('.menu-toggler');
const sideBar = document.querySelector('.side-bar');
let tick = document.getElementById('tick');
let cross = document.getElementById('cross');
var c = 1;

function updateSidebarState(isOpen) {
  sideBar.classList.toggle('active', isOpen);
  cross.style.display = isOpen ? 'inline' : 'none';
  tick.style.display = isOpen ? 'none' : 'inline';
  c = isOpen ? 0 : 1;
}

// page navigation variables
const navItemLinks = document.querySelectorAll('.nav li a');
const pages = document.querySelectorAll('.page');

// variables for filtering
const filterBtn = document.querySelectorAll('.filter-item');
const itemCategory = document.querySelectorAll('.item-category');

// toggling sidebar in mobile
menuToggler.addEventListener('click', function(){
  updateSidebarState(c === 1);
});


// page navigation functionality
function navigateToPage(pageId) {
  // Remove active from all pages
  for (let j = 0; j < pages.length; j++) {
    pages[j].classList.remove('active');
  }
  
  // Add active to selected page
  const targetPage = document.getElementById(pageId);
  if (targetPage) {
    targetPage.classList.add('active');
  }
  
  // Update active nav link
  for (let k = 0; k < navItemLinks.length; k++) {
    const href = navItemLinks[k].getAttribute('href');
    if (href === '#' + pageId) {
      navItemLinks[k].classList.add('active');
    } else {
      navItemLinks[k].classList.remove('active');
    }
  }
}

// Handle navigation link clicks
for (let i = 0; i < navItemLinks.length; i++) {
  navItemLinks[i].addEventListener('click', function(event){
    event.preventDefault();
    
    const href = this.getAttribute('href');
    if (href.startsWith('#')) {
      const pageId = href.substring(1); // Remove the # character
      navigateToPage(pageId);
      window.location.hash = href; // Update browser URL
      if (window.innerWidth <= 1024) {
        updateSidebarState(false);
      }
    }
  });
}

// Handle browser back/forward buttons and direct hash navigation
window.addEventListener('hashchange', function() {
  const hash = window.location.hash.substring(1); // Remove the # character
  if (hash) {
    navigateToPage(hash);
  }
});

// Initialize page based on current hash on page load
window.addEventListener('load', function() {
  const hash = window.location.hash.substring(1);
  if (hash) {
    navigateToPage(hash);
  } else {
    // Default to About page if no hash
    navigateToPage('about');
    window.location.hash = '#about';
  }
});

// added eventListener in filter buttons
for (let i = 0; i < filterBtn.length; i++) {
  filterBtn[i].addEventListener('click', function(){

    // remove all active class from filter button
    for (let i = 0; i < filterBtn.length; i++) {
      filterBtn[i].classList.remove('active');
    }
    // added active class on filter button clicked
    this.classList.add('active');

    // show item, based on filter button click
    for (let i = 0; i < itemCategory.length; i++) {
      const itemCategoryText = itemCategory[i].textContent;
      console.log(itemCategoryText);
      switch (this.textContent) {
        case itemCategoryText:
          itemCategory[i].parentElement.classList.add('active');
          break;
        case 'All':
          itemCategory[i].parentElement.classList.add('active');
          break;
        default:
          itemCategory[i].parentElement.classList.remove('active');
      }
    }
  });
}