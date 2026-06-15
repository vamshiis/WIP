/* FORMAT-TING Category of DATE & TIME Function. 
   FORMAT() :
   Syntax : FORMAT (value, Format, culture(optional))
                    Deafult culture : 'en-US'  
      - Formats a Date or Time Value              
      - Return to String Values
      - we have different Format specifiers for date time format and they are case-sensitive.

*/
-- Q. FORMAT CreationTime column of Orders to dd,ddd,dddd , MM,MMM,MMMM , USA_Format, European_Format
SELECT OrderID,
       CreationTime,
       FORMAT(CreationTime, 'MM-dd-yyy') AS USA_Format,
       FORMAT(CreationTime, 'dd-MM-yyyy') AS European_Format,
       FORMAT(CreationTime, 'dd') AS dd,
       FORMAT(CreationTime, 'ddd') AS ddd,
       FORMAT(CreationTime, 'dddd') AS dddd,
       FORMAT(CreationTime, 'MM') AS MM,
       FORMAT(CreationTime, 'MMM') AS MMM,
       FORMAT(CreationTime, 'MMMM') AS MMMM,
       FORMAT(CreationTime, 'yy') AS yy,
       FORMAT(CreationTime, 'yyy') AS yyy,
       FORMAT(CreationTime, 'yyyy') AS yyyy
FROM   Sales.Orders;


-- Show Creation Time using the following Format
-- Day Wed Jan Q1 2025 12:34:56 PM
SELECT OrderID,
       CreationTime,
-- Use DATENAME() for quarter generation as it returns the value as string then only we can concat.
-- tt specifier in FORMAT() gives us whether its AM or PM.
'DAY ' + FORMAT(CreationTime, 'ddd MMM') + ' Q' + DATENAME(quarter, CreationTime) + FORMAT(CreationTime, ' yyy hh:mm:ss tt') AS Custom_Format,
-- Wrap around "" if there is static value to include after or in between a function result.
-- like f-strings in python 
FORMAT(CreationTime, '"DAY" ddd MMM "Q"') + DATENAME(quarter, CreationTime) + FORMAT(CreationTime, ' yyy hh:mm:ss tt')
FROM   Sales.Orders;

/* Formatting Use Case : 
   Data Aggregations 
   - We use formatting on dates before doing aggregations. 
   - where need to display a sales report by month 
   - we can simply format a date to Jan 26 rather than it beeing in DATETIME2 format for report making.
*/
SELECT 
FORMAT(CreationTime, 'MMM yy') Order_month,
COUNT(*) orders
FROM Sales.Orders
GROUP BY FORMAT(CreationTime, 'MMM yy');

/* DATA STANDARIZATION 
   - In projects the data is Extracted from various sources like .csv file, API's, Database into one central storage.
   - Here each source can have different format for date.
   - For analytice there could be problem if there is no standard format of date column.
   - So we clean up the format into one clean and standard format.
   - That me we have to format the incoming data to a standard format.
   - Once we have a standard format we can use it for analytics and reports.
   - so this is a common use case in data preparation and in data cleanup by formatting different formats into one clean formats.
   */

/* ==============================================================================
   DATE FORMAT SPECIFIERS Practice
===============================================================================*/
SELECT 
TOP(1)
OrderID,
CreationTime,
-- D specifier --> returns the datetime2 column as day_of_week, month_name day, year(yyyy)
FORMAT(CreationTime,'D') Formatted_value
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- d specifier --> returns the date as day/month/year - short date pattern
FORMAT(CreationTime,'d') 
FROM Sales.Orders
UNION ALL 
SELECT TOP(1)
OrderID,
CreationTime,
-- dd specifier --> returns the day of the month with leading zero 
FORMAT(CreationTime,'dd') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- ddd specifier --> returns the abbreviated name of day 
FORMAT(CreationTime,'ddd') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- dddd specifier --> returns the full name of day 
FORMAT(CreationTime,'dddd') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- M specifier --> returns 'Month_name month_number(no leading zeroes)' 
FORMAT(CreationTime,'M') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- MM specifier --> returns Month_Number (With leading zero for single digit month number)
FORMAT(CreationTime,'MM') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- MMM specifier --> returns Abbreviated Month Name
FORMAT(CreationTime,'MMM') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- MMMM specifier --> returns Full Month Name
FORMAT(CreationTime,'MMMM') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- y specifier --> returns `month_name 4-digit-year(like 2026)`
FORMAT(CreationTime,'y') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- yy specifier --> returns `2-digit-year(like 26)`
FORMAT(CreationTime,'yy') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- yyy & yyyy specifier --> returns `4-digit-year(like 2026)`
FORMAT(CreationTime,'yyy') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- hh --> returns Hour in 12-hour clock with leading zero
FORMAT(CreationTime,'hh') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- HH --> returns Hour in 24-hour clock with leading zero
FORMAT(CreationTime,'HH') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- %m --> returns minute without a leading zero for single digits
FORMAT(CreationTime,'%m') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- mm --> returns minute 
FORMAT(CreationTime,',mm') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- s --> returns sortable Date String(2026-12-12T14:05:09)
FORMAT(CreationTime,'s') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- %s --> returns single digit second
FORMAT(CreationTime,'%s') 
FROM Sales.Orders
UNION ALL
SELECT TOP(1)
OrderID,
CreationTime,
-- s --> returns two digit second
FORMAT(CreationTime,'ss') 
FROM Sales.Orders;


-- use this to insert different specifiers to check easily
SELECT 
'1-12-2026' as date,
FORMAT(CAST('1-12-2026 13:40:01:11' AS datetime2),'ss') 