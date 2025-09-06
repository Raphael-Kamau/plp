/* Java Script is a scripting language used to create and control dynamic website content, 
such as interactive forms, animations, and other user interface elements. 
It is a client-side language, meaning that it runs in the user's web browser rather than on the web server. 
JavaScript is often used in conjunction with HTML and CSS to create rich, interactive web applications. */

// single line comments are created using two forward slashes

/* multi-line comments are created using a forward slash and an asterisk to start the comment, 
and an asterisk and a forward slash to end the comment */

// Declaring variables
// const is used to declare values that do not change over time
// let is used to declare values that may change over time
// var is an older way to declare variables, and is less commonly used in modern JavaScript

const name = "Kamunyu Raphael";
const gender = "Male";
let age = 19;

// using variables
console.log("Hello, happy to meet you, my name is " + name);
console.log("I am " + age + " years old");

// changing the value of a variable
age = 21;
console.log("I just had my birthday, I am now " + age + " years old");

let car = {
    car_name: "ISUZU",
    car_model: "MUX",
    year: "2024",
    color: "black",
    transmission: "Manual",
    fuel: "Diesel"
};

console.log(car.car_name);

//  Operators
// They include: arithmetic and logic
// Arithmetic operators: + - * / % ++ --
let a = 5;
let b = 3;

// Addition 
console.log("Addition: " + a + b);

// Subtraction 
console.log("Subtraction: " + a - b);
// Multiplication 
console.log("Multiplication: " + a * b);
// Division 
console.log("Division: " + a / b);
// Modulus 
console.log("Modulus: " + a % b);
// Increment 
console.log("Increment: " + ++a);
// Decrement 
console.log("Decrement: " + --b);

// Logical operators: && || !
let x = 5;
let y = 10;

// AND operator
console.log(x < 10 && y > 5); // true
// OR operator
console.log(x < 10 || y < 5); // true
// NOT operator
console.log(!(x < 10)); // false

// Conditional statements
// if, else if, else
let time = 10;

if (time < 12) {
    console.log("Good morning");
} else if (time < 18) {
    console.log("Good afternoon");
} else {
    console.log("Good evening");
}

// Loops
// for, while, do while

// for loop
for (let i = 0; i < 5; i++) {
    console.log("Iteration number: " + i);
}

// while loop
let j = 0;
while (j < 5) {
    console.log("While loop iteration: " + j);
    j++;
}

// do while loop
let k = 0;
do {
    console.log("Do while loop iteration: " + k);
    k++;
} while (k < 5);






