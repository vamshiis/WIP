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

