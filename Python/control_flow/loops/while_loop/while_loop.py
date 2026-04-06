''' While loop : 
     - Repeats a block of code - over and over as long as condition is True!!
     - There are 2 categories of while
        1. While condition (Classical type)- Runs if condition is true and ends if condition is false.
        2. while True - Runs infinitely so we add break statement to forcefully exit the loop.
'''
''' While condition (Classical type) :
      - we need to initalize the loop variable value.
      - Next condition gonna run until its true and executes the while loop body for that loop.
      - always update the loop variable in each loop else it ends up as infinte loop.
'''
#  Counter with While loop :
counter = 1
while counter <= 5:
    print(counter)
    counter += 2

''' while True :
   - while + if + break makes the infinite loop to end.
   - we build a infinte loop, have the variable to hold value or may be user inputs, then check for a condition using "if + break" to exit the loop.
   - we will be using the if statement and condition to meet and then we will use break statement to end the loop.
   - Its like Infinite loop with the Add on of checking the condition the scope of the checking should be inside the loop.

# Dont run this it leads to infinte running on systems until you press ctrl + c 
# while True:
#     print('You are in infinte loop')
'''

# write a program that keeps asking "Do you agree?" until the user types "yes"
# using while condition :
answer =""
while answer != 'yes':
    answer = input('Do you Agree? (yes/no): ')
print('Thank you!!')

# using while True :
# it don't need initialization unlike how while condition required to run
while True:
    answer = input('Do you Agree? (yes/no): ')
    # Must need the condition to break out of if loop 
    if answer == 'yes':
        break
print('Thank you!!')    
# Among both while True is better to use as it dont required any variable to initialize in the start.
    
''' while condition vs while True :
 
    while condition :
     i = 1        ---> Initialization
     while i < 4: ---> condition
        print(i)
        i += 1    ---> Update
    - Exists Normally if the condition is false
    - safer + more Readable
    - use cases : counter , limited retries , validating the input from the user
    
    while True :
    while True:
        x = input('Enter hit or flop')
        if x == 'flop':
            break
    - Must have extra if + break
    - Risk of infinite Loop + More flexible    
    - use case :  
        open ended : waiting to get trigger from external sources like Databases/ Stream/ API etc.
'''

''' Challenge :
    - only 3 attempts
    - Yes within three attempts -> "Glad we're on the same page"
    - otherwise "3 strikes. you're out!"
'''
# using while condition + else 
# same approach if the while loop exsit normally without hitting any break statement, the else is gonna be executed.
# if the break is hit then the else part wont be executed same as for - else loop.
attempts = 0
while attempts < 3:
    # print(f'Attempt number - {attempts + 1}')
    answer = input('Do you Agree? (yes/no): ')
    if answer == 'yes':
        print('Glad we are on the same page')
        break
    attempts += 1
else:
    print("3 strikes, You are out!")

# using while True 
# Here we need to exit Infinite loop our only option is if inside the while loop break is hit then only this infinte loop exits.
# so we can't use while - else for this while True thing.
attempts = 0
while True:
    answer = input('Do you Agree? (yes/no): ')
    if attempts < 3 and answer == 'yes':
        print('Glad we are on the Same page')
        break
    attempts += 1
    if attempts == 3:
        print("3 strikes, You are out!!")
        break

