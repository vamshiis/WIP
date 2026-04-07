''' loops + else :
    - else is used with the loops in order to have data validations.
    - It can be used with for loop and while condition loop
    - we have some rules in order to use the else with the loops.
    1. Natural Exhaustion
    2. Forced Termination
    3. Iteration skips
    4.Zero Iteration Loops
'''
''' 1. Natural Exhaustion:
       - The else block is essentially a completion handler.
       - It executes only if the loop terminates naturally without hitting break inside the loop.
       - If the loop ends naturally in for loop that means it checked every item in the sequence.
       - If the loop ends naturally in the while loop this means condition Naturally became False. 
'''
''' The for loop example - Its more like a data validation thing
    - If the items in sequence are all iterated then,
       else block acts as "Verification Passes" Stamp.
    - Here loop ended naturally after iterating the sequence completely.
    - so the else will be executed succesfully   
'''
scores = [10,50,60,70]
for score in scores:
    if score > 0:
        print(score)
else:
    print('All Items in Sequence Executed Successfully!!')
    
''' The while loop example:
    - Here the condition should turn naturally false.
    - Then the else block will be executed
'''
attempts = 0
while attempts < 3:
    print(f'Attempt number - {attempts + 1}')
    answer = input('Do you Agree? (yes/no): ')
    if answer == 'yes':
        print('Glad we are on the same page')
        break
    attempts += 1
else:
    print("3 strikes, You are out!")

''' 2. Forced Termination :
        - If the break statement is hit the loops have forcefully ended not naturally.
        - so the else block after the loop will be completely bypassed.
        - break destroys the else
'''
''' Foor loop example :
    - Here if the specified condition is met inside the loop, and it has break combined then else will not be executed
'''
persons = ['Chetta','John','Kurian','Subashu','Thomas','Albert']
for person in persons:
    if person.lower() == 'subashu':
        print(f'{person} is found!!')
        break
else:
    print('Person is still inside the cave')

''' while loop example :
    - In this loop also same if the loop body breaks out forcefully for the condition we exepected to break,
       then else wont be executed.
'''
Tries = 0
while Tries < 3:
    if Tries == 2:
        print('Reached max attempts!!')
        break
    Tries += 1
else:
    print('Guessed correctly in given attempts!!')

''' 3. Iteration Skips :
      - The continue statement acts as a "Skip" Button.
      - It stops the condition satisfied Iteration skips int he for loop and goes on to loop around other available items.
'''

marks = [10, 20, 30]
for m in marks:
    if m == 20:
        continue
    print(m)
else:
    print('''surprise!! surprise!!
The for loop exited naturally!!.
It ran all the items in the sequence,so now i can be executed successfully!!
        ''')
    

''' 4. Zero Iteration Loops 
       - What if the loops wont even run once??
       - If you for loop and empty list or the while loop's condition is false from the very first check the loop is completely skipped. 
       - However, the loops are never stopped by break statements, Python considers this as natural Exhaustion.
       - so now the else block will be executed immediately.
'''
# Using for loop for Zero iteration loop
scores = []
for score in scores:
    print("executing for loop")
    print(score)
else:
    print("For loop not executed even once")

# While loop for zero iteration loop
score = 0
while score == 1:
    print("executing while loop")
    print("new score")
    break
else:
    print("while is not executed even once")

''' Note : else can't be used for while True :
          - The while True doesn't sustain the usage of else.
          - The while True actually is a infinite loop, we specify the condition and if met breaks the infinite loop.
          - so there is not possible case where we can use else with while True.
          - Even if used the else wont be executed in any case the while True always exits loop only when break is hit!!!
'''