import random
''' random() :
    Syntax : random()
    random function
    output : float
    - returns a random float between 0.0 and 1.0 
'''
print(random.random())

''' randint() :
    Syntax : randint(start,end)
    random function
    output : int
    - gets a random whole number from start to end(both included)
'''
print(random.randint(1,6))

''' 
    The above both functions are used to generate test data (dummy) for like age,ID,or prices.
    Random Sampling - picking a smaller,random part of huge dataset
'''

# Challenge
# Generate the random integer between 1 to 100, and check if the result is an even number.
x = random.randint(1,100)
print(f"{x} is generated")
# Normal if - else block
if x % 2 == 0: 
    print(f"{x} is a even Number")
else:
    print(f"{x} is not an even number" ) 

# # Ternary if - else block
generated_value = f'{x} is even Number' if x % 2 == 0 else f'{x} is not even Number'   
print(generated_value)
