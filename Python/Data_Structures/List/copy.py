''' Copying List
    - In real data projects developers don't directly work on the original data.
    - Maybe we will be expermenting or not sure what we do at inital stages, after N tries we will do what we need always we do trial & error thing.
    - for this we go and copy the original data and starts to experiment things.
    - but how do we even do that we copy the original thing and use that to update, mutate do stuff as we like.
    - This will be even useful to check what was the changed data with comparing to have idea of what was changed after we applied some operations,
       as we have raw_data and modified_data.
    - there are lot of benefits and reasons for copying the data.
    - So copying a data in the list is very tricky as we can end up either copying the original values or just the address where the original points,
        so we need to be careful while copying.
    - reference, copy, shallow copy, deep copy    
'''

''' -------------------------- How to copy ? -----------------------------'''
''' Copying List (Assignment '=')
    - This type of copying leads to just the assigning of original variable to the new variable.
    - This will copy the reference (i.e the address of the object) where raw_data variable was pointing.
    - This will lead to reflect changes in original data as well when we change something in the copy list.
    - so, an assignment leads to assigning or referencing not any new data.
'''
letters = ['a','b','c']
# create a copy of the list in a new variable
letters_copy = letters
letters_copy.append(5)
letters.pop()
# we can see the mutation occurs in both the lists even if we have copied, we can also confirm by logging the id's of both.
# so both the variable references the same list in memory
print(f' Original: {letters}')
print(f' Copy    : {letters_copy}')


''' Copying List (Shallow Copy)
    - As we seen in previous concept we were getting the original list itself for playing around, but we need the real copy of original data.
    - In order to do it we use `.copy()` method which creates a new container a new list that is independent from the original list, 
       where each variable the original and new variable will be pointing to it's respective list objects unlike how “=” was behaving.
    - now they are independent the new variable list mutation will not effect the original variable list.
    copy() :
    Method
    output : list 
    - creates a separate list in the memory
'''
numbers = [1,2,3,4]
copy_numbers = numbers.copy()
# Real checking with mutation :
copy_numbers.append(8)
print(f' Original: {numbers}')
print(f' Copy    : {copy_numbers}')
# print(numbers.copy().pop())
