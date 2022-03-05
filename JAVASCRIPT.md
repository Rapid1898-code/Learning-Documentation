# JAVASCRIPT
---

#### OPERATOR, INPUT, OUTPUT [jump to...](#operator-input-output)
#### STRING [jump to...](#string)
#### ARRAY [jump to...](#array)
#### CONTROL STRUCTURE AND ITERATION [jump to...](#control-structure-and-iteration)
#### FUNCTION [jump to...](#function)
#### OBJECT [jump to...](#object)
#### CONSTRUCTOR, CLASS [jump to...](#constructor-class)
#### OBJECT ORIENTATION - 4 PILLARS OOP [jump to...](#object-orientation---4-pillars-oop)
#### DOCUMENT, QUERYSELECTOR, EVENTLISTENER [jump to...](#document-queryselector-eventlistener)
#### CSS VARIABLE HANDLING [jump to...](#css-variable-handling)
#### API ACCESS [jump to...](#api-access)
#### JQUERY [jump to...](#jquery)
#### DATE [jump to...](#date)
#### MATH [jump to...](#math)
#### LOCAL STORAGE [jump to...](#local-storage)
#### MODULE EXPORTS [jump to...](#module-exports)
#### ASYNCHRONOUS HANDLING [jump to...](#asynchronous-handling)
#### REQUESTS [jump to...](#requests)
#### NODE.JS [jump to...](#node.js)
#### REACT [jump to...](#react)
#### TOOLS OVERVIEW [jump to...](#tools-overview)
#### EXAMPLE FULL STACK [jump to...](#example-full-stack)
#### AZURE AUTHENTICATION [jump to...](#azure-authentication)
#### PKG (create executable from node.js) [jump to...](#pkg-(create-executable-from-node.js))
#### HEROKU (hosting web-apps, running scripts in the cloud) [jump to...](#heroku-(hosting-web-apps-running-scripts-in-the-cloud))
#### NODEMAILER (send mails) [jump to...](#nodemailer-(send-mails))

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
let age = 24
```
Defining without assigning (var gets value undefined)
```markdown
let var
```
Define 2 variables (one without value and one with value)
```markdown
let var, age = 25
```
Define and assign 3 variables (a=5, b=8, c=12)
```markdown
let [a, b, c] = [5, 8, 12]
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
Shows the type of the variable as string (eg. "number", "string", "boolean")
```markdown
typeof (x)
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
Swap 2 variables
```markdown
[x, y] = [y, x]
```
Exit javascript node program
```markdown
process.exit(1)
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
extract only the first character
```markdown
s.slice(0,1)
```
last char of a string
```markdown
s.slice(-1)
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
s = s.toLowerCase()
```
Uppercase the whole string
```markdown
s = s.toUpperCase()
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
Replace "abc" with "xyz" for any occurrences in the string (only working for new browsers!)
```markdown
sNew = s.replaceAll("abc","xyy)
```
2nd method for replacing everything (works for more browsers!)
```markdown
sNew = s.replace(/abc/g,"xyz")
```
Concatenate 2 strings
```markdown
sNew = s1.concat(s2)
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
Returns True if the string end with "?"
```markdown
s.endsWith("?")
```
Returns char for specific ascii-code
```markdown
char = String.fromCharCode(65)
```
Check if char is in A-Z
```markdown
char.match(/[A-Z]i)
```
Spread-Operator for string (=> build array with each character)
```markdown
[...s]
```
Convert object-element to string
```markdown
s = JSON.stringify(obj)
```
Convert datetime-object to string in format "yyyy-mm-dd"
```markdown
calcDate.toISOString().split('T')[0]
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
x > 0)                           => Return true if all elements are bigger than 0
```markdown
arr.every(x
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
Concatenate the array to a string seperated by " "
```markdown
arr.join(" ")
```
a > b ? 1 : -1)               => Order array ascending
```markdown
arr.sort((a,b)
```
a > b ? -1 : 1)               => Order array descending
```markdown
arr.sort((a,b)
```
Ordering long method with function
```markdown
arr.sort(function(a,b) {return a > b ? 1 : -1}
```
Find max value in an array with spread operator
```markdown
Math.max(...arr)
```
Find min value in an array with spread operator
```markdown
Math.min(...arr)
```
Array Destrucuring Expl1 (a will be "Ha" and b will be "Ho"
```markdown
let [a,b] = ["Ha","Ho","Hi","He"]
```
Array Destrucuring Expl2 (a will be "Ha" and d will be "He"
```markdown
let [a,,,d] = ["Ha","Ho","Hi","He"]
```
Array Destrucuring Expl3 (a will be "Ha" and rest will be ["Ho","Hi","He"]
```markdown
let [a,...rest] = ["Ha","Ho","Hi","He"]
```
Swapping values (a will be b and b will be a)
```markdown
[a,b] = [b,a]
```

<br>Iterate trough array by index and element (with shortform)<br>
<br>Outputs index and Outputs element of array
<br>(return is not working here - forEach loops are allways running for all elements)
```markdown
arr.forEach((elem,idx) => {
    console.log(idx)
    console.log(elem)
})
```

<br>Iterate through array by elements and index (with longform)<br>
<br>Outputs index and Outputs element of array
<br>(return is not working here - forEach loops are allways running for all elements)
```markdown
arr.forEach(function(elem,idx) {
    console.log(idx)
    console.log(elem)
})
```

<br>Iterate trough an array with 1sec pause at every element
```markdown
names.forEach((name, i) => {
  setTimeout(() => {
    display(name);
  }, i * 1000);
});
```

<br>Map Method - Short Method (Maps a functionality to all elements of the array - every element multiplicated by 2)
```markdown
    let newarr = arr.map(x => x * 2);
```

<br>Map Method - Long Method (for more code)
```markdown
    let newarr = arr.map (function(x) {
        x = x * 2
    }
```

<br>Filter Method - Long Method (Filters all values which are > 6 eg. in a new array)
```markdown
let newarr = arr.filter (function(x){
    if (x > 6) {
        return true
    }
})
```

<br>Filter Method - Short Method in one line
```markdown
let newarr = arr.filter(x => x > 6);
```

<br>Reduce Method - for doing something with the array and output / calculate something
<br>"total" is the new calculation element - result of this is the sum of all elements of the array
<br>every element is added to total - 0 is the default value of "total"
```markdown
erg = arr.reduce ((total, elem) => {
    return total + elem
},0)
```

<br>FindIndex Method - find the index-location of an element in the array (if nothing is found it returns -1)
```markdown
let idx = arr.findIndex(x => {
  return x < 10;
})

```

<br>Some Method - checks whether at least one element in the array passes the test - returns boolean answer
<br>1st line defines the check function - 2nd line checks the array with the function
```markdown
const even = (element) => element % 2 === 0;
arr.some(even)
```

<br>Every Method - checks whether all elements in the array passed the test by the defined function - return boolean answer
<br>1st line defines the check function - 2nd line checks the array with the function
```markdown
const isLower = (elem) => elem < 40;
arr.every(isLower)
```

<br>example for a setTimeout
<br>the first and second message will appear immediately - the middle message only after 2 seconds
```markdown
console.log('First message!');
setTimeout(() => {
   console.log('This message will always run last...');
}, 2000);
console.log('Second message!');
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
case value1: case value 4       // Do something when expression is value1 or value4
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
Iterate through a string
```markdown
for (let char of text) {}
```
Iterate through the keys of an object
```markdown
for (let key in obj) {}
```

<br>For loop with pause at any iteration
```markdown
for (let i = 0; i < 5; i++) {
  setTimeout(() => {                            // Pause at any iteration for 5 seconds / 5000 ms
    console.log("hey");
  }, i * 5000);
}
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

<br>Access property / shows value of the key "name" (1st method) => John (dot.notation)
```markdown
obj.name
```
Shows value of the key "name" (2nd method) => John (bracket notation)
```markdown
obj["name"]
```
Shows key "age" of the object => 30 (dot notation)
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
Delete a property of an object (dot notation)
```markdown
delete obj.age
```
Delete a property of an object (bracket notation)
```markdown
delete obj["age nr"]
```
Check if a property / method is in an object
```markdown
if ("property" in obj) {...}
```
Read the keys of an object into an array
```markdown
arr = Object.keys(obj)
```
Read the values of an object into an array
```markdown
arr = Object.values(obj)
```
Read alle key / value pairs of an object into an (nested) array
```markdown
arr = Object.entries(obj)
```
Check if xyz i part of the object
```markdown
obj.hasOwnProperty("xyz")
```


<br>Check if Object is empty
```markdown
Object.keys(obj).length === 0 && obj.constructor === Object
```

<br>Iterate through the keys of the object and outputs key and value
```markdown
for (let key in obj) {
    console.log(key, obj[key]
}
```

<br>Other example for an object
<br>teacher count must have quotations cause it contains a space character
```markdown
var school = {
  name: 'The Starter League',
  location: 'Merchandise Mart',
  "teacher count": 10
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
    this.make = carMake,                            // Define properties for the constructor
    this.carModel = carModel,                       // "this" is referencing to the actual object
    this.carColor = carColor,
    this.honk = function(){                         // Define a mtehod for the constructor
        alert(`BEEP ${this.carModel} BEEP`)         // Alert something when the method is called (with prop this.carModel)
    }
}
let car1 = new MakeCar("Honda","Civic","black")     // Create a new car1 (with codeword "new")
let car2 = new MakeCar("Tesla","Roadster","red")    // Create a new car1
```

<br>Make a Object with the shorthand
```markdown
let robotFactory = (model, mobile) => {             // Define constructor with two parameters
    return {
        model: model,                               // property1
        mobile: mobile,                             // property2
        beep(){                                     // method
            console.log("Beep Boop")
        }
    }
}
```

<br>Make a Object with the new class method (longhand)
```markdown
class MakeCar{                                      // Define the classs
    constructor (carMake,carModel,carColor){        // Define properties for the class
        this.make = carMake                         // Assign the properties of the class to the concrete individual object
        this._carModel = carModel                    // "this" is referencing to the actual object (use "_" to indicate that this properties should only changed with getters)
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

<br>Define a getter in the class (returns the name-property of the class-element
<br>So when somebody is requesting for obj.name - the return will be for _name
<br>When somebody is changing with obj.name = "xzy" - nothing happens, cause the property is named _name
<br>Of course with obj._name there would be a change possible - but this is very bad practice cause due the "_" the variable should not be touched
```markdown
  get name() {
    return this._name;
  }
```

<br>Inherit a class from another class
<br>The class Cat inherits from the class Animal with the keyword "extends"
<br>With super - the attributes name and age will be taken / inherit from the class Animal
```markdown
class Animal {
  constructor(name, age){
	this.name = name
	this.age = age
  }
  speak() {
	console.log("Blablabla")
  }
}

class Cat extends Animal {
  constructor(name, age, usesLitter) {
    super(name, age);
    this._usesLitter = usesLitter;
  }
}
```

<br>Define static function - this can only be done for the class itself (or for the instances of the class)
```markdown
    static generateName() {...}
```



---
## OBJECT ORIENTATION - 4 PILLARS OOP
[jump to top...](#javascript)<br><br>
4 pillars of object orientation in practice
class Animal {              // ENCAPSULATION - storing properties and methods together in one object
constructor(name) {     // (made it easier to add new stuff / easier to read)
this._name = name   // ABSTRACTION - name of the object will be set to _name (so hidden)
}
get name() {            // using a getter to return when somebody wants the name with obj.name
return this._name
}
speak() {
console.log(`${this._name} makes a sound`)
}
}

class Dog extends Animal {      // INHERITANCE - make class from another class (share parent properties / methods)
constructor(name, breed) {  // (helps to elimante redundant code)
super(name)             // grabs / inherits the "this._name = name" from the class Animal
this._breed = breed     // abstract the breed with _breed (could / should not be touched from anybody)
}
get breed() {
return this_breed
}
speak() {
super.speak()           // grab the speak method from the parent class Animal
console.log(`${this._name} barks`)  // get an additonal output (so one line from the parent class and one individual)
}
}

class Cat extends Animal {
constructor(name, breed) {
super(name)
this._breed = breed
}
get breed(){
return this._breed
}
speak() {
super.speak()
console.log(`${this.name} meows`)
}
}

let simba = new Dog("Simba", "Shepard")
let machi = new Dog("The Machine", "Pitbull")
let salem = new Cat("Salem", "American Shorthair")

let farm = [simba,machi,salem]
for (a of farm) {       // POLYMORPHISM code written to use interface (eg. speak-function) and
a.speak()           // knows how to use it at different objects (eg. barks or meows)
}                       // (helps to avoid if/else and switch cases)




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
Change class of the element to "MyClass"
```markdown
.className = "MyClass";
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
{do something},10000)          => Do something any 10 seconds
```markdown
setInterval(()
```
Func1 is running with a delay of at least 2 seconds (with own seperate function)
```markdown
setTimeout(func1, 2000)
```
{do something},1000)            => Do something and wait 1 second (function direct in the statement)
```markdown
setTimeout(()
```

<br>Add some elments to an ul-element
```markdown
var li = document.createElement("li")           // create new li-element
li.textContent = "new text"                     // add text to the new element
document.querySelector("ul").appendChild(li)    // append the new li-element to the ul-element
```



---
## CSS VARIABLE HANDLING
[jump to top...](#javascript)<br><br>
Read all control- and input-elements<br>
Output is not an array - its a node-list (does not have all methods like an array)
```markdown
let inputs = document.querySelectorAll(".controls input");
```


<br>input.addEventListener("change", handleUpdate));    => Wait for change in any element and call the function "handleUpdate"
```markdown
inputs.forEach(input
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

<br>Using a API using async / await
```markdown
async function getSomethingFromAPI() {
	const res = await fetch("url").catch(e => {
		console.log("Error - Fetch not possible...")
	})
	if (!data) {
		console.log("Error - Data / JSON wrong...")
	} else {
		const data = await res.json()
		console.log(data)
	}
}
getSomethingFromAPI()
```

<br>sometimes the URL also has a search query parameter<br>
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

<br>ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>      => include before body-tag
```markdown
<script src="
```
put all jQuery code in this function (waiting until the the page has loaded an the DOM is ready)
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
Returns numeric acttual date as number (helpful to calculate some timespans)
```markdown
let t1 = Date.now()
```
Assign actual seconds from actual date variable "now"
```markdown
let secondes = now.get.Seconds()
```
Convert datetime-object to string in format "yyyy-mm-dd"
```markdown
calcDate.toISOString().split('T')[0]
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



---
## LOCAL STORAGE
[jump to top...](#javascript)<br><br>
Allows to store data across browser sessions<br>
Set item to local storage (name is the key and Bob is the value)
```markdown
localStorage.setItem ("name","Bob")
```
Get item from local storage (name is the key)
```markdown
localStorage.getItem ("name")
```
Delete item from local storage (name is the key)
```markdown
localStorage.delItem ("name")
```
Delete the whole local storage
```markdown
localStorage.clear()
```



---
## MODULE EXPORTS
[jump to top...](#javascript)<br><br>
Define module with Node.js (in a file)
```markdown
let Obj = {}            // define an object
Obj.prop = "xyz"        / define something in the object eg. a function
module.exports = Obj    // export the file as module to node.js
```

<br>Use a module
```markdown
const Obj = require('./module.js');     // import the module for using
Obj.funcFromModule                      // use the function from the module
```

<br>Define module with export
```markdown
let Menu = {};
export default Menu;
```

<br>Import module with import
```markdown
import Menu from './menu';
```



---
## ASYNCHRONOUS HANDLING
[jump to top...](#javascript)<br><br>
running synchronous - outputs 1,2,3
```markdown
function houseOne(){ console.log('Paper delivered to house 1')}
function houseTwo(){console.log('Paper delivered to house 2')}
function houseThree(){console.log('Paper delivered to house 3')}
houseOne()
houseTwo()
houseThree()
```

<br>running asynchronous - outputs 1,3 and then after 3 seconds 2
<br>in the 2nd function the setTimeout-api is called with a delay of 3000ms / 3 seconds
```markdown
function houseOne(){ console.log('Paper delivered to house 1')}
function houseTwo(){
	setTimeout(() => console.log('Paper delivered to house 2'), 3000)
}
function houseThree(){console.log('Paper delivered to house 3')}
houseOne()
houseTwo()
houseThree()
```

<br>running asynchronous - outputs 1, after 3sec => 2 and immediately afterwards 3
<br>the 2nd function is using a callback (using a function)
<br>setTimeout is called with a 3sec delay - then 2 is printed - and then with callback() 3 as the argument of the function 2
```markdown
function houseOne(){ console.log('Paper delivered to house 1')}
function houseTwo(callback){
    setTimeout(() => {
        console.log('Paper delivered to house 2')
        callback()
    }, 3000)
}
function houseThree(){console.log('Paper delivered to house 3')}
houseOne()
houseTwo(houseThree)
```

<br>using a promise (promise is an object)
```markdown
const promise = new Promise((resolve, reject) => {		// define the promise and asign to a variable
    const error = false
    if(!error){
        resolve('Promise has been fullfilled')			// when the promise is resolved
    }else{
        reject('Error: Operation has failed')			// when there is an error
    }
})
console.log(promise)
promise
    .then(data => console.log(data))		// doing this when the promise is resolved
    .catch(err => console.log(err))			// doing this when the promise is not resolved has an error
```

<br>using async / await
```markdown
function houseOne(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Paper delivered to house 1')
        }, 1000)
    })
}
function houseTwo(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Paper delivered to house 2')
        }, 5000)
    })
}
function houseThree(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Paper delivered to house 3')
        }, 2000)
    })
}
async function getPaid(){						// defining a async function
    const houseOneWait = await houseOne()		// awaits the ending of function houseOne
    const houseTwoWait = await houseTwo()		// waiting for ending function houseTwo
    const houseThreeWait = await houseThree()	// waiting for ending function houseThree
    console.log(houseOneWait)
    console.log(houseTwoWait)
    console.log(houseThreeWait)
}
getPaid()										// after 5seconds (longest functtion running) the output is done
```

<br>create an executor function
```markdown
const executorFunction = (resolve, reject) => {
  if (someCondition) {
      resolve('I resolved!');
  } else {
      reject('I rejected!');
  }
}
```

<br>construct a new variable with "new Promise"
```markdown
const myFirstPromise = new Promise(executorFunction)
```

<br>example for a promise handling with resolve, reject and .then
```markdown
let prom = new Promise((resolve, reject) => {
  let num = Math.random();
  if (num < .5 ){
    resolve('Yay!');
  } else {
    reject('Ohhh noooo!');
  }
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

const handleFailure = (rejectionReason) => {
  console.log(rejectionReason);
};

prom.then(handleSuccess, handleFailure);
```

<br>example using a promise with .then and .catch
<br>.then is handling the resolved part and .catch is handling the rejected part
```markdown
prom
  .then((resolvedValue) => {
    console.log(resolvedValue);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
```

<br>define a async-function with function declaration:
```markdown
async function myFunc() {
  // Function body here
};
```

<br>define a async-function with function expression
```markdown
const myFunc = async () => {
  // Function body here
};
```

<br>example for handling a async function
```markdown
async function withAsync(num){
  if (num === 0){
      return 'zero';
    } else {
      return 'not zero';
    }
}
```



---
## REQUESTS
[jump to top...](#javascript)<br><br>
<br>create xml http request object instances
```markdown
const xhr = new XMLHttpRequest()
```
assing the url
```markdown
const url =  'https://api-to-call.com/endpoint'
```
set the resonse type to json
```markdown
xhr.responseType = 'json'
```
{}                   =>
```markdown
xhr.onreadystatechange = ()
```

<br>use GET statement for reading an URL
```markdown
xhr.onreadystatechange = () => {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    return xhr.response;
  }
xhr.open('GET', url);
xhr.send();
};
```

<br>use POST statement for writing something back to an URL
```markdown
const xhr = new XMLHttpRequest();
const url = 'https://api-to-call.com/endpoint';
const data = JSON.stringify({id: '200'});

xhr.responseType = 'json';

xhr.onreadystatechange = () => {
  if(xhr.readyState === XMLHttpRequest.DONE){
    return xhr.response;
  }
}

xhr.open('POST', url);
xhr.send(data);
```



---
## NODE.JS
[jump to top...](#javascript)<br><br>
<br>https://nodejs.org/en/
```markdown
home of node.js
```
https://nodejs.org/dist/latest-v15.x/docs/api/
```markdown
docu of the modules
```
check if and which node.js version is installed
```markdown
node --version
```
node package manager - show the installed version
```markdown
npm --version
```
create a package.json files with all necessary project informations
```markdown
npm init
```
initialize node-project - with the parameter "-y" without prompting for additonal informations
```markdown
npm init -yarn
```
install module "uuid" - node_modules folder is created - dependencie is added to package.json
```markdown
npm install uuid
```
install module as development dependencie
```markdown
npm install -D nodemon
```
install all modules according to the dependencies in the package.json
```markdown
npm install
```
update the dependencies of the project
```markdown
npm update
```
install several modueles in one line
```markdown
npm i ejs dotenv
```

<br>how to link 2 js-files
```markdown
// in the first file:
const pers = {            // define object in a file
    name: "John",
    age: 30
}
module.exports = pers     // make object usable for other files

// in the second file:
const person = require("./person")      // use person from other file
console.log(person)
```

<br>Setup a simple server
```markdown
const http = require("http")
const fs = require("fs")
http.creatorServer((req,res) => {
	fs.readFile("demofile.html", (err, data) => {
		res.writeHead(200, {"Content-Type": "text/html"})
		res.write(data)
		res.end()
	})
}).listen(8000)
```

<br>Module path
<br>The path module provides utilities for working with file and directory paths.
```markdown
const path = require("path")    // include module
console.log(__filename)         // outputs the whole path of the file
path.basename(__filename)       // outputs only the filename
path.dirname(__filename)        // outputs the dirname of the file
path.extname(__filename)        // outputs the extention of the file
path.parse(__filename)          // outputs several infos as object (root,dir,base,ext,name)
path.parse(__filename).base     // outputs only the base filename
path.join(__dirname, "test", "hello.html")  // use dirname and appends the 2 text-infos to the path
```

<br>Module fs
<br>The fs module enables interacting with the file system
const fs = require("fs")        // include module
```markdown
// Create folder
fs.mkdir(path.join(__dirname, "/test"), {}, (err)  =>  {
    if (err) throw err;
    console.log("Folder created...")
})

// Create and (over)write to file
// write file to the joined path
// name of the file is "hello.txt"
// content of the file is "Hello World!"
fs.writeFile(path.join(__dirname, "/test", "hello.txt"), "Hello World!", (err)  =>  {
    if (err) throw err
    console.log("File written to...")
})

// Create and append to file
fs.writeFile(path.join(__dirname, "/test", "hello.txt"), "Hello World!", (err)  => {...})

// Read file
fs.readFile(path.join(__dirname, "/test", "hello.txt"), "utf8", (err, data)  =>  {
    if (err) throw err
    console.log(data)
})

// Rename file
fs.rename(path.join(__dirname, "/test", "hello.txt"),
            path.join(__dirname, "/test", "hello2.txt"), (err, data)  =>  {
    if (err) throw err
    console.log("File renamed...")
})
```

<br>Module os
The os module provides operating system-related utility methods and properties.<br>
include module
```markdown
const path = require("os")
```
outputs the os platform (eg. win32 for windows, darwin for macos)
```markdown
os.platform()
```
outputs architecture (eg. x64, x32)
```markdown
os.arch()
```
cpu informations (model,speed,times for every core)
```markdown
os.cpus()
```
free memory (eg. 18717655040)
```markdown
os.freemem()
```
total memory (eg. 34237403136 for 32GB RAM)
```markdown
os.totalmem()
```
home directory of the user (eg. c:\Users\Max)
```markdown
os.homedir()
```
uptime of the computer in seconds (eg. 13463)
```markdown
os.uptime()
```
```markdown

=> Module url
=> The url module provides utilities for URL resolution and parsing.
const url = require("url")  => include module
const myUrl = new URL("https://www.xyz.com")     => assign URL
myUrl.href          => the whole url (eg. https://www.rapidtech1898.com/htmlFinanztools/en/aktienbewertungInSekundenEN.html)
myUrl.toString()    => 2nd method to get the whole url
myUrl.hostname      => the hostname of the url (eg. www.rapidtech1898.com)
myUrl.host          => the host of the url (including port number - when it exists in the url)
myUrl.pathname      => the pathname (eg. /htmlFinanztools/en/aktienbewertungInSekundenEN.html)
myUrl.search        => the search-parameters of the url (eg. ?id=100&status=active)
myUrl.searchParams  => show parameters (eg. URLSearchParams { 'id' => '100', 'status' => 'active' }
myUrl.searchParams.append('abc','123')  => add a parameter with id=abc and value=123

=> Loop through params
```
<br>console.log(`${name}: ${value}`))
```markdown
myUrl.serachParams.forEach((value,name)
```
```markdown

=> Module http
=> The HTTP interfaces in Node.js are designed to support many features of the protocol
const http = require("http")  => include module
```
// Create Server
// Outputs Hello World! on the link "localhost:5000"
<br>{
```markdown
http.createServer((req, res)
```
res.write("Hello World!")
res.end()
<br>console.log("Server running..."))     // running on port 5000
```markdown
}).listen(5000, ()
```
```markdown

=> Simple Server
```
const http = require('http')    // http-module needed
const fs = require('fs')        // fs-module (filesystem) needed
<br>{
```markdown
http.createServer((req, res)
```
{             // reads file and shows it in browser
```markdown
fs.readFile('demofile.html', (err, data)
```
res.writeHead(200, {'Content-Type': 'text/html'})
res.write(data)
res.end()
})
}).listen(8000)                 // listening on port 8000 - access with localhost:8000
```markdown

=> Simple GET-API
```
initial steps:
npm init
touch server.js
npm install express --save

const express = require("express")                  // use express for CRUD
const app = express()                               // Create(POST), Read(GET), Update(PUT), Delete(DELETE)
const PORT = 8000

<br>{
```markdown
app.get("/", (request, response)
```
response.sendFile(__dirname + "/index.html")    // response is at html-file
})

<br>{                            // server listening on port 8000
```markdown
app.listen(PORT, ()
```
console.log(`Server running on port ${PORT}`)
})
```markdown

=> Server with Client connection
```
//Server server.js:
const express = require("express")
const app = express()
const cors = require("cors")
const PORT = 8000
app.use(cors())
let savage = {
"age": 28,
"birthname": "Sayaa Bin Abraham-Joseph",
"birthLocation": "London, England"
}
<br>{     // returns the savage object
```markdown
app.get("/api/savage", (request, response)
```
response.json(savage)
})
<br>{        // listen on port (first entry for hosting on eg. horuku - second one for localhost)
```markdown
app.listen(process.env.PORT || PORT, ()
```
console.log(`Server running on port ${PORT}`)
})

