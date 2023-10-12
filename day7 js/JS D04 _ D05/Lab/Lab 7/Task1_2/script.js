//1-
console.log('%c1-', 'font-weight: bold; font-size: 25px; color: red;');

//a-
// First Method
var images1 = document.images;

for (var i = 0; i < images1.length; i++) {
  console.log(images1[i]);
}
// Second Method
var images2 = document.getElementsByTagName('img');
for (var i = 0; i < images2.length; i++) {
  console.log(images2[i]);
}
console.log('------------------------------');

//b-
var citylist = document.getElementsByName('City')[0];
var citylistoptions = citylist.getElementsByTagName('option');
for (var i = 0; i < citylistoptions.length; i++) {
  console.log(citylistoptions[i]);
}
console.log('------------------------------');

//c-
var secondtable = document.getElementsByTagName('table')[1];
var rows = secondtable.getElementsByTagName('tr');
for (var i = 0; i < rows.length; i++) {
  console.log(rows[i]);
}
console.log('------------------------------');
//d-
var blues = document.getElementsByClassName('fontBlue');
for (var i = 0; i < blues.length; i++) {
  console.log(blues[i]);
}

//2-
//a-
var firstAnchor = document.getElementsByTagName('a')[0];
firstAnchor.href = 'http://training.com';
firstAnchor.textContent = 'Training';
//b-
var lastImage = images1[images1.length - 1];
console.log(lastImage);
lastImage.style.border = 'solid pink 2px';
//c-
function FindChecked() {
  var element = document.querySelector('input[type="checkbox"]:checked');
  alert(element.value);
}
//d-
var element = document.getElementById('example');
element.style.backgroundColor="pink";


//3-