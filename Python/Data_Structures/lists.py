# ''' List :
#     - List is a ordered collection of Items
#     - List's are changeable
#     - Allows Duplicates
#     - Lists are like no rules can do whatever we want do with the data
#     - This are very common and widely used in Python
# '''
# ''' ---------- How to Create ? ---------'''
# # Empty list
# empty = []
# print(empty)
# print(type(empty))

# # ---- Lists with similiar data types and manual item entry ----
# # List with String items --> Adding items to the list manually there can be other ways too to add items.
# names = ['vamshi', 'vamsh', 'john']
# print(names)
# print(type(names))

# # List with Number's item's
# numbers = [1, 2, 3]
# print(numbers)

# # ---- Lists with Mixed Data Types ------
# mixed_list = [1, 'a', 'True', None]
# print(mixed_list)

# ''' Creation of List with Built-in function list()
#     list(value)
#     built - in function
#     output : list
#     - Convert an iterable (sequence) into a list
# '''
# empty = list()
# print(empty)

# letters = list('Vamshi')
# print(letters)


# numbers = list(range(5))
# print(numbers)
# print(len(numbers))

# # --------- Nested Lists - Matrix --------------
# # Similiar Data Types Nested List
# matrix = [
#     [1, 2, 2],
#     [3, 2, 4],
#     [7, 9, 0]
# ]
# print(matrix)
# print(type(matrix))

# # mixed Nested List
# mixed_matrix = [
#     [1, 2, 3],
#     ['vamshi', 'john', 'unknown'],
#     [True, False]
# ]
# print(mixed_matrix)

# ''' --------------- Access & Read ----------------'''

# lst = [1, 2, 3, 4, 5]
# # To access and read all items in the list
# print(lst)

# ''' Indexing - used to retrive only 1 value where we need to specify index value.
#     To Access Only specific item from the list
#     - For accessing only 1 item  from list we need the Indexing Technique
#     - positive index from left to right and starts from 0,1,2,....
#     - negative index from right to left and starts from -1,-2,-3,....
# '''
# print(lst[1])  # positive index number for accessing from left to right
# print(lst[-1])  # Negative index number for accessing from right to left

# ------- Access and read Nested List (Matrix) ----------

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Get whole matrix
# print(matrix)
# # Get only one row
# print(matrix[1])  # Access 2nd row of matrix
# print(matrix[-1]) # Access last row of matrix
# # Get only one value
# print(matrix[-1][-1])

# ''' Slicing - To retrieve multiple Items
#     - We have to have boundaries which are start and end indexes for slicing.
#     - In slicing stop Index is not inclusive
#     - In slicing if we want the start index  to be " 0 " then we can skip it as it is default in slicing [ : end index]
#     - In slicing if we want the end index  to be " -1 or len(variable) - 1 " then we can skip it as it is default in slicing [ Start index : ]
#     - [ : ] this brings entire list where no start and end indexes given, it treats the default values for indexes in this case.
# '''
# # Slicing in normal List
# lst = ['a', 'b', 'c', 'd', 'e']
# # Get the first two items
# print(lst[:2])
# # Get the last two items from the list
# print(lst[-2:])
# # Get whole list
# print(lst[:])

# # Slicing in Nested List (Matrix)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# #  Get first two rows
# print(matrix[:2])
# # Get last two rows
# print(matrix[1:])
# # Get first 2 items from the list 3 of the matrix list
# print(matrix[2][:2]) #Remeber : Cinema seat search - To search for a target values specify the row number first then, apply slicing to it.

# --------------------- How to Unpack ?? -------------------
# ''' Unpacking List's
#     - So far we placed multiple items into the list and packed them.
#     - so now we can now unpack the items and use them wisely.

#     Why we need to Unpack things??
#     - lets say we have a personal info with items as name, age , role , city etc.
#     - Each item has its own importance and we can apply various operations on the different items.
#     - To use them differently first we need to hold them in separate variable so we can easily apply the corresponding data types operations.
# '''
# person = ['john', 22, 'Data Engineer', 'paris']

# # Wwithout Unpacking
# # using only indexes makes code long and hard to extend
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

# # With Unpacking
# # Unpacking list of variables, sepeareted by commas
# # Rule : Variable order must match the list values order
# # Unoacking is clean, easy,  and makes code simple to extend
# name, age, role, country = person
# print(role)
# print(age)

# ''' Rest Collector - Asterisk * 
#     - if we want to unpack things and think to only unpack specific start or end or both and move rest into separate list we need to use Asterisk (*)
#     - * Asterisk Stores the Rest in New list 
#     - Python gonna assign specified variable with that value and take everything leftover into new list.
#     - Rule : only one asterisk(*) is allowed in unpacking
# '''
# # first and last items matters and rest everything in middle can be stored or unpacked into another list
# name, *details, country = person

# print(name)
# print(details)

# # Start item matters and rest can be moved into details list while unpacking
# # for this we need to specify the variable for first item and asterisk *
# # Be careful with the order of values if in future we change the order the variable assignment changes in unpacking
# name, *details = person
# print(name)
# print(details)

# # last item is important and rest everything can be moved into details
# *details, country = person
# print(details)
# print(country)

# # Rules fpr unpacking

# # Nr. of variables must match the values exactly - not less, not more
# numbers = [1, 2, 3, 4]
# first, second, third, last = numbers

# # Note : *Asterisk collects leftovers, and it’s fine if there are none
# bags = ['plastic']
# variant_1, *rest = bags
# print(variant_1)
# print(rest)  # Empty list

# #  Note : Can Unpack any sequence (list, tuples, strings, etc.)
# message = 'hello'
# first, *rest = message
# print(first)
# print(rest)

# ''' Skipping Items underscore "_" 
#     unpacking using "_"
#     - If the value is not that important at the time of unpack we can simply use _ to skip that item and move ahead.
#     - we can use multiple underscores
# '''
# person = ['john', 22, 'Data Engineer', 'paris']
# # Unpack only name, role rest eveything skip it. 
# name, _, role, _ = person

# ''' power of Asterisk(*) and underscore(_)
#     - If we want start , end items and the middle items are so long that we end up using more _ to skip items.
#     - Instead we can combine the power of Asterisk(*) with the underscore(_) 
#     - we can use * and move to new list but we want to skip them, so * gonna take middle part instead of storing in new list we use "_" to skip complete middle part now.
# '''
# # Unpack first and last value , but skip all values in middle
# name , *_ , country = person
# print(name)
# print(country)
# print(*_) # Skipped Part

