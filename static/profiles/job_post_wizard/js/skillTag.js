function add(id){
        var tag = document.getElementById(id).innerText
        var inputStr = ''
        inputStr = document.getElementById('input').value
        if (!inputStr.includes(tag)){
        document.getElementById('input').value =tag + ',' + inputStr
        var outputStr = document.getElementById('input').value
        inputStr = document.getElementById('input').value
        console.log(inputStr);
        }
        else{
        inputStr=inputStr.replace(tag,'')
        inputStr=inputStr.replace(',,',',')

        document.getElementById('input').value = inputStr
        }

        document.getElementById("demo").innerHTML = inputStr

        }