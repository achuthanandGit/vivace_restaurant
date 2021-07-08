!(function($) {
  "use strict";

  var fullDate = new Date();
  //convert month to 2 digits
  var twoDigitMonth = ((fullDate.getMonth().length+1) === 1)? (fullDate.getMonth()+1) : '0' + (fullDate.getMonth()+1);
  var currentDate = fullDate.getFullYear() + "-" + twoDigitMonth + "-" + fullDate.getDate();
  $('#book-date')[0].defaultValue  = currentDate;
  $('#book-date')[0].max  = currentDate;
  $('#book-date')[0].min  = currentDate;

  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 1;
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        if ($(this).attr("href") == '#header') {
          scrollto = 0;
        }

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function() {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Mobile Navigation
  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      $('.mobile-nav-overly').toggle();
    });

    $(document).on('click', '.mobile-nav .drop-down > a', function(e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });

    $(document).click(function(e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.nav-menu, #mobile-nav');

  $(window).on('scroll', function() {
    var cur_pos = $(this).scrollTop() + 200;

    nav_sections.each(function() {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
      }
      if (cur_pos < 300) {
        $(".nav-menu ul:first li:first").addClass('active');
      }
    });
  });

  // Toggle .header-scrolled class to #header when page is scrolled
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
      $('#topbar').addClass('topbar-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
      $('#topbar').removeClass('topbar-scrolled');
    }
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
    $('#topbar').addClass('topbar-scrolled');
  }

  // Real view height for mobile devices
  if (window.matchMedia("(max-width: 767px)").matches) {
    $('#hero').css({
      height: $(window).height()
    });
  }

  // Intro carousel
  var heroCarousel = $("#heroCarousel");
  var heroCarouselIndicators = $("#hero-carousel-indicators");
  heroCarousel.find(".carousel-inner").children(".carousel-item").each(function(index) {
    (index === 0) ?
    heroCarouselIndicators.append("<li data-target='#heroCarousel' data-slide-to='" + index + "' class='active'></li>"):
      heroCarouselIndicators.append("<li data-target='#heroCarousel' data-slide-to='" + index + "'></li>");
  });

  heroCarousel.on('slid.bs.carousel', function(e) {
    $(this).find('h2').addClass('animate__animated animate__fadeInDown');
    $(this).find('p, .btn-menu, .btn-book').addClass('animate__animated animate__fadeInUp');
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });

  $('.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Menu list isotope and filter
  $(window).on('load', function() {
    var menuIsotope = $('.menu-container').isotope({
      itemSelector: '.menu-item',
      layoutMode: 'fitRows'
    });

    $('#menu-flters li').on('click', function() {
      $("#menu-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      menuIsotope.isotope({
        filter: $(this).data('filter')
      });
    });
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".events-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Initiate venobox lightbox
  $(document).ready(function() {
    $('.venobox').venobox();
  });

  $('#btn-submit-msg').on('click', function(event) {

    $('#contact-response-msg').removeClass('alert-success').removeClass('alert-danger').addClass('d-none');  

    var ul = $("#contact-validation-list");
    ul.empty();

    var name = $('#name').val().trim();
    var mail = $('#mail').val().trim();
    var subject = $('#subject').val().trim();
    var message = $('#message').val().trim();

    var errorList = []

    if(!name) 
      errorList.push('Name : Please enter atleast 4 characters');

    if(!mail) 
      errorList.push('Email : Please enter valid email.');
    
    if(!subject) 
      errorList.push('Subject : Please enter atleast 8 characters.');

    if(!message) 
      errorList.push('Message : Please enter some message.');

    
    if(errorList.length > 0) {
      $.each(errorList, function (idx, error) {
        ul.append("<li>" + error + "</li>")
      });
      ul.removeClass('d-none');
    } else {
      ul.addClass('d-none');
      $.ajax({
        type:'POST',
        url: 'contact/',
        data:{
            name:name,
            mail:mail,
            subject:subject,
            message:message,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(response){
            document.getElementById("contact-form").reset();
            if(response.isSuccess)
              $('#contact-response-msg').addClass('alert-success').removeClass('d-none').text(response.message);
            else
              $('#contact-response-msg').addClass('alert-danger').removeClass('d-none').text(response.message);
        },
        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          $('#contact-response-msg').addClass('alert-danger').removeClass('d-none').text("Internal error occured, please try again.")
        }
      });  
    }  
  });

  $('#btn-submit-book').on('click', function(event) {

    $('#book-response-msg').removeClass('alert-success').removeClass('alert-danger').addClass('d-none');  

    var ul = $("#book-validation-list");
    ul.empty();

    var name =  $('#book-name').val().trim();
    var mail = $('#book-mail').val().trim();
    var phone = $('#book-phone').val().trim();
    var date = $('#book-date').val();
    var time = $('#book-time').val().trim();
    var peopleCount = $('#book-people').val().trim();
    var message = $('#book-message').val().trim();

    var errorList = []

    if(!name) 
      errorList.push('Name : Please enter atleast 4 characters');

    if(!mail) 
      errorList.push('Email : Please enter valid email.');
    
    if(!phone || parseInt(phone) == NaN)
      errorList.push('Phone : Please enter valid phone number.');

    if(!date) 
      errorList.push('Date : Please enter valid date.');

    if(!time) 
      errorList.push('Time : Please enter valid time.');
    else if(!(time.toLocaleLowerCase().includes("pm") || time.toLocaleLowerCase().includes("am")))
      errorList.push('Time : Please include AM/PM.');

    if(!peopleCount) 
      errorList.push('No. of people : Please enter atleast 1.');
    else if(parseInt(peopleCount) < 1 || parseInt(peopleCount) > 50)
      errorList.push('No. of people : Minimum number of people is 1 and maximum is 50.');

    if(!message) 
      errorList.push('Message : Please enter some message.');

    if(errorList.length > 0) {
      $.each(errorList, function (idx, error) {
        ul.append("<li>" + error + "</li>")
      });
      ul.removeClass('d-none');
    } else {
      ul.addClass('d-none');
      $.ajax({
        type:'POST',
        url: 'book/',
        data:{
            name:name,
            mail:mail,
            phone:phone,
            date:date,
            time:time,
            peopleCount:parseInt(peopleCount),
            message:message,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(response){
            document.getElementById("book-form").reset();
            if(response.isSuccess)
              $('#book-response-msg').addClass('alert-success').removeClass('d-none').text(response.message);
            else
              $('#book-response-msg').addClass('alert-danger').removeClass('d-none').text(response.message);
        },
        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          $('#book-response-msg').addClass('alert-danger').removeClass('d-none').text("Internal error occured, please try again.")
        }
      });  
    }  
  });

})(jQuery);