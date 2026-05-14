''' return :
    -  return keyword is used to send the result back to the function call
    - by default if there is no return in function it returns 'None' to the function call
    - we use return in order to store the result of function in variable and use it up later in the actual code
    - we can use multiple return statements inside the function
'''
def cleanup(name):
    cleaned = name.strip().lower()
    return cleaned
cln_name = cleanup(' JoHnnY  ')


# With no return it still returns None to function call
# We used if else so any of one will be executed and only one return will work in this case
def cleanup(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
    return cleaned
    
cln_name = cleanup(' JoHnnY  ')


# We can return multiple values separated by commas
# If multiple values are returned from a fucntion it returns them as "Tuple"
def cleanup(name):
    lower_cleaned = name.strip().lower()
    upper_cleaned = name.strip().upper()
    return lower_cleaned,upper_cleaned
cln_name = cleanup(' JoHnnY  ')
print(cln_name)
print(type(cln_name)) #Tuple -> as its tuple we can unpack them instantly just 
lower_name,upper_name = cleanup('  VaMsHIII   ')
print(lower_name)
print(upper_name)


