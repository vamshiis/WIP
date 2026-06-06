/* DML ( DATA MANIPULATION LANGUAGE )
   - Modify (Manipulates) the Data
   The Commands we have in DML are : 
   INSERT
   UPDATE
   DELETE
*/
/*
 • INSERT : 
      We add new rows into existing table or new table.
      we have 2 ways to enter the values
  1. Manual Entry (Values) : 
     - Target the table and insert the table.
    Syntax : 
        INSERT INTO table_name (col1,col2,...(optional))
        VALUES (val1,val2,...)
    RULE : Match the number of columns and values
    NOTE : IF col_names are not given then it expect a value for every col in table for that row.
         So if you want to add value to one column specify the col and enter the value.
    Always Mention column names for clarity and maintainability
    Be careful with VARCHAR values entry, sometimes we can endup giving another col value.
*/
-- With col and val matching
INSERT INTO customers (id,first_name,country, score)
VALUES 
    (6, 'Anna','USA', NULL),
    (7,'Sam', NULL, 100)

-- If all values for column ignore specifying cols
INSERT INTO customers 
VALUES
    (8, 'Max', 'Spain', Null)

-- Insert values for Specific Columns
-- We Can Skip the NULLABLE VALUES
INSERT INTO customers (id,first_name)
VALUES (9, 'John')

INSERT INTO customers (id,first_name)
VALUES (10, 'Doyle')


/* 
  2. INSERT USING SELECT
  - We are having a SOURCE TABLE with all the Data
  - And also we have another table that is TARGET TABLE that needs the data to be loaded.
  - So we first query the SOURCE TABLE to select the data that need to be inserted into target table.

*/
-- Insert data from 'customers' into 'persons'
/* Flow:
   - First check the source table.
   - next chek the Schema of Target table to know the NULLABLE columns.
     Databases >> database_name >> Tables >> dbo.table_name >> Columns 
   - Now if the columns exist in Source Table which are required for Target Table directly include them.
   - If the column is not available in source and can accept NULL in target table assign NULL for that column or 
     ask If there is any static value to be inserted.
   - If the column is not present in Source table and that column is NOT NULL in the Target Table you need to definetly
     include the static value for the column in SELECT.
   - At last add the INSERT query by specifying all the col_lables.
   - By this way we are querying the Source Table using SELECT and INSERT-ing into Target Table.
*/

INSERT INTO persons (id,person_name,birth_date,phone) 
SELECT
    id,
    first_name,
    NULL,
    'Unknown'
FROM customers;

SELECT * FROM persons;


/* UPDATE 
   - Modify the rows which are already existing.
   Syntax : 
        UPDATE table_name
          SET col_1 = val_1
              col_2 = val_2
        WHERE <condition>
   NOTE : Always use WHERE to avoid UPDATING all rows unintentionally.
*/
/*  UPDATION FOR ONE SINGLE ROW : 
Change the score of customer 6 to 0 
   - Write the update statement 
   - must include the WHERE clause it filter the rows that need a update
   - Next before running update check that rows which are filtered out using SELECT
   - then run the update to verify the total rows filtered before and after update are same.
*/
UPDATE customers
SET score = 0 
WHERE id = 6;

--SELECT *
--FROM customers
--WHERE id = 6;

-- Change the score of customer 10 to 0 and update the country to UK
UPDATE customers
SET score = 0,
    country = 'UK'
WHERE id = 10

SELECT * FROM customers;

/* UPDATION FOR SUBSET OF ROWS :
   - Filter out the rows on the condition
*/
UPDATE customers
SET score = 0
WHERE score IS NULL;

SELECT *
FROM customers
WHERE score IS NULL;

SELECT * FROM customers;

/* DELETE 
   - Removes already existing rows from the table.
   Syntax : 
        DELETE FROM table_name
        WHERE <condition>
   Note : Always use WHERE to avoid DELETING all rows unintentionally.
*/
-- Delete all customer with ID greater than 5
DELETE FROM customers
WHERE id > 5

SELECT *
FROM customers
WHERE id > 5;

SELECT * FROM customers;

-- Delete all data from table persons
-- TRUNCATE : Clears the whole table at once without checking or logging
-- very fast than DELETE command 
-- Deletes data but TABLE still Exists.
TRUNCATE TABLE persons;

SELECT * FROM persons;