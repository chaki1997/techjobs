/**
 * Created by uzer on 9/21/2019.
 */


        function getvalue() {
            var x=document.getElementById('input_school');
            school=document.getElementById('input_school').value;
            $.ajax({
                type: "POST",
                async:false,
                data:{'school':school},
        url: 'http://127.0.0.1:8000/education/post/',

        dataType: 'json',

        success: function (data) {

        }
      });







        }



