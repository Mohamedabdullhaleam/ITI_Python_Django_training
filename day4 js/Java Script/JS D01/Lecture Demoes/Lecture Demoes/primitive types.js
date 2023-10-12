//alert("welcome from external ")

//str = "A";
//console.log(str)
//console.log(typeof str)
////========
//str = "22";
//console.log(str)
//console.log(typeof str)

//
//console.log("my name is AbdAllah")
//console.log('my name is AbdAllah' + "and my age is 29 years old" + "i works at ITI")
//console.log('i\'m abdAllah')
//console.log("i\"m abdAllah")
//console.log('i\'m abdAllah and \
//    i have 29 years old and i\
//     works at ITI')
//console.log("my name is \n Ali ")

str = "abdAllah"
//console.log(str,typeof str)
//console.log(`my name is ${str}
//i'm 29 years old
//i works at iti `)
//console.log("2" + "2") // string
//console.log(2 + "2") // string
//console.log(2 + 2) // Number
//console.log(true + "2") // string
var num = 20;
//console.log(num , typeof num)
//console.log(num + num) // Number

//// boolean
//var bool = true;
//console.log(bool, typeof bool)
//console.log(bool + "2") // string
//console.log(bool + num) // number
/*console.log(false + num) */// number
//=========
//if (num % 2 == 0) {
//    console.log("even")
//}
//else {
//    console.log("Odd")
//}

// ========================   trenary operator

//(condition ? true: false)
//(num % 2 == 0 ? console.log("even") : console.log("Odd"))

//====================
//var x = 2;
//var y = "2"
//console.log(x == y)  // true
//console.log(x === y)  // false
//console.log(x === x)  // true

///////  null & undefined

//var x;
//console.log(x, typeof x)
//var y = null;
//console.log(y, typeof y)

//console.log(x == y) // true
//console.log(x === y) // true

// ============ object type (Language object )

//var str = "Ali"; //  primitive stirng
//console.log(str, typeof str)

//var str = new String("welcome to js")
//console.log(typeof str, str.constructor.name)
//str[0] // 'w'
//str.length //13
//str.charAt(0) // == str[0]
//str.valueOf() // return primitive value from String Object ==> "welcome to js"

//str.substring(1, 4)// return string in indexex 1,2,3 ==> elc

//str.substring(4) //'ome to js'
//str.slice(1, 4)// return string in indexex 1,2,3 ==> elc
//str.slice(4) //'ome to js'
//str.slice(-2) // return from last of string ==> "js"
//str.substr(1, 4)// return form index 1 to index 4 >> elco

//str.indexOf("e") // 1
//str.lastIndexOf("e") //6
//str.indexOf("z")// -1
//str.toUpperCase()
//str.toLowerCase()
//str.replace("w", "he")// 'heelcome to js'
//str.split()  //["welcome to js"]
//str.split("e") //['w', 'lcom', ' to js']
//str.split(" ") // ['welcome', 'to', 'js']
//var arr = str.split(" ")
//arr[0][0] // "w"
//arr[0].charAt(0)//// "w"

// ================
var str = new String("I Love js")
var  newstr=""
console.log(`before  :${str.valueOf()} `)
for (var i = 0; i < str.length; i++) {
    if (str[i] == str[i].toUpperCase()) {  //I==I
       newstr+= str[i].toLowerCase()

    }
    else {
        newstr+= str[i].toUpperCase()

    }


}
console.log(`After :${newstr} `)








