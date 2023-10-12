addEventListener('load', function () {
    run = document.getElementsByTagName("img")[0]
    txt = document.getElementById("txt");
    result = document.getElementById("right")
    run.addEventListener('click', function () {

        result.innerHTML=txt.value
    })

})