'''
input() function :
   - Its a built in function in python.
   - User needs to enter something until then the progrsm halts until user types something and gives the code required value.
   - using input() alone reads the users responsebut immediately discards it.
   - To keep the value ,assign it to variable.
   - It makes code interactive.
   - The values of the input() function are dynamic values.
'''
name=input('Enter your name:') # Here the name variables value is dynamic.
print(name,"is a user")

''' Hard coded(static) value vs Dynamic value
    Hard coded(static) value: Fixed piece of data written directly in to the code that never changes at runtime.
    Dynamic value           : value entered by the user that can vary each time the user runs the program.
    
'''
country='India' # Hard coded value
state = input("enter country name:") # Dynamic value