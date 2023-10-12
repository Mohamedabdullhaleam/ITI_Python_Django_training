////// Functions 
//function fun1() {
//    console.log(`welcome to js `)
//} // function declaration

//fun1(); // function Calling

function fun2(_name) {
    console.log(`welcome ${_name}`)
}

//fun2("ali")  // welcome ali
//fun2 //   return function declaration
//fun2() // welcome undefined
//fun2("ali", "ahmed") // welcome ali

//function doubleNum(num) {
//    return num * 2;
//}

    // optional params
//function sum(a,b, c) {
//    if (c == undefined) {
//        console.log(`plz enter c value `)
//    }

//    else {
//        console.log(`sum= ${a + b + c}`)
//    }

//}

//////  default params
//function sum(a=0, b=0, c=0) {

//        console.log(`sum= ${a + b + c}`)

//}
////////////////////////////// argument (Array-Like)

//function sum(a=0, b=0, c=0) {

//    console.log(arguments)

//}

//function sumAll() {
//    sum = 0;
//   // console.log(arguments)
//    for (var i = 0; i < arguments.length; i++) {
//        sum += arguments[i]
//    }
//    console.log(`sum = ${sum}`)
//}

/////////////  Math 
//Math.PI
//Math.pow(2, 3)  // 8
//Math.sqrt(25) // 5
//Math.round(2.2)  // 2
//Math.round(2.7) // 3
//Math.ceil(2.1)  // 3

//Math.floor(2.9)  // 2

//Math.floor(Math.random() * 10) 

/////////////////// Date
//var dt = new Date()
//dt.getDate() 
//dt.getFullYear()
//dt.getHours()
//dt.getMinutes()
//dt.getSeconds()
//dt.toLocaleString()
//dt.getDay() // return number sunday= 0;

//dt.getMonth()

//dt.toString()
//dt.toString().split(" ")
//dt.toString().split(" ")[1] // return Mongth
//dt.toString().split(" ")[0] // return Day 
 

