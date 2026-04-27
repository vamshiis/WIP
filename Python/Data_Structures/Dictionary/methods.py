user = {'id':1,'age':25,'city':'peru'}

''' Accessing value :
   - we can access values through specifying the keys
   - But if the specified key is not available it throws the keyError 
'''
print(user['age']) # can access
# print(user['name']) # won't access throws KeyError

''' get() 
    Syntax : reference_variable.get(key,default_value)
             if default_value give None is not returned if key not found
             if no default_value mentioned and key is not found None is returned
    Output : Value(Data type solely depends on how its being stored)         
    - If we are not sure whether a key exist in the dictionary or to escape from KeyError we need to use get()
    - Returns the value safely, gives None if missing
    - Missing key returns None or default value.
    - we can specify the Default value, which will be retirned if Key is not found which was returning None now it will return Default Value
'''
print(user.get('age'))
print(user.get('name','Unknown'))

''' Checking Keys Availability:
   in operator
   - Tests if the key is inside the dictionary
   - Returns Boolean 
'''
print('age' in user)
print('name' not in user)

''' Viewing Objects : 
    - gives us a live view of the dictionary's keys,values, or key value pairs
    - In Python, .keys(), .values(), and .items() are all Dictionary Views.
    What is a "View"?
    - A view is a live window into the dictionary's internal data.
    - It does not create a new list or a separate copy of the keys.
    - It stays linked to the dictionary.
    - The 3 Golden Rules of View Objects
        1. Dynamic          : If the dictionary changes, the view updates instantly.
        2. Memory Efficient : It uses memory because it just "looks" at the dictionary's existing hash table.
        3. Set-Like         : Specifically, dict_keys and dict_items support set operations like & (intersection) and | (union).
'''
''' keys() :
    Syntax : variable.keys()
    Output : dict_keys View Object
    - Returns all the KEYS in our dictionary
'''
print(user.keys())

''' values() :
     Syntax : variable.values()
     Output : dict_values View object  
    - Returns all the VALUES in our dictionary
'''
print(user.values())

''' items() :
    Syntax : variable.items()
    output : dict_items view object
    - Returns all (key,value) pairs of our dictionary
    -  Each element inside the view is a Tuple(like (id, 1))
    - This method will be perfect when we need key and value together for
      looping, transforming data, building new dicts, comparing and more
'''
print(user.items())

''' print(user) - output : {'id': 1, 'age': 25, 'city': 'peru'}
   - we can use normal print(users) to get items of dictionary
   - But if we do it we get them in dictionary form which will be useful to display
   - we cant able to loop around that output or perform any operations with it just.
   - so we need to always use variable.items() so that we can use that result to loop,compare,transform and more.
'''
# print(user)

