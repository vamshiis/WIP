'''
   Data Types :
       - Python automatically detects Data Types.
       - Dynamic : Data Types can change any time.
       - Data is Stored in Different types and Different Sizes.
       - Knows how to operate data.
             ex: adding 2 numbers of integer and 2 number of type String
                1. 2 + 3 = 5
                2. "2" + "3" = "23"
'''
# Detects the data types and automatically handles the data type based operation
a = 2
b = 3
c = a+b
print(a+b)  # In integers it does arthemtic operation of adding them.
print(type(c))
a = "2"
b = "3"
c = a+b
print(c)  # output : 23 In strings it joins the text
print(type(c))

'''
     Categories of Data Types :-
     No value: Empty values --> None(Special value)
     Single Value: Primitve Types
                  - have values like   int--> 50,
                                       float--> 23.4,
                                       Str--> hello,
                                       Bool--> true 
     Multiple Value: These are Data Structures (or) collections (or) containers.
                     Many values like  list--> [1,2,3],
                                       dict-->{ a:1,b:2,c:3},
                                       Tuple--> (a,b,c),
                                       set --> {1,2}
                                    
'''
# Data Types
# int --> whole Numbers without decimals
a = 10

# float --> Numbers with decimal Points
b = 3.15

# Str --> Represnts text or a sequence of characters
c = 'Hello'
d = "Hi"
e = "123"

# Bool
'''-can be True or False
 - used to handle logic and decision making
 - Case-Sensitive first Char always Capital'''
f = True
g = False

# None --> means "No Value","Nothing" or "Unknown". It's used to show the absence of data.
h = None

i = ""  # Blank "" is a string value with no characters inside,it is not same as None!
j=" "  #White Space " " is a string value with 1 or more spaces,it is not same as None! 