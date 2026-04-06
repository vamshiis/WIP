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
''' print the pattern :
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
'''
for i in range(1,7):
    print(i * '* ')    

'''
     Nested for loop :
     - Its like loop inside another loop, for every item of outer loop the inner loop executes completely.
'''
for x in range(3):
    for y in range(2):
        print(x,y)
 
'''use cases :
     - we have 2 major use cases
       1. Crossing  and combining the data / pairing the data or Cartessian
          - It's all about we have 2 different types of Lists , were we wanna see all possible combinations among them.
          - The each value of one list is combined or paired with other List's values.
'''
colors = ['red','blue','green']
sizes = ['L','M','S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')

''' 2.Navigate Hierarchy : 
    - useful when we need drill down and execute something.
    - If we have different layers,level or hierarchy we will be using nested for loops.
    - use cases:
     - If we want to have file named with year_month_date.csv we gonna have year,month,date
       automation to generate such files then nested loops gonna do it.
     - If we want to do data related operations on the table's rows then we need to navigate through 
       table, column and reach row for each table and column then we need nested loops.
'''
years = [2026,2027]
months = ['Jan','Feb']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')

''' Think if we have n Tables and each table has same columns and we need to write this query 
    SELECT count(*) FROM customers WHERE id IS NULL; to check nulls,
    so we gonna end up writing same query instead we can automate through nested for loops.
    '''
tables = ['customers','orders','products','status']
columns = ['id','create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')