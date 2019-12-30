/**
 * Created by uzer on 9/15/2019.
 */


$('.Continue_button').click(function(){
            if($('.input100').val() === ""){
                document.getElementById("msg").innerHTML = 'empty';
                return}

                username =$('#username').val()
    function validateUserDetails() {
        $.ajax({
            url: "http://127.0.0.1:8000/validate/get/",
//            url: "http://5845b0ee.ngrok.io/validate/get/",

            dataType: 'json',
            type: "post", // or "get"
            async:false,

            data: username,
            success: function (data) {

                console.log(data.result)
                console.log(typeof data.result)
                if (data.result == false){
                    $(".login_form").fadeOut(function(){
    $(".login_form_password").fadeIn();
  });
                }else if (data.result == true){
                    document.getElementById("msg").innerHTML = 'user does not exists';
                }








            }
        });

    }

    validateUserDetails()







});
        $('.Back_button').click(function(){

            $(".login_form_password").fadeOut(function(){
    $(".login_form").fadeIn();
  });
});
