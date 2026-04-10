''' How to sort ??
   - The data inside the list is up to date there is no change needed.
   - But the data is chaotic we need to sort in some order .
   - sorted data will be very useful in real applications like
    1. Rank by price in a product list so, we need to sort them.
    2. sort the names alphabetically in the names list
'''
''' ------------------------- sorting list -------------------------
    Sort in either ascending or descending order where items order matters.
'''

# Using the Attackers : In-place modifiers who attacks the data directly, no clone is made.
''' sort() :
    Method
    output : None
    - sorts the data in lowest to highest form (Ascending order)
    - only supports on Data Structures with similiar data types
'''
# Normal 1D-list
letters = ['a', 'c', 'b']
# sort the list in ascending order
letters.sort()
print(letters)

# Nested 2D-list
''' comparison rules :
    sort() involves the check of < (lesser than) item while comparing as it needs to sort data in ascending order.
    Rule 1:  value Priority - compares the values of each lists index and which is smaller that is thrown to first.
    Rule 2: length priority - if one list is prefix of another list the list with lesser items is smaller
'''
# Equal row items lists Checks for value priority
matrix = [
    ['g', 'f', 'i'],
    ['a', 'b', 'd'],
    ['a', 'b', 'd']
]
# sort whole matrix
matrix.sort()
print(matrix)


# prefix row and unequal row items
matrix = [
    ['g', 'f', 'i', 'k', 'q'],
    ['a', 'z', 'r', 'z'],
    ['a', 'z', 'r',]
]
matrix.sort()
print(matrix)

# sort specific row of the matrix
# always target the row we want to sort.
matrix = [
    ['g', 'f', 'i'],
    ['a', 'b', 'd'],
    ['a', 'b', 'd']
]
matrix[0].sort()
print(matrix[0])


''' sort reverse :
    Syntax : .sort(reverse=True)
    Method
    output :None
    - sorts the data in highest to lowest form (Descending order)
    - only supports on Data Structures with similiar data types
'''
# Normal 1D-list
numbers = [2, 3, 4, 10, 50, 100]
numbers.sort(reverse=True)
print(numbers)

# Nested 2D-list
''' comparison rule :
    - .sort(reverse = True) involves the check of > (greater than) item while comparing as it needs to sort data in descending order.
     Rule 1:  value Priority - compares the values of each lists index and which is greater that is thrown to first.
    Rule 2: length priority - if one list is prefix of another list the list with more items is greater in the > comparison
'''
# - Equal row items with no prefix list prefers the Rule 1 : Value Comparison rule check
numbers = [
    [9, 5, 7],
    [3, 8, 0],
    [5, 8, 1]
]
numbers.sort(reverse=True)
print(numbers)

# unequal row with a prefix list --> prefers Rule 2 : Length Comparison rule check
# there can be unequal rows with no prefix list
numbers = [
    [5, 8, 1, 5],
    [9, 5, 7],
    [9, 5, 7, 10, 11, 12]
]
numbers.sort(reverse=True)
print(numbers)

# sort the specific row list items in desscending order
numbers = [
    [5, 8, 1, 5],
    [9, 5, 7],
    [9, 5, 7, 10, 11, 12]
]
numbers[2].sort(reverse=True)
print(numbers[2])

# By using the Cloners : which clones the original list and perform its operations.
''' sorted() :
    Function
    output : list or input to function data type
    - Clones the original data and does sorting
'''
numbers = [100, 90, 40, 50, 20, 99]
# Sort the data without changing the original list
sorted_numbers = sorted(numbers)
print(f'original list : {numbers}')
print(f'sorted list   : {sorted_numbers}')
print(f'''
If did in-place sorting ID'S would've been the same :
    original list ID : {id(numbers)}
    sorted list ID   : {id(sorted_numbers)}''')


''' sorted() :
    Function
    Syntax : sorted(variable,reverse = True)
    output : list or input to function data type
    - Clones the original data and does sorting
'''
numbers = [99, 70, 40, 80, 20, 100]
# sort the list in descending order with cloning the original list
sorted_numbers = sorted(numbers, reverse=True)
print(f'original list : {numbers}')
print(f'sorted list   : {sorted_numbers}')


''' ------------------------------ Reversing List -----------------------
           sort the data i dont'care about the order of the items
'''
# using Attackers :
''' reverse() : 
    Method (In - place modifiers)
    output :None
    - Flip the list around the values order isn't a matter anymore
    - This method is different than the argument 'reverse = True' we used in the sort.
    - There is no sorting logic involved in this method just makes for ex :last items first and first items last
'''
# Normal 1D-list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# Nested 2D-list
# No comparisons just make last item first and first item last
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
numbers.reverse()
print(numbers)

''' reversed() :
    Function
    output : iterator  
    - clones the original list and then does it operations.
'''
# Normal 1D-list
numbers = [100,90,80,56,78,69]
reversed_numbers = list(reversed(numbers)) # reversed holds the address to original list and a counter pointer to the end of the list item. 
# use for loop or list() to retrieve items 
reversed_numbers = reversed(numbers)
print(f'original list: {numbers}')
print(f'reverse list: {reversed_numbers}')

# Nested 2D-list
numbers = [
    [1,2,3],
    [5,6,7],
    [9,11,23,56]
]
reverse = list(reversed(numbers))
print(reverse)
