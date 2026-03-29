# -------------------- cleaning Category -------------------------------
''' Clean Whitespaces :
  Strip() , lstrip() and rstrip()
    - By default cleans whiteSpaces 
    strip() : 
    str method
    output : string
    - removes spaces from both ends
    - removes tabs and multiple spaces 
    - It only removes spaces at the start or end, not in the middle.
    lstrip() : 
    str method
    output : string
    - removes spaces from left side of a string
    rstrip() :
    str method
    output: string
    - removes spaces from right side of a string
- Trim spaces from user Input so always use .strip() method to remove all extra spaces from both ends.  
'''
text = " Engineering"
print(text.lstrip())
text = "Engineering "
print(text.rstrip())
text = " Engineering "
print(text.strip())
# If want to remove other than whitespaces
print("######abc######".strip("#"))

# Without looking simply how to identify the whitespaces of the values.
# Detect extra Spaces :
text =" Engineering "
print(len(text))
print(len(text.strip()))
print(len(text) - len(text.strip())) #The Number of whitespaces
print(len(text) == len(text.strip())) #To check if the data before strip and after strip are equal

''' Case Conversions :
    lower():
    str method 
    output : string
    - makes all letters lowercase
    
    upper():
    str method 
    output : string
    - makes all letters uppercase
    use case : 
    standardize text case - make sure text is always in lowercase.
    clean data for matching - lowercase all text to prevent case- based mismatches during search or comparisons
    clean before search - Always trim spaces and lowercase your data and search before matching.
'''
text = "PYTHON"
print(text.lower())
text="python"
print(text.upper())
# data conversion and cleaning
search = 'Email '.lower().strip()
data = ' eMaIl'.lower().strip()
print(search == data)

# CHALLENGE
'''
 convert this  
 messy_data "968-maria, (D@t@ Engineering );; 27y  "  into
 clean_data = "name: maria | role: data engineering | age: 27" 
'''
messy_data = "968-maria, (D@t@ Engineering );; 27y  "

# Hard - coded way work for this data only.
clean_data = messy_data.strip().lower().replace(";", "").replace("@", "a").replace(" ","").replace(",", "").replace("(", "").replace(")", "").replace("-", "")
# print(clean_data)
name = clean_data[3 : 8]
role = clean_data[8 : 12] + " " + clean_data[12 : -3]
age = clean_data[-3 :- 1]


# Dynamic way - works for the data with same format all over.
parts = messy_data.split(",")  # ["968-maria" " (d@t@ engineering );; 27y  "]

name_part = parts[0]  # "968-maria"
rest_of_data = parts[1]  # " (d@t@ engineering );; 27y  "

name = name_part.split("-")[1]  # ["968","maria"] --> "maria"

role_and_age = rest_of_data.split(";;")  # [" (d@t@ engineering )", "27y  "]
role_part = role_and_age[0]  # " (d@t@ engineering )"
age_part = role_and_age[1]  # "27y  "

role = role_part.replace("(", "").replace(")", "").replace("@", "a").replace(";;", "").strip()  # "data engineering"
age = age_part.strip()[0:2]  # "27y" --> "27"

csv_data = name + " , " + role +" , " + age
print(csv_data)
print(f"name : {name} | role: {role} | age : {age}")
