'''Comparison Operators :
    - compare values and returns True or False
    - == , != , < , > , <= , >=
    we can perform on following conditions : 
    value operator value    --> 3 > 2 --> True
    variable operator value --> x = 5 --> x < 2 --> False
    Expression operator value --> 2-1 != 3 --> True
    function operator value   --> len("hi") == 3 --> False
'''
print(10 == 10)
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print(7 <= 7)

# Strings can be compared too! we can compare strings too alphabetically, not just numbers
# As python is case-sensitive so "a" and "A" are treated as different values.
print("a" < "b")
print('a' > 'b')
print('a' == 'b')
print('a' == 'A')

# Chained Comparison
# It evaluates from left to right, checking each condition one by one
print(1 < 4 < 6)

# Chained comparison work like SQL's BETWEEN. They check if a value is between two bounds.
# Is age between 18 and 30
age = 18
print(age <= age <= 30)
age = 30
print(age <= age <= 30)
age = 36
print(age <= age <= 30)
