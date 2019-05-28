$(document).ready(function(){
    $('#action_menu_btn').click(function(){
        $('.card').slideToggle();
        $('#chat').append(`<div class="img_cont fab" style="background: white;border-radius: 100%" id="fab" onclick="openup();">
        <img src="{% static "images/bot.png" %}" class="rounded-circle user_img" id="fab">
        <span class="online_icon"></span>
    </div>`);
    });
    $("#question").addEventListener("keyup", function(event) {
        // Number 13 is the "Enter" key on the keyboard
        if (event.keyCode === 13) {
          // Cancel the default action, if needed
          event.preventDefault();
          // Trigger the button element with a click
          $("#submit").click();
        }
      });
});
function openup(){
        alert('hello');
        $('.card').slideToggle();
        var fab = document.getElementsByID("fab");
        fab.parentNode.removeChild(fab);
}

