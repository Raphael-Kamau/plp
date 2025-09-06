-- 1. SQL to create table student
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- 2. SQL to insert 3 records
INSERT INTO TABLE student (
    VALUES(1, 'Kamunyu Raphael', 23),
    (2, 'Wanjiku Ann', 19),
    (3, 'Austin Willis', 20),
    (4, 'Kamunyu Patrick', 21),
    (5, 'Kamunyu Trizah', 25)
);

-- 3. SQL to update age of student
UPDATE TABLE student
SET age = 20
WHERE id = 2; 