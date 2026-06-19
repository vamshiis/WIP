/* NULL FUNCTIONS  
    
    What is NULL ? 
    - NULL Means Nothing, unknown!!
    - NULL is not equal to anything!
    - NULL is not a zero
    - NULL is not empty string
    - NULL is not a blank space.
    - It is simply nothing.
    - It tells us there no value and it is missing.
    - It like we say i dont know what this value means.

    Ex : How a NULL can be stored!
         - Lets say we have a registration form where it asks for first_name, middle_name(optional), last_name.
         - Here some users can fill optional filed or some wont even fill it as its an optional.
         - so if filled they keep the value, if not filled and the column allows NULL database holds NULL as value.
         id        first_name      middle_name     last_name
         01        john            Kevin           Dux
         02        Amily           NULL            Monde
         03        Mark            Billy           Butcher

         - In the above case the row 2 has a null the user has not entered the value for that field.
         - Since middle_name can allow NULL's it can hold NULL for non-entry simply.
*/
/* HOW TO HANDLE NULL's 
   
   1. Replacing a NULL
      - This function will help us to manipulate the data inside our database eacily.
      - This help us to handle the NULL Values.
      Scenario 1 : Replace a NULL value to a known value like 40
                   To do this we use 2 functions : 
                   1. ISNULL()
                   2. COALESCE()
      Scenario 2 : Replace a value to NULL 
                   We use a function
                   1. NULLIF()

   2. Checking for NULL Exsistence in a table's column.
      Scenario 1 : To check if NULL exists, we use
                   
        --->  IS NULL - This returns all the records of the specified column which contains NULL
      
      Scenario 2 : To check if NULL don't exists, we use
                   
        --->  IS NOT NULL - This returns all the records of specified column which do not contain NULL.
*/

/* ISNULL() : 
   - Replaces 'NULL' with a specified value

   Syntax : ISNULL(value, replacement_value)
            Default Replacement_value = 'unknown'
   Scenario 1 : Replacing a NULL with a static value.
                ISNULL(column_name, 'unknown')
   Here 'unknown' is default we can change to other static value as well to display for all NULL founds in the column.

     EX: ISNULL(Shipping_Addr, 'Unknown')
         OrderID   shipping_Addr   ISNULL
            1            A           A
            2            NULL        Unknown
            3            NULL        Unknown

   Scenario 2 : Replacing a NULL with a Helper Column.
                ISNULL(column_1, column_2)
   - Here 'column_2' will replace the records which has got NULL in the 'column_1'.
   - Also it pulls the column_2's same row value to fill the column_1 value.
   - we cant gurantee there can absolutely be a value from the column_2 when the column_1 hits a NULL value.
   - There may be a value or there may be not from the column_2 No gurantee.

   Ex:   ISNULL(Shipping_Addr, Billing_Addr)
         OrderID   shipping_Addr   Billing_Addr  ISNULL
            1            A              B           A
            2            NULL           C           C
            3            NULL           NULL        NULL
*/

/* COALESCE() 
   - Returns the first non-null value from a list.

   Syntax : COALESCE(value1, value2, value3, ...)
   It also has same scenario as ISNULL() to fill a replacement with static value and from another column.
   - But we faced if column_2 also doesnt have a value and has NULL the column_1 who has NULL will be left with NULL.
   - IN COALESCE() we can simply give another argument the third one if column_2 also returns a NULL fill a third argument passed value.
   - we pass a static value for the end if everything fails it fills. 
   -Its more like safe fallback.

   Scenario 1: COALESCE(column_1, static_value) --> works same as ISNULL()
   Scenario 2: COALESCE(column_1, column_2)     --> works same as ISNULL()
   Scenario 3:
   Here we can provide a third argument a safe fall back value to fill when another column fails to fill the column_1 value.
   COALESCE(column_1, column_2, static_value)
   Example : 
         COALESCE(Shipping_Addr, Billing_Addr, 'N/A')
         OrderID   shipping_Addr   Billing_Addr  COALESCE
            1            A              B           A
            2            NULL           C           C
            3            NULL           NULL        N/A (Static _value)

    ISNULL Vs. COALESCE
    The comparison between these 2
             ISNULL()                       COALESCE()
        - Limited to two Values         - Unlimited values can be passed
        - Faster to implement           - Slower
        - Disadvantage of ISNULL        - Advantage It is available in all Databases
            In different SQL falvour
            we have different KEYWORD
            like in,
            SQL Server --> ISNULL
            Oracle  --> NVL
            MYSQL --> IFNULL
    - Always use COALESCE() if in fututre we need to migrate to another DB we need to modify the scripts.
    - Don't use ISNULL() until you need to optimize the query just.
*/

