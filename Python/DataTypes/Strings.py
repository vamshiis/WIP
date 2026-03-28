# Types category :
# Built in functions in Strings
# name = "Vamshi"
# # Type
# print(type(name))
# age = 23
# print(type(age))
# # print('Your age is:' + age) can't combine a string with an integer using + operator.
# print('your age is :'+str(age)) # str() converts any data into str data type. Its done to just execute this line it wont change in the memory.
# # age=str(age) --> this leads to change in memory completely converted from int to str data type.

# Math category :
'''len()
len(value) 
 - built-in function
 - output: int
 - counts everything even spaces
 - returns the number of items in a value 
 - returns the number of characters in string
 use case : 
 - validates input length.
 - check password quality make sure then password meets the min length requirements.
'''
# password = '   123a'
# print(len(password)) # output : 7 (includes spaces)
# if len(password) < 8:
#     print('ypur password is too short!')


''' count() :
count(substring)
 - str method
 - output: int
 - returns how often a word appears in the string.
   use case :
    - Word frequency Check --> Counts how many times a specific word appears.
    - Detects Quality Issues --> count how many unwanted characters in the data.
'''
# text = """
# Python is easy to learn.
# Python is powerful.
# many people love python.
# """
# print(text.count("Python"))

# Transformations Category -->  used to shape the String

''' replace()
 - used to replace the specified Character.
 - replace() is not just for changing the values we can also remove unwanted parts by replacing them with any empty string("")
 - chained methods are executed in order from left to right.
   each replace() runs on the result of the one before it.
 use case:
  clean Numeric Formats --> replace commas with dots in European-style decimal numbers
  change phone number format --> replace special characters with something else
  clean numeric formats --> remove symbols and commas to prepare foe numeric conversions
'''
# price = '1234,56'
# print(price.replace(",", "."))
# phone = "123-4567-456"
# print(phone.replace("-", "/"))
# print(phone.replace("-", ""))
# price="$1,599.99"
# print(price.replace("$","").replace(",",""))
# Challenge - remove format the phone number print with 00 upfornt
# phoneNumber="+49 (176) 123-4567"
# print("00"+phoneNumber.replace("+","").replace(" ","").replace("(","").replace(")","").replace("-",""))
# # Alternative way
# # import re
# # clean_number = re.sub(r'\D', '', phoneNumber) #removes everything other than digits.

''' Concatination (+):
  operator
  output: string
  - joins (concatinates) two strings into one.
  use case:
  Build file path - build dynamic paths using folder and file variables.
'''
# fName = "Vamshi"
# lName = "S"
# lName = fName + " " + lName
# print(lName)

# folder = "c:/users/vamshi/"
# file = "report.csv"
# full_file_path = folder+file
# print(full_file_path)


''' f-String
    - f-string is a formatted string is a modern, super-easy way to format and build strings.
    - lets us easily put variables and expressions directly inside the string values
'''
# name = 'vamshi'
# age = 23
# is_student = True
# # Normal way
# # Hard to read -There are lot of plus signs and we have to worry about spaces and types
# # print("My name is " + name + " ,I am " + str(age) + " years old, and Student Status is " + str(is_student))
# # modern and professional way - f-String way
# # print(f"My name is {name}, I am {age} years old, and Student status is {is_student}.")
# # we can also use the expressions inside the f-string
# # print(f"2 + 3 = {2 + 3}")
# # Only variables and expressions are allowed inside the {} of the f-string,if we want {} to get displayed use them twice.
# # print(f"{{Use of curly braces inside f-strings}}")

''' split()
    syntax : split(separator)
    str method
    output: list of strings
    - split() breaks a string into smaller parts.
    use case:
    - Break comma-separated values intp individual items.
    - Separate Date and Time in a single String
    - Break date,month,year 

'''
# stamp="2026-03-28 09:31"
# iden="2026-03-28"
# print(stamp.split(" "))
# print(iden.split("-"))

# csv_file="1234,Max,USA,1970-10-05,M"
# print(csv_file.split(",")) #There are more ways to do it but this is just an example.

''' String Repetation (*)
    Syntax : 'string' * number
    Operator
    output : string
    - It repeats the string Multiple times.
    use case:
    - Style Your Logs - use repeated characters to create clear sections in output.
 '''
# print("ha" * 3)
# print('=' * 50)

''' Extraction Category 
  name = “Hello” —> we think it's treated as one value but python treats it differently each letter is treated as character and they have index.
  There are 2 types of indexes :
  - Positive Index --> starts from left ot right and with index value 0
  - Negative Index --> starts from right to left and with index value -1 
  - use positive indexes to extract part from left side(start) of string
  - use negative indexes to extract part from right side(end) of string
'''
''' Indexing 
    Syntax : 'string'[ Index ]
    Operator
    output : string
     To extract the specified index character.
'''
# text = "Python"
# print(text[0])
# print(text[5])
# print(text[-1])
# print(text[-3])

''' Slicing 
    Syntax : 'string'[ start : end : step ]
    By default consider step size as "1"
    Operator
    output : string
    - Slicing Extracts a part of the string
    '''
# date = '2026-03-28'
# print(date[0:4])
# # Open-ended slicing : If we leave the start index empty, Python starts from index 0.
# print(date[:4])
# print(date[5:7])
# print(date[8:])
# print(date[8:len(date)])

# -------------------- cleaning Category -------------------------------
''' Clean Whitespaces :
  Strip() , lstrip() and rstrip()
    - By default cleans whiteSpaces 
    strip() : 
    str method
    output : string
    - removes spaces from both ends
    - removes tabs and multiple spaces 
    - It only removes spaces at the start or end, not in the middle.
    lstrip() : 
    str method
    output : string
    - removes spaces from left side of a string
    rstrip() :
    str method
    output: string
    - removes spaces from right side of a string
- Trim spaces from user Input so always use .strip() method to remove all extra spaces from both ends.  
'''
# text = " Engineering"
# print(text.lstrip())
# text = "Engineering "
# print(text.rstrip())
# text = " Engineering "
# print(text.strip())
# # If want to remove other than whitespaces
# print("######abc######".strip("#"))

# Without looking simply how to identify the whitespaces of the values.
# Detect extra Spaces :
# text =" Engineering "
# print(len(text))
# print(len(text.strip()))
# print(len(text) - len(text.strip())) #The Number of whitespaces
# print(len(text) == len(text.strip())) #To check if the data before strip and after strip are equal

''' Case Conversions :
    lower():
    str method 
    output : string
    - makes all letters lowercase
    upper():
    str method 
    output : string
    - makes all letters uppercase
    use case : 
    standardize text case - make sure text is always in lowercase.
    clean data for matching - lowercase all text to prevent case- based mismatches during search or comparisons
    clean before search - Always trim spaces and lowercase your data and search before matching.
'''
# text = "PYTHON"
# print(text.lower())
# text="python"
# print(text.upper())
# # data conversion and cleaning
# search = 'Email '.lower().strip()
# data = ' eMaIl'.lower().strip()
# print(search == data)

# challenge
messy_data = "968-maria, (D@t@ Engineering );; 27y  "
clean_data = messy_data.strip().lower().replace(";", "").replace("@", "a").replace(" ","").replace(",", "").replace("(", "").replace(")", "").replace("-", "")
# print(clean_data)
name = clean_data[3 : 8]
role = clean_data[8 : 12] + " " + clean_data[12 : -3]
age = clean_data[-3 :- 1]
# print(age)
csv_data= name + " , " + role +" , " + age
print(csv_data)
print(f"name : {name} | role: {role} | age : {age}")
