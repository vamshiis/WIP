
/* Filtering Data : 
   
WHERE Operators : 
1. Comparison Operator : 
   - Compares two things!
   It can be a condition -> Expression operator Expression
   Types of comparisons we can do is: 
   column1 = column2  --> first_name = last_name
   column1 = value    --> first_name = 'John'
   Function = value   --> UPPER(first_name) = 'JOHN'
   Expression = value --> price * quantity = 1000
   (Advanced)
   Subquery = value   --> (SELECT AVG(sales) From orders) = 1000
*/
-- Retrieve all customers from Germany
SELECT *
FROM customers
WHERE country = 'Germany';

-- Retrieve all customers who are not from Germany
SELECT *
FROM customers
--WHERE country <> 'Germany';
WHERE country != 'Germany';

-- Retrieve all customers with a score greater than 500
SELECT *
FROM customers
WHERE score > 500;

-- Retrieve all customers with a score of 500 or more
SELECT *
FROM customers
WHERE score >= 500;

-- Retrieve all customers with a score less than 500
SELECT *
FROM customers
WHERE score < 500;

-- Retrieve all customers with score 500 or less
SELECT *
FROM customers
WHERE score <= 500;

/* 2. Logical Operators
   AND:
   - All conditions must be TRUE then only it will consider the  row.
   OR:
   - Atleast one of the condition must be TRUE to filter the row.
   NOT:
   - Reverse operator excludes the matching values.
*/
-- Retrieve all customers who are from USA and have a score greater than 500
SELECT *
FROM customers
WHERE country = 'USA' AND score > 500; 

-- Retrieve all customers who are either from the USA or have a score greater than 500
SELECT *
FROM customers
WHERE country = 'USA' OR score > 500;

-- Retrieve all customers with a score not less than 500
SELECT * 
FROM customers
--WHERE NOT score < 500;
WHERE score >= 500;


/* 3. Range Operator 
BETWEEN:
   checks if a value falls between the range the values are inclusive.
*/
-- Retrieve all customers whose score falls in the range between 100 and 500
SELECT *
FROM customers
WHERE score BETWEEN 100 AND 500;

/* 4. Membership operator
   IN:
    Checks if a value exists in list.
   NOT IN:
     Works exact opposite to IN selects only records that aren't specified.
*/
-- Retrieve all customers from either Germany or USA
SELECT *
FROM customers
WHERE country IN ('Germany','USA');

/* 5. Searching Operator 
   LIKE:
    Search for a pattern in text
    To build a pattern we have 2 special characters
    '%' -> Anything like 0, 1 , many characters
    '_' -> Exactly 1 character
*/
-- find all customers whose first_name starts with 'M'
SELECT *
FROM customers
WHERE first_name LIKE 'M%'

-- find all customers whose first_name ends with 'n'
SELECT * 
FROM customers
WHERE first_name LIKE '%n';

-- find all customers whose first_name contains a 'r'
SELECT *
FROM customers
WHERE first_name LIKE '%r%';

-- find all customers whose first_name has 'r' in the third position.
SELECT *
FROM customers
WHERE first_name LIKE '__r%';