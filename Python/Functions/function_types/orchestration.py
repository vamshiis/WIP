# we receive an email from a user
# we must check if it is valid
# If it is not valid, we log the problem
# If it is valid, we clean it and store structured information
# And we log what happened

# Action Function
def write_log(message):
    with open(r'C:\Users\vamshi\Demo\app.log','a') as file:
        file.write(message+'\n')

# Validation Function
def email_validation(email):
    return '@' in email and '.' in email

# Transformation Function
def email_cleanup(email):
    cln_email = email.strip().lower()
    username,domain = cln_email.split('@')
    return {'Username' : username,
            'Domain' : domain}

# Orchestrator function
def orchestarator_fun(email):
    write_log('App started')
    write_log('Checking for validity.....')
    if not email_validation(email):
        write_log(f'Invalid Email Received : {email}')
    else:
     cleaned_email = email_cleanup(email)
    write_log(f'Valid Email and Processed email is : {cleaned_email}')
    write_log('Operation Completed')


email = input('Please enter Your Email: ')
orchestarator_fun(email)