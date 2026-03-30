# type() --> this function is used to know the type of the datatype.
x = 5
y = 5.12
z = 3 + 3j
print(type(x))
print(type(y))
print(type(z))

''' int 
    Syntax : int(value)
    Built-in function
    output : int
    - converts compitable value into int value.
'''
x = '24'
print(type(x))
x = int(x)
print(type(x))
print(x * 4)

''' float
   Syntax : float(value)
    Built-in function
    output : float
    - converts compitable value into float value.
'''
x = 3
print(float(x))
x = '3.14'
print(float(x))

''' complex
    Syntax : complex(real,imag)
    Built-in function
    output : complex
    - creates a complex number using real and imaginary parts
'''
x = 3
y = 4
print(complex(x, y))
