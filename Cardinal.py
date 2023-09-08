# Functions

def Logout():
    
    global Account_V
    global Admin_Account_V
    global Commandline
    
    Admin_Account_V = False
    Account_V = False
    Commandline = True

def Exit():

        global Commandline
        global Login
        global Account_Login
        global Account
        global Admin_Login
        global Admin_Account
        global Admin_Confirm
        global Admin_Confirm_User
        global Admin_Confirm_Gen_User
        global Admin_Confirm_Pass
        global Admin_Confirm_Gen_Pass
        global Confirm
        global Change_Gen_User_V
        global Change_Gen_Pass_V
        global Chagne_Admin_User_V
        global Change_Admin_Pass_V
        
        Commandline = False
        Login = False
        Account_Login = False
        Account = False
        Admin_Login = False
        Admin_Account = False
        Admin_Confirm = False
        Admin_Confirm_User = False
        Admin_Confirm_Gen_User = False
        Admin_Confirm_Pass = False
        Admin_Confirm_Gen_Pass = False
        Confirm = False
        Change_Gen_User_V = False
        Change_Gen_Pass_V = False
        Chagne_Admin_User_V = False
        Change_Admin_Pass_V = False

# Switching Variables

Commandline = True
Login_V = False
Account_Login_V = False
Account_V = False
Admin_Login_V = False
Admin_Account_V = False
Admin_Confirm = False
Admin_Confirm_User = False
Admin_Confirm_Gen_User = False
Admin_Confirm_Pass = False
Admin_Confirm_Gen_Pass = False
Confirm = False
Change_Gen_User_V = False
Change_Gen_Pass_V = False
Chagne_Admin_User_V = False
Change_Admin_Pass_V = False

# Variables

cinnu = ""
cinnp = ""

# Registers

a = 0
b = 0
c = 0
x = 0
y = 0
z = 0

# Account Info

Account_User = "Guest"
Account_Pass = "Password"
Admin_User = "Admin"
Admin_Pass = "Testing"


# Body

print()

while Commandline == True:
    
    cin = input("Cardinal/ : ")
    print()

    if cin == "login":
        
        Commandline = False
        Login_V = True
        
        while Login_V == True:
            
            print()
            print("Welcome to Cardinal")
            print("The features will be limited due to being in early development.")
            print("Release version 0.00.00.000")
            print()
            print()
            print("1.Guest Login")
            print("2.Admin Login")
            print("3.Back")
            print()
            
            cin = input("Cardinal/Login/ : ")
            print()
            
            if cin == "guest login":
                
                Login_V = False
                Account_Login_V = True
                
                while Account_Login_V == True:
                    
                    cinu = input("Enter the username : ")
                    print()
                    
                    if cinu == Account_User:
                        
                        cinp = input("Enter the password : ")
                        print()
                        
                        if cinp == Account_Pass:
                            
                            Account_Login_V = False
                            Account_V = True
                            
                            while Account_V == True:
                                
                                print("hi")
                                print()
                                
                                Account_V = False
                                Login_V = True
                            
                        else:
                            
                            print("Password may be incorrect.")
                            print("Please try angain")
                            print()
                            
                            Account_Login_V == True
                    
                    else:
                        
                        print("Username may be incorrect.")
                        print("Please try again")
                        print()
                        
                        Account_Login_V == True
                        
            elif cin == "admin login":
                
                Login_V = False
                Admin_Login_V = True
                
                while Admin_Login_V == True:
                    
                    cinu = input("Enter Admin user : ")
                    print()
                    
                    if cinu == Admin_User:
                        
                        cinp = input("Enter the password : ")
                        print()
                        
                        if cinp == Admin_Pass:
                            
                            Admin_Login_V = False
                            Admin_Account_V = True
                            
                            while Admin_Account_V == True:
                                
                                print("hi")
                                print()
                                
                                Admin_Account_V = False
                                Login_V = True
                            
                        else:
                            
                            print("Login failed")
                            print("Aborting to commandline")
                            print()
                            
                            Admin_Login_V = False
                            Commandline = True
                            
                    
                    else:
                        
                        print("Admin username may be incorrect.")
                        print("Please try again")
                        print()
                        
                        Admin_Login_V = True
                        
            elif cin == "back":
                
                print("Exiting to commandline")
                print()
                
                Login_V = False
                Commandline = True
                        
    elif cin == "help":
        print()
        
    elif cin == "exit":
        
        Exit()