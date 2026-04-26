'''
1. Ordered 
   Python gonna remember the order of the items of our list 
   the way we defined them.
'''
my_list = [1,2,3]
print(my_list) #Ordered

''' 
2. Duplicates 
   Python allows duplicates values in the Lists
'''
my_list = [10,20,30,10,20,30]
print(my_list)

''' 
3.Indexed
  Each value has its own index which we can use them to retrieve.
'''
my_list = [10,20,30]
print(my_list[0]) 

''' 
4.Mutable
  Lists are Mutable in Python we can insert, update,sort and remove items.
'''
my_list = [10,20,30,50,70,88,99,5,3]
my_list[0] = 20 #insertion at specific index
print(my_list)

my_list.remove(20) # removes a value if no value return valueError, we have pop(), remove(), del list[index], 
                  # del list[start:end](removes specified range index value), clear()
print(my_list)

my_list.sort(reverse=True)
print(my_list)
