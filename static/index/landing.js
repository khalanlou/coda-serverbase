/**************** hamburger-menu ****************/
function openNav() {
    document.getElementById("side-nav").style.width = "270px";
    document.getElementById("Main").style.marginLeft = "50px";
    document.getElementById("side-nav").style.backgroundColor = "rgb(255, 255, 255, 0.5)";
    document.getElementById("header").style.opacity = "70%";
  }
  
  function closeNav() {
    document.getElementById("header").style.opacity = "100%";
    document.getElementById("side-nav").style.width = "0";
    document.getElementById("Main").style.marginLeft= "0";
  }
/**************** hamburger-menu ****************/

/**************** page-loader ****************/
var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 1000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("Main").style.display = "block";
  document.getElementById("main").style.opacity = "100%";
}
/**************** page-loader ****************/

$('[data-toggle="tooltip"]').tooltip({
  delay: {
      show: 10000,
      hide: 0
  }
});

/**************** navbar-scroll ****************/
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    document.getElementById("navbar-scroll").style.top = "0";
  }
  else {
    document.getElementById("navbar-scroll").style.top = "-80px";
  }
}
/**************** navbar-scroll ****************/
 
/**************** fix-width ****************/
function resize() {
  if ( $(window).width() > 1370) {     
    $("#main").addClass('container');
    $("#main").removeClass('container-fluid');
  }
  else
  {
    $("#main").addClass('container-fluid');
    $("#main").removeClass('container');
  }
}
$(window).on("resize", resize);
resize();
/**************** fix-width ****************/