/* USE CASE - HANDLING NULL's
   
   1. DATA AGGREGATIONS : 
      - We can use ISNULL() | COALESCE() to handle the NULL before doing data aggregations.
      - Aggregate functions like SUM(),MIN(), MAX(), AVG(), COUNT(Column_name) this will ignore the records with NULL on the specified column.
        Let say we have 3 records where 2 are 10,20 values and 1 record is NULL, then the average would be
                                  AVG() = 10+20/2 = 15
           - Observe one thing the NULL record is completely ignored and the value divided by also changed.
           - This will effect our final result as we are doing a selective average on the known values.
           - To tackle this we need to replace the NULL first and then we need to perform aggregations.
           - After we replace NULL with 0 we get  AVG() = 10+20+0/3 = 10 
           - See how quickly our analysis were wrong and by handling it correctly we got correct metric.
      - COUNT(*) will count all the record it don't care if there is a NULL in a record or not.
*/

-- Find the average scores of the customers.

/* OVER()
   - It is an window function to display the table as it is without collapising all records due to aggregation done.
   It tells SQL: 
    "Calculate the average of the entire column, but do not collapse my rows. 
    Keep every single customer row visible, and just paste that total average next to every single row."
   - Use when no group by used but aggregation required as output.
   - Again choose only over() if you need the table columns other than aggreagated value as result.
   - If you need only the aggreagted value alone dont use it simply.
   Its like scale up the aggregated value for every row available on the table.
*/
-- Handling a NULL before aggregations is mandatory because it can lead to incorrect metric's 
-- if NULLs not handled properly.
SELECT
CustomerID,
Score,
COALESCE(Score,0) score_2,
AVG(Score) OVER() AvgScore,
AVG(COALESCE(Score,0)) OVER() avg_score2
FROM Sales.Customers;

/* 2. MATHEMATICAL OPERATIONS 
      - Handle NULL before doing mathematical operations.
      Let say we do mathematical operation numbers and strings
      Ex :
      5 + 5 = 10 , 0 + 5 = 5 but NULL + 5 = NULL
      'A' + 'B' = 'AB',  '' + 'B' = 'B', NULL + 'B' = NULL

    So anything with a NULL in calculation it turn entire result into NULL 
    It shows No Mercy literally.
    So we need to handle the NULL value carefully
*/
-- Display the full name of customers in a single field.
-- by merging their first and last names,
-- and adding bonus points to each customer's score.

SELECT 
CustomerID,
FirstName,
LastName,
COALESCE(FirstName, '') + COALESCE(LastName, '') Full_name, -- Using COALESCE to handle NULL and use a hardcoded ''.
CONCAT_WS('', FirstName, LastName) full_concat_name, -- Handles NULL internally and returns value if any one of value is still NULL
Score,
COALESCE(Score, 0) + 10
FROM Sales.Customers;

