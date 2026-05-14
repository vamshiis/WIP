# Task : Clean an email and split it into username and domain

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username,domain = cl_email.split('@')
    return {'Username' : username,
            'Domain' : domain}
print(clean_and_split_email('    VoMsHiIi@GmAiL.CoM    '))