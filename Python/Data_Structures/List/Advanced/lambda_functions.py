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


''' lambda + map() :
    - In the `map()`  function we need a data transformation (a function) and a Iterable.
    - But previously we were using the built - in functions like `upper()` , `lower()` for the map function argument.
    - But what if we required a special & custom function where we need to transform to custom transformation.
    - we can use lambda functions for this types , we will be specifying what we need to do.
    - lambdas + map() will help us set up the custom data transformation.
'''
# Prices are stored as messy strings and need cleaning to floats
prices = ['$12.89', '$9.99', '$10.75']
''' 
    - with the way prices are stored in the list above we cant perform the aggregator operations we need to transform the data
    - But do we have a In-built function where we can send each item to remove the $ and convert from str type to int type. Answer is 'NO'
    - we need a custom function in order to do that we write a lambda logic first and hand it to map() to apply it for each item.
'''
# Step 1 : always try with one value considering all possible combinations
'''
   p = '$12.89'
   print(float(p.replace('$', '')))
'''

# Step 2 : If for a single value it has worked use the same logic in the lambda expression and give it to map() or filter()
# using list way to display
print(list(map(lambda p: float(p.replace('$', '')), prices)))

# using for loop way to display
for price in map(lambda p: float(p.replace('$', '')), prices):
    print(price)

