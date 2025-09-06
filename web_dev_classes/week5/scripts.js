// scripts.js
// Part 1: Variables and Conditionals
let userName = prompt("Enter your name:");
if (userName) {
  console.log(`Welcome, ${userName}!`);
  document.getElementById("greeting").textContent = `Hello, ${userName}!`;
} else {
  console.log("No name entered.");
}

// Part 2: Custom Functions
function Message() {
    alert(`Happy to have you here ${userName}!`);
}
Message();


// Part 3: Loops
let cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"];
for (let i = 0; i < cars.length; i++) {
    console.log(cars[i]);
}

// Part 4: DOM Manipulation
document.getElementById("greeting").style.color = "blue";
