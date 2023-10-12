function fun(){
    console.log("welcome to js")
}
//////////////////////////////
function fun2 (name){
    console.log(`welcome ${name} to our project`)
}
//////////////////////////////
function addition(a=0,b=0,c=0){ //default params to avoid NAn
    console.log(`sum= ${a+b+c}`)
    console.log(arguments)    //we can get use it 
}
//////////////////////////////

function addall(){
    var sum = 0 ;
    for (let i=0;i<arguments.length ; i++){
        sum+=arguments[i];
    }
    console.log(`sum=${sum}`)
}
////////////////////////////
var dt = new Date();
dt.getDate();
dt.getDay();
dt.getMinutes()
////////////////////////////
fun();
fun2("mohamed");
console.log(fun); //return the the body of the function
