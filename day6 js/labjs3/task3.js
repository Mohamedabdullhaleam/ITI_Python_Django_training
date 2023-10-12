var counterI = 0;
var counterJ = 0;

setInterval(function () {
    counterI++;
    document.title = counterI;
}, 1500);

setInterval(function () {
    counterJ++;
    var tableElement = document.createElement('table');
    tableElement.textContent = counterJ;
    document.body.appendChild(tableElement);
    tableElement.style.border = "5px solid red";
}, 1500);
