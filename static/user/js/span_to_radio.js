function add(id){
        var tag = document.getElementById(id).innerText
        var inputStr = ''
        inputStr = document.getElementById('input').value
        if (!inputStr.includes(tag) && tag == 'Work as Freelancer'){
        tag = 'Freelancer'
        document.getElementById('input').value =tag
        var outputStr = document.getElementById('input').value
        //inputStr = document.getElementById('input').value
        console.log(inputStr);
        }else if (!inputStr.includes(tag) && tag == 'Hire of Project'){
        tag = 'Company'
        document.getElementById('input').value =tag
        }

        else{
        inputStr=inputStr.replace(tag,'')
        inputStr=inputStr.replace(',,',',')

        //document.getElementById('input').value = inputStr
        }

        document.getElementById("demo").innerHTML = inputStr

        }