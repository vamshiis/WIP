/* Part_Extraction Category of DATE & TIME FUNCTIONS :
    We have Following Functions
    - DAY()
    - MONTH()
    - YEAR()
    - DATEPART()
    - DATENAME()
    - DATETRUNC()
    - EOMONTH()
*/
-- Various way to query a date columns
SELECT 
OrderId,
-- Table Date Columns
OrderDate,
ShipDate,
CreationTime,
-- Hardcoded date column
'2027-01-14' Future_Date,
-- GETDATE() Function column
GETDATE() Today
FROM Sales.Orders

/* Part Extraction */
-- 1.DAY() - Returns the day from a date.
-- 2.MONTH() - Returns the month from a date.
-- 3.YEAR() - Returns the year from a date.
-- Syntax : DAY(date), MONTH(date), YEAR(date)
-- Return Type is 'INT'

SELECT 
OrderID,
CreationTime,
YEAR(CreationTime) Year,
MONTH(CreationTime) Month,
DAY(CreationTime) Day
FROM Sales.Orders

/* 4. DATEPART() - Returns a specific part of date as a number.
                   Return Type is 'int'
   We can extract the quarter , week info from the dates using this function.
   Syntax : DATEPART(part, date)
            Ex: DATEPART(month, orderDate) can also be done as 
                DATEPART(mm, OrderDate) 'mm' is abbrevation for Month
*/
SELECT 
OrderID,
CreationTime,
DATEPART(year,CreationTime) Year_dp,
DATEPART(mm,CreationTime) Month_dp,
DATEPART(dd,CreationTime) Day_dp,
DATEPART(hh,CreationTime) hh_dp,
DATEPART(week,CreationTime) week_number,
DATEPART(quarter,CreationTime) quarter
FROM Sales.Orders

/* 5. DATENAME() - Returns the name of a specific part of a date.
                 Syntax : DATENAME(part, date)
                 Returns a String for month, weekday and even though day,year are ints they are stored as strings.
                 
    Useful in reports to display month names, weekday names instead of numbers.
*/
SELECT 
OrderID,
CreationTime,
DATENAME(mm,CreationTime) Month_dn,
DATENAME(weekday,CreationTime) weekday_dn, --wk for abbrevation
DATENAME(dd,CreationTime) day_dn, -- Display as numerical data but stored as Strings
DATENAME(year, CreationTime) Year_dn -- Display as numerical data but stored as Strings
FROM Sales.Orders

/* 6. DATETRUNC() 
- Truncates the date to the specific part. 
- Syntax : DATETRUNC(part,Date)
- Return : Maintains same dtype of used date column 
- Here we just reset things inside the DATETIME2 format.
-            YYYY-MM-DD HH:MM:SS
             2030-04-23 13:12:46
             Time resets to 00
             Date resets to 01
- If part given as 
  minute then datetime format turns into 2023-04-23 13:12:00
  hour   then datetime format turns into 2023-04-23 13:00:00
  day    then datetime format turns into 2023-04-23 00:00:00
  month  then datetime format turns into 2023-04-01 00:00:00
  year   then datetime format turns into 2023-01-01 00:00:00
- So upto given part is kept but rest to right is reset.
- 
*/
SELECT 
OrderID,
CreationTime,
DATETRUNC(minute,CreationTime) minute_dt,
DATETRUNC(day,CreationTime) day_dt,
DATETRUNC(yy,CreationTime) year_dt
FROM Sales.Orders

-- Why DATETRUNC is useful in data anlysis.
-- lets say we want to find the per month orders.
-- In below query as CreationTime is DATETIME2 Format we have everything unique so we cant even group by.
SELECT
CreationTime,
COUNT(*)
FROM Sales.Orders
GROUP BY CreationTime;

-- To overcome above problem we need to truncate our datetime column until month so we can group by and do analysis quickly.
SELECT
DATETRUNC(mm,CreationTime) Creation,
COUNT(*)
FROM Sales.Orders
GROUP BY  DATETRUNC(mm,CreationTime);

-- Now if we wanna find sales for every year if the creationTime column is datetime2 type we need to again truncate to get the actual result.
SELECT
DATETRUNC(yy,CreationTime) Creation,
COUNT(*)
FROM Sales.Orders
GROUP BY  DATETRUNC(yy,CreationTime);

/* EOMONTH()
   Returns the last day of the month
   Syntax : EOMONTH(date)
   Return Type 'DATE'
   ex: 2025-08-14 -> EOMONTH() -> 2025-08-31 // Turns the day to months end day
       2025-02-01 -> EOMONTH() -> 2025-08-28
       2025-08-31 -> EOMONTH() -> 2025-08-31 // Stays the same no change
*/
-- Turn date to End of month dates
SELECT 
OrderID,
CreationTime,
EOMONTH(CreationTime) End_Of_Month
FROM Sales.Orders;

