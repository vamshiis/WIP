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
password = '   123a'
print(len(password)) # output : 7 (includes spaces)
if len(password) < 8:
    print('your password is too short!')


''' count() :
count(substring)
 - str method
 - output: int
 - returns how often a word appears in the string.
   use case :
    - Word frequency Check --> Counts how many times a specific word appears.
    - Detects Quality Issues --> count how many unwanted characters in the data.
'''
text = """
Python is easy to learn.
Python is powerful.
many people love python.
"""
print(text.count("Python"))
