import reg_Validation as validation
import Write_To_File as fileWriting

def email_val(username):
    email_valid = validation.user_Validation(username)
    if (email_valid):
        print('Valid Email')
    else:
        print('Invalid Email')
        username = input('Enter the Valid Email: ')
        email_val(username)

def pwd_val(password):
    pwd_valid = validation.pwd_Validation(password)
    if (pwd_valid):
        print("Password is valid")
    else:
        print("Invalid Password !!")
        password = input('Enter Password Again: ')
        pwd_val(password)

def main():
    username = input('Enter the Username: ')
    email_val(username)
    password = input('Enter the Password: ')
    pwd_val(password)
    print('Registration Successfull!!')
    fileWriting.write_file(username,password)
