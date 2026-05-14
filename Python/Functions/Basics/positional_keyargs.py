''' Rule :
    Number of Arguments must match the number of Parameters

    • Positional Arguments :
    - Values pass to the function based on their Order
    - Rule :
      The order of Arguments must match the order of the parameter
    
    • Keyword Arguments :
    - Values pass to the function based on their Names
    - Readability :
        - Keyword Arguments are easier to read and understand than positional.
    - Safety :
        - Keyword arguments are safer since they reduce mistakes with clear names
    - Overhead :
        - Keyword arguments take more time to write and maintain.

    > Which to choose between them??
    - Depends on the number of Parameters
    - 2 - 3 use positional arguments
    - > 3 use keyword arguments

    Mixed Arguments :
    Rule :
     We must start with Positional Args then Keyword Args

    Default Parameter:
    - Parameter that has already a value so if we don't pass anything Python uses that value automatically. 
    - A default value fixed to be used by function even if argument is not passed to function.
    Syntax :
    - function_name(param1,param2,param3 = 'default',param4 = 'default')
    - first the arguments passing parameters to be declared later the default guys to be declared to the end 
    - we cant mix them like (param1,param2 = 'default',param3) it will throw error.
'''


def full_name(f_name,l_name,country = 'N/A'):  # f_name, l_name : Parameter and country = default parameter 
    f_name = f_name.strip()  # cleaned : Local variable
    l_name = l_name.strip()
    print(f'{f_name} {l_name} From  {country}')
full_name('  John','Vijay   ','GE') #Positional Arguments
full_name(f_name = '  Kurry', l_name ='M   ',country ='GE') #Positional Arguments
full_name('  Kurry', l_name ='M   ',country ='GE') #Mixed Arguments


def calculate_total(d,a=0,b=0,c=0):
    print('value of a is', a)
    print('value of b is', b)
    print('value of c is', c)
    print('value of d is', d)
calculate_total(1)