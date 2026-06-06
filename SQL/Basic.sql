---- Use the MyDatabase 

/* Fields (Columns) Retrieval */

--Retrieve The customer table
SELECT *
FROM customers;

---- Retrieve The orders table
SELECT *
FROM orders;

---- Selective columns
SELECT 
	first_name,
	country,
	score
FROM customers;

/* WHERE clause */
-- Retrieve Customers with scores not equal to 0
SELECT *
FROM customers
WHERE score != 0;

-- Retrieve records where country is 'Germany'
SELECT *
FROM customers
WHERE country = 'Germany';

SELECT first_name, country
FROM customers
WHERE country = 'Germany';

/* ORDER BY 
   - Orders in Ascending Order by Default.
   - DESC orders them in Descending Order
*/
-- Retrieve all the customers all sort the result by the highest score first
SELECT *
FROM customers 
ORDER BY score DESC;

-- Retrieve all the customers all sort the result by the lowest score first
SELECT *
FROM customers
ORDER BY score;

/* NESTED ORDER BY 
   - If column contains Repeated values introduce another condition for tie break value's in the ORDER BY itself to sort.
   - The first ORDER BY condition on particular column can lead to have repetation rows of same columns.
   - Then we find a different sorting pattern on other column due to First ORDER BY
   - So we introduced a Second ORDER BY to follow for the tied rows done by first ORDER BY.
*/
-- Retrieve all the customers and sort the result by country and then by the highest Score
SELECT *
FROM customers
ORDER BY country, score DESC;

/* GROUP BY */
-- Retrieve Score for each country and sort by highest score
SELECT 
	country,
	SUM(score) AS country_scores
FROM customers
GROUP BY country
ORDER BY country_scores DESC;

--Retrieve Score for each country
SELECT 
	country,
	SUM(score) AS total_scores,
	COUNT(id) AS total_Customers
FROM customers
GROUP BY country;

/* HAVING 
  - Filters the Groups based on aggregate values.
*/
/* Find the average score for each country considering only
Customers with score not equal to 0 And return only those countries
with an average score greater than 430 */
SELECT 
	country,
	AVG(score) AS avg_score
FROM customers
WHERE score != 0 
GROUP BY country
HAVING AVG(score) > 430;

/* DISTINCT 
   - Removes Duplicates (Repeated Values) each value appears only once
*/
-- Retrieve All unique Countries
SELECT DISTINCT country
FROM customers;

/* TOP(Limit)
   - Restrict the number of Rows
*/
-- Retrieve top 3 customers
SELECT TOP(3) *
FROM customers;

-- Retrieve TOP 3 customers with highest Score
SELECT TOP 3 *
FROM customers
ORDER BY score DESC;

-- Retrieve lo west 2 customers
SELECT TOP 2 *
FROM customers
ORDER BY score ASC;

-- Retrieve the Two most recent Orders
SELECT TOP 2 *
FROM orders
ORDER BY order_date DESC;

/* Static Values */
SELECT 123 AS static_number

SELECT 'Hello' AS static_string

-- Usage in Queries
SELECT 
	id,
	first_name,
	'New Customer' As customer_type -- Can be used to assign a static column, not stored in DB
FROM customers

