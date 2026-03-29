# Types category :
# Built in functions in Strings
name = "Vamshi"
# Type
print(type(name))
age = 23
print(type(age))
print('Your age is:' + age) #can't combine a string with an integer using + operator.
print('your age is :'+str(age)) # str() converts any data into str data type. Its done to just execute this line it wont change in the memory.
age=str(age) # this leads to change in memory completely converted from int to str data type.
