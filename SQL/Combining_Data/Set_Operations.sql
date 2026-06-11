/* SET OPERATORS : 
   To combine the 2 tables by adding rows of one table to another.
   Syntax : 
   query_1 
   SET_OPERATOR 
   query_2
   Rules : 
   1. SQL CLAUSE 
   - ORDER BY can be used only once
      - SET Operator can be used almost in all clauses 
      - WHERE | JOIN | GROUP BY | HAVING
      - ORDER BY is allowed only once at the end of entire query (i.e after query_2)
   2. NUMBER OF COLUMNS
   - Same Number of Columns
      - The number of columns in each query must be the same.
   3. DATA TYPES
   - Matching Data Types
      - Data Types of columns in each query must be comptabile.
   4. ORDER OF COLUMNS
   - Same Order of Columns
      - The Order of the columns in each query must be same.
   5. COLUMN ALIASES
   - First Query Controls Aliases
      - The column names in the result set are determined by the column names specified in the first query.
   6. CORRECT COLUMNS
   - Mapping Correct Columns
      - Even if all rules are met and SQL shows no errors, the result may be incorrect.
      - Incorrect column selection leads to inaccurate results.
*/
/* UNION
   - Returns all distinct rows from both queries.
   - Removes duplicate rows from the result.
*/
-- Combine the data from employees and customers into one table
-- First check which columns makes sense to combine from both the tables.
-- Then include both column carefully by order and check dtypes of both columns and combine them.
-- In this question it havent said anything so go by UNION which removes duplicates and repeates that row once.
SELECT 
    FirstName,
    LastName
FROM Sales.Customers
UNION
SELECT 
    FirstName,
    LastName
FROM Sales.Employees;

/* UNION ALL :
   - Returns all rows from both queries, including duplicates
   - UNION ALL is Faster then the UNION
   - Because it doesnt perform any additional steps to check for duplicates and remove unlike how UNION does.
   - If we are 100% about the both tables there arent any duplicate rows on combine just use the UNION ALL blindly.
   - USE UNION ALL to find duplicates and quality issues.
*/

-- Combine the data from employees and customers into one table including duplicates.
SELECT 
FirstName,
LastName
FROM Sales.Customers
UNION ALL
SELECT 
FirstName,
LastName
FROM Sales.Employees;

/* EXCEPT (Minus)
   - Returns all distinct rows from the first query that are not found in second query.
   - It is the only one where the order of the queries affect the final result.

   Difference between EXCEPT AND NULL
   EXCEPT: 
   - Automatically performs a DISTINCT operation on your results. 
   - Even if Table A has 10 duplicate rows that do not exist in Table B, EXCEPT will compress them and return only 1 unique row.
   - Matches NULL = NULL exactly and ignores them in result
   - Only consider the row to be unique if all column values from first_query is not found in the second_query.
   - its like complete row with column value  aganist all rows of another query
   
   LEFT ANTI JOIN:
   -  Preserves the exact row count of your first table. 
   - If Table A has 10 duplicate rows that do not match Table B, it will return all 10 rows
   - It cant compare NULL == NULL in joins and filter them out.
   - This will return the duplicate as well if matched multiple times.


   Table A (Day 1)
   StudentID  Name   Status
   1         Alice   Present
   1         Alice   Present
   2         Bob     Present
   3         Charlie Late

   Table B (Day 2)
   StudentID    Name    Status
   1           Alice    Present
   3           Charlie  Present
QUERY :
SELECT StudentID, Name, Status FROM TableA
EXCEPT
SELECT StudentID, Name, Status FROM TableB;

   The Output Result
   Running this query returns exactly two rows:
   StudentID        Name        Status     Why it behaves this way
   2                Bob        Present     He does not exist in Table B at all, so he is included.
   3                Charlie    Late        Even though Charlie is in Table B, his status changed from Late to Present.
                                            Because the entire row is not an exact match, his Day 1 row is included!

  EXCEPT vs LEFT ANTI JOIN :
  Feature                      EXCEPT                              LEFT ANTI JOIN
  Duplicates            Removes duplicates (DISTINCT)              Keeps all duplicates
  NULL Behavior         Matches NULL safely                        Requires manual NULL handling
  Column Control        Compares all columns                       Compares only chosen ON keys
  Performance           Can be slower on large datasets            Often faster with proper indexin
*/
-- Find the employes who are not customers at the same time.
-- Its like returning the non-matching rows from the left table.
-- Checks for same rows in the 2nd table and ignores them 
-- only includes those non matching rows in the final result.

