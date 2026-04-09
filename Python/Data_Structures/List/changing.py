''' How to change?
   - as time flies we mend to change the data that is exsisting or make changes to data.
   - we have 3 types of changes.
      1. Add data - when we need to add new entries to exsisting list
      2. Remove data - when we need to discard bad quality data
      3. Update data - when we need to overwrite the existing data.

  ### List of **In-Place Mutators**'
    - All the in place modifiers returns None except pop() 
    - This list help to change the data and perform the 3 types we disscussed above
    
     Here are the most common ones that return`None`:
    1. append(): Adds one item to the end.
    2. insert(): Adds one item at a specific index.
    3. remove(): Deletes the first occurrence of a value.
    4. sort(): Rearranges the list in order.
    5. reverse(): Flips the list order.
    6. extend(): Merges another list into the current one.
    7. clear(): Removes everything.

    ***** Why this matters for "Chaining": **** 
     - Since all of these return `None`, you can never do this:
     - my_list.append(1).sort() —-> CRASH! (Because you're effectively trying to do`None.sort()`)

    The One Exception:.pop()
     - There is one "rebel" method.`.pop()`modifies the list in-place (removes an item), but it returns the item it just removed instead of`None`.
     - Even with`.pop()`, you**still can't chain**another list method after it, because the return value is the*item*(like a number or string), not the list!
     
    Pro-Tip :
     - If you ever see`None`appearing in your`print()`statements or getting an`AttributeError`, it almost always means you tried to assign the result
       of an in-place modifier to a variable, like this : `new_list = old_list.append(5)`—>`new_list`is now`None`!

    The In-place Modifier's show No mercy.
    They are "destructive" methods because they don't bother making a copy to be safe—they go straight for the jugular of the original data in memory.
'''
''' --------------------- Add Items ---------------------------------- '''
# Easy and lazy way to add the item into the list.
''' append() :
    method
    Output : None
    - Append the new value at the end of the list!!
    - It's like Stacking new items to the end of list
'''
# Normal 1D-list
letters = ['a','b','c']
letters.append('x')
print(letters)

# Nested 2D-list
matrix =[
    [1,2,3],
    [4,5,6]
]
matrix.append([7,8,9])
print(matrix)

# Insert the item at specific position
''' insert() :
    method  --> In - place Modifier
    output : None
    Syntax : insert(index,'value')
    - Inserts the value at specific position.
    -flexible and have control where to add
'''
# Normal list
letters.insert(1,'m')
# letters.insert(letters.index('a') + 1,'m') --> combo of methods usage to find index
print(letters)

# Nested List
matrix.insert(0,['a','m','v'])
print(matrix)

# Add item at end of specific row in nested list
'''
   - we need always specify the row for this as it anyhow addition to the end we can use append()
   - if we do directly matrix.append('a) it creates a new pointer for matrix and point the string object,
       so there will be new string value at the end of the matrix.
    - if we really want to add at specific position in nested list we have rows numbers, we can target that row and use methods on them.
'''
# The trap
# matrix.append('x') #just adds x as string value to the nested list at the end
matrix[1].append('x') #now it has the context of row 1 and it adds the string value in the row 1 list to the end.
print(matrix)

# Add 'z' at the start of third row
# we cant use append as its index speific now.
matrix[len(matrix)-2].insert(0,'z')
print(matrix)

''' ------------------------------- Remove Items ------------------------'''
''' How to Remove?
    - After analyzing we might find duplicates, old data, Bad data in the list.
    - we try to remove them using various methods
'''
# Nuke the whole list
''' clear() :
    Output : None
    Method --> In - place modifier
    - Removes everything from the list!!
    - Its like hitting the reset button.
'''
alpha = ['a','b','c','b']
alpha.clear()
print(alpha)

''' Delete Items
     - we have 2 methods to do it
     - By value    - remove()
     - By Position - pop()
'''
''' remove() :
    Method -->  In - place modifier
    output : None
    Syntax : variable.remove(value)
    - it removes by the value passed to the method.
    - Removes only the first match
'''
# Normal List - 1D list
alpha = ['a', 'b', 'c', 'b']
# alpha.remove('b').remove('b') in place modifiers returns none as result means they mutate original list so this throws error of attritbute error
alpha.remove('b')
# print(alpha.remove('b'))
print(alpha)

# Nested List - 2D list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix.remove([1,2,3]) # we need to specify value for remove() method anyhow
print(matrix)

# remove the 4 (specific item) from the list --> ( if asked to specify value to remove)
matrix[1].remove(4)
print(matrix)

''' pop() :
    Method'
    output : None
    - There is one "rebel" method.
    - .pop() modifies the list in-place (removes an item), but it returns the item it just removed instead of None
    - Specify the position index and it removes from the specified index value.
    - by default it has power to remove the last item
    - Removes and return an item
'''
# Normal list 1D-list
# Remove the last item
bet = ['a','b','c']
bet.pop()
print(bet) # removes the last item from the list
print(bet.pop()) #shows the removed item from the list
removed = bet.pop()
print(removed) # only for pop() we can store it in a variable , for rest all in place modifiers they return None.

# Since remove() demands the specification of item to remove
#       pop() demands  the specification of index to remove an item

# remove first item from the list
list = [1,2,3]
remove = list.pop(0) # returns the Immutable object
print(f'Removed Item :{remove}')

# Nested List 2D-list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# remove the last row from the matrix
matrix.pop() #returns the mutable object in 2D list
print(matrix)
# remove the second list first item from matrix --> (if asked to specify position of item)
matrix[1].pop(0)

# remove the last item of the first list
matrix[0].pop() # by default pop() will remove the last item, so don't need to mention index for this.

''' ----------------------------- Update Items --------------------------'''
'''
   - After we analyze and check we may find duplicates, bad data, old data.
   - But this time we have the feature to update data instead of throwing (remove operation)
   - like we may be a customer who changes his email, or price of product changes like existing data changes we need to update it.
'''
''' 
    How to update the data ? 
      - we don't have dedicated methods to update values we have assignment operators “=”.
      - we need to specify the lists with index number and assign the new values.
      - we are just overwriting the value.
'''
# Normal list 1D-list
letters = ['a', 'b', 'c']
# update the first item to the value 'x'
letters[0] = 'x'
# Be careful if not specified index whole list gonna be list and type too changes
letters = 'z'
print(letters)
print(type(letters))

# Nested List 2D-list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# update the last row completely
matrix[-1]=['a','b','c']
# update a specific item in the row 1 col 1
matrix[1][1]= 'b'
print(matrix)