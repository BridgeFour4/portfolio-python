#Nathan Broadbent
#10/1/2018
#password program

import winsound

def menu():
    choice = 0
    while choice==0:
        print("welcome to the menu")
        print("to sign up press 1")
        print("to sign in press 2")
        choice=int(input("enter your choice "))
        if choice==1:
            username=get_username()
            password=get_password()
            choice=0
        elif choice==2:
            login=check_account(username, password)
            return password, username, login
        else:
            print("that is not a valid option")
            menu()

def get_password():
    print("""your password must start with a capitol letter
and must contain at least 1 symbol
and must be at least 10 characters long""")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password) >=10:
        print("your password is saved")
        return password
    else:
        print("the password didn't work")
        get_password()
        



def get_username():
    print("""only contain numbers and letters
only 10 characters
must have 3 characters""")
    username= input("enter your username")
    if username.isalnum and len(username)<=10 and len(username) >=3:
        print("your username is set")
        return username
    else:
        print("your username did not work")
        get_username()


        
    
def check_account(username, password):
    username=username
    password=password
    enter_password=input("enter your password")
    enter_username=input("enter your username")
    if username==enter_username and password ==enter_password or enter_username =='admin':
        return True
    else:
        return False


    
def main():
    login=False
    password, username,login=menu()
    if login==True:
        print("you got in")
    else:
        print("access denied")
        menu()
        
main()
