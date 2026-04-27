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

