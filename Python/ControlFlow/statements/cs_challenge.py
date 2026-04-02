# Challenge - 1 :
email = "/omshiii@gmail.com"
email = email.strip()

# if-elif-else block
# This code stops at the first condition that returns True.
# Email must not be Empty
if email == '':
    print('Email cannot be empty.')

# Email must contain a '.' and '@'
# if the condtions aren't available we need to print message. so we need to negate(if not present means False so turn it to True) in order to print the message.
# if they are present means if condition return true we should not print message. so the not operator gonna turn True into False and hence the message won't be printed so that says we passed the condition.
elif not ("." in email and "@" in email):
    print('must contain . and @ ')

# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print('Email must contain one @ ')

# Email must end with '.com', '.org', or '.net'
elif not (email.endswith(('com', '.org', '.net'))):
    print('Email must ends with .com., .org or .net')

# Email must not be longer than 254 characters
elif len(email) > 254:
    print('Email must not be longer than 254 characters')

# Email must start and end with a letter and digit
# isalnum() - Checks if the string contains only letters or digits.
elif not (email[0].isalnum() and email[-1].isalnum()):
    print('Email must start and end with a letter or digit')
else:
    print('Email is valid')


# Independent If statements :
# If we want all conditions to be evaluated? we use Independent if statements.
# we can't have standalone else, so to have the message that all conditions are satisfied we need boolean check of valid that prints if all if statements above it are false.
email = '-v@mshiii@gmail.om'
email = email.strip()
valid = True  # if any condition fails to satisfy turn valid to False.
if email == '':
    print('Email cannot be empty.')
    valid = False
if not ("." in email and "@" in email):
    print('must contain . and @ ')
    valid = False
if email.count('@') != 1:
    print('Email must contain one @ ')
    valid = False
if not (email.endswith(('com', '.org', '.net'))):
    print('Email must ends with .com., .org or .net')
    valid = False
if len(email) > 254:
    print('Email must not be longer than 254 characters')
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print('Email must start and end with a letter or digit')
    valid = False
if valid:
    print('Email is valid')

# Challenge - 2 :
# Validate the Quality and Correctness of the passwords:

password = "@### @@@@@@@@@"
has_uppercase = False
has_lowercase = False

# Must not be empty 
if password == '':
    print("Password can't be Empty")

# length of password shouldn't be longer than 8 characters
if len(password) > 8:
    print("password can't be longer than 8 characters")    

#Must contain atleast one upper character 
for char in password:
    if char.isupper():
        has_uppercase=True
        break
if not has_uppercase:
    print('Must contain atleast 1 UpperCase Letter')

# Must contain atleast one Lower character
for char in password:
    if char.islower():
        has_lowercase = True
        break
if not has_lowercase:
      print('Must contain atleast 1 LowerCase Letter')

#password and email shouldn't be same as email 
# Added the name of email and password also shouldnt't match  
if password == email or password == email[0:email.find('@')]:
    print('email shouldnt be same as email')

# Shouldnt contain any spaces
if ' ' in password:
    print('should not contain Spaces')

# Password must start and end with digit or letter 
if not (password[0].isalnum() and password[-1].isalnum()):
    print('Must start and end with letter or digit')
