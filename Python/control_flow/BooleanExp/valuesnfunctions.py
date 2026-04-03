# Values:
print(True)
print(False)
print(type(True))

# Functions :-
''' bool :
    Syntax : bool(value)
    built-in function
    output : boolean
    - True --> if the value is non-empty or non-zero
    - False --> if the value is empty or zero
'''
print(bool(123))
print(bool('hi'))
print(bool()) #nothing so false
print(bool(0))
print(bool("")) #empty so false
# None isn't empty - it's Missing!
# None means no value. '''' Empty means the value exsist, but empty string
print(bool(None))

''' any 
    Syntax : any([var1,var2,var3...])
    output: Boolean
    - Returns True if at least one value is True.
'''
email = ''
phone=''
username='vamshii'
# Condition : 
# Allow registrations if any field is filled.
print(any([email,phone,username]))
''' all
    Syntax : any([var1,var2,var3...])
    output: Boolean
    - Returns True if all values are True.
'''
# Condition:
# Allow registrations only if all the fields are filled.
print(all([email, phone,username]))

print(isinstance(123,int))
print(isinstance('hi',str))
print(isinstance(True,str))

print("hello".endswith('o'))
print("hello".startswith("h"))