// Client Main.js:
document.querySelector("button").addEventListener("click",getRapName)
async function getRapName(){
try {
const res = await fetch("http://localhost:8000/api/savage")
const data = await res.json()
console.log(data)
} catch(err) {
console.log(err)
}
}

// Client index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>
<h1>Get Rappers birth name</h1>
<h2>Result: </h2>
<button>Click Me</button>
<script src= "js/main.js"></script>
</body>
</html>
JSX: show the "title" only when "showtitle" is true using a ternary expression
```markdown
{showTitle ? title : ""}
```
Define States with default value "" (title is the state, setTitle the state-function)
```markdown
const [title, setTitle] = useState("")
```
```markdown



###### REACT
=> Javascript library for building user interfaces especially for single-page applications (like facebook, twitter etc.)
=> React allows developers to create large web applications that can change data, without reloading the page
components  => webpage is divided in many components (like on facebook)
props       => every component has some properties (size, color, shape, etc.) - arguments are passed into components
states      => and components have states (like the counter for likes / dislikes / unread messages etc.) - if state changed => component has to react and re-render
react       => contains the APIs for creating components
react-dom   => contains the APIs for rendering to the browser DOM
JSX         => syntax extension to JS

npx create-react-app nameProject            => create react app in a folder with the name "nameProject"
npm install --global yarn                   => install yarn (if not allready installed)
yarn start                                  => start the react app (default on http://localhost:3000/)
standard-folder "public" / index.html       => is the base setup for html-file (important is <div id="root"></div> - where everything get rendered from react)
standard-folder "public" / favicon.ico      => icon of the tab
standard-folder "public" / manifest.json    => name, shortname of the react-app (description of the application)
standard-folder "src" / index.js            => entry-point for the react-app (get everything from App and render this to the div-element with the root-id)
standard-folder "src" / app.js              => main react-app called App

<Info></Info>                           => call the component "Info"
<Info />                                => 2nd method to call the component "Info"
{title}                                 => JSX: use the variable "title" in the react html code
<AddItem text="blabla" number={2} />    => Define a prop "text" in a component-call and a numeric prop "number"
function AddItem(props)                 => Use the props in the component (access with props.text or props.number)
function AddItem(text, number)          => Or use the props destructured in the component
function AddItem({text, number=99})     => Define component with default prop for "number"
<p>{props.number}</p>                   => Render the props.number in a paragraph-tag

import { useState } from "react"        => Import useState
const [count, setCount] = useState(0)   => Define States with default value 0 (count is the state, setcount the state-function)
<p>Title: {title} </p>                  => Use the variable in the tags
<button onClick={updateCounterClicked}>Update Counter</button>     => function is called when the button is pressed
const updateCounterClicked = () => {setCount(count + 1)}           => count i incread by one in the function (=when the button is pressed)

=> Use component in a seperate file
```
Define component in sepearte file: export default function Info() {
Import the component and use it: import Info from "./Info.js"

or

Define function as normal: function Info() {
Export the function at the bottom: export default Info;
Import the component and use it: import Info from "./Info.js"
```markdown

=> Simplest possible App.js file
```
import './App.css';
function App() {
return (
<div className="App">
<p>My website is running!</p>
</div>
);
}
export default App;
```markdown

=> Example for a component with class based syntax
```
import React from "react"

class Info extends React.Component {
render() {
const title = "This is my title."
const showTitle = true

return (
<div>
```markdown
        <p>Manage your stuff</p>
      </div>
    )
  }
}

export default Info;
```



<br>Example (with old Class syntax)
```markdown
index.html in folder <public> with: <div id="root"></div>
    => defines initial root-element where all the input goes to
index.js in folder <src> with: ReactDOM.render(<App />, document.getElementById('root'));
    => renders APP and put this in the div with id=root
app.js
    => Import components with:
        import React, { Component } from 'react';
        import './App.css';
        import Header from './Header';
        import SectionMain from './SectionMain';
        import Aside from './Aside';
        import Footer from './Footer';
    => Render components
        class App extends Component {
          render() {
            return (
              <div className="App">
                // call Header with the 2 props
                <Header backColor="green" width="50%"></Header>
                <SectionMain></SectionMain>
                <Aside></Aside>
                <Footer></Footer>
              </div>
            );
          }
        }
footer.js
    => Import react and styling-file
        import React, { Component } from 'react';
        import './Footer.css';
    => Render components
        class Footer extends Component {
          render() {
            return (
                <footer className="Footer">
                </footer>

            );
          }
        }
        export default Footer;
```
header.js
class Header extends Component {
render() {
// header get 2 props
const style = {
width: this.props.width,
backgroundColor: this.props.backColor
}
// using the style object from above to style the header
return (
<header style={style} className="Header-main">
</header>

);
}
}




---
## TOOLS OVERVIEW
[jump to top...](#javascript)<br><br>
https://zellwk.com/blog/crud-express-mongodb/
<br>NODE.JS
```markdown
Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that
runs on the V8 engine and executes JavaScript code outside a web browser.
```

<br>Express
<br>https://zellwk.com/blog/crud-express-mongodb/
```markdown
Is a framework for building web applications on top.
It simplifies the server creation process that is already available in Node.
```

<br>NODEMON
```markdown
Nodemon restarts the server automatically when you save a file that’s used by the server.js
npm install nodemon --save-dev          // insatllation as development dependency

Add this in package.json
    "scripts": {
        "dev": "nodemon server.js"
    }
now you can start nodemon with: npm run dev
```

<br>CRUD
<br>is an acronym for Create, Read, Update and Delete.
```markdown
It is a set of operations we get servers to execute (POST, GET, PUT and DELETE requests respectively).
This is what each operation does:
    Create (POST) - Make something
    Read (GET)- Get something
    Update (PUT) - Change something
    Delete (DELETE)- Remove something
POST, GET, PUT, and DELETE requests let us construct Rest APIs.
```

<br>Package Managers
<br>to automatically download 3rd party packages
```markdown
help automate the process of downloading and upgrading libraries from a central repository
npm (starting 2015) - node package manager
yrn (starting 2016, alternative to npm - but npm packages under the hood)
bower (starting 2013 - older one, was in before npm / yarn popular)
```

<br>Module Bundler
<br>to create a single script file
```markdown
A JavaScript module bundler is a tool that gets around the problem with a build step
(which has access to the file system) to create a final output that is browser compatible
(which doesn’t need access to the file system
browserify (starting 2011)
webpack (starting 2015)
```

<br>Transpiler
<br>to use future JavaScript features
```markdown
Transpiling code means converting the code in one language to code in another similar language.
for CSS eg. Sass, Less, Stylus
for JavaScript eg. babel, TypeScript, CoffeeScript (starting 2010)

```

<br>Task Runner
<br>to automate different parts of the build process
```markdown
For frontend development, tasks include minifying code, optimizing images, running tests, etc.
npm scripts (nowadays the most popular - use the capabilities built into the npm)
grunt, gulp (in earlier times)
```

<br>Template Engines
```markdown
Pug
EJS Embedded Java Script
Nunjucks
```

<br>Postman
<br>Testing APIs in an web-applicaton
```markdown
https://www.postman.com/
```

<br>EJS
<br>Embedded Javascript Template
```markdown
HTML with Javsscript logic in it
eg. for flexible li-elements from a db
<% for (let i=0; i<info.length; i++) {%>
    <li class="rapper">
        <span><%= info[i].stageName %></span>
        <span><%= info[i].birthName %></span>
        <span class="del">delete</span>
    </li>
<% } %>
```

<br>Curl
<br>For testing api endpoints
<br>https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/
```markdown
curl --version                  => Check the installed curl version
curl https://api.github.com     => show all apis from github
curl https://api.github.com/users/zellwk/repos      => show all repos from a specific user (zellwk)
curl https://api.github.com/users/zellwk/repos\?sort\=pushed    => show all repos with parameters ("\" have to be before the "=")
curl -X POST https://api.github.com/user/repos                  => tries to create an repo via api (use -X before the command)
curl -H "Content-Type: application/json" https://api.github.com -v      => shows the header of the api
curl -X POST <URL> -d property1=value1 -d property2=value2              => send data via the api with the -d properties
curl -x POST -u "username:password" https://api.github.com/user/repos   => send post-request with authentification (use -u property)
```

<br>Passport
<br>Passport is authentication middleware for Node.js. Extremely flexible and modular, Passport can be unobtrusively dropped in to
any Express-based web application. A comprehensive set of strategies support authentication using a username and password,
Facebook, Twitter, Azure AD and many more

<br>MVC
<br>Architectural Concept which is used by many frameworks (ruby on rails, django, laravel, etc.)
<br>stands for: Model / View / Controller
<br>https://youtu.be/1IsL6g2ixak
```markdown
never repeat yourself / structured programming
Client (Browser,HTML,CSS,JS) => Server (Linux,Windows,PHP,Ruby,Python) => Database (MySQL,PostgresQL,NoSQL,MongoDB)
View is the Client (only thing the user sees, speaks only with controller, manly html and css)
Controller is the Server (processes requests, server-side logic, middle man between view and model)
Model is the Database (Adding/Retrieving from or to the database, speaks only with the controller)
```

<br>MONGOOSE
Define schemas for the db in the mongoDB
Define how the data-collection (table) in mongoDB looks like


---
## EXAMPLE FULL STACK
[jump to top...](#javascript)<br><br>
full example see: \DEV\LeonNoel-100Devs\class33\rap-names-express
<br>Setting up the project
```markdown
mkdir api-project		// make new directory for project
cd api-project			// change directory to the project
npm init				// initzialize npm project / npm-environment
npm install express		// install express
npm install mongodb/	// install mongodb/
npm install ejs			// install ejs
```

<br>Setup Server / Middleware
```markdown
const express = require('express')
const app = express()
const MongoClient = require('mongodb').MongoClient
const PORT = 2121       // define port for localhost-access
require('dotenv').config()

app.set('view engine', 'ejs')
app.use(express.static('public'))
app.use(express.urlencoded({ extended: true }))
app.use(express.json())
```

<br>Connect to DB
<br>database in this example on Atlas MongoDB
<br>under "Database Access": create an user with password (can be different than the normal Atlas MongoDB login)
<br>under "Network Access": whitelist the IP with which the access is be done
<br>store the critical credentials info in a sepearte file called ".env"
```markdown
// make an ".env" file where the DB-string is stored - and add .env to the .gitignore so the file get not public on github later
DB_STRING = mongodb+srv://<Username from Database Access>:<Password for that user>@cluster0.ram23.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
// define basis for db-connection
let db,
    dbConnectionStr = process.env.DB_STRING,
    dbName = 'rap'
// connect to mongoDB (with error handling)
MongoClient.connect(dbConnectionStr, { useUnifiedTopology: true })
    .then(client => {
        console.log(`Connected to ${dbName} Database`)
        db = client.db(dbName)
    })
    .catch(err =>{
        console.log(`Connection to db not possible - error ${err}`)
    })
```

<<<<<<< HEAD
<br>Setup Server
=======
<br>Listen to the Server / Port
<br>process.env.PORT for Heroku-Access and PORT for localhost-access
>>>>>>> 61569b7546d3c8fea997213d558b450d38fe7f8b
```markdown
app.listen(process.env.PORT || PORT, ()=> {
    console.log(`Server running on port ${PORT}`)
})
```

<br>GET / Read Access example for the API
<br>Read data from the db collection "rappers" - sort them according hte likes - an put it in an array
<br>Call the index.ejs file with the input for "data" (= the array)
<br>(1) server.js: app.get
<br>(2) server.js: reads data from mongodb and triggers the index.ejs to render
<br>(3) index.ejs: renders the file with the given data from mongodb
<br>(4) index.ejs: spits out the actual html
```markdown
app.get('/',(request, response)=>{
    db.collection('rappers').find().sort({likes: -1}).toArray()
    .then(data => {
        response.render('index.ejs', { info: data })
    })
    .catch(error => console.error(error))
})
```

<br>POST / Create example for the API
<br>Add element to the db collection "rappers" -
<br>with the information for stageName / birthName from the form on index.ejs and the field likes with 0
<br>console log on the server and redirect to / for the GET to refreh the page index.ejs (new element get displayed)
<br>(1) index.ejs: form with action ("/insertxyz" and method (POST) - has a text-input and a submit
<br>(2) index.ejs: when submit is clicked the api-action /insertxyz is called with the data
<br>(3) main.js: insert the new collection/dataset in the db
<br>(4) main.js: call the method "/" again to update the index.ejs with GET

```markdown
app.post('/addRapper', (request, response) => {
    db.collection('rappers').insertOne({stageName: request.body.stageName,
    birthName: request.body.birthName, likes: 0})
    .then(result => {
        console.log('Rapper Added')
        response.redirect('/')
    })
    .catch(error => console.error(error))
})
```

<br>PUT / Update example for the API
<br>Update the element in the db collection "rappers" -
<br>Search for stageName and birthName and update the likes-element with +1
<br>make new sort + console.log informatin and response json
<br>(1) main.js: eventlistener in the client-side js
<br>(2) main.js: when element is clicked call the function and make an fetch to the api-call
<br>(3) main.js: awaits response and gives to the server.js the data (put-method, headers, body with the data)
<br>(4) server.js: get the data from the main.js and updates the db - response to the main.js
<br>(5) main.js: awaits the response and reloads the page - so the updated data can be seen
```markdown
app.put('/addOneLike', (request, response) => {
    db.collection('rappers').updateOne({stageName: request.body.stageNameS, birthName: request.body.birthNameS,likes: request.body.likesS},{
        $set: {
            likes:request.body.likesS + 1
          }
    },{
        sort: {_id: -1},
        upsert: true
    })
    .then(result => {
        console.log('Added One Like')
        response.json('Like Added')
    })
    .catch(error => console.error(error))

})
```

<br>DELETE example for the API
<br>Delete the element in the db collection "rappers" -
<br>according to the stageName
<br>console.log informatin and response json
<br>(1)-(5): same as the PUT example only with the methode DELETE
```markdown
app.delete('/deleteRapper', (request, response) => {
    db.collection('rappers').deleteOne({stageName: request.body.stageNameS})
    .then(result => {
        console.log('Rapper Deleted')
        response.json('Rapper Deleted')
    })
    .catch(error => console.error(error))
})
```

<br>HTML example for index.ejs
<br>the css and client-js file is stored in the folder "public" - so it get linked with the ejs-file
<br>all rappers get from the array "info" (is given from data from the server.js file) -
<br>is dynamically written to the html-file (ejs build the html-code and "spits" it out)
<br>in the second part are the form fields for adding new rappers on the html-page
```markdown
// Show current rappers
<h1>Current Rappers</h1>
<ul class="rappers">
<% for(let i=0; i < info.length; i++) {%>
    <li class="rapper">
        <span><%= info[i].stageName %></span>
        <span><%= info[i].birthName %></span>
        <span><%= info[i].likes %></span>
        <span class='fa fa-thumbs-up'></span>
        <span class='fa fa-trash'></span>
    </li>
<% } %>
</ul>

// Add a rapper
<h2>Add A Rapper:</h2>
<form action="/addRapper" method="POST">
    <input type="text" placeholder="Stage Name" name="stageName">
    <input type="text" placeholder="Birth Name" name="birthName">
    <input type="submit">
</form>
```

<br>Local JS example (for the index.ejs)
<br>1st Part: Adenvetlistener for Icons
<br>2nd Part: Deleting and element
<br>3rd Part: Updating the likes / +1 like
```markdown
// AdventListener for all trash and thumbs-up icons
const deleteText = document.querySelectorAll('.fa-trash')
const thumbText = document.querySelectorAll('.fa-thumbs-up')
Array.from(deleteText).forEach((element)=>{
    element.addEventListener('click', deleteRapper)
})
Array.from(thumbText).forEach((element)=>{
    element.addEventListener('click', addLike)
})

// Function for handling deleting locally
// Read the stageName and birthName for the element which should be deleted
// and handover this information to the API (server.js)
// Finally reload the index.ejs with "location.reload()"
async function deleteRapper(){
    const sName = this.parentNode.childNodes[1].innerText
    const bName = this.parentNode.childNodes[3].innerText
    try{
        const response = await fetch('deleteRapper', {
            method: 'delete',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
              'stageNameS': sName,
              'birthNameS': bName
            })
          })
        const data = await response.json()
        console.log(data)
        location.reload()
    }catch(err){
        console.log(err)
    }
}

// Function for handling a +1 like
// Read the stageName and birthName for the element which should be +1 liked
// and handover this information to the API (server.js)
// Finally reload the index.ejs with "location.reload()"
async function addLike(){
    const sName = this.parentNode.childNodes[1].innerText
    const bName = this.parentNode.childNodes[3].innerText
    const tLikes = Number(this.parentNode.childNodes[5].innerText)
    try{
        const response = await fetch('addOneLike', {
            method: 'put',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
              'stageNameS': sName,
              'birthNameS': bName,
              'likesS': tLikes
            })
          })
        const data = await response.json()
        console.log(data)
        location.reload()

    }catch(err){
        console.log(err)
    }
}
```


---
## AZURE AUTHENTICATION
[jump to top...](#javascript)<br><br>
```markdown
Keys to provide in the config.js
clientID: in Azure Active Directory => App registration => take the id
clientSecret: in the App-Registrierung => Certificates & secrets => take the value

=> in Azure Active Directory
- in App registrations
- New registration and give name eg. TestBlablabla
- choose "in any organizational directory AND personal microsoft accounts"
- register
- copy application client-id to in config.js at client-id

=> in the registered Application and in Authentication
- redirect uri: http://localhost:2121/auth/openid/return from config.js
- front-chanell logout URL: https://localhost:2121
- check ID tokens checkbox

=> in the registered Application and in Certificates & secrets
- new client secret
- enter description and expires
- copy the value (not id!) in config.js at client-secret
```


---
## PKG (create executable from node.js)
[jump to top...](#javascript)<br><br>
https://www.npmjs.com/package/pkg
<br>create an executable (for all plattforms and standard node-version)
```markdown
pkg nameOfFile.js
```
create exe with specific node-version for windows
```markdown
pkg scrapeAppStore.js --targets node12-win-x64
```

---
## HEROKU (hosting web-apps, running scripts in the cloud)
[jump to top...](#javascript)<br><br>
Heroku
<br>Hosting APIs in the cloud
```markdown
// Initial setup
git init (when .git is not in the folder of the api)
echo '{}' > composer.json               // for PHP: additional when deploying an PHP-api
echo "web: node server.js" > Procfile   // for Express: create profile (tells heroku what the server-file is)
git add .
git commit -m "upd"
heroku login -i                         // login to heroku
heroku create simple-rap-api            // create entry on heroku
heroku git:remote -a simple-rap-api     // name of the app on heroku
git push heroku master                  // push everything to heroku (or git push heroku main)
set config vars in heroku under <seetings> in the app

// Ongoing updates
git add .
git commit -m "upd"
heroku login -i
heroku git:remote -a financerapidapi
git push heroku main (or git push heroku master)
```



---
## NODEMAILER (send mails)
[jump to top...](#javascript)<br><br>
https://nodemailer.com/about/
https://www.freecodecamp.org/news/use-nodemailer-to-send-emails-from-your-node-js-server/














