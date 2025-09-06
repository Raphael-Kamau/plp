/* SQL week two practice */ 
-- Question 1
/* Retrieve checkNumber, paymentDate, and amount from payments table */
SELECT checkNumber, paymentDate, amount 
FROM payments;
-- Question 2
/* Retrieve orderDate, requireDate, status from orders table */
SELECT orderDate, requireDate, status FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- Question 3
/* Display firstName, lastName, email from employees */
SELECT firstName, lastName, email FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- Question 4
/* Retrieve all columns and records from offices */
SELECT * FROM offices;

-- Question 5
/* Fetch productName, quantityInStock from products sorted by buyPrice ascending and limited to 5 records */
SELECT productName, quantityInStock FROM products
ORDER BY buyPrice ASC
LIMIT 5;

