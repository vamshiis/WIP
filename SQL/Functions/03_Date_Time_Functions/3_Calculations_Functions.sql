/* Calculations Category of DATE_TIME Function's:

   DATEADD() - Adds or subtracts a specific time interval to/from a date.
               we can add/ subtract years,months and days.
   Syntax : DATEADD(part, interval, date)
            part -> the part to target like year,month or day.
            interval -> give positive value to add and negative to subtract.
            date -> On the column you wanna perform this operation.
*/
SELECT
OrderID,
OrderDate,
DATEADD(month, 3, OrderDate) AS [Three Months Later],
DATEADD(year, 2, OrderDate) AS [Two Years Later],
DATEADD(day, 5, OrderDate) AS [five days later],
DATEADD(day, -10, OrderDate) AS [Ten days Before]
FROM Sales.Orders

SELECT
DATEADD(day, 5, CAST('2026-05-30' AS DATE)) [5 days later]

/* DATEDIFF() 
   - Find the Difference between two dates.
     syntax : DATEDIFF(part, start_date, end_date)
   - It is an amazing Function to do the analysis on data.
*/
-- Find the Age of employees 
SELECT
EmployeeID,
CONCAT_WS(' ',FirstName,LastName),
BirthDate,
DATEDIFF(year,BirthDate,GETDATE()) as Age
FROM Sales.Employees;

-- Find the average Shipping duration in days for each month
SELECT
--OrderID,
--OrderDate,
--ShipDate,
Month(OrderDate),
AVG(DATEDIFF(day, OrderDate, ShipDate)) Avg_days_to_ship
FROM Sales.Orders
GROUP BY Month(OrderDate)

--Time Analysis 
-- Find the number of days between each order and previous order
SELECT 
OrderID,
OrderDate CurrentOrdersDate,
LAG(OrderDate) OVER (ORDER BY OrderDate) prev_Order_date,
DATEDIFF(day, LAG(OrderDate) OVER (ORDER BY OrderDate), OrderDate) Nr_of_days
FROM Sales.Orders;


-- practice to understand DATEDIFF is not about subtracting but to reach the boundary of end_date based on specifier.
/* 
   - Lets say we want the difference of years between 2025-06-12 and 2027-05-23
   - If we apply the DATEDIFF(year, 2025-06-12, 2027-05-23 ) we get the Result as '2'
      What it does under the hood ??
       - It tries to reach the specified year by counting from start_date to end_date
       - In start_date year is 2025 and in end_date the year is 2027
       - The start_date year tries to reach end_year by counting 1.
       - So from 2025 --> 2026 we count 1
            from 2026 --> 2027 we count 2
       - This is know as "Boundary crossing" rather than subtraction
    TRAP:
    what if the start_date is 31-12-2025 and end_date is 21-01-2026 if we try to count year between this two date 
    - on rough by looking we say '0" years since the start date is on 31-12 and end_date hasn't still crossed 31-12 which is still at 21_01
      means it still left with dates to turn it self to 31-12 then only we can say it has crossed the start_date set boundary at count becomes 1.
    - But due to the underlying calculation the DATEDIFF does it will completely ignore what is month and day in end_date.
    - Counts +1 until it reaches the end_date year.
    - so thats how it returns 1 even there is no year has passed.
*/
/*
   Important specifier is week for weekly reports 
   - if we want a reports of week we need to place a range to get the last week operations data.
   - to do it we need to find the start date of last week and end date 
   - we get there by either hardcoding a date of last week from monday to sunday 
   - but if hard coded it works for only last week what if we need a query that can pull any given date last week operation's
   - Then this query fails good for once time use if we hard code it.
   - But for future use it fails.
   - so we need to write a dynamic query that can adapt any given date last week data retriveal.
   - So we use the 'week' specifier.
   - The week specifier only counts the sundays crossed between 2 dates given
   - Here 06-06 is saturday and 07-06 is sunday if we apply a week specifier in DATEDIFF function we get '1' which indicates a week has been completed.
   - But it was just a day change from 06 - 07 so it doesnt care of a length of 7 called as week parameter instead it sees a sundary cross parameter alone and decides
    whether a week is done or not.
*/
SELECT 
    DATEDIFF(week, '2026-06-06', '2026-06-07') AS WeekDiff_Test1,
    DATEDIFF(week, '2026-06-07', '2026-06-12') AS WeekDiff_Test2;

DECLARE @OrderDate DATE = '2026-06-07'; -- Sunday
DECLARE @ShipDate  DATE = '2026-06-12'; -- Friday

/* what if order and ship done in same week then there will be no count of week instead we get 0.
   - But wait does this really a good idea to ignore a fast delivered order in average days of delivery calculation.
   - The answer is 'No'. no one try to ignore a order with faster delivery date to analyse 
   - so we try to get the days of delivery trackings, shipment tracking, transit tracking to know the average days taken to complete each operation
     rather than to calculate in weeks we need to choose day report for accurate tracking.
   - If we choose weeks we are simply ignoring the strict week to week time taken orders to deliver and ignoring the faster and slower who falls in between weeks.
*/
-- try to change orderDate and ShipDate from week to week and days-days to know why we need to consider a day specifier to track.

SELECT 
    DATEDIFF(week, @OrderDate, @ShipDate) AS WrongCalendarWeeks,
    DATEDIFF(day, @OrderDate, @ShipDate) AS TotalDays,
    DATEDIFF(day, @OrderDate, @ShipDate) / 7 AS RightBusinessWeeks;

    SELECT 
    -- Test 1: A Wednesday
    DATEADD(week, DATEDIFF(week, 0, '2026-06-10'), 0) AS SnappedToMonday1,

    -- Test 2: A Friday
    DATEADD(week, DATEDIFF(week, 0, '2026-06-12'), 0) AS SnappedToMonday2;
    -- DATEADD - on which part of date, how much to add, on what column/ date
    -- DATEDIFF - on which part of date, past_date, recent_date

    SELECT
    CAST(0 AS DATETIME) AS FIRST_MONDAY,
    DATEDIFF(week, 0,GETDATE()) [1st_monday_to_this_week_monday]; -- 66597
    
    -- This is how we get get week date by getting last week monday start and sunday as end 
    DECLARE @Thisweekmonday DATETIME = DATEADD(week,DATEDIFF(week, 0,GETDATE()),0);
    DECLARE @Lastweekmonday DATETIME =  DATEADD(day, -7, @Thisweekmonday);
    DECLARE @Lastweeksunday DATETIME = DATEADD(second, -1, @Thisweekmonday);
    
    SELECT 
    @Thisweekmonday [This_week_monday],
    @Lastweekmonday [last_week_(monday)start],
    @Lastweeksunday [last_week_(sunday)end],
    DATEDIFF(day,@Lastweekmonday,@Lastweeksunday) + 1 AS days_tracked;