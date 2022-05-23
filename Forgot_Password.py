def forgot_pwd(username):
    for line in open("accountinfo.txt","r").readlines():
        login_info = line.split()
        if username == login_info[0]:
            password = login_info[1]
            print("Your Password is:",password)
            print("Login with this Password")

        else:
            print("No Password exists with that Username!!")
            print("Please enter Correct Username for getting the Password")
            print('<Suggestion> If you dont have account Register Yourself!!!')

def main():
    username = input("Please enter your username: ")
    forgot_pwd(username)