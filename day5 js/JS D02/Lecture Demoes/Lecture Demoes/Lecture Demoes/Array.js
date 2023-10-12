//var arr = new Array(); // empty Array == 
var arr = [];
//console.log(typeof arr, arr.constructor.name)

//arr[0] = 10
//arr[1] = 30
//arr[9] = 60
//arr[99] = 15
// spars Array

//for (var i = 0; i < arr.length; i++) {
//    console.log(i,arr[i])
//}

0 in arr  // true 
1 in arr // true
10 in arr // false
// in operator checks if index has avlue in array 
console.log("///////===========")

//for (item in arr) {
//    console.log(item,arr[item])
//}

//console.log("///////=========== for of ")
//for (i of arr) {
//    console.log(i)
//}

//var arr2 = [23, 34, 40, "ali", "Apple", true, null]

//console.table(arr2)
arr = [20, 23, 12, 13, 5, 30, 90, 200]
arr.push(100, 25) // add at end of arr and return new arr length
arr.pop() // return last index in arr  
arr.unshift(130, 220) // add at front  of arr and return new arr length
delete arr[1] 
arr.shift() // return first index in arr and shift the rest of elements
arr.shift()
//arr.includes(200)
//arr.join() // '20,23,12,13,5,30,90,200,100'
//arr.join("a") // '20a23a12a13a5a30a90a200a100'
//arr.join("+") // '20+23+12+13+5+30+90+200+100'
//eval('alert("hi")')

//eval(arr.join("+"))

//arr.forEach(loop)

//function loop(elm, indx) {
//    console.log(`indx : ${indx}  elm = ${elm }`)

//}
//function loop(elm) {
//    console.log(`elm = ${elm}`)

//}

//arr.forEach(function (elm, indx) {
//    console.log(`indx : ${indx}  elm = ${elm}`)

//})


//var res = arr.filter(function (num) {
//    //if (num >25) {

//    //    return num;
//    //}
//    return num > 25;

//})
///////////////  // arr = [20, 23, 12, 13, 5, 30, 90, 200,200]

arr.sort(function (a, b) {
   if (a > b)
       return 1;
   else if (a < b)
       return -1;
   else
       return 0;

//})

//arr.sort(function (a, b) {
//   return    a - b


//})

arr.sort(function (a, b) {
    return b - a


})