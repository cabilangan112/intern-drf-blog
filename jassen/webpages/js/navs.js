window.onscroll = function() {myFunction()};

var cssmenu = document.getElementById("cssmenu");
var sticky = cssmenu.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    cssmenu.classList.add("sticky")
  } else {
   cssmenu.classList.remove("sticky");
  }
}