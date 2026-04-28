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

