# Logical Operator (and | or) :
# Used to combine Multiple boolean expressions

# and - both the conditions needs to be True
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)
# and - any one of the conditions needs to be True
print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# Checking user credentials before login
email = True
password = False
print(email and password)

# not - It reverse the truth it turns true into false and false into true
print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

name = ""
print(not name)
print(not 0)

# Execution Order :
'''
   mixed logical expression
  - AND operator has highest priority than OR

'''
print(5 == 5 or 8 > 5 and 6 < 4)  # True

# To control the order use parantheses () for expression
print((5 == 5 or 8 > 5) and 6 < 4)  # False

# TASK :
# Allow access only if the user is logged in or they are guest
# but they must not be banned
# Understanding the access Should be granted if the user is logged in or is using guest mode, but they should be banned,
# not can't be clubbed with and or must use any of the operator together like and not else or not sort of.
is_logged_in = True
is_guest = False
is_banned = False

print((is_logged_in or is_guest) and not is_banned)
