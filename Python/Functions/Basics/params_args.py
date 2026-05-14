''' Parameters :
    - Names used in function defination that describes what data the function expects.
    Arguments : 
    - Actual values passed in a function call that are assigned to parameters.
 
'''
# Normal way 
name = '    CaIlLee '
print(name.strip().lower())

''' Hard Coded Function:
    - Always performs the required operations on the hard coded values inside the function.
    - Any number of calls made it still returns the same result
    - Not very much recommend to use.
'''
def clean_name():
    name = '    CaIlLee '
    print(name.strip().lower())

clean_name()
# clean_name() # Does same work as before cleans up same name in fucntion

''' Dynamic Function
    - Always performs the required operations on the dynamic values.
    - Here for this function we need Argumenst and parameters.
    - Parameter accepts the values 
    - Arguments are the actual values
    - Every function call can pass different arguments
'''
def clean_name(name): #Parameter 
    print(name.strip().lower())

clean_name('  JoHN  ') #Argument
clean_name('Viktor   ')
