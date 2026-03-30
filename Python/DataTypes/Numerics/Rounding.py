import math
''' absolute numbers (abs)
    abs()
    Syntax : abs(value)
    Built-in function
    Output : int
    - Returns the absolute(non-negative) value of a number.
    use case : 
    - useful for measuring distance or size, regardless of direction.
'''
print(abs(2-10))

''' Rounding Numbers
   - Sometimes Numbers are messy we round them to make the result easier to read and work with.
'''

''' round() 
    Syntax : round(value)
    - rounds the number to nearest whole number
    - for exact .5(half numbers) what it does is "Bankers rounding" means rounding to even numbers. 
    use case : 
    - Handy in data analysis to clean up numbers for reports or save space
'''
price = 35.545678
print(round(price))
# round(number,ndigits) --> rounds the number to the specificed number of decimal places.
print(round(price,2))

''' floor() 
    Syntax : math.floor(value)
    - Rounds down the value.
'''
print(math.floor(price))

''' ceil()
    Syntax : math.ceil(value)
    - Rounds up the value
    use case : 
    - perfect for data engineering - like splitting data into pages or batches.
'''
print(math.ceil(price))

''' trunc()
    Syntax : math.trunc(value)
    - cuts off the decimal part and keeps the whole number(no rounding)
'''
print(math.trunc(price))
# the above line can also be done through int() 
print(int(price))

'''
     when to use int() vs trunc() ??
    - If we are not using math already, just use int() it's simple and built in.
    - If we already have imported math, use trunc() it makes our intent clear.
'''
