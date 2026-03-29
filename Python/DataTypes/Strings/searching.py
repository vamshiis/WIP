# ------------------------------ Searching Category ---------------------------
''' 
    startswith : 
     Syntax : startswith(substring)
     str method
     output : boolean
     - Check if the string begins with a specific word.
     use case : 
     - to check for the match of country code in phone numbers.
'''
phone = "+91-9xxxxx78"
print(phone.startswith("+91"))
print(phone.startswith("+49"))

'''endswith :
     Syntax : endswith(substring)
     str method
     output : boolean
     - check if the string ends with specific word. 
     use case:
     - to check for the match of specific domain emails at the end.
     - to check if the file is a CSV file.
'''
email="vomshiii@gmail.com"
print(email.endswith("gmail.com"))
print(email.endswith("outlook.com"))

''' in :
     Syntax : 'substring' in 'string' or variable
     Operator
     output : boolean
     - check if a word exists in the string.
     use case : 
     - to check for valid email ? check for "@"
     - check if the URL is an API endpoint
'''
file = "data_products.csv"
print(file.endswith(".csv"))

valid_email = "vomshiii@gmail.com"
print("@" in valid_email)
valid_email = "vomshiiigmail.com"
print("@" in valid_email)

url = "https://api.company.com/v1/data"
print('/api' in url)

''' find() : 
       Syntax : `find( substring)`
       str method
       output : number
       - returns the starting position of a word in the string.
'''
phone1="+91-8989xxxxx"
phone2="91-98xxxxxx"
phone3="00091-95xxxxxx"

# Hard coded way
print(phone1[4:])
print(phone2[3:])
print(phone3[6:])

# Dynamic way
print(phone1.find("-"))
print(phone1[phone1.find("-") + 1:])
print(phone2[phone2.find("-") + 1:])
print(phone3[phone3.find("-") + 1:])
