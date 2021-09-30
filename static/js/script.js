loadScreendata();

// Header setting
$(window).scroll(function () {
  let scrollTop = $(window).scrollTop();
  //console.log("scrollTop", scrollTop);
  if (scrollTop > 100) {
    $("#header-section").addClass("sticky-nav");
  } else {
    $("#header-section").removeClass("sticky-nav");
  }
});

// Header mobile version setting
$(window).resize(function () {
  let windowWidth = $(window).width();
  if (windowWidth < 760) {
    $("#header-section").addClass("sticky-nav");
    $(".toggle-menu")
      .addClass("d-none d-sm-none d-xs-none")
      .removeClass("d-block d-sm-block d-xs-block");
  } else {
    $("#header-section").removeClass("sticky-nav");
  }
});

function loadScreendata() {
  let windowWidth = $(window).width();
  if (windowWidth < 760) {
    $("#header-section").addClass("sticky-nav");
    $(".toggle-menu")
      .addClass("d-none d-sm-none d-xs-none")
      .removeClass("d-block d-sm-block d-xs-block");
  } else {
    $("#header-section").removeClass("sticky-nav");
  }
}

$(".toggle-icon").click(function () {
  if ($(this).hasClass("collapsed")) {
    $(this).removeClass("collapsed");
    $(".toggle-menu")
      .addClass("d-none d-sm-none d-xs-none")
      .removeClass("d-block d-sm-block d-xs-block");
  } else {
    $(this).addClass("collapsed");
    $(".toggle-menu")
      .removeClass("d-none d-sm-none d-xs-none")
      .addClass("d-block d-sm-block d-xs-block");
  }
});
