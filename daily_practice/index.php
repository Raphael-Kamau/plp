<?php
// Database connection  
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "serenahotel";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection Failed: " . $conn->connect_error);
}

// Fetch form data
$name = $_POST['name'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);

// Insert into database
$sql = "INSERT INTO staff (name, email, password) VALUES ('$name', '$email', '$password')";

if ($conn->query($sql) == TRUE) {
    echo "Submitted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