-- Turn the End of Month Dates to First of month dates
SELECT 
OrderID,
CreationTime,
DATETRUNC(mm,EOMONTH(CreationTime)) First_Of_Month
FROM Sales.Orders;


/* USE CASES */

/* -------------Data Aggregations--------------- */
--  Q.How many orders were placed each year?

-- If for analysis directly use the functions which will be faster to compute the results.
SELECT 
YEAR(OrderDate) years,
COUNT(*)  order_count
FROM Sales.Orders
GROUP BY YEAR(OrderDate);

-- Used in pipelines to maintain the dtype of column same so downstream users can use various date and time functions easily.
SELECT
DATEPART(yy,DATETRUNC(yy,OrderDate)) years,
COUNT(*) order_count
FROM Sales.Orders
GROUP BY DATETRUNC(yy,OrderDate);

-- Q.How many orders are placed each month??

-- This too can be used in downstream data anlaysis process
SELECT 
MONTH(OrderDate) Month,
COUNT(*) order_count
FROM Sales.Orders
GROUP BY MONTH(OrderDate);

-- If needed names of each month dtype stays string use this for reporting(data analysis) not in pipelines.
SELECT 
DATENAME(MM,OrderDate) month,
COUNT(*) order_count
FROM Sales.Orders
GROUP BY DATENAME(MM,OrderDate);

-- To maintain the same dtype of the column used we need to use datatrunc() operation useful in pipelines.
SELECT 
DATEPART(mm,DATETRUNC(mm,OrderDate)) as months, -- dtype stays the same as 'OrderDate' dtype 
COUNT(*) order_count
FROM Sales.Orders
GROUP BY DATETRUNC(MM,OrderDate);

/* ----------- DATA FILTERING -------------*/
-- Filtering Data using an integer is faster than using a string
-- so when need to filter the datetime dtype column use individual operations
-- like MONTH(), DAY(), YEAR() and DATEPART()
-- Don't use DATENAME() OR DATETRUNC() 
-- Even the allowed should be avoided for filtering because where needs to first get the ourput of the function applied to the column
-- Then only it can filter out date column this takes 2 operations.
-- If we pass the bare column + raw date constarints it simply need to match and filter no conversion operation required

-- Q.show all orders that were placed during the month of february
SELECT 
*
FROM Sales.Orders
WHERE MONTH(OrderDate) = 2;

-- Practice of specifiers like quarter, week, iso_week and function DAYOFYEAR()
SELECT
'2026-02-01', 
DATEPART(quarter,'2026-04-01') AS dp_quarter, -- gives int format of quarter
DATENAME(quarter,'2026-04-01') AS dn_quarter, -- says the string format of quarter
 -- Full DATETIME2 dtype value is returned
 -- Truncates DATETIME2 dtype value's whole Time format
 -- Even if there is only DATE format the whole value is returned as DATETIME2 format by making Time format 0's.
DATETRUNC(quarter, '2026-04-01 23:23:23.055') AS dt_quarter;

-- If wanted whats the day count out of 365 days use DAYOFYEAR() function
SELECT
 GETDATE() AS today,
 DATEPART(DAYOFYEAR, GETDATE()) day_of_year;

-- Weeks truncation with iso_week and week
 SELECT 
  'today',
  -- 2026-05-31 00:00:00 -- Sunday
  -- 2026-06-01 00:00:00 -- monday
  -- 2026-06-06 00:00:00 -- saturday
  -- 2026-06-07 00:00:00 -- sunday
  -- 2026-06-08 00:00:00 -- monday
  -- 2026-06-09 00:00:00 -- Tuesday
  -- Always truncs a date to its sunday start date and time like "sunday_date 00:00:00"
  -- EX 2026-06-09 if passed to datetrunc() this truncs to 2026-06-07 00:00:00
  -- similarly 2026-06-06 if passed this truncs to 2026-05-31 00:00:00
  DATETRUNC(week, '2026-06-09') AS date_trunc
  UNION ALL
  SELECT
  'Iso_week',
  -- ISO truncs the date to monday midnight while week truncs date to sunday midnight.
  -- EX : 2026-06-09 23:32:32 truncs to 2026-06-08 00:00:00
  --      2026-06-06 11:18:18 tuncs to 2026-06-01 00:00:00
  DATETRUNC(iso_week, GETDATE()) 