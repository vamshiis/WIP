# Identity (is) operator :
# Checks if two variables refer to the same object in memory

# For Multiple Values :
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x == y)
print(x is y)

x = ['a', 'b']
# '=' Between Two variables - Assigns one variable to the same object that another variable is referring to
y = x  # we assigned the exsisting variable that points to object to new variable. now this new variable too hold same value and points to same ID the one exsisting variable points.
print(y)
print(x == y)
print(x is y)

# For single Values :
x = 5
y = 5
print(x == y)
print(x is y)

# Task
# Validate the email address. It must be filled in and not empty.
email = ""
print(email != "")
email = None
print(email != "") # Returns True means there is an email but its a None value
# None - means no value at all, it is unknown 
# "" - means an empty but it is known,it is string
print(email is not None and email != "") # This works we specifically daying email shouldn't be None and not equal to "" empty.
# print(email != None and email != "") we can also use this but use "is" with None.
# Best Practice : Use "is" instead of == when checking for None habit from SQL