''' Dictionary :
   - The structure of the dictionary makes its characteristics slightly different from othe data structures.
1. Ordered 
   Python gonna remember the order of the items of our list 
   the way we defined them.
'''
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}
print(my_dict) # Ordered

''' 2. Duplicates 
    - Here we have keys and values in dictionary 
    - For Keys   : Keys must be Unique, if duplicate key is added the latest added key value pair overwrites previous pair.
    - For Values : Values can be duplicates, python dont care about the value duplicates.
'''
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a':20,
    'd':30
}
print(my_dict)

''' 3.Indexed 
    - dict is not Indexed, they are keyed
    - They have their own type of Indexes which are keys in this case
    - we can access  values using the keys only, we cant use index numbers to access them.
'''
print(my_dict['a'])

''' 4. Mutable
    - dict values are mutable
    - we need to access them through keys and assign new value.
'''
my_dict['d'] = 50
print(my_dict)