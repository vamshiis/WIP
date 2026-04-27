''' SETS Methods :
    add()     --> single Item insertion
    update()  --> multiple item insertion but only Iterables(list,tuple,string)
    remove()  --> only if your sure the value exsists use remove, otherwise just don't 
    discard() --> removes value if present No drama if they don't exsist unlike how remove() does. 
      '''

a = {10,20,30,40}
''' How to add an item ??
   - Note : Index - Based methods do not work with SETS
   add() :
   - Inserts the item somewhere in the set, but only if it is new.
   - Ignores the Duplicate entries to add into sets.
   - only works to add a single item at a time no multiple items adding is supported.
'''
a.add(50) # Adds randomly in the set based on slot it got.
print(a)

''' update() :
    - Merges another group of values(Iterables) into the set.
    - useful to add multiple values at once just
    Note : 
    we can use math operators as quick shortcuts : | , & , - , ^ to perform this set methods.
'''
a.update([1,2,3],'Hello',{4,5,6,999})
a |= {100001,100002} # |(pipe) is used to update the set and give the iterable values
print(a)

''' How to remove ??
    remove() :
    - we can use remove() method which takes value as input to remove the specified item just.
    - but it always removes only if it exists otherwise it throws error "KeyError"
    - Throws Error if the value is missing
    - we need to have a check if the value exists first and then we need to write a if condition and remove it hetic task.
    - If sure the value exists which you wanna remove then use remove() method other wise don't use it just.
'''
# a.remove(20000)
# print(a)

# To make sure the value actually exists and use of remove method we need to do this massacare
# new_set = {1,2,3}
# removable = 100
# if removable in new_set:
#     new_set.remove(removable)
# print(new_set)

''' "Saviour"
    - The problem with remove() was it removes only if it exists otherwise it throws Key Error just.
    - so we are falling back to have a check and remove sort of but now we have discard().
    discard() :
     - Removes the item if it exists and does nothing if it does not
     - Literally doesnt throw any error if the value doesnt exists 
'''
a.discard(20000)
print(a)

# pop() - we have pop guy too but it removes a last guy but here in set there isnt a concept of index so it removes some random guy.
# a.pop() - not recommended to use with sets