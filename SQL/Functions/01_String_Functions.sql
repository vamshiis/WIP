/* String Functions 
   We have 3 Categories 
   # String Manipulation
      - CONCAT()
      - CONCAT_WS()
      - UPPER()
      - LOWER()
   # String Calculation
      - LEN()
   # String Extraction
      - LEFT()
      - RIGHT()
      - SUBSTRING()
*/
-- **Manipulation Functions**
-- 1.CONCAT() - Combines multiple strings into one
-- Show a list of customers first name together with their country in one column
SELECT 
first_name,
country,
CONCAT(first_name,'-',country) AS name_country
FROM customers

-- 2.UPPER() - Converts all the characters to uppercase 
-- 3.LOWER() - Converts all the characters to lowercase 
-- Convert first name to lower case
SELECT 
LOWER(first_name) AS low_name
FROM customers
-- Convert the first name to uppercase
SELECT 
UPPER(first_name) AS up_name
FROM customers;

-- 4. TRIM() - Removes Leading and Trailing Spaces
-- Find the customers whose first name contains leading or trailing spaces
SELECT first_name,
LEN(first_name) len_name,
LEN(TRIM(first_name)) trim_len,
LEN(first_name)  -  LEN(TRIM(first_name)) flag -- anyone with flag value 1 or more that value has spaces
FROM customers
WHERE LEN(first_name) !=  LEN(TRIM(first_name))
--WHERE first_name != TRIM(first_name)

-- 4. REPLACE - Replaces specific character with a new character
-- Remove dashes (-) from a phone number
SELECT
'123-456-789' AS PHONE,
REPLACE('123-456-789','-','') AS clean_phone;

--Replace file extension
SELECT 
'report.txt',
REPLACE('report.csv','.txt','.csv') AS new_file


-- **CALCULATION**
-- 1. LEN() - Count how many characters
-- Calculate the length of first_name
SELECT
first_name,
LEN(first_name)
FROM customers;

-- **String Extraction**
-- 1. LEFT() - Extracts specific number of characters from the start
-- 2. RIGHT() - Extracts specific number of characters from the End
-- Both needs a (value, Nr.of characters) as arguments, left gets from first and right get end characters.

-- Retrieve the first two characters of each first name.
SELECT 
first_name,
LEFT(TRIM(first_name),2) first_2_char
FROM customers;

-- Retrieve the last 2 characters of each first name
SELECT
first_name,
RIGHT(first_name,2) last_2_chars
FROM customers

-- 3. SUBSTRING() - Extracts a part of string at a specified position.
-- It need the (value,start_pos,length) arguments to be passed to get a substring out of string.

-- Retireve a list of customers first names removing the first character.
SELECT
first_name,
SUBSTRING(TRIM(first_name), 2, LEN(first_name)) sub_name
FROM customers