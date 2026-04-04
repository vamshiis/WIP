items = (1, 2, 3, 4, 5)
# Here item is a loop variable and items is a sequence which is called Iterator. 
for item in items:
    print(f'loop {item} value is : {item} ')

# What sequences are allowed to be used in for loops ??
# Any objects that are iterable can be used in for loop.
 
# A tuple 
items = (1, 2, 3, 4, 5)
for item in items:
    print(item)
# A List
# The sequence can have any sort of same or mixed data type value's 
items = [1,'hi','a','b']
for item in items: 
    print(item) 
# A string
# Each character is treated as value in a String
items = 'Analytics'
for item in items:
    print(item)
    
''' A built-in function range()
Syntax : range(start,stop,step)
        start - optional default = 0
        stop - doesn't include in final output
        step - optional default = 1
# Generates a sequence of numbers that starts from 0.
# considers range from "0" and ends before the specified number. 
'''
for item in range(1,5):
    print(item) 

# Set of even numbers :
for item in range(0,10,2):
    print(item)    

# set of odd numbers :
for item in range(1,10,2):
    print(item)

# Challenge : 
for i in range(1,7):
    print(i * '*')    