/* 3.JOINS 
     - Handle the NULL before JOINING tables.
     Scenario A :
     If KEY Column is not containing any NULL
      - In order to join tables we need the keys from both table.
      - If the keys are NOT NULL and does exists the join will be done successfully.
     
     Scenario B:
     If KEY Column contains a NULL 
      But,
      What if we have a key column with a NULL then the records gonna be not considered and we lose data
      In final result after joining the data.
  
  Example on Scenario B : 
  TABLE 1                          TABLE 2                        QUERY :
  YEAR     TYPE     ORDERS         YEAR     TYPE     SALES        SELECT
  2024      a        30            2024      a        100         a.year, a.type, a.ORDERS, b.SALES
  2024     NULL      40            2024      NULL     200         FROM TABEL1 a
  2025      b        50            2025      b        300         JOIN TABLE2 b
  2025      NULL     60            2025      NULL     200         ON  a.year = b.year
                                                                  AND a.type = b.type;
  RESULT : 
          Year     Type   Orders     Sales
          2024      a      30        100
          2025      b      50        300
  - Here we did a join on combo key column the same pair in one table need to be present in another table on the same both columns.
    Row 1
  - we check for 2024,a does it exists in Table2 as well if yes it includes with its sales, orders as well.
    Row 2
  - Next we have 2024,NULL checks in Table2 for 2024,NULL yes it exists logically but NULL = NULL this comparison fails we are comparing UNKNOWN = UNKNOWN
    SQL will ignore when NULL = NULL is compared entirely those records are ignored if such comparison happens.
    Row 3
  - Checks for 2025,b it exists on table2 so it includes it in result.
  Row 4
  - Same 2025,NULL is present so it's logically available but NULL = NULL Comparison is not a valid comparison so it doesnt include it in result.

  - With this we are loosing the data and getting an inaccurate results.
  - If we have NULLS in the keys upon join we will loose the records so, its very important to handle the NULL's inside the keys before doing the JOINS.

   How to solve it ??
   - Either we use the COALESCE() OR ISNULL() in the JOIN
   - we will use null directly upon the join which colum key has it.
   - we have NULL's on Table1.type, Table2.type column
   TABLE 1                          TABLE 2                        QUERY :
  YEAR     TYPE     ORDERS         YEAR     TYPE     SALES        SELECT
  2024      a        30            2024      a        100         a.year, a.type, a.ORDERS, b.SALES
  2024      ''       40            2024      ''       200         FROM TABEL1 a
  2025      b        50            2025      b        300         JOIN TABLE2 b
  2025      ''       60            2025      ''       200         ON  a.year = b.year
                                                                  AND ISNULL(a.type, '') = ISNULL(b.type, '');
 - Here we just temporarily replacing NULL with '' we arent mutating the original NULL and overwriting it to database.
 - So whatever value we replaced for NULL's its just a temporary thing exists for this query.

 RESULT : 
          Year     Type   Orders     Sales
          2024      a      30        100
          2024      NULL   40        200
          2025      b      50        300
          2025      NULL   60        200

 why NULL's Surfaced Again ??

 - The result table will refer the original table and what we say in select statement those things are displayed.
 - Here in query we havent said anything in SELECT statement we said to just display those columns.
 - But before that JOINS have happened which allowed the records to join successfully by turning NULL to '' on fly and getting
   a valid comparison for 2024,'' and 2025,'' this records passed join check and came this fasr now.
 -  SQL is allowing those since they have been replaced to '' and compared.
 - But SELECT will look at the unchanged table and get the stuff it has been ordered to get to display.

 /* Proper and broken explanation :
 - As we discussed above we are just replacing a NULL value with a '' for until this query runs.
 - So whatever operation this does will be done on temporary things created on the fly.
 - we have said replace a NULL to '' it doesnt mutate original DB to remove that NULL and place '' in DB.
 - So SQL when try to join if it sees a NULL it must first replace NULL to '' and then take it for join.
 - So thats why temporarily the function removed NULL sticker and placed '' sticker.
 - Now SQL gonna compare 2024,'' with the Table2 for 2024,''
 - Since we have even replaced the Table2 with the ISNULL operation on the key column it will also hold '' for NULL in that key column.
 - so the '' == '' is True and SQL even allows it as valid comparison.
 - it allows that record to reflect in the result table.
 - But the result table will see the NULL since we placed the ISNULL() operartion in JOINs but not in the SELECT statement for the same columns.
 - Thats why the NULL's are still visible in the result table.
*/
*/


/* 4. SORTING DATA 
      - Handle the NULL before sorting data
      Lets say we have 15,NULL,20 if we sort it by default in ASC it shows the result as NULL,15,20
      
      IN ASC the NULL's are displayed first and then the lowest to highest values.

      IN DESC for 15,NULL,20 --> 20,15,NULL the NULL is shown at the end

      - Its neither high nor lowe its a unknown value just so SQL just throws NULL first and then lower values in ASC 
      - in DESC it just throws NULL's to bottom.
      - so thats why handle the NULL's before Sorting 
*/

-- TASK : 
-- Sort the customers from lowest to highest scores, with NULLs appearing last.

-- Normal way NULL show up at the top. but we need NULL at the bottom.
SELECT 
CustomerID,
Score
FROM Sales.Customers
ORDER BY Score;

-- Method 1 - Replace the NULLs with very big number to keep NULL at bottom when sorted in ASC 
--            Disadvantage : 
--            If we use big number for now if in future any record with that number can appear and make the sort messier.
--            Also in future the hard coded value can fall between some numbers and show NULL in between the sorted data.
SELECT 
CustomerID,
Score,
COALESCE(Score, 99999) as hard_code_null
FROM Sales.Customers
ORDER BY COALESCE(Score, 99999);

