''' How to change?
   - as time flies we mend to change the data that is exsisting or make changes to data.
   - we have 3 types of changes.
      1. Add data - when we need to add new entries to exsisting list
      2. Remove data - when we need to discard bad quality data
      3. Update data - when we need to overwrite the existing data.
'''
''' --------------------- Add Items ---------------------------------- '''
# Easy and lazy way to add the item into the list.
''' append() :
    method
    output : list
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
    method
    output : list
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