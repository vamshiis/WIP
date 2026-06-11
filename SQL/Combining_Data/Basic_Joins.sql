/*
   JOINS : 
   - We join tables based on the key columns.
   why to use joins ??
   1. Recombine Data
    - Data about customers is spread across multiple tables in database.
    - Like customer, address, reviews, orders
    - So to see the bigger picture of customers data we need to join everything 
      that’s how we recombine and use them.

   2. Data Enrichment
    - Getting Extra Data
    - Sometimes we have Master table like Customers.
    - We need a zip codes of their address where zip code table is reference table.
    - so we use join to get the extra info from reference table for our master table.
    - That’s how we can have the Extra info.

   3. Check for Existence
    - Lets say we have customers table
    - We want to filter out users who have ordered or not ordered.
    - So we simply join the customer table with a lookup table orders
    - so if we join we end up having filtered rows who have ordered.
    - If we negate this operation we can get users who have not ordered.
    - That’s how joins gonna help us for filtering too.

    Types of joins :
    Basic                                Advanced
    1. No Join                          1. Left Anti Join
    2. Inner Join                       2. Right Anti Join
    3. Left Join                        3. Full Anti Join
    4. Right Join                       4. Cross Join
    5. Full join
*/

/* No Join 
  - Returns Data From Tables without combining them.
*/
-- Retrieve all data from customers and orders in two different results.
SELECT * 
FROM customers;

SELECT *
FROM orders;


/* INNER JOIN : 
   - Returns only matching rows from both Tables
   - We do this join based on key columns.

*/
-- Retrieve all customers along with their orders, but only for customers who have placed an order.
-- Gives who all have placed orders
--SELECT * FROM customers;
--SELECT * FROM orders;
SELECT 
    c.id,
    c.first_name,
    o.order_id,
    o.order_date
FROM customers AS c
INNER JOIN orders AS o  ON c.id = o.customer_id;

/* LEFT JOIN 
   - Returns all rows from left and only matching from right.
   - Main table is left table so it shows all rows even if it matches records from right table or not.
*/
-- Get all customers with their orders including those without orders
-- gives both orders placed ad=nd not placed customers info
SELECT 
    c.id,
    c.first_name,
    o.order_id,
    o.order_date
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id;

/* RIGHT JOIN:
   - Returns all rows from right and only matching from left
   - the right table should be joined onto left table.
   - Always try to convert the right joins to left joins
   - Left joins are easier to understand so convert a right join into left join
   - just flip the sides of table and write the query.
   - Right table becomes the main table and left table becomes the right table and then apply the left join.
*/
-- Get all orders customer info even if orders dont have customer info too
-- gives all orders details who have placed or any missing customer info.
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.order_date
FROM customers AS c
RIGHT JOIN orders AS o ON o.customer_id = c.id;

-- Right join converted to Left join 
SELECT 
    c.id,
    c.first_name,
    o.order_id,
    o.order_date
FROM orders AS o
LEFT JOIN customers AS c ON c.id = o.customer_id;

/* FULL JOIN
   - Return all rows from both tables.
   - order of table doesnt matter 
*/ 
-- Summary of both tables 
SELECT *
    --c.id,
    --c.first_name,
    --o.order_id,
    --o.order_date
FROM customers AS c
FULL JOIN orders AS o ON c.id = o.customer_id