''' --------------- Access & Read ----------------'''

lst = [1, 2, 3, 4, 5]
#---------------------To access and read all items in the list---------------------
print(lst)

#---------------------To Acess and read one item from the list----------------------
''' Indexing - used to retrive only 1 value where we need to specify index value.
    To Access Only specific item from the list
    - For accessing only 1 item  from list we need the Indexing Technique
    - positive index from left to right and starts from 0,1,2,....
    - negative index from right to left and starts from -1,-2,-3,....
'''

# Indexing in normal 1D list
print(lst[1])  # positive index number for accessing from left to right
print(lst[-1])  # Negative index number for accessing from right to left

# Indexing in 2D - Nested List (Matrix) 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Get whole matrix
print(matrix)
# Get only one row
print(matrix[1])  # Access 2nd row of matrix
print(matrix[-1]) # Access last row of matrix
# Get only one value
print(matrix[-1][-1])

# -------------- To access and read multiple items from the list -----------------
''' Slicing - To retrieve multiple Items
    - We have to have boundaries which are start and end indexes for slicing.
    - In slicing stop Index is not inclusive
    - In slicing if we want the start index  to be " 0 " then we can skip it as it is default in slicing [ : end index]
    - In slicing if we want the end index  to be " -1 or len(variable) - 1 " then we can skip it as it is default in slicing [ Start index : ]
    - [ : ] this brings entire list where no start and end indexes given, it treats the default values for indexes in this case.
'''

# Slicing in 1D - normal List
lst = ['a', 'b', 'c', 'd', 'e']
# Get the first two items
print(lst[:2])
# Get the last two items from the list
print(lst[-2:])
# Get whole list
print(lst[:])

# Slicing in 2D - Nested List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#  Get first two rows
print(matrix[:2])
# Get last two rows
print(matrix[1:])
# Get first 2 items from the list 3 of the matrix list
print(matrix[2][:2]) #Remeber : Cinema seat search - To search for a target values specify the row number first then, apply slicing to it.
