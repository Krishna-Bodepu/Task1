import Registration as reg
def login(username,password):
    for line in open("accountinfo.txt","r").readlines():
        login_info = line.split()
        if(username == login_info[0]):
            if(password == login_info[1]):
                print("Correct credentials!")
                print('Login Successfull')
            else:
                print('Please Enter Correct Password')
                print('<Suggestion> If you dont have account Register Yourself!!!')
        else:
            print('Please Enter Correct Email')
            print('<Suggestion> If you dont have account Register Yourself!!!')

def main():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    login(username,password)