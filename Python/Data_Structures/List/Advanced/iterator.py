import math
''' Iterator : 
    The Iterator Protocol
    - An Iterator is a stateful object that allows for sequential traversal through a container. 
    - In Python, an object is considered an iterator if it implements the Iterator Protocol, consisting of two methods:
    - __iter__() / iter(): Returns the iterator object itself.
    - __next__() / next(): Returns the next value in the sequence. If no items remain, it raises the StopIteration exception.
'''
''' How Iterator is actually created ??'''
numbers = [1,2,3]
# Manual Iterator Creation
new = iter(numbers)
print(new) # Iterator object address
# It's an exhaustive retriveal where next() is used to bring the items for us. 
print(next(new)) #1
print(next(new)) #2
print(next(new)) #3
print(next(new)) #StopIteration

''' enumerate() :
    function
    Syntax : enumerate(iterable , start = 0)
    output : Iterator
    - enumerate is a iterator which we can use in for loop to iterate over items.
    - by default the start is 0 we can specify start as we wish
    - Enumerate use case :
      - Find the exact position of the bad data in the list.
      
'''
letters = ['a', 'b', 'c']
# print(enumerate(letters))  # Returns <enumerate object at 0x00000269EAAC5D00>

# To see the content in the object we need to wrap around list / other data structures(which calls repeatedly next() to store in specified Data structure)
# or use in for loop which uses internal next().
# print(list(enumerate(letters))) # when used list() it's like running the next() repeateadly to get all items and store in the list.

# When the __next__() method is called on any iterator, it can only return exactly one object. It cannot return multiple independent variables at the same time.
# so when internally in the for loop next() is called on enumerate, it will return a tuple object. which consist of 2 values in int (index,value)
# Returns each time an tuple object
for package in enumerate(letters):
    print(package)

# Iterable Unpacking. Any iterable object (Tuples, Lists, Strings) can be unpacked into multiple variables in a single line of code.
# enumerate returns the tuple for each single loop which is iterable and iterable unpacking can be done on the same line.
# So, as long as variables equal to values we can unpack things easily.
for i, l in enumerate(letters):
    print(i, l)

# assign ids starting from 101
employees = ['anna', 'bishop', 'catlyn']
for id, employee in enumerate(employees, start=101):
    print(id, employee)

''' reversed() :
    function
    Syntax : reversed(Iterable)
    output : Iterator
    - Returns an iterator that flips the data order
'''
letters = ['a', 'b', 'c']
# print(list(reversed(letters)))
for l in reversed(letters):
    print(l)

''' Zip :
    function
    Syntax : zip(iterable_1,iterable_2,...,strict = False)
    output : Iterator
    - combines two or more sequences into pairs(tuples)
    - default strict value False if True all the iterable items should be same.
'''
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
# print(list(zip(numbers, letters)))
for package in zip(numbers, letters, strict=True):
    print(package)


''' Advanced Iterators :
    - sometimes we want to do the data transformations like change the lowercase item in list to uppercase
    - using for loop : Loop through items and for each item apply the method upper().
    - In python we have a samrter solution to do this instead,
    - Map() function :  
      Syntax : map(function, Iterables, strict = False(default))
                      which takes 2 arguments 
                       1. function - which we want to repeat for each item
                       2. Iterable's - which contains the items
        - for each item it applies the function and throws out the item which is transformed
        - so the output not gonna be a list it will a map iterator object which can be used in for loop or we can use list() to get transformed items.
        - Map gonna take the list apply the transformation that we define for each item.   
        - Has Strict = False as default which ensure mapping Stops when the shortest iterable is exhausted.
        - If strict = True and one of the arguments is exhausted before the others, raise a ValueError.
        *** Note *** : 
        Map is fast, clean way to do data transformation.       
'''

# calculate the values from both list as base and power using map() function :
base = [2, 3, 4]
power = [2, 3, 4]
for result in map(math.pow, base, power, strict=True):
    print(result)

# Transform the data into upper case and stor them in list
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

# Transform list item to to integers and store them in list.
numbers = ['1', '2', '3']
print(list(map(int, numbers)))

# Transform the data by Cleaning up the list by removing all unwanted spaces
names = ['     vamshi', 'joe ', '    michael']
# print(list(map(str.strip,names)))
transform = map(str.strip, names)
for name in transform:
    print(name)

# It won't be executed as same iterator "transform" is being used to loop.
# If iterator made outside the for loop it works only for one loop
# If In-line Iterator is made for every loop  then Iterator is gonna be created and generates items.
for name in transform:
    print(name)
