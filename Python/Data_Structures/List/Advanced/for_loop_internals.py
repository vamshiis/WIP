# Create a Iterator object explicitly
list = [1,2,3]
iterator_list = iter(list)
print(next(iterator_list)) 
print(next(iterator_list)) 
print(next(iterator_list)) 


# Once an iterator reaches the end, it cannot be reset. A new iterator must be created using iter() to traverse the data again.
list = [1, 2, 3]
iterator_list = iter(list)
print(next(iterator_list))  # 1
print(next(iterator_list))  # 2
print(next(iterator_list))  # 3
# print(next(iterator_list)) #StopIteration start again the script or declare new Iterator to get the same values again


# The for loop is designed to catch the StopIteration signal internally and terminate the loop gracefully without crashing the program.
'''  Passing an Iterator (for item in iterator_list:)
    - create a iterator in memory lets say address (0X1111) which internally consist 2 things 
                        1. Address to actual iterable means list object address (0X2222)
                        2. Counter = 0
    - when the 1st for loop runs
        Step 1: 
          - The Golden rule of for loop is No matter what you give a for loop, its very first step is always to call iter() on the object you passed it.
            may it be an iterable object or Iterator Object.
          - so, the internal_iterator_creator = iter(Iterator) 
                --> internal_iterator_creator = iter(0X1111) ---> internal_iterator_creator = 0X1111
            Note : When you ask an iterator for an iterator, it just says, "I'm already an iterator!" and returns itself. 
                   It does not create a new bookmark. It just hands the loop the exact same bookmark you created at the top of your script. 
        - Step 2 : 
         item = next(internal_iterator_creator) --> item = next(0X1111) go to the iterator address you find 2 things address to iterable(0X2222) and counter = 0
                               follow the iterable address and bring the counter valued index value of the iterable and hand it to item, and increment the counter by 1.
                            ex : counter = 0 -- going to address (0X2222) ---> list=[1,2,3] bring index 0 value ---> item = 1 , counter = 1
                                 counter = 1 -- going to address (0X2222) ---> list=[1,2,3] bring index 1 value ---> item = 2 , counter = 2
                                 counter = 2 -- going to address (0X2222) ---> list=[1,2,3] bring index 2 value ---> item = 3 , counter = 3
                                 counter = 3 -- going to address (0X2222) ---> list=[1,2,3] bring index 3 value ---> item = None, throw StopIteration
                                 Goes into expect block and executes it body where we can see break the infinite loop breaks.
        - Now when a 2nd for loop is hit
        Step 1 :
          - in same way goes to create a internal_iterator_creator = iter(Iterator) 
                --> internal_iterator_creator = iter(0X1111) ---> internal_iterator_creator = 0X1111
        Step 2 :
         hits item = next(internal_iterator_creator) --> item = next(0X1111) go to the iterator address 
               you find 2 things address to iterable(0X2222) and counter = 3 (here it has value 3 because already our pointer is sitting at the end)
               Iterator remembers where it is unlike the normal for loop
        so now item = stopIteration for the first loop itself because the pointer is already at the end.
        so we dont even get a single Item it returns nothing for the second loop.  
        so if you want to loop through list again and again dont given the Iterator as a sequence to the loop.
        if you want to run once and dont want it again just give the Iterator to the for loop.   
        most of the function like zip(), reversed(), filter(), map() runs on this rule once they give they dont remember them it goes forward no back looking.
        so if you want to again Iterate declare again the list and create a iterator and give to for loop or run the script again.  
                                
'''
list = [1, 2, 3]

Iterator = iter(list)
# executes --> returns items from the list
print('1st loop items :')
for item in Iterator:
    print(f' {item}')

# executes but returns nothing
print('2nd loop items :')
for item in Iterator:
    print(f' {item}')


# creation of internal for loop logic:
''' 
    for loop internals using the while True logic
    Rule 1 : Passing a Sequence (for item in my_list:)
        - Everytime if the iterable as sequence is passed it will create a new iterator for every for loop.
        - creates a iterator for every loop and prints every item in the list
    Rule 2 : Passing an Iterator (for item in iterator_list:)
        - Everytime a Iterator is passed it remebers where it ends and doesnt loop through again.
        - Doesn't create iterator for each loop instead remebers upto which item it gave back just.
        - write any n loops but only prints the items once and after it gives literaly nothing.
'''
''' Passing a Sequence to for loop :'''
numbers = [1, 2, 3, 4]
# for loop (sugar coat of while True loop)
# This works same as for loop prints the items once and ends the infinite loop
# Execute another for loop as well 
print('------------Executing while True loop :---------------')

iterator = iter(numbers)
while True:
    try:
        item = next(iterator)
        print(item) 
    except StopIteration:
        break

print('------------Executing sugar coated for loop :---------')
for items in numbers:
    print(items)

''' Passing a Iterator to for loop :'''
numbers = [1, 2, 3, 4]
outer_iterator = iter(numbers)
# This works same as for loop prints the items once and ends the infinite loop
# Doesn't Execute another for loop as items exhausted in the first for loop itself
print('------------Executing while True loop :---------------')
inner_iterator = iter(outer_iterator)
while True:
    try:
        item = next(inner_iterator)
        print(item) 
    except StopIteration:
        break

print('Executing sugar coated for loop : literally gives nothing this time')
for items in outer_iterator:
    print(items)
