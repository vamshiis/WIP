# -------------------------- Explore and Analyze ---------------------------
''' 
    - Before doing anything complex we need to first understand the content of our data so, we need to analyze the data we have.
    - If we have data we need to explore and analyze
    - we need to start asking quick questions like
    - what is the len of list? , what is highest and lowest value in the list ? , do list satisfy or pass or data quality checks? etc.
    - we have lot of functions to explore and analyze the data some are :
         - max() , min() , sum() , len() --> this will help us analyze the data.
    - To have the completness & Exsistence Check we have
         - all() - if all values are true 
         - any() - if any value is true
    - We also have Methods to search and count
       -  variable.count() , variable.index()     
    - we also have membership and identity operators to check something
       - in operator - to check if it exsist!!
       - is operator - to check if same objects
    - we can also use comparison operators 
       - '==' and '>' operators
'''

numbers = [1, 2, 3, 4, 5]
# Functions:
''' max() : 
    - Function
    - output : List Item
    - Find the highest Value
'''
print(f'max : {max(numbers)}')
''' min() : 
    - Function
    - output : List Item
    - Find the lowest Value
'''
print(f'min : {min(numbers)}')

''' sum() - Aggregate function
    - Function
    - output : number
    - Finds the total by summing all values.
'''
print(f'Sum : {sum(numbers)}')

''' len() 
    - Function 
    - output : number
    - finds the length of a list (number of items)
'''
print(f'Length : {len(numbers)}')

''' all() 
    - Function
    - output : True/False
    - returns True if all values are True
'''
print(f'All : {all(numbers)}')
# Here 0 is considered as no value and it is False in boolean equivalence
print(f'All : {all([1, 0, 2])}')
# Here '' is also considered as no value so it becomes false.
print(f'All : {all(['a', '', 'c'])}')
print(f'All : {all(['a', 'b', 'c'])}')

''' any()
    - Function
    - output : True/False
    - returns True if any one value is True.
'''
print(f'Any : {any(numbers)}')
print(f'Any : {any([1, 0, 2])}')
print(f'Any : {any(['a', '', 'c'])}')
# Returns False at least one value should exsist
print(f'Any : {any(['', '', ''])}')
# Returns False at least one value should exsist
print(f'Any : {any([0, 0, 0])}')

''' count() :
    - Syntax : Variable.count(value to count)
    - Method
    - output : Number
    - return how many times a value appears in the list.
    - useful to find if the specified value is unique or duplicate in the given list.
'''
print(f'Count : {numbers.count(5)}')

''' index() :
    - Syntax : variable.index(value to search)
    - Method
    - output : Number (index value)
    - returns the position of the first occurance of a value
'''
print(f'Index : {numbers.index(5)}')

''' in :
    - Operator
    - output: True / False
    - Checks if a value exists in a sequence
'''
print(4 in numbers)
print(8 in numbers)
print(8 not in numbers)



''' Comparison operators :  
    - The first element are compared, if they're equal,Python moves to the next element
    **** Golden Rule for comparison operators *****
    - Think of the comparison as a Race to the first difference:
    - Priority 1 (Value): The moment a number is bigger/smaller than its partner at the same index, the race ends.
    - Priority 2 (Length): If the race ends in a tie (all items match), the "Longer" list is crowned the winner of the > comparison, 
                           and the "Shorter" list is the winner of the < comparison.

'''
# '==' - checks if two variables values are identical.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(list1 == list2)

# using < or >
# Same sizes list
''' Rule 1 : The first Difference
     - Python compares items at the same index.
     - The moment it finds two items that are not equal, the comparison ends.
     - Nothing else in the list matters after this point.
'''
list1 = [9, 2, 3]
list2 = [11, 4, 3]
print(list1 < list2)  # compares 9 < 11 --True , so output is True

list1 = [1, 2, 5]
list2 = [1, 2, 3]
# Compare 1 < 1 = equal --> next values 2 < 2 = equal -->next values 5 < 3 = False
print(list1 < list2)

list1 = [1, 2, 5]
list2 = [1, 2, 5]
print(list1 < list2) # it always checks on condition for rach index value and then marks them false if equal , so this are identical but list1 < list2 is false

''' Rule 2 : The Prefix Rule (length priority)
    - If one list is 'prefix' of other (eg. [1, 2] vs [1, 2, 5])  the shorter list will be considered smaller.   
    - working :
       - Iterative comparison : Python checks list1[0] vs list2[0] if they are equal moves to index 1
       - Next Item : compares list1[1] vs list2[1] if they are too equal moves to index2
       - Exhaustion check : The list1 has ended. It sees list2 still has items left at index 2 (5),while list1 has nothing left.
       - The decision : - In lexicographical logic, "nothing" is always less than "something".
                        - Since list1 ran out of items first and all its existing items matched, 
                          it is automatically deemed the smaller list. 
       - If all compared elements match, the shorter sequence is always considered less than the longer sequence. 
       - This is exactly how words are sorted in a dictionary: "app" comes before "apple" because it is a prefix that ends sooner.
       *** Most Important criteria *** : The list1 should be prefix of list2 then only this rule apply
'''
list1 = [1, 2]
list2 = [1, 2, 5]
# we are asking: "Is list1 a shorter prefix or does it have a smaller value at the first point of difference?"
print(list1 < list2) # True - sorts like ascending order

# Here the comparison operator changes to compare longer list 
list1 = [1, 2, 5, 7]
list2 = [1, 2, 5]
# we are asking: "Is list1 longer than its prefix or does it have a larger value at the first point of difference?" 
print(list1 > list2) # True - sorts like descending order gives higher list forst upon comparison

list1=[9]
list2=[1,2]
print(list1 < list2) # Here it is not prefix so it compares values first 9 < 1 (no) - so false 

# Tricker question is empty list [] < [1] list with one item
print([] < [9])  #True
'''
   - first compare value : no value of first list so no comaprison happens 
   - next check length : empty list length is 0 and item list length is 1 so, here 0 < 1 (lengths) yes so output : True
   - if same question asked as [] > [1,2,3] its false.
   - checks values there is no value in list1 so no comparison happens.
   - checks the length list1 len = 0 and list2 len = 3 --> 0 > 3 --> false 
'''
print([] > [1,2,3]) #False

''' Rule 3: Deep Comparison (Nested Sequence)
    - If the items being compared are themselves lists, 
    Python "steps inside" them to perform the same checks recursively.
'''
list_a = [1,[2,2]]
list_b = [1,[2,4]]
print(list_a < list_b) #True

''' Rule 4 : Type Strictness 
    - You cannot compare items if Python doesn't know how to relate them (e.g., String vs Integer). 
    - This will crash your program.
'''
list_a = [1,'hello']
list_b = [1,3]
# print(list_a < list_b)
# compare 1 < 1 but they are equal, 
# next goes after hello < 3 wooo what's this nahh Type Error cant use < between str and int instances.

# If two lists are identical and if we check < or > it returns false 
list_z = [1,2,3]
list_y = [1,2,3]
print(list_z > list_y)  #False
print(list_z < list_y)  #False
print(list_z == list_y) #True

''' is Operator :
    - It checks the address of the variables to which object they are pointing.
'''
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1 is list_2) #False list_1 address can be somthing 4567 and list_2's 67800 so that's why its false even if values are same

list_1 = [1,2,3]
list_2 = list_1
print(list_1 is list_2) #True here list_2 copies the address of list_1 , so now they both have same addresses 