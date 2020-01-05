function moveToSelected(element) {

    if (element == "next") {
      var selected = $(".selected").next();
    } else if (element == "prev") {
      var selected = $(".selected").prev();
    } else {
      var selected = element;
    }
  
    var next = $(selected).next();
    var prev = $(selected).prev();
    var prevSecond = $(prev).prev();
    var nextSecond = $(next).next();
  
    $(selected).removeClass().addClass("selected");
  
    $(prev).removeClass().addClass("prev");
    $(next).removeClass().addClass("next");
  
    $(nextSecond).removeClass().addClass("nextRightSecond");
    $(prevSecond).removeClass().addClass("prevLeftSecond");
  
    $(nextSecond).nextAll().removeClass().addClass('hideRight');
    $(prevSecond).prevAll().removeClass().addClass('hideLeft');
  
  }
  
  // Eventos teclado
  $(document).keydown(function(e) {
      switch(e.which) {
          case 37: // left
          moveToSelected('prev');
          break;
  
          case 39: // right
          moveToSelected('next');
          break;
  
          default: return;
      }
      e.preventDefault();
  });
  
  $('#carousel div').click(function() {
    moveToSelected($(this));
  });
  
  $('#prev').click(function() {
    moveToSelected('prev');
  });
  
  $('#next').click(function() {
    moveToSelected('next');
  });


function moveToSelected_movies(element) {

    if (element == "next_movies") {
      var selected_movies = $(".selected_movies").next_movies();
    } else if (element == "prev_movies") {
      var selected_movies = $(".selected_movies").prev_movies();
    } else {
      var selected_movies = element;
    }
  
    var next_movies = $(selected_movies).next_movies();
    var prev_movies = $(selected_movies).prev_movies();
    var prevSecond_movies = $(prev_movies).prev_movies();
    var nextSecond_movies = $(next_movies).next_movies();
  
    $(selected_movies).removeClass().addClass("selected_movies");
  
    $(prev_movies).removeClass().addClass("prev_movies");
    $(next_movies).removeClass().addClass("next_movies");
  
    $(nextSecond_movies).removeClass().addClass("nextRightSecond_movies");
    $(prevSecond_movies).removeClass().addClass("prevLeftSecond_movies");
  
    $(nextSecond_movies).nextAll().removeClass().addClass('hideRight_movies');
    $(prevSecond_movies).prevAll().removeClass().addClass('hideLeft_movies');
  
  }
  
  // Eventos teclado
  $(document).keydown(function(e) {
      switch(e.which) {
          case 37: // left
          moveToSelected_movies('prev_movies');
          break;
  
          case 39: // right
          moveToSelected_movies('next_movies');
          break;
  
          default: return;
      }
      e.preventDefault();
  });
  
  $('#carousel_movies div').click(function() {
    moveToSelected_movies($(this));
  });
  
  $('#prev_movies').click(function() {
    moveToSelected_movies('prev_movies');
  });
  
  $('#next_movies').click(function() {
    moveToSelected_movies('next_movies');
  });
  