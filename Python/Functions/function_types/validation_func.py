# Task : Check if the password is valid

def valid_password(password):
    return len(password) >= 8
print(valid_password('123456'))
print(valid_password('12345678'))

# Task : Check if email has basic valid format
def is_valid_email(email):
    return '@' in email and '.' in email
print(is_valid_email('saragmail'))
print(is_valid_email('sara@gmailcom'))
print(is_valid_email('sara@gmail.com'))