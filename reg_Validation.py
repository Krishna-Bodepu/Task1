import re

def user_Validation(username):
    regex = r'\b[A-Za-z0-9]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, username)):
        return True
    else:
        return False

def pwd_Validation(password):
    specialSymbols = ['@', '$', '!', '%', '*', '#', '?', '&']
    if len(password) < 6:
        print('length should be at least 6')
        return False
    if len(password) > 16:
        print('length should be not be greater than 16')
        return False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        return False
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        return False
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        return False
    if not any(char in specialSymbols for char in password):
        print('Password should have at least one of the Special Symbols')
        return False
    else:
        return True