/* Method 2 - Use CASE WHEN to find the flags and sort
   - In this method we write CASE WHEN to find null and assign 1 as flag for them and 0 as flag for existing value.
   - So if we order by this same CASE WHEN logic the 1 is pushed down to last as all are 0 they are kept in first.
     but still as there is tie the scores wont be in ascending order.
   - In ORDER BY if first condition does have tie it needs to have second condition to sort out.
   - So we provide a second condition to sort by or a column itself to have a ascending order sort comparing
      between 2 number who had tied.
   - If 2nd condition is not given the column follows the original tables column order.
-- */
SELECT 
CustomerID,
Score,
CASE WHEN Score IS NULL THEN 1 ELSE 0 END as flag
FROM Sales.Customers
ORDER BY CASE WHEN Score IS NULL THEN 1 ELSE 0 END;

/* NULLIF() 
   - Compares two expression returns : 
     - NULL, if they are equal.
     - First Value, if they are not equal
   Syntax : NULLIF(Value1, Value2)
   - Here we have value_2 just for a check we never gonna return value_2
   - If the compared value is True it returns NULL.
   - If the comparison fails it returns first_value.
   - Its basically like place the expecting value and check if that value available it gives you a NULL.
   - special case if use in dividing by zero place NULL inplace of 0 when dividing by 0 that will help us from getting error.
     but we can see a NULL atleast rather than crashing the query.

   NULLIF(PRICE, -1)
   - if each row value of PRICE == -1 we get a NULL
   - if each row value of PRICE != -1 we get PRICE row value.
   ORDERID    PRICE   NULLIF
     1         90     90     90 == -1 NO  -> RETURN PRICE VALUE
     2         -1     NULL   -1 == -1 YES -> RETURN NULL

     USED IN ANALYSIS 
     - ORIGINAL PRICE  compared to DISCOUNT PRICE
     - If they are both equal then we have a error in the discount calculation as we wont get same prices after discount.
     - So this NULLIF helps us to flag the unexpected results.
     - we place the expecting value as second parameter whoever from first parameter hits this value they gets NULL.
     - So the expected result are hit and that can be evaluated based on the context what you are looking for.
     - Here i placed discount_price in 2nd price as i expect the discount_price would have been decreased lower than original_price.
     - IF I get all values then I can safely say the discount price are safely calculated.
     - IF anywhere i see a NULL that means the discount_price is not calculated and its still same as original price.
     - can be used to immediately check the discount applied on all products on a festival season to make most sales and attract customers.

     NULLIF(Original_price, discount_price)
     ORDERID    Original_price    discount_price    NULL_IF
        1          150               50               150
        2          250               250              NULL

   USE CASE :

   1. DIVISION BY ZERO :
      - Preventing the error of dividing by zero
*/
-- Find the sales price for each order by dividing sales by quantity
SELECT 
OrderId,
Sales,
Quantity,
-- Sales / Quantity as price -- fails as we can have in 0 quantity so we need to place NULL atleast to get the result.
Sales / NULLIF(Quantity, 0) as Price
FROM Sales.Orders;


/* IS NULL 
   - Returns TRUE if the value IS NULL, otherwise it returns FALSE.
   Syntax : value/ Expression  IS NULL

   IS NOT NULL
   - Returns TRUE if the values IS NOT NULL, otherwise it returns FALSE.
    Syntax : value/ Expression  IS NULL

    USE CASE :
   1. Filtering Data
      - Searching for information using both IS NULL | IS NOT NULL
      - Like filtering only the non null values by removing null's

   
*/
-- TASK
-- Identify the customers who have no scores
SELECT 
*
FROM Sales.Customers
WHERE Score IS NULL;

-- Show customers who has score
SELECT 
* 
FROM Sales.Customers
WHERE Score IS NOT NULL;

/* 2. ANTI JOINS :
      - Finding the matched rows between tables.
      - In SQL there is nothing like ANTI join we combine JOINS + WHERE to get the ANTI results.
      - If 2 tables are joined over a key column the matched rows will hold the values.
      - when join is made on to something the table who is in join will hold NULL on the key column if there is no match
        on the main table.
      - Lets say we have customers table and orders table
      - on join with orderID for both table we get the customers who have placed orders joined but the orders who dont have customers will be left NULL.
      - AFTER join if we filter data upon the joining tables key column NULL value we can find the orders with no customers simply.
      - This what makes ANTI JOINS.
      - If we ask the joining table who are nulls we get the info about the missing or matchingb records from main table.
*/
-- Show all details for customers who have not placed any orders.
SELECT 
*
FROM Sales.Customers
SELECT 
*
FROM Sales.Orders;
-- LEFT Anti Join 
SELECT 
c.CustomerID,
FirstName,
LastName,
Country
FROM Sales.Customers c
LEFT JOIN Sales.Orders o ON c.CustomerID = o.CustomerID
-- Once the right table has no match from left table the all columns values on 
-- right table holds NULL so we can filter on any column but do it on the key column used to join 
WHERE o.CustomerID IS NULL  