SELECT
firstname,
lastname
FROM Sales.Employees
EXCEPT 
SELECT
FirstName,
LastName
FROM Sales.Customers;
----Check and verify both tables individually
--SELECT
--firstname,
--lastname
--FROM Sales.Employees;
--SELECT
--FirstName,
--LastName
--FROM Sales.Customers;

/* INTERSECT 
   - Returns common rows between two tables.
   - Order of the Table doesn't matter
*/
-- Find employees who are also customers.
SELECT 
    FirstName,
    LastName
FROM Sales.Employees
INTERSECT
SELECT
     FirstName,
    LastName
FROM Sales.Customers;

/* UNION AND UNION ALL USE CASES : 
   - Combine similiar information Containing Tables before analyzing the data
   - We have a database with tables like employees, customers, students, supliers 
     Here we combine similiar tables together and have a person table and then create a report.
   - So in this case we gonna require to combine all the tables first and then analyze it with sql query and generate a report.
   - similarly the orders, big companies can store every years data into separate table of orders.
   - To do analyses on orders of the company we need to combine those all the orders tables across all years and generate a single order table
     to do analysis and generate a report.
*/
/* TASK :-
   Orders are stored in separate tables (Orders and OrderArchive), Combine all orders into one report without duplicates.
Important note  
- Never use an Asterisk(*) to combine tables, list needed columns instead
- we might end up in future changing the schema of tables or hae=ve various scenarios.
- So always specify the column names in the combining of data of 2 tables.
- Source Flag :
  Include additional column to indicate the source of each row.
  Add static values for both the tables simply.
*/
-- UNION USE CASE
SELECT 
       'Orders' AS SourceTable
      ,[OrderID]
      ,[ProductID]
      ,[CustomerID]
      ,[SalesPersonID]
      ,[OrderDate]
      ,[ShipDate]
      ,[OrderStatus]
      ,[ShipAddress]
      ,[BillAddress]
      ,[Quantity]
      ,[Sales]
      ,[CreationTime]
FROM Sales.Orders
UNION
SELECT 
       'OrderArchive' AS SourceTable
      ,[OrderID]
      ,[ProductID]
      ,[CustomerID]
      ,[SalesPersonID]
      ,[OrderDate]
      ,[ShipDate]
      ,[OrderStatus]
      ,[ShipAddress]
      ,[BillAddress]
      ,[Quantity]
      ,[Sales]
      ,[CreationTime]
FROM Sales.OrdersArchive
ORDER BY OrderID;

/* EXCEPT USE CASE 

   USE CASE 1
   DELTA DETECTION :
     Lets say we have data load up into data warehouse from sorce systems.
     ON DAY 1 :
      we load customer_id 1,2 info
     ON DAY 2 :
      we try to load customer_id 1,3 info 
      Here the customer_id 1 already exists in data warehouse so we need to store only customer_id 3 row.
      For this we need to every day compare the data of current day with previous day using EXCEPT operator.
      Using EXCEPT we will be left out with unmatched rows in day 2 that will be customer_id 3 
      so thats how we add new rows into data warehouse.
      Note : customer_id 1 on both days are same not different thats why we are ignoring that row based on EXCEPT condition.
   
   USE CASE 2
   DATA COMPLETENESS CHECK :
   EXCEPT operator can be used to compare tables to detect dispenceries between databases.
     - let's say we are migrating database from A to B 
     - now to check whether everything from database A have successfully migrated into database B we need to check using EXCEPT.
     CHECK 1: 
      To check if there is any data left in database A that is still need to be transferred.
      We need to do database_A query EXCEPT database_B query.
      If we are succesfully migrated the result should be empty leading to everything in database A and database B matches.
      So nothing is left everything is transferred.
    CHECK 2:
      We have check from the original source but we need to check at copied source too if it matches the source.
      Because new copied source can have data that source doesnt have. we need exact copy of source nothing more and nothing less simply.
      So we need to make sure both the sides have same data, we make sure to check on the database B also.
      for this we need to use EXCEPT but now flip the query in the except statement.
          database B query EXCEPT database A query
      If this too returns a empty result we have exact data in the both databases nothing more nothing less just.
    This lets us have a data dispencery check when migrating a database simply.
*/