var text = "Welcome to js";
var timerwindow = window.open("", "", "width=400,height=400");

for (var i = 0; i < text.length; i++) {
    setTimeout(function(chr) {
        return function() {
            timerwindow.document.write(text.charAt(chr));

            if (index === text.length - 1) {
                setTimeout(function() {
                    timerwindow.close();
                }, 500);
            }
        };
    }(i), i * 500); 
}
