# Challenge-1
# Check if user's Name is not empty and the age is greator than or equal to 18
user_Name = 'Vamshi'
age = 18
print(user_Name != "" and age >= 18)

# Challenge-2
# Check if Password is at least 8 characters long and does not contain spaces.
password = '12345 678'
print(len(password) >= 8 and ' ' not in password)

# Challenge-3
# Check if user's email is not empty, contains '@' and ends with '.com'
# to check a substring in string use in operator 
user_email = "xyz@gmail.com"
print(user_email != '' and '@' in user_email and user_email.endswith('.com'))

# Challenge-4
# check if username is a string, is not None and is longer than 5 Characters.
# ''," " is treated as string means empty if we check isinstance of for such data it will return true means its an str.
# So we need to use isalpha() combinedly to ensure username is not empty even if its an string and is alphabetical.
user_Name = 'vomshii'
print(isinstance(user_Name, str) and user_Name is not None and len(user_Name) > 5 and user_Name.isalpha())

# Challenge-5
# Question : Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.
user = 'Admin'
email_status = 'xyz'

# Old way - acc to what asked in the question:
# checks for specific values matching as described.
# In the below line other than banned it can still allow who can have status like pending, abcd, xyz. 
# If we are strict to allow verified guy it wont work it will allow anything in email_status other than banned.
print((user == 'moderator' or user == 'Admin') and  (email_status == 'verified' or email_status != 'banned'))

# Advanced approach - should allow users who are admin,moderators and email_status is verified or pending :
# Store all possible cases in list and check if the given user input value is in the list.
# Works for known cases or values only.
# acts like Strict Bouncer check and allow who has values in the given list values other than those values are simply returned false.
users_allowed = ['admin', 'moderator']
status = ['pending', 'verified']
print(user.lower() in users_allowed and email_status.lower() in status)