addEventListener('load', function () {

    //clickMeBtn.onclick = fun1;
    //function fun1() {
    //    alert("user Clicked")
    //}

    updateBtn.onclick = fun2;
    function fun2() {

        document.title = "Updated"
    }

    updateBtn.onclick = function () {

        document.body.style.backgroundColor = "lightgreen"
    }
    updateBtn.addEventListener('click', fun2)

    ///////////////////////////
    testingDiv.addEventListener('mouseover', function(event){
        //console.log(`mouse over Event`)
        //console.log(event)
    })// mouseover


    testingDiv.addEventListener('mousemove', function (event) {
        //console.log(`mouse move Event`)
        this.innerHTML = "<h2 align='center'><font color='green' face='tahoma'>" + event.x +" : "+event.y+ "</font></h2>"
        

    })// mousemove

    testingDiv.addEventListener('mouseout', function () {
        //console.log(`mouse out Event`)

    })// mouseout

  

})// load