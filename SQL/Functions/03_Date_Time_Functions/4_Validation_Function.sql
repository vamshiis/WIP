/* VALIDATION Category of DATE TIME Functions 
   
   We only have 1 Function under this Category.
   
   ISDATE() : Check if a value is a date.
               Return 1 if the string value is a valid date.
   - We can pass a DATE as STRING value and function returns 1.
   - we can also pass a integer to check and still it returns 1.
   - It only returns 1 - 'TRUE' for the date passed as standard format '2025-06-12' --> String value.
   - If we pass jumbled format '12-10-2026' it returns 0 'False'
   Syntax : ISDATE(value)
            EX : ISDATE('2026-06-10') Returns 1
                 ISDATE(2025)         Returns 1
   USE CASE:
   -  We can verify the data of a string column whether we can CAST it to the DATE datatype.
      we apply IFDATE() and catches only those dates whose flag is '1' for the final CAST simply.
   - Useful to check and validate 
*/
SELECT 
ISDATE('123') DATE_CHECK_1,
ISDATE('2025-06-12') DATE_CHECK_2, -- Standard format passes the check and returns 1
ISDATE('20-08-205') DATE_CHECK_3,  -- Not a Standard Format the check will return 0
ISDATE('2026') DATE_CHECK_4,       -- YEAR passes the check and returns 1
ISDATE('08') DATE_CHECK_5          -- Month the check gonna return 0 


/* USE CASE : 
   - Here in this 4 dates we have 3 as standard format which can be evaluated to TRUE when IFDATE() function is applied.
   - And only 1 date has a date quality issue which will return 0 if DATEIF is applied.

   - Now our Task is to cast the Date column which are in String data type to DATE data_type.
   - So we will apply the 'SUBQUERY' which gonna CAST all specified columns values to said data type.
*/
-- Raw Data
SELECT '2025-08-20' AS OrderDate UNION
SELECT '2025-08-31' UNION
SELECT '2025-08-19' UNION
SELECT '2025-08';

-- Solution
SELECT 
   --CAST (OrderDate AS DATE) AS OrderDate 
/*
   - The above line Fails as it expects all the values to be compatabile to convert to DATE data_type but 4th value is not a DATE compatabile
   - So we need to pass it through a function DATEIF() and catch the ones which returns value as 1 as it indicates the Value is DATE compatabile.
   - USING CASE WHEN to find the return of 1 by DATEIF() and other who value is 0 gets NULL in new column of DATE data type.
   - It is a important step before doing analysis to have a proper and clean data, and it also helps to find the data quality issues.
*/ 
    OrderDate,
    ISDATE(OrderDate),
    CASE WHEN ISDATE(OrderDate) = 1 THEN CAST (OrderDate AS DATE) 
        ELSE '9999-01-01' -- Instead of getting NULLS we can hard code the value and later can filter to find those records based on hard coded value
    END [New Order Date] -- Old values which were string and are comptabile are now successfully converted to DATE data type.   
FROM   
(
        SELECT '2025-08-20' AS OrderDate UNION
        SELECT '2025-08-31' UNION
        SELECT '2025-08-19' UNION
        SELECT '2025-08'
) AS t;
-- Lets see the rows with BAD quality data whose string value is not a date.
-- so we can see and repair the data or to find the required record that has been neglected by improper data
--WHERE ISDATE(OrderDate) = 0

/* TRY_CAST() & TRY_CONVERT() :
   We can do the same work without using a CASE WHEN.
   
   We have 2 Functions to handle the data type conversion.
   TRY_CAST() :
   Syntax : TRYCAST(column_name AS data_type)

   - If the String value is standard date and contains non compatabile date then we can use TRY_CAST()
   - So TRY_CAST will check to convert a specified column values to specified data type by checkig it compatability.
   - Here we wanna try to convert to date by checking it with ISDATE() and then cast if there pass this function and verify its compatability for DATE data type.
   - But TRY_CAST will do that under the hood by checking the compatability itself and safely insert NULL for non-compatabile values simply.
   - we need to have the column value in the following condition in order to use TRY_CAST to convert a string values to DATE data type
     1. All values needs to be Standard format like 2026-06-12 (yyy-mm-dd)
     2. If the date format is anything other than standard format it displays null in the end result even for valid date format like yyyy/mm/dd.

   - Use it directly if all values follows same pattern inside the string values.
   TRY_CONVERT() : 
   Syntax : TRY_CONVERT( data_type, column_name, style_code)
   OUTPUT : for a date conversion from string to date we do we get the Standard format of the date like yyy-mm-dd

   - If the column has string values and all are dates which are in Non-standard format then we can use TRY_CONVERT().
   - In TRY_CONVERT() we can specify the style_code for the pattern it has so it can safely convert without crashing.
   Rules to use:
   1. All the string values date format needs to be in the specified style_code format.
   2. Even if one string value is compatabile but doesnt follow the said style_code specifier format it displays NULL.

   - Use this only when there is non-standard format of dates in string values by specifying the style_code.
*/

-- Above query with TRY_CAST() function.
SELECT 
OrderDate,
TRY_CAST(OrderDate AS DATE) new_date
FROM   
(
        SELECT '2025-08-20' AS OrderDate UNION
        SELECT '2025-08-31' UNION
        SELECT '2025-08-19' UNION
        SELECT '2025-08'
) AS t;


-- Using TRY_CONVERT see the string holds non standard date format so we specified that pattern style code.
SELECT TRY_CONVERT(DATE, '31/01/2026', 103) AS CleanDate;
-- Outputs: 2026-01-31 perfectly!


/* Then how to handle the mixed patterns inside the string value.
  
  To handle a column with mixed formats, we can layer multiple TRY_CONVERT functions inside a COALESCE function. 
  COALESCE evaluates options from left to right and picks the first one that successfully works (is not NULL)
*/
SELECT
    MixedDateString,
    COALESCE( 
             TRY_CAST(MixedDateString AS DATE),
             TRY_CONVERT(DATE, MixedDateString, 103),
             TRY_CONVERT(DATE, MixedDateString, 101),
             '1990-01-01'
    ) AS FinalStandardDate
FROM (VALUES 
    ('2026-06-15'),  -- Standard format
    ('15/06/2026'),  -- DD/MM/YYYY format
    ('06/15/2026'),  -- MM/DD/YYYY format
    ('GarbageText')  -- Totally broken text
) AS TestTable(MixedDateString);