/* NULL vs EMPTY vs BLANCK SPACES 
   
   NULL   - Means NOTHING, unknown!
   EMPTY  - String value has zero characters
   BLANK
   SPACES - String Value has one or more space characters.

   - For '' and ' ' we see nothing in the result display.
   - Its hard to detect the data quality issues by seeing this thing.
   - to overcome we can calculate an find length.
   - if there is a blank space we get '1' and if its empty it gets '0'
   - So calculate the length to find the blank spaces and empty values to be precise.
   

   	                  NULL	    EMPTY String	   Blank Space
Representation	      NULL	      ‘’	           ‘    ‘
Meaning	              unknown	unknown, 	       known, space value
                                empty value
Data Type	          Special 	String (0) → size  String (Size 1 or more)
                      Marker
Storage               Very 	    occupies memory	   occupies memory(each space)
                      minimal
Performance	          Best	    Fast	           Slow
Comparison To find	  IS NULL 	= ‘’	           = ‘  ‘
*/




/* DATA POLICY 
   - Set of rules that defines how data should be handled.
   1. Only use NULLs and empty Strings, but avoid blank spaces.
   2. Only use NULLs and avoid empty strings and blank spaces. 
   3. Use the default value 'unknown' and avoid using NULLs, empty strings and blank spaces
   */
WITH orders AS(
  SELECT 1 Id, 'A' Category UNION
  SELECT 2, NULL UNION
  SELECT 3, '' UNION
  SELECT 4, '  ' 
)
SELECT
*,
DATALENGTH(Category) AS CategoryLen,

-- Policy-1 Avoid having balnk spaces in data use TRIM() function on column to delete whitespaces.
TRIM(Category) AS Policy_1,
-- DATALENGTH(TRIM(Category)) AS Policy_1 -- This is just a check after TRIM

-- Policy 2 Convert '' value to NULL
-- so first turn ' ' blanck spaces to empty string and then use NULLIF
-- Remember we give expecting value in order to get NULL for matched values.
NULLIF(TRIM(Category), '') Policy_2,

/* Policy - 3 - here we have to turn NULL to a value so we have to use ISNULL OR COALESCE
    - Here we have to first trim blank spaces to empty
    - Then turn empty to NULL's using NULLIF use expectation value as '' as we turned everything blank soaces to '' and already '' exists anyhow.
    - Now we have NULL's alone no more spaces and empty.
    - If we have NULL we can use COALESCE() or ISNULL() to turn the NULL to default value.
    - so 
      Turn '  ' blank spaces to ''     ---> Use TRIM()                ---> Turn's ' '    to '' Empty value 
      Turn ''   Empty value to NULL's  ---> Use NULLIF()              ---> Turn's ''     to NULL's  Value
      Turn NULL's to Default values    ---> Use COALESCE()/ ISNULL()  ---> Turm's NULL's to 'unknown' default values
 */ 
COALESCE( NULLIF( TRIM(Category), '' ), 'unknown') Policy_3

FROM Orders

/* BEST APPROACH 
   USE
   Policy - 2 : 
   If doing Insertion
   - Replacing empty strings and blanks with NULL during data preparation before
     inserting into a database to optimize storage and performance.
   If doing preparation 
   - Replacing empty strings, blancks, NULL with default value during data preparation 
     before using it in reporting to improve redability and reduce confusion.
   - For inserting in the database using the policy 2 will be more optimized way

  - If preparing data before showing it in report like POWERBI and Tableau
  - If its one of the last step before showing the data to the users we go with the policy 3
  - Because showing a word like NULL in a report is hard to read and understand so placing a unknown word says alot of meaning
    saying there is a missing data 
  - If we use policy 3 to store data in database its a bad to store aa huge word 'unknow' rather than having NULL's
*/

/* NULL Function
   - NULLs is a special markers means missing value.
   - Using Nulls can optimize storage and performace

   Function
   - we have various functions to handle NULL's
   1. COALESCE() / ISNULL() 
      If wanted to replace a NULL with a Value
       NULL --> 30
   2. NULLIF
      If wanted to replace a value with a NULL
       30 --> NULL
   3. IS NULL | IS NOT NULL
      To check if null exists or not.
- We have to treat NULL's specially before we do any TASK.

use cases : 
Handle NULLs          - Before doing Data Aggregations
                        Before doing any mathematical operations
                        Joining Tables
                        Sorting data
Finding unmatched data - Left Anti Join
DATA policies --> Provide NULLs, Default Values
        