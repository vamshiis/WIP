''' Combining List's
    - In Real Projects developers dream to have all the data at one place so they can perform the required operations.
    - But the data will be spread around in different data structures lets say all are in lists where we have customer data in customer list, orders list , products list etc.
    - so we have to combine all the data lists into one single list and make a perfect list
    - It's like stitching list's together to make a dream list
    - In python we have different ways on how to combine list's
'''

''' "+" operator :
    - we will combine 2 lists into single list
    "*" operator :
    - quickly makes the copies of given list
'''
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combo = letters + numbers
print(combo)
print(numbers*2)

''' nested list
   - we want them to be combined but want them to be separated inside the list like isolated.
'''
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combo = [letters, numbers]
print(combo)

''' extend() :
    Method (In-Place modifier)
    Syntax : list_1.extend(list_2)
    output : None
    - lets say we want to have flat list with combining lists but we don't want to create another new list and use + or nested list method to combine.
    - instead what we wnated is change one list and add another list to it just.
    - we have a method called extend() which stretches one list with another list its like method append() which add the items to the end.
    - we can change one list with combining the other list
    - extend doesn't create a new list; it expands the original one.
'''
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)

''' Combining using zip() :
     zip() :
     Method
     Syntax : zip(list_1,list_2)
     output : Iterator
    - lets say we don;t want the flat list with all the items and also at the same time
       we dont want to have the nested list where there are isolated lists inside
    - we want to pair up the lists instead like first item from list_1 and first item from list_2 and so on..
    - for this  we use a data structure called zip()
    - we can pair List with String Value
    - The output of the zip will be Iterator but we use list() function to see whats isnide 
       It contains the list of tuples "[()]" with the pairs
    - The pairing works for the shortest items list which we can pair up
      
        **Rule 1: Equal Sizes (Perfect Match)**
                When all inputs have the same number of items, zip() pairs everything from start to finish.
                Behavior: Every item is included in the output.
        
        **Rule 2: Unequal Sizes (The "Shortest Wins" Rule)**
                  When inputs have different lengths, zip() stops as soon as the shortest input is exhausted.
                  Behavior: Extra items in longer lists are ignored/dropped.        
        
        **Rule 3: The strict Argument (The Safety Check)**
                  Introduced in Python 3.10, this argument forces the function to verify that all inputs are the same length.
                   strict=False (Default): Follows Rule 2 (ignores extras).
                   strict=True: Raises a ValueError if lengths don't match. Use this when data loss is not allowed.
      
        **Rule 4: Strings as Arguments**
                  If you pass a string (like "HI" ) into zip(), Python treats it as a list of characters (`'H'`,`'I'`).
                  Behavior: If the string is shorter than your lists, the output will be limited to the number of characters in that string.
'''
# pair all the items from both the lists where sizes of both lists are equal.
letters = ['a', 'b', 'c']
numbers = [1,  2,  3]
# combo = zip(letters,numbers) #returns the Iterator Object
combo = list(zip(letters, numbers))
print(combo)

# pair all the items from both the lists where sizes of both lists are unequal
letters = ['x', 'y', 'z']
numbers = [ 1,  2,  3,  4] # 4 will be left out as the shortest list can only be paired up together
combo = list(zip(letters,numbers))
print(combo)

''' Data Safety Check : 
    As soon as any part of the input (list, string, or tuple) runs out of items, the whole function stops right there.
    Without strict: It quits quietly and just gives you what it managed to pair (the "Shortest Wins" rule).
    With strict=True: It still quits, but it screams (throws a ValueError) to let you know the sizes didn't match.
    
    - verify if both the list are of same sizes then only pair them up 
    - by default the strict will be false means whoever is smaller makes that many pairs.
    - If asked to check if the data is getting lost then we need to do safety check using strict = True.
    - If iterables don't match then it throws Value Error.
'''
# with equal size and safety check
letters = ['x', 'y', 'z']
numbers = [1,  2,  3,  ]
#checks for both the lists to be same if returns list of tuple then both lists are of same size.
combo = list(zip(letters,numbers, strict=True)) 
print(f'Applied strictness {combo}')

#  with unequal size and safety check
letters = ['x', 'y', 'z']
numbers = [1,  2,  3, 4]
# doing safety check with strict = True if returned "valueError" then the lists are not same.

# combo = list(zip(letters,numbers,strict = True))
# print(f'Applied Safety Check? {combo}')

# use argument but apply the data safety check 
letters = ['x', 'y', 'z']
numbers = [1,  2,  3, 4]
# returns valueError as HI is 2 items and letters,numbers are too unequal so it returns valueError
# ValueError: zip() argument 3 is shorter than arguments 1-2

# combo = list(zip(letters, numbers, 'HI',strict=True)) 
# print(f'with argument and lists safety check? {combo}')

# Pass string as an argument
letters = ['x', 'y', 'z']
numbers = [1,  2,  3,  4]
# Here the priority to pair is given to zip function argument so 2 pair of tuples made.

combo = list(zip(letters,numbers,'HI')) 
print(combo)

# Task 
# Pair Customers with their IDs (rebuild the relationship) also use the safety check.
ids = [101,102,103]
names = ['john','maya','sara']
print(list(zip(ids,names,strict=True)))