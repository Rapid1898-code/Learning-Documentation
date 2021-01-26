# JAVASCRIPT
---

#### OPERATOR, INPUT, OUTPUT [jump to...](#operator-input-output)
#### STRING [jump to...](#string)
#### ARRAY [jump to...](#array)
#### CONTROL STRUCTURE AND ITERATION [jump to...](#control-structure-and-iteration)
#### FUNCTION [jump to...](#function)
#### OBJECT [jump to...](#object)
#### CONSTRUCTOR, CLASS [jump to...](#constructor-class)
#### DOCUMENT, QUERYSELECTOR, EVENTLISTENER [jump to...](#document-queryselector-eventlistener)
#### CSS VARIABLE HANDLING [jump to...](#css-variable-handling)
#### API ACCESS [jump to...](#api-access)
#### JQUERY [jump to...](#jquery)
#### DATE [jump to...](#date)
#### MATH [jump to...](#math)


---
## OPERATOR, INPUT, OUTPUT
[jump to top...](#javascript)<br><br>
<br>Comments in Javascript
```markdown
// Comment something
```
Multiline comments
```markdown
/*Text xzy*/
```
Declare and assign string (possible with "" or '') - "var" was the earlier version in the past for that
```markdown
let intStr = "7"
```
Linebreak and Tab should not used - is morely css-stuff for formating
```markdown
"/n /t"
```
Declare a variable and assign int (also signed int like -36)
```markdown
let age = 25
```
Defining without assigning (var gets value undefined)
```markdown
let var
```
Declare a constant and assign int (constant can not be changed like variables)
```markdown
const age = 25
```
Declare and assign float (also signed float like +4.5763
```markdown
let float = 5.14876
```
Change String to Int with base 10
```markdown
let intNum = parseInt(intStr,10);
```
Declare and assign string
```markdown
let floatStr = "5.14673"
```
Change String to Float
```markdown
let floatNum = parseFloat(floatStr);
```
Defines+Assigns a variable (if user exists/has a value use that - otherwise initialize with "guest"
```markdown
let v = user || "guest"
```
Open windows for entering something and store in const inp
```markdown
const inp = prompt("Enter:")
```
Convert numeric value to string
```markdown
num.toString()
```
2nd method to convert numeric value to string
```markdown
num + ""
```
3rd method to convert number / int to a String
```markdown
String(n)
```
Converts String to Number / Int
```markdown
Number(s)
```
Shows the type of the variable (eg. number, string, boolean)
```markdown
typeof x
```
Modulo / Rest of the division (=> 1)
```markdown
7 % 2
```
Check 2 values / variables (result in true / false)
```markdown
x == y
```
Equal value and equal type
```markdown
x === y
```
Not equal
```markdown
x != y
```
Not equal value and not equal type
```markdown
x !== y
```
Greater, lesser, greater + equal , lesser + equal
```markdown
>,<,>=,<=
```
Check if value is NaN (NotANumber) - eg. when converting with Number() and the value is no number
```markdown
isNaN(x)
```
Check if n is a integer
```markdown
Number.isInteger(n)
```
Makes variable +1
```markdown
num++;
```
Outputs variable num in console
```markdown
console.log(num)
```
Outputs element as table (eg. for objects, arrays)
```markdown
console.table(object)
```
Alert information in a window
```markdown
alert("Text!")
```
Alert some text with outputing the variable "name" between (using backticks "`"
```markdown
alert(`Bla ${name} bla`)
```
Round to 2 decimal digits
```markdown
n = n.toFixed(2)
```



---
## STRING
[jump to top...](#javascript)<br><br>
<br>Define a string
```markdown
let s = "this is a test"
```
String with linebreak \n
```markdown
let s = "this \n text"
```
show the whole string
```markdown
s[0]
```
extracht only the first character
```markdown
s[0,1]
```
last char of a string
```markdown
s[-1]
```
slicing 2 chars from pos 3 and 4
```markdown
s.slice[3,5]
```
slice from pos 3 to the end
```markdown
s.slice[3]
```
shows the length of the string
```markdown
s.length
```
Lowercase the whole string
```markdown
s.toLowerCase()
```
Uppercase the whole string
```markdown
s.toUpperCase()
```
Returns the second char of a string
```markdown
s.charAt(1)
```
Search if "xyz" is int the string - returns the position where found - when not found returns -1
```markdown
s.search("xyz")
```
Check if string/chars are in
```markdown
s.includes("ee")
```
Delete all whitespaces at the beginning and the end
```markdown
s.trim()
```
Repeat string 3 times
```markdown
s.repeat(3)
```
Split the words in a array
```markdown
s.split(" ")
```
Delete all whitespaces at the beginning and the end
```markdown
s.trim()
```
Fills leading zero in a string with allways 3 chars - eg. 006
```markdown
s.padstart(3,"0")
```
Find Index of first occurence of this string
```markdown
s.indexOf("ee")
```
Outputs the x character in the string => second char of the string (same as s[1])
```markdown
s.charAt(1)
```
Get the last 3 chars of the string
```markdown
s.slice(-3)
```
2nd variant: Get the last 3 chars of the string
```markdown
s.substr(s.length-3)
```
Return Ascii-Code of the first character of the string
```markdown
s.charCodeAt(0)
```
Returns char for specific ascii-code
```markdown
char = String.fromCharCode(65)
```
Check if char is in A-Z
```markdown
char.match(/[A-Z]/i)
```



---
## ARRAY
[jump to top...](#javascript)<br><br>
<br>Define an array
```markdown
let arr = [];
```
Define an array and initialize it
```markdown
let arr = [6,7,8];
```
Define multidim array
```markdown
let mat= [[1,2,3],[4,5,6],[7,8,9]]
```
Get second element => 7
```markdown
arr[1]
```
Access last element in array
```markdown
arr[arr.length-1]
```
Get element in the matrix => 5
```markdown
mat[1][1]
```
Replace the third element
```markdown
arr[2] = 9
```
Returns list as a string => "6,7,8"
```markdown
String(Arr)
```
Must allways be compared with triple = (only == would be wrong)
```markdown
a1 === a2
```
Total count of the elemets in the array
```markdown
arr.length
```
Extracts and delete element at the end (fast!)
```markdown
arr.pop()
```
Extracts and delete element at the begin (slow!)
```markdown
arr.shift()
```
Append new elements to the array at the end (fast!)
```markdown
arr.push("X","Y")
```
Add new elements to the array at the beginning (slow!)
```markdown
arr.unshift("Y","Z")
```
Copy elements from index 2 to index 3 => result is one char at index 2
```markdown
ergArr = arr.slice(2,3)
```
Copy the last 2 elements of the array
```markdown
ergArr = arr.slice(-2)
```
Delete 1 element beginning from index 2
```markdown
arr.splice(2,1)
```
Delete 2 elements beginning from the index 0 - and insert the elements 10 and 11
```markdown
arr.splice(0,2,10,11)
```
From index -1 delete 0 elements and add 3 and 4
```markdown
arr.splice(-1,0,3,4)
```
Delete 2 elements beginning from the index 0 - and assign them to ergArr
```markdown
ergArr = arr.splice(0,2)
```
Concatenate 2 arrays to one
```markdown
ergArr = arr1.concat(arr2)
```
Returns first index position of element "xyz" (if not exists result is -1)
```markdown
arr.indexOf("xyz")
```
Return the last index position of the element "xyz"
```markdown
arr.lastIndexOf("xyz")
```
Check if string exists in the array
```markdown
arr.includes("xyz")
```
Reverse the entire array
```markdown
arr.reverse()
```
Split the words in a array
```markdown
arr = varStr.split(" ")
```
Join the elements from the array in a string with ", " as seperator
```markdown
varStr = arr.join(", ")
```
Check if object is an array (if array = true)
```markdown
Array.isArray(arr)
```
Iterate through index of the array
```markdown
for (let i=0; i < arr.lenth; i++) {do smth.}
```
Iterate through array elements
```markdown
for (let elem of arr) {alert(arr)}
```
Convert a node-list to an array
```markdown
arr=Array.from(document.querySelectorAll("a"))
```
2nd method for converting node-list to an array
```markdown
arr=[...document.querySelectorAll("a")]
```

<br>Iterate trough array by index and element (with shortform)<br>
Outputs index and Outputs element of array
```markdown
arr.forEach((elem,idx) => {
    console.log(idx)
    console.log(elem)
})
```

<br>Iterate through array by elements and index (with longform)<br>
Outputs index and Outputs element of array
```markdown
arr.forEach(function(elem,idx) {
    console.log(idx)
    console.log(elem)
})
```

Maps a functionality to all elements of the array - every element multiplicated by 2
```markdown
newarr = arr.map(x => x * 2);
```
Concatenate the array to a string seperated by " "
```markdown
arr.join(" ")
```

Order array ascending
```markdown
arr.sort((a,b) => a > b ? 1 : -1)
```
Order array descending
```markdown
arr.sort((a,b) => a > b ? -1 : 1)
```
Ordering long method with function
```markdown
arr.sort(function(a,b) {return a > b ? 1 : -1}
```

<br>Filter Method - Long Method (Filters all values which are > 6 eg. in a new array)
```markdown
newarr = arr.filter (function(x){
    if (x > 6) {
        return true
    }
})
```

<br>Short Method in one line
```markdown
newarr = arr.filter(x => x > 6);
```

<br>Reduce Method - for doing something with the array and output / calculate something<br>
"total" is the new calculation element - result of this is the sum of all elements of the array<br>
every element is added to total - 0 is the default value of "total"
```markdown
erg = arr.reduce ((total, element) => {
    return total + element
},0)
```



---
## CONTROL STRUCTURE AND ITERATION
[jump to top...](#javascript)<br><br>
If condition with else if and else
```markdown
if (condition is true) {
    =>Do something
}else if (condition is true){
    =>Do something else
}else{
    =>Default else
}
```

<br>If structure with logical and
```markdown
if (a == 9) && (b == 7) { c = "Hurra!" }
```
If structure with logical or
```markdown
if (a == 9) || (b == 7) { c = "Hurra!" }
```
If structure with logical not
```markdown
if !(a > 13)
```

Switch Expression
```markdown
switch (expression) {           // Switch expression for multiple options
case value1:                    // Do something when expression is value1
    // Do something
    break;                      // Break necessary for any case / value
case value2:                    // Do something when expression is value2
    // Do something
    break;
default:                        // When no case is mathing - then do this
    => Do something
    break;
}
```

<br>Iteration from 1 to 5 with for-loop
```markdown
for (let i=1; i<=5; i++) {}
```
Iteration backwards from 3 to 0 with for-loop
```markdown
for (let i=3; i>=0; i--) {}
```
Iterate through an array
```markdown
for (let i=0; i<arr.length; i++) {}
```

<br>While loop with break condition
```markdown
while (x < 4) {
    if xyz === "abc" {break}
}
```

<br>Do While loop with break condition
```markdown
do {} while (x < 4)
```
Endless while loop - has to be exited somewhere
```markdown
while (true) {}
```

<br>Iterate through array by elements (x)
```markdown
arr.forEach((x) => {
    console.log(x)
})
```

<br>Are all falsy values - can checked with if (xyz)...
```markdown
0,"",'',null,undefined,NaN
```
Ternary Operator for if - if isNight=true then s=Night - else s=Day
```markdown
isNight ? s="Night" : s="Day"
```



---
## FUNCTION
[jump to top...](#javascript)<br><br>
Normal Function Decleration
```markdown
function addFunc(x=0,y=0) {    // Define a function    - with default value 0 if no input is given
    let erg = x+y              // Calculate erg
    return erg}                // Return erg value
addFunc(3,5)                   // Function Call
```

<br>Function Expression (used for anonymous functions)
```markdown
const add = function(x,y) {...}     // Define a function expression (function is assigned to an variable
add(3,5)                            // Function Call
```

<br>Anonymous Function with Fat Arrow syntax
```markdown
const add = (x,y) => {...}
add(3,5)                            // Function Call
let h = a => a % 3                  // Even shorter without parentees
```

<br>return-statement with "?" or "||"
```markdown
return (age > 18) ? true : console.log('Did parents allow');    // When age > 18 returns true - otherwise output something in the console
return (age > 18) || console.log('Did parents allow');          // Same logic with "||"
```

<br>Use Rest Parameters to accept any number of arguments
```markdown
function max(...numbers) {                // Any numbers of arguments
    => do something with a loop
}
```

<br>AddEventListener with parameters in the function
```markdown
document.querySelector("#dayToday").addEventListener("click",function() {   // define addEventListener as normal but use "function ()"
    toggleBackground("today", 6)                                            // call the function with parameters inside
}, false);
```



---
## OBJECT
[jump to top...](#javascript)<br><br>
properties = attributes of the object (eg. color, shape, minutes, seconds)<br>
methods = functions of the object (eg. start/stop on a stopclock)<br>
everything in javascript is an object (with properties / methods)<br>
eg. arr.length is a property of the object array<br>
eg. arr.pop() is a method of the object array<br>
<br>Define an object (literal syntax)
```markdown
let obj = {}
```
2nd method to define object (construtor syntax)
```markdown
let obj = new Object()
```

<br>Define an object and initialize it
```markdown
let obj = {
    name: "John",
    age: 30,                // last "," i allowed and called trailing / hanging (its easier so to add/remove/move properties of the object)
    shout() {               // Defines a method for the object
        return "Hurra!"
    }
}
```

<br>Access property / shows value of the key "name" (1st method) => John
```markdown
obj.name
```
Shows value of the key "name" (2nd method) => John
```markdown
obj["name"]
```
Shows key "age" of the object => 30
```markdown
obj.age
```
Add a new propertie to the object
```markdown
obj.newOne = "xyz"
```
Add a new method to the object
```markdown
obj.newMethod = function(var) {...do someth...}
```
Call the new method
```markdown
obj.newMethod(25)
```
Check if key is in the object
```markdown
age in obj
```
Delete a property of an object
```markdown
delete obj.age
```
Iterate through the keys of the object and outputs key and value
```markdown
for (let key in obj) {alert(key,alert, obj[key]}
```
Store all the keys of the object in an array
```markdown
Object.keys(obj)
```
Check if a property / method is in an object
```markdown
if ("property" in obj) {...}
```
Check if Object is empty
```markdown
Object.keys(obj).length === 0 && obj.constructor === Object
```


<br>Other example for an object
```markdown
var school = {
  name: 'The Starter League',
  location: 'Merchandise Mart',
  students: 120,
  teachers: ['Jeff', 'Raghu', 'Carolyn', 'Shay']
};
```

<br>4 Pillars of Object Orientation
- Abstraction = hide everything internally what is not usable for the user of the object
- Encapsulation = very object should be independent and not dependencies outside
- Inheritance = objects can take the properties of existing objects
- Polymorphism = redefine methods for derived classes (object can behave in different ways)




---
## CONSTRUCTOR, CLASS
[jump to top...](#javascript)<br><br>
Make a Object with the old method
```markdown
function MakeCar (carMake,carModel,carColor){       // Define the constructor function
    this.make = carMake                             // Define properties for the constructor
    this.carModel = carModel                        // "this" is referencing to the actual object
    this.carColor = carColor
    this.honk = function(){                         // Define a mtehod for the constructor
        alert("BEEP ${this.carModel} BEEP")         // Alert something when the method is called (with prop this.carModel)
    }
}
let car1 = new MakeCar("Honda","Civic","black")     // Create a new car1 (with codeword "new")
let car2 = new MakeCar("Tesla","Roadster","red")    // Create a new car1
```

<br>Make a Object with the new class method
```markdown
class MakeCar{                                      // Define the class
    constructor (carMake,carModel,carColor){        // Define properties for the class
        this.make = carMake                         // Assign the properties of the class to the concrete individual object
        this.carModel = carModel                    // "this" is referencing to the actual object
        this.carColor = carColor
    }
    honk(){                                         // Define a method for the class
        alert("BEEP ${this.carModel} BEEP")         // Alert something when the method is called (with prop this.carModel)
    }
}
let car1 = new MakeCar("Honda","Civic","black")     // Create a new car1 (with codeword "new")
let car2 = new MakeCar("Tesla","Roadster","red")    // Create a new car1
```

<br>Give new property and function
```markdown
MakeCar.prototype.wash = true                       // Give all the created cars from the class "MakeCar" a new property "wash"
MakeCar.prototype.newFunc = function () {           // Give all the created cars from the class "MakeCar" a new function "newFunc"
    console.log("We have a new function!"
}
```



---
## DOCUMENT, QUERYSELECTOR, EVENTLISTENER
[jump to top...](#javascript)<br><br>
Add Eventlistener
```markdown
document.querySelector('#check').addEventListener('click',func1)        // New Method / create an Event Listener / execute function "func1" when mouse is clicked
...'onmouseenter'...                                                    // New Method / create an Event Listener / exceute function "func2" when mouse-cursor is over the element
...'input'...                                                           // Event Listener with trigger input
...'change'...                                                          // Event Listener with trigger every change in the element
...'mousemove'...                                                       // Event Listener with trigger when mouse is moved over the element
...'transitionend'...                                                   // Event Listener with trigger when the transistion ends
document.getElementById("green").onclick = funcGreen                    // Old Method / Waiting for click on this element (by ID) as a "event-listener"
```

<br>E.G. document.querySelector('=>idBlue').addEventListener('click',changeToBlue)
```markdown
function funcGreen() {                                      // Define function
  document.querySelector("body")
    .style.backgroundColor = "rgba(241,63,247,1)"           // Change BackGroundColor-Style to rgba-color green (as inlinecode in the rendering - not in the html-code)
  document.querySelector("body").style.color = "white"      // Change Fontcolor to white (as inlinecode in the rendering - not in the html-code)
}
```

<br>Use EventListner for alle elements with a specific class
```markdown
let elements = document.querySelectorAll(".panel");             // Select all elements with class "panel"
elements.forEach(elem => elem.addEventListener("click",func1))  // Iterate trough every element and create EventListener - when clicked start func1 for the element
function func1() {                                              // Function is run with the activated Element for the EventListener
    this.classlist.toggle("newClass")}
```

<br>Old Method / Select an element by ID
```markdown
document.getElementById
```
New Method / Select (first) a <tag> or .class or =>id
```markdown
document.querySelector("xyz")
```
Select all elements which have h2 and store it in the constante c
```markdown
const c = document.querySelectorAll("h2")
```
Element-Listener waiting for a click7
```markdown
.onclick
```
Change BackgroundColor
```markdown
.style.backgroundColor
```
Change Font Color
```markdown
.style.color
```
Hide element in DOM
```markdown
.style.display = "none"
```
Change Text of the selected element
```markdown
.innerText = "xyz"
```
Concatenate 3 variables with space between (old method)
```markdown
.innerText = v1 + " " + v2 + " " + v3
```
Concatenate 3 variables with space between (new method with the "`"-char called template string)
```markdown
.innerText = `${v1} ${v2} ${v3}`
```
Read the value/text of the field
```markdown
.value
```
Show the ID of the selected element
```markdown
.id
```
Set the src of a image
```markdown
.src
```
Manipulate classes informations
```markdown
.classList
```
Toggle the class hidden (when triggered class is deleted OR added (when the next click occured)
```markdown
.classList.toggle("hidden")
```
Add the class hidden
```markdown
.classList.add("hidden")
```
Check if element contains class "cl"
```markdown
.classList.contains("cl")
```
Remove the class from the element
```markdown
.classList.remove("wiggle")
```
Call function "func1" every second (1000ms)
```markdown
setInterval(func1, 1000)
```
Do something any 10 seconds
```markdown
setInterval(()=> {do something},10000)
```
Do something and wait 1 second
```markdown
setTimeout(()=> {do something,1000}]
```



---
## CSS VARIABLE HANDLING
[jump to top...](#javascript)<br><br>
Read all control- and input-elements<br>
Output is not an array - its a node-list (does not have all methods like an array)
```markdown
let inputs = document.querySelectorAll(".controls input");
```


Wait for change in any element and call the function "handleUpdate"
```markdown
inputs.forEach(input => input.addEventListener("change", handleUpdate));
```

<br>Handle Update<br>
(For definition and using the variables in CSS have a look at CSS.txt)
```markdown
function handleUpdate() {
    const suffix = this.dataset.sizing || '';       // read the sizing-parameter for the triggered element (used data-sizing in html)
    document.documentElement.style.setProperty(`--${this.name}`, this.value + suffix);
        // set the variable in css (name according to --name in css)
        // use the value from the read element from the adventlistener
        // and use the suffix which is read above
        // full property looks eg. like "--spacing: 10px"
}
```


---
## API ACCESS
[jump to top...](#javascript)<br><br>
<a href="https://learn.shayhowe.com/advanced-html-css/jquery/" style="font-style: italic">https://learn.shayhowe.com/advanced-html-css/jquery/</a>
<br>request data from API  get data back in JSON format
<br>Reading / Fetching the informations from an API-url
<br>Request the API-content and output as JSON-information
<br>alle the information is stored in data
<br>last part is the error handling when something wrong happens
```markdown
fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })
    .catch(err => {
        console.log("error ${err}")
    });
```

<br>sometimes the URL also hase a search query parameter<br>
eg. <a href="https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita" style="font-style: italic">https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita</a><br>
"s" is the parameter and "margarita" the serach string<br>
eg. <a href="https:/api.nasa.gov/planetary/apod?api_key=DemoKey&date=2020-10-10" style="font-style: italic">https:/api.nasa.gov/planetary/apod?api_key=DemoKey&date=2020-10-10</a><br>
here are used 2 parameters - one "api-key" and the second "data"

=>eg. use horoscope api<br>
<a href="https://aztro.readthedocs.io/en/latest/" style="font-style: italic">https://aztro.readthedocs.io/en/latest/</a><br>
need to use browserify<br>
<a href="http://browserify.org/#install" style="font-style: italic">http://browserify.org/#install</a><br>
so the require can also run with html (otherwise it only works in the IDE)<br>
parse the JSON-content to an object: let obj = JSON.parse(body)



---
## JQUERY
[jump to top...](#javascript)<br><br>
library for javascript<br>
- Traversing<br>
- Manipulating<br>
- Events<br>
- Effects

include before body-tag
```markdown
<script src="=>ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
```
<br>put all jQuery code in this function (waiting until the the page has loaded an the DOM is ready)
```markdown
$(document).ready(function(event){...});
```
Class selector
```markdown
$('.feature');
```
Descendant selector
```markdown
$('li strong');
```
Multiple selector
```markdown
$('em, i');
```
Attribute selector
```markdown
$('a[target="_blank"]');
```
Pseudo-class selector
```markdown
$('p:nth-child(2)');
```



---
## DATE
[jump to top...](#javascript)<br><br>
<br>Assign variable to actual date
```markdown
let now = new Date()
```
Assign actual seconds from actual date variable "now"
```markdown
let secondes = now.get.Seconds()
```



---
## MATH
[jump to top...](#javascript)<br><br>
<br>Random number between 1 and 6 like a cube (Math.random returns value between 0 and 1)
```markdown
Math.floor(Math.random()*6) + 1
```
Nearest Upward rounding => 44
```markdown
Math.ceil(43.8)
```
Return the square-root => 3
```markdown
Math.sqrt(9)
```
Use PI
```markdown
Math.PI
```
Round down the float => 5
```markdown
Math.floor(5.95)
```
First number to the power of the second => 8
```markdown
Math.pow(2,3)
```
Creates the cube root => 3
```markdown
Math.cbrt(8)
```
Returns the absolute number => 3
```markdown
Math.abs(-3)
```
Returns the Minimum of the values => 1
```markdown
Math.min(1,2,3)
```
Returns the Maximum of the values => 3
```markdown
Math.max(1,2,3)
```










