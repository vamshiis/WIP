/* ADVANCED JOIN TYPES 
   - To get the unmatched rows in current main table always filter rows based on other table.
   - filter rows of other table on the key column which are NULL
   - After LEFT or RIGHT JOIN simply to get ANTI JOINS
   - filter the joining tables key column's Null rows 
   - So TO do any ANTI JOINS 
     . Perform normal joins first 
     . If its a left anti join do left join and then filter the rows 
*/

/* LEFT ANTI JOIN 
   - Returns Row from Left that has NO MATCH in Right.
   - Returns only unmatching rows from left table.
   - LEFT JOIN gives us all customer (who have placed orders + who haven't placed)
   - LEFT ANTI JOIN gives info of customers who didn't placed orders just.
   - To achieve LEFT ANTI JOIN we need to use LEFT JOIN + WHERE clause to filter the 
     LEFT join results records.
*/
-- Get all customers who haven't place any orders
SELECT *
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.customer_id IS NULL;

-- Get customers who have placed orders. (Don't use INNER JOIN)
-- Get all customers along with their orders, 
-- but only for customers who have placed an order (Without using INNER JOIN)
SELECT *
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.customer_id IS NOT NULL
-- Verify WUTH INNER JOIN
SELECT *
FROM customers AS c
INNER JOIN orders AS O ON c.id = o.customer_id


/* RIGHT ANTI JOIN 
   - Return Rows from right that has no match in left
*/
-- Get all orders without matching customers
SELECT *
FROM customers AS c
RIGHT JOIN orders AS o ON c.id = o.customer_id
WHERE c.id IS NULL;

-- Get all orders without matching customers (Using LEFT JOIN)
SELECT *
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.id
WHERE c.id IS NULL

/* FULL ANTI JOIN 
   - Return Only Rows that dont match in either tables
   - Get only unmatching rows from A and get only unmatching rows from B
*/
-- Find customers without orders and orders without customers
SELECT *
FROM customers AS c
FULL JOIN orders AS o ON c.id = o.customer_id
WHERE c.id IS NULL OR o.customer_id IS NULL;

/* CROSS JOIN :
   - Combines every row from left with every row from right
   - All Possible Combinations - 'CARTESIAN JOIN'
   - We always end up getting (A row's * B row's) row's as resultant table.
   - Useful in Simulation and Testing
   - Like having Products and different size tables to map and price a product for different sizes.
*/
-- Generate all possible combinations of customers and orders.
SELECT *
FROM customers
CROSS JOIN orders;