''' if statement :
    Defines the first condition
    "If this is true, do this otherwise do nothing.
    Syntax : if condition1:
                do A
    Rules : 
     - Only one if
     - starts with if
     - required
     - Can be Standalone            
'''
score = 100
if score >= 90:
    print('A')

''' else Statement :
    Runs only if all previous conditions are false
    -If nothing was true,do this instead
    Syntax : if Condition1:
                do A
            else:
                do B    
    Rules : 
     - comes at end
     - No condition
     - optional
     - cannot standalone
     - only one else            
'''

score = 50 
if score >= 90:
    print('A')
else:
    print("F")    

''' elif statement :
    - Asks a follow-up question
    - Only runs if previous conditions were false
    - If the first wasn't true, try this one
    Syntax :
     if condition1:
        do A
     elif Condition2:
        do C
     else:
        do B  
    Rules :
    - Comes after if statements
    - Can use Multiple elif
    - elif needs conditions same as how if needs them
    - elif can be optional
    - elif cannot standalone
'''
score = 50
if score >= 90:
    print('A')
elif score >= 80:
    print('B')   
else:
    print("F")

''' Branching - elif elif statements  '''
score = 65
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')        
else:
    print("F")

''' Nested if 
    - If the first if block is true immediately ask second question
    - remeber each if has its own else linked up 
    - Python evaluates Boolean condition directly
    - Avoid explicit comparisons == True or == False
'''
score = 65
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:    
        print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print("F")

''' Conditions :
    - Two or more conditions are asked at a time and linked together with and , or.
    - if "and" is used between conditions then it returns True only if both are true!
    - if "or" is used between conditions then it returns True only if atleast one is true!
'''
score = 50
submitted_project = False
if score >= 90 and submitted_project:
        print("A+")
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60 or submitted_project:
    print('D')
else:
    print("F")

''' Independent Ifs :
    - Each if is checked separately
    - All conditions are tested - even if one is already true
'''
user = 'Admin'
email_status = 'banned'

if user.lower() == 'admin':
    print("Secret Vault Access Granted")
else:
    print("Secret Vault Access Revoked")
if email_status.lower() == 'verified':
    print("Welcome Admin")   
else:
    print('''
you are not allowed to access this info.
either you aren't admin or your email isn't verified.
Please contact Admin!!
          ''')    

''' Ternary if 
   - instead of writing more lines of if - else blocks  we can use Ternary if.
   - it is quick and short
   Syntax : do A if condition 1 else do B
   Rules :
     - We can't skip else must use both if and else
     - cannot use elif in this ternary if only if and else are allowed
     - The output of this inline if is stored in a variable
     - we can only use ternary if if the logic is simple
    Note : 
    Simple Logic = inline - if
    Complex Logic = classical - if  
'''
user ='Admin'
print('Acess Granted!!' if user.lower() == 'admin' else 'Acess Revoked ')

# Chanining of ternary if
score = 50
grade = 'A' if score >=90 else 'B' if score >=80 else 'C' if score >=70 else 'D' if score >=60 else 'F'
print(grade)

''' case-match
    - Evaluate a value against multiple values
    - Runs the code of the first match
    - can be used only for matching values.
'''
# Task
# Convert the full country names into 2-letter abbreviations.

''' by using if , else , elif
    - very over writing code with this conditional statements
    - need to chain methods for each statement very tidy work 
    - use this if,else,elif blocks for flexible logic and multiple conditions
    '''
country ='INDIA'

if country.lower() == 'united states' :
    print('US')
elif country.lower() == 'india':
    print('IN')    
elif country.lower() == 'germany':
    print('GE')    
elif country.lower() == 'egypt':
    print('EG')    
else:
    print('Unknown Country')    

''' Real Nightmare arrives when we have messy data to perform this matching thing, then we have to apply methods and functions to clean.
     - in if,else,elif block code we have to write for each single if and elif
     - But in case-match write once to clean up the data and use it to match things out. 
'''

''' By using case-match 
    - very simple we check for matching case and prints out 
    - no overwriting unlike how we written for if,else,elif code
    - works as switch case statements.
    - can easily chain method for data cleanup where we need to match and change things.
    - can be used only for matching values.
    - Note : used for checking matching values only 
'''
match country.lower():
    case 'united states' | 'USA': # if multiple value leads to same result we use | and chain them its like or 
        print('US')
    case 'india':
        print('IN')
    case 'egypt':
        print('EG')
    case 'germany':
        print('GE')
    case _:     # Default case use _ 
        print('unknown country')                 