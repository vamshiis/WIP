/* CASTING 

  CONVERT() - converts a date or time value to a different data type & Formats the value.
  SYNTAX : CONVERT(data_type, value [,style](optional)) 
           deafult style - 0 
  Ex : CONVERT(INT, '123')
       CONVERT(VARCHAR, OrderDate, '34') --> style is given as 34 to convert.
  - Only Convert can change from one data type to another data type and format the date & time using style specifiers.
*/
SELECT
CONVERT(INT, '123') [String to Int Convert],
CONVERT(DATE, '2026-06-10') [String to date Convert],
CreationTime,
CONVERT(DATE, CreationTime) [datetime converted to date dtype] 
FROM Sales.Orders

-- Convert the datatype of CreationTime to VARCHAR and format the date to USA standard
SELECT
CreationTime,
CONVERT(VARCHAR,CreationTime, 32) [USA std. style:32], --Dtype converted and formatted to to USA format
CONVERT(VARCHAR,CreationTime, 34) [EURO std. style:34]
FROM Sales.Orders;

/* CAST - Convert a value to a specified data type.
   Syntax : CAST(value AS data_type)
*/
SELECT
CAST('123' AS INT) AS [String to Int],
CAST(123 AS VARCHAR) AS [Int to String],
CAST('2026-06-11' AS DATE) [String to Date],
CAST('2026-06-11' AS DATETIME2) [String to DateTime],
-- CAST datetime2 data type to date of creationtime column in orders
CreationTime,
CAST(CreationTime AS DATE) [DATETIME2 TO DATE]
FROM Sales.Orders


/* TRY_CAST() : 
   Returns NULL for non-compatabile conversion rather than throwing ERROR
   Syntax : TRY_CAST(value AS data_type)
*/
SELECT ('90' AS INT) [Casted_Values] UNION 
SELECT('Hello' AS INT) --> Non- compatabile so places NULL instead of throwing an Error

/* TRY_CONVERT() : 
   - Returns NULL for the non-compatabile pattern rathern than a Error.
   - In convert we give style code to convert a said style pattern to specified data type
*/
SELECT TRY_CONVERT(DATE, '2025-07-10') ['Converted_value'] UNION
SELECT TRY_CONVERT(DATE ,'900000')  --> Rather than throwing Erro it places NULL for this value 