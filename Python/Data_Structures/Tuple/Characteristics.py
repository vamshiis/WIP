'''
1. Ordered 
   Python gonna remember the order of the items of our tuple 
   the way we defined them.
'''
my_tup = (1, 2, 3)
print(my_tup)  # Ordered

''' 
2. Duplicates 
   Python allows duplicates values in the tuple
'''
my_tup = (10, 20, 30, 10, 20, 30)
print(my_tup)

''' 
3.Indexed
  Each value has its own index which we can use them to retrieve.
'''
my_tup = (10, 20, 30)
print(my_tup[0])

'''
4.Mutable
  Tuples are Immutable we cant change them
'''
my_tup = (1,2,3)
my_tup[0] = 0
print(my_tup)

'''
But we can use functions on the tuples which can be converted to List and then we can mutate them.
remember its just the copy of the items not original tuple which the functions return us.
'''
my_tup = (9, 8, 7, 6, 3, 2, 1)
# To make sure you work with tuple and have the safety check always, so always convert them back into tuples.
print(id(my_tup))
my_tup = tuple(sorted(my_tup))
print(id(my_tup))
print(my_tup)
# usage of sorted function which returns the List as output.
sorted_tup = sorted(my_tup)
print(sorted_tup)

sorted_tup[0] = 0
print(sorted_tup)


