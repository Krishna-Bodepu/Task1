import Registration as reg
import Login as log
import Forgot_Password as f_pwd

def main():
    print('1. Register')
    print('2. Login')
    print('3. Forgot Password')
    option = input('Enter any above options above: ')
    if(option == '1'):
        reg.main()
        main()
    elif(option == '2'):
        log.main()
        main()
    elif(option == '3'):
        f_pwd.main()
        main()
    else:
        print('Invalid Option')
        main()

if __name__ == '__main__':
    main()