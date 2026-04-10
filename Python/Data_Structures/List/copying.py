import copy
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

''' Copying List - Deep Copy 
    

'''
matrix = [
    [1,2],
    [3,4]
]
# using shallow copy (.copy() method)
matrix_copy = matrix.copy()
# Remove last list from original nested list
matrix.pop()
# Add a new item in the 1st row of the copied list
matrix_copy[0].append(10)
print('original:', matrix)
print('Copy    :', matrix_copy)
# Confirmation of copied list or not
print('original ID:', id(matrix))
print('Copy ID    :', id(matrix_copy))

''' Using the Deep copy (functions deepcopy() and copy())
    - Inside the copy module we have 2 functions 
        1. copy()
        2. deepcopy()

    deepcopy() : 
     function
     import from copy module
     Syntax : module_name.function_name(variable/value)
      - so now if we use `deepcopy()` its gonna go layer by layer and copy how deep is our nested list.
      - so this makes the issue of shallow copy solved where the
      - `top level is Independent and a real copy`
      - `Deeper level is also a Independent and a real copy`
      - so Deep copy is the safest way to create a copy of nested lists
'''
matrix = [
    [1, 2],
    [3, 4]
]
matrix_copy = copy.deepcopy(matrix)
# # Remove the last row from the nested list
matrix.pop()
# # Add a new item in the 1st row of the copied list
# # copy.deepcopy() creates a true, independent copy for all levels
matrix_copy[0].append(8)
print('original:', matrix)
print('Copy    :', matrix_copy)
# # Confirmation of copied list or not
# print('original ID:', id(matrix))
# print('Copy ID    :', id(matrix_copy))

''' copy() :
    function
    import from copy module
    Syntax : module_name.function_name(variable/value)
    - similiar to shallow copy method copies the top level only
    - copy.copy() is more general than list.copy(), not limited to lists
    - useful for the Data structures which doesnt have their own method of copy()
    - always go with the methods if they exsist if not use functions.
    - as list has the copy() method use that its gonna be faster than function copy()
'''
# we can have done this too but this is same as shallow copy
# copy.copy() creates a shallow copy just like the method copy()
# matrix.copy = copy.copy(matrix)

''' is operator :
    - use is operator to confirm if the variables are independent(i.e real copy) or shared(i.e. shared copy )
    
'''
original = [
    [1,2],
    [3,4]
]

# Tip : use the is operator to check if the copies are truly independent
# Assignment "="
copy1 = original
print("Same Object?", original is copy1,"\n")

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared List?", original[0] is copy2[0],"\n")

# Deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy2)
print("Shared List?", original[0] is copy2[0], "\n")
