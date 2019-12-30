function add(id){
        var tag = document.getElementById(id).innerText



        document.getElementById('input').value =tag


       }


function addJobStatus(id){
        var tag = document.getElementById(id).innerText
        if (id == 'tag1'){
        tag = 'freelancer'
        }else if (id == 'tag2'){
        tag = 'full time'
        }

        //alert(id)

        document.getElementById('input').value =tag
        }


