''' List : 
    - List is a ordered collection of Items
    - List's are changeable
    - Allows Duplicates
    - Lists are like no rules can do whatever we want do with the data
    - This are very common and widely used in Python
'''
''' ---------- How to Create ? ---------'''
# Empty list
empty = []
print(empty)
print(type(empty))

# ---- Lists with similiar data types and manual item entry ----
# List with String items --> Adding items to the list manually there can be other ways too to add items.
names = ['vamshi', 'vamsh', 'john']
print(names)
print(type(names))

# List with Number's item's
numbers = [1, 2, 3]
print(numbers)

# ---- Lists with Mixed Data Types ------
mixed_list = [1, 'a', 'True', None]
print(mixed_list)

''' Creation of List with Built-in function list()
    list(value) 
    built - in function
    output : list
    - Convert an iterable (sequence) into a list
'''
empty = list()
print(empty)

letters = list('Vamshi')
print(letters)


numbers = list(range(5))
print(numbers)
print(len(numbers))

# --------- Nested Lists - Matrix --------------
# Similiar Data Types Nested List
matrix = [
    [1, 2, 2],
    [3, 2, 4],
    [7, 9, 0]
]
print(matrix)
print(type(matrix))

# mixed Nested List
mixed_matrix = [
    [1, 2, 3],
    ['vamshi', 'john', 'unknown'],
    [True, False]
]
print(mixed_matrix)

