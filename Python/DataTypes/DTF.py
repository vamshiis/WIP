'''
    Data Types + Functions :
     - There are specific Tools for Specific Data types
     - Function + Data Types 
           Do something(functions) to Data(Values)
            value --> function --> new value
        There are three main types of functions:
        1. Stand Alone Functions : 
            They are functions that can be used directly in python.
             ex: print(),type()
        2. Methods of Class :
            They are also functions but complicated, where they belong to something.
            we can't use them directly but need to create something before using them. 
            ex: upper(),replace()
        3. Operations (Magic Methods)  
            Operations are also fucntions, behind the scenes.
            They are like shortcuts to use the hidden functions.
            ex : +,/,>,<,==,in,or
     - where do they come from ? 
            - The standard Library comes with Python.
            - There is are also third-party libraries like Numpy,Pandas,TenserFlow etc.
            - There are also the user-defined functions.
    Modules :

- It is a python file that contain code which can be reusable.

Built - in Module :

- The built-in module its always connected so we don't need to connect it for every code file we write.
- Inside this module we have
1. Stand-Alone functions / Built-in functions
2. Classes

Built-in Functions : 

- They are Built-in functions which doesn't need to import into the code.

Classes :

- It is like a blue print
- we have a class for each data type in python.
- For each class we have special functions called as Methods
- Methods are attached to only those classes

       ex : for class Str we have methods like upper(),replace()

             for class int we  have methods like to_byte()

***Some important points :***

> Data or value's is like Object's in Python that is connected to specific data type class and this class has multiple methods, so Now this object can use its Data Types methods.
> 

> **can it use other functions or other classes methods??**
> 

> ***Any object expect its own classes method's its can't use the method's of other classes  which is totally not allowed to use .***
> 
- for functions it depends on the python rules and the functions which makes sense to apply can be applied like.
- for  “hello” object  to find length of string we can use Len() function   and also type() to know the data type .
- we can't use math modules functions on object's of class Str.

> ”hello” ←— object of Data type Str.
> 
- As it is attached to class Str without limitations we can use all the methods of the class Str on this object.
- can't use the math module function as it won't make any sense.
- can use some functions based on python rules and which can make sense.

> 50 ←— object of Data Type int
> 
- This object can use all the method's of class int.
- can use the all Math module's functions it makes sense to use them on numbers.
- can't use the methods of other classes

Math module :

- Math module is very powerful to do the math operations.
- Its not a built in module we need to import it each time we write code if we need to perform math operations in code.
- this too contain  functions like abs(),round(),floor() etc.
'''
# Functions
text = 'hi'
number = 10
print(text)
print(number)
# type() - returns the data type of the a value, so we can know what kind of object it is.
print(type(text))
print(type(number))
print(len(text))
# print(len(number)) Not allowed for type int
# Methods
print(text.upper())
print(text.lower())
# print(number.upper()) Not allowed to use the methods of other class as upper() method can only be used in type Str
print(number.bit_length())
# print(text.bit_length()) Not allowed to use the int methods on the str objects.
