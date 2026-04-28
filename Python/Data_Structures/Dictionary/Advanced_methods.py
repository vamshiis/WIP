''' Changing of Dictionary'''

user = {'id': 1, 'age': 25, 'city': 'peru'}
''' Assign Keys :
    - we have 2 functionalities of assign key
    - Inserts a new key value pair if it doesn't exists
    - For single pair updation : Updates the value if the key exists
'''
# Add new pair
user['name'] = 'John'

# Update exsisting Pair value
user['age'] = 30

print(user)

''' updating :
    update() :
    Syntax : variable.update({key-value,key-value,....})
             - Its like define new dictionary kind of
    - Adds new keys and updates existing ones using another dictionary.
    - It will overwrite the exsisting data who has same key names and 
      if not found it adds them as new pair just.
'''
user.update({'age': 40, 'city': 'berlin','status':'pending'})
print(user)

''' Removing :
    pop() :
    Syntax : variable.pop(key, default_value)
             - If key found it returns the value
             - If key not found and default_value is defined it returns default_value instead of KeyError
    - Removes a key from the dictionary and returns its value, or returns our default if the key is missing
    - Actually pop() method return us the value it caught unlike all other in place modifier methods.
    - But needs to sure the key you are passing to pop it does exsist in dictionary.
    - If key not present it gonna return the KeyError - if key not found, Python throws a KeyError
    - So if you or sure it exsist use pop otherwise just dont or define the default value it prints that thing
'''
age = user.pop('age')
salary = user.pop('salary','Not Found') # key is not available so it throws KeyError if no default mentioned but now default is given it will display that.
print('Employee Age:',age)
print('Salary :', salary)

''' Does pop() removes the last item from dictionary ?? 
    - What if we dont pass any arguments for pop() does it still removes the last item from the dictionary 
      like how it did in the list data structure.
    - The answer is No it throws TypeError it atleast expects one argument, 
      it doesnt behave how it behaved for list data structure just.
    - for that behaviour to happen without passing an argument how can we remove a last item from dictionary we need use popitem() method.
'''
''' popitem() :
    Syntax : variable.popitem()
    Output : a single tuple which contains (key, value)
    - returns and deletes the most recent key value pair from the dictionary.
'''
user1 = {
    1 : 'key',
    2 : 'password'
}
# print(user1.popitem()) # a tuple (1, key)
''' since its a iterable we can unpack it instantly
 Method 1 : If there is a single collection as a output out of a method do k,v = user1.popitem() then print k, v
    • we can make it work in loop but loop treats a item as container and for each element inside it it asks for k,v 
    • since its a single tuple this line fails for k,v in user1.popitem()
 Method 2 : we can either wrap it around the another container means wrap it around a list [user1.popitem()] or use user1.popitem(), if you want a loop to unpack things for single item.
    • But looping is done for 1 or more items not for a single item so we should always go with method 1 
'''
# Method 1 
k,v = user1.popitem()
print(k,v)
# Method 2
for k, v in user1.popitem(), :  # A comma after a single item turns it into a tuple of one tuple
    # print(type(k),type(v))
    print(k,v)
print(user1)

''' Creation : 
    - What if we need the same value for all the keys in a dictionary
    - we will be constructing the dictionary by specifying all the keys one by one and then repeat the same value.
    - But to avoid typing ssame thing again and again we have aspecial method to construct such dictionaries in python fromkeys()
'''
# Method 1
user = {
    'id': None,
    'name': None,
    'age': None,
    'city': None
}

''' fromkeys() :
    Syntax : dict.fromkeys([iterable of keys] , deafult_value)
             - we pass 2 arguments for .fromkeys()
               1. iterable of keys  - include all the keys who needs the default guy just.
               2. Default_value - this value will be given to all the keys in the list
    Output : a new dictionary
    - Builds a new dictionary where all keys gets the same default value.
    use case : 
    - Useful to build the dictionary structure with the default values.
    - If we want to create a brand new dictionary where we dont know the value of each key just so this can be useful rather than overwriting.
    - Later when we need to insert value for those we need to update them by targeting the specific keys just.
'''
user2 = dict.fromkeys(('id', 'name', 'age', 'city'), None)
# user3 = dict.fromkeys(['id','name','age','city'],None)
# user4 = dict.fromkeys({'id','name','age','city'},None)
# user5 = dict.fromkeys('hello',None)
print(user2)
# Later we can update each keys value by specifying them
user2['age'] = 20
print(user2)


# Real World Applications
''' 1.use case : DataBase or API Records : 
    - Returns records are stored as dictionaries where column names are keys and the row values are dictionary values
'''
# Representing a single row from a database or API
row = {
    'id': 101,
    'name': 'Catlie',
    'country': 'SF',
    'age': 25,
    'status': 'active'
}

''' 2. Use Case : Mapping To Friendly Values
    Great for converting technical codes into friendly lables
'''
#  Mapping Translations to Friendly Values
status_map = {
    '01': 'Open',
    '02': 'In Progress',
    '03':  'Done'
}

''' 3. Use Case : Mapping Abbrevations
    Turning short Abbrevations into full readable names.
'''
# Mapping Abbrevations
country_name = {
    'DE': 'Denmark',
    'IN': 'India',
    'FR': 'France'
}

''' 4. Use Case : config and Environment Data
    Store System setting like host, port, and usernames in one place.
'''
# Storing Environment Variable & configuration
system_conn = {
    'DB_HOST': 'prod-db.company',
    'DB_PORT': 4567,
    'DB_USER': 'Admin_user',
    'DB_NAME': 'Sales_analytics'
}
''' 5. Use Case : ETL and Pipeline Settings
    Great for storing run parameters and controlling how your ETL pipeline loads data
'''
''' 6. Use Case : Meta Data
    Data about our Data (structure of the data Schema)
'''

''' Challenge
    user = {'id' : 1, 'name': 'john', 'age' : 30, 'city': 'Paris'}
    1. create New dict
    2. Keep only pairs with string values
    3. Convert the Values to Uppercase
    4. Elegant and short solution
'''
''' Dictionary comprehension : 
    - follows same rules as list comprehension
    1. Runs a for loop on the dictionary and gets a item each time unpack them just
    2. Checking for a condition check if the condition is true if yes it goes for data transformation, or else it goes to for loop to get next item.
    3. Data Transformation write here what you wanna print just and perform the opertion what you wanna see
'''
user = {'id': 1, 'name': 'john', 'age': 30, 'city': 'Paris'}
user_string = {
    k: v.upper()            # Data Transformation
    for k, v in user.items()  # Loop
    if isinstance(v, str)   # Filter
}
print(user_string)
