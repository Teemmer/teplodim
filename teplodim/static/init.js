(function($){
  $(function(){
    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.slider').slider( { height: '100%'});
    $('.parallax').parallax();

    $('.pushpin-demo-nav').each(function() {
      var $this = $(this);
      var $target = $('#' + $(this).attr('data-target'));
      $this.pushpin({
        top: $target.offset().top,
        bottom: $target.offset().top + $target.outerHeight() - $this.height()
      });
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
