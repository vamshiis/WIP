DATE & TIME FUNCTIONS
What is DATE ??
- A Date can repersent a event / deadline/ info about something very important.
- EX : 2026-06-12 
  we have 3 components in date year - 2026, month - 06, day - 12
- In database we call this 3 components structure as a date in SQL and Databases.

What is Time ??
- Time refers to a specific point within a day.
- EX : 23:45:59 --> 23 - Hour, 45 - Minutes(0 to 59) , 59 - Seconds(0 to 59)
- So with this 3 components we call it a Time in Database and SQL.

What is DATE-TIME Format ?
- If we combine this both we get a new format know as TimeStamp.
- In Oracle, PostgresSQL, MySQL we call it as TimeStamp Format.
- In MICROSOFT SQL SERVER We call it as 'DateTime2' Format.
- So in this format we have date information together with the time information.
- Ex : 2026-06-12 12:02:23 
    Here we have 6 components from left to right
    Here we have the like hierarchy in this structure 
    We start with the highest which is the year --> month --> day --> hours --> minutes --> seconds
- We also can see the fractions of the seconds in databses for the DATETIME format.
So this are the 3 Formats in SQL DATE, TIME, DATE-TIME

In SQL We have 3 different Sources and Order to query the DATES.
1. DATE columns from Table.
2. Hardcoded constant String value.
   EX : '2025-06-20' its is hardcoded and static for all rows for specific Table
3. GETDATE() FUunction 
   - It is the first and most important function we use in SQL.
   - It Returns the current date and time at the moment when the query is executed.

DATE & TIME FUNCTIONS OVERVIEW : 
Now we have clear understanding of what is Date&Time in SQL.
How to manipulate those information with the Using SQL functions.
             2026-06-12
- One of the thing we can do with the date is we can go and extract different parts of the DATE like
- if we want the year we extract the YEAR 
- if we want the month we extract the MONTH
- if we want the day we extract the DAY
This is called "PART EXTRACTION"

2. We can change the DATE format
   - Instead of having - between in the date we can format to yy/MM/dd
   - we can also format it as 20 Aug 2025, 20.08.2025

3. Another category is we can do DATE calculations.
   - we go to our date and add 3 years.
   - we can find difference between 2 dates.

4. We can test and validate this DATE whether it is a real which SQL gonna understand.
we can put it to test in the output we get TRUE(1) or FALSE(0)

DATE & TIME Functions : 
1. PART EXTRACTION Category
    - DAY()
    - MONTH()
    - YEAR()
    - DATEPART()
    - DATENAME()
    - DATETRUNC()
    - EOMONTH()

2. FORMAT & CASTING 
    - FORMAT()
    - CONVERT()
    - CAST()

3. CALCULATIONS
    - DATEADD()
    - DATEDIFF()

4. VALIDATION
    - ISDATE()