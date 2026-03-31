''' is_integer : 
    Syntax : value.is_integer()
    float class method
    output : Boolean
    - check if a float has no decimal part(is a whole number)
    use case : 
    check if numbers are truely whole numbers. floats with .0 might just be from file exports.
'''
x = 7.0
print(x.is_integer())
y = 7.1
print(y.is_integer())
# numbers such as 7.0 ,7.00 ,3455.00 ,34.00 are integers not floats.

''' isinstnace
    Syntax : isinstance(value,type)
    built-in function
    output : Boolean
    - checks if a value belongs to a certain data type.
'''
x = 70
print(isinstance(x, int))
x = 70.4
print(isinstance(x, int))
print(isinstance(x,float))
x = ''
y = ' '
z = 'vam'
print(isinstance(x, str)) # True - str
print(isinstance(y, str)) #True - str
print(isinstance(z, str)) #True - str
