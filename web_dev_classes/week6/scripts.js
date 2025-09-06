// JavaScript file
function validatePassword() {
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");
  message.innerHTML = "";

// Regular expressions to check password criteria
  const upperCase = /[A-Z]/.test(password);
  const lowerCase = /[a-z]/.test(password);
  const specialChar = /[!@#$%&*()^~_,.{}<>|]/.test(password);
  const number = /[0-9]/.test(password);
  const lengthCriteria = password.length >= 8;

    // Collect unmet criteria
  const errors = [];

    // Check each criterion and add to errors if not met
  if (!upperCase) errors.push("• At least one uppercase letter");
  if (!lowerCase) errors.push("• At least one lowercase letter");
  if (!specialChar) errors.push("• At least one special character");
  if (!number) errors.push("• At least one number");
  if (!lengthCriteria) errors.push("• Minimum of 8 characters");
    
// Display results
  if (errors.length === 0) {
    message.innerHTML = "✅ Password strength is good!";
    message.style.color = "green";
  } else {
    message.innerHTML = "❌ Your password did not meet requirements:<br>" + errors.join("<br>");
    message.style.color = "red";
  }

// Clear message after 5 seconds
  setTimeout(() => {
    message.innerHTML = "";
  }, 5000);
}

// Theme toggle function
function theme() {
  document.body.classList.toggle("dark-theme");
}
