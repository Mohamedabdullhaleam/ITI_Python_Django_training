//q1
var mySentence = "java script is a good programming language";
var words = mySentence.split(" ");

for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substring(1);
}

console.log("q1")
console.log(words.join(' '))
/////////////////////////////////////
//q2
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
console.log("q2")
console.log(`After :${newstr} `)
//////////////
var stru="thequickbrownfoxjumpsoverthelazydog";
 var uniqelement="";
 for (var x=0;x < stru.length;x++)
 {
 if(uniqelement.indexOf(stru.charAt(x))==-1)
  {
  uniqelement += stru[x];  
   }
  }
  console.log("q3")
  console.log(uniqelement)
  //////////////////
  //q4
  wordl="mohamed ahmed abdullhaleam ";
  longestWord=0;
  var splited =wordl.split(" ");
  for(var i = 0; i < splited.length; i++)
  {
    if(splited[i].length > longestWord){ 
	longestWord = splited[i].length;
    reallongest=splited[i] 
    }
}
console.log("q4")
console.log(longestWord,reallongest)