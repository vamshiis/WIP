''' Variables : 
    We have 3 types of variables and we differentiate based on life cycle and accessibility
    Global variable:
      - It is defined outside the function scope and can be used anywhere inside the code.
      - It lives as long as the code runs and once the code ends the variable is destroyed.
      - It is created when code runs and ends when code is done.

    local variable:
    - It is created inside the function body or inside the scope 
    - It will be created during the execution of the function not when the function is created.
    - when python hits the line then it creates itself in the memory with value it calculated or hard coded just.
    - later used up by other parts of the code which has local variable usage in its code line.
    - The local variable will not be used outside the scope or function it has been declared.
    - The local variable is destroyed once the function execution ends.
    - The local variable holds the processed version of the value passed to function.
    - It will helpful to quickly compare the raw value and processed value 

    Parameter : 
    - The parameter is a placeholder variable which ensure the type of data or value that is accepted by function
    - It is created during function object creation, the variable acts as a placeholder with no value in it.
    - Later when function call is trigerred the argument passed through function call is assigned to the parameter value and then the function is executed.
    - Keeps the raw value to be resued
'''
case_rule = 'lower' # case_rule : Global variable
def clean_name(name): # name : Parameter
    cleaned = name.strip() # cleaned : Local variable 
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print('The Raw value :', name)
    print('The Processed value :', cleaned)
   
clean_name('  JoHN  ')
clean_name('Viktor   ')

