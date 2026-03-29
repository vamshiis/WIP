
# ----------------------- Validation Category -----------------------------
#  we apply validations to prevent "invalid" or "garbage" data from entering our system 
''' isalpha() : 
       str method
       output : Boolean
       - Check if the string has only letters.
'''
country = "USA"
print(country.isalpha())
country = "INDIA"
print(country.isalpha())
name = "Al9ha"
print(name.isalpha())

'''isnumeric() :
     str method
     output : Boolean
     - check if the string has only numbers
     - only accepts whole number , the float numbers aren't allowed like 3.19 sort of
     - must only contain numbers like “123456789” it shouldn't be like “123-456-789”  then it returns false for such value.
'''
phone="1234"
print(phone.isnumeric())
phone='123-456'
print(phone.isnumeric())
phone='3.14'
print(phone.isnumeric())

''' isalnum() :
     - A string is alpha-numeric if all characters in the string are 
     alpha-numeric andthere is at least one character in the string.
'''
zipcode = '123AB'
print(zipcode.isalnum()) 
zipcode = '123-AB'
print(zipcode.isalnum()) 
