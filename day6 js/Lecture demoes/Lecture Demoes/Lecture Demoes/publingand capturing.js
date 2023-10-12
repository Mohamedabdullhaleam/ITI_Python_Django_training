addEventListener('load', function () {

    first.addEventListener('click', function () {

        alert("first Div")
    })

    second.addEventListener('click', function () {

        alert("second Div")
        //event.stopPropagation();
    })


    third.addEventListener('click', function (event) {
       event.stopPropagation();
      //  alert("third Div")
    })


})//load