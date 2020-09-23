jQuery( document ).ready(function( $ ) {

    //Use this inside your document ready jQuery 
    $(window).on('popstate', function() {
       location.reload(true);
    });
 
 });


const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#message').fadeOut('slow');
},5000);




