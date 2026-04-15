''' lambda functions : 
    - In Python, a lambda is an Anonymous Function.
    - Normally, when you build a tool (a function), you give it a permanent name so you can find it later. 
    - A lambda is a tool you build on the fly, use exactly once, and then immediately throw in the trash.
    - The syntax for a lambda is strictly limited to one single line of code. It looks like this:
        Syntax : lambda arguments: expression
        Example : The lambda creates the tool, and we immediately use it by putting (5, 10) at the end.
                  result = (lambda x, y: x + y)(5, 10) --> print(result) ---> 15
    - The greatest superpower of a lambda function is it has an implicit return.    

••> How Normal function (def) vs lambda function are created in memory ??
    **When you use `def`:**
        1. Python finds a plot of land in RAM (e.g., Address `1000`).
        2. It builds the function instructions there.
        3. It creates a permanent **Name Pointer** (like `add_numbers`) and ties it to Address `1000`.
        4. Because it has a name, it lives in memory until your script completely finishes.

    **When you use `lambda`:**
        1. Python finds a plot of land in RAM (e.g., Address `5555`).
        2. It builds the function instructions there.
        3. **It does NOT create a name.** It just hands the raw address `5555` directly to whatever is asking for it (like a `map` function).
        4. As soon as that line of code finishes running, Python's Garbage Collector sees an unnamed tool sitting at Address `5555`, assumes it is trash, 
           and instantly deletes it to free up memory!      

     Quick Summary on Lambda function: 
     - Create Quick & Custom Logic  
     - one-line function
     - Assit others : map(lambdas) , filter(lambdas) , sorted(lambdas)
     - Add Dynamic and flexibility         
'''
''' why not to assign lambdas to a variable ??
   - Here variable acts as function name kind of so we can pass arguments to it.
   - Never assign a lambda to a variable in large production codebases it will break the infrastructures.
   - Its okay to assign in small and learning scripts.
   - Always use lambdas in tools like map() and filter() dont name them or else you will run into trouble when there is an error.
   - when there is an error in lambda functions it shows error in <lambda> not as function name.
   - if you surely wanna name a function create a normal function instead if any error occurs it throws error at <multiply> thing instead of <lambdas>.
   - 
'''
# variable(multiply) stores a lambda function which doubles a number.
multiply = lambda x: x * x
print(multiply(2))

# Check if a letter exsist in a string.
check =  lambda i : i in 'Python'
print(check("n"))
print(check("m"))


