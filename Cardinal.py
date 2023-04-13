# Functions

def Login_Function():
    
    Login_V = True
        
    while Login_V == True:
            
        print("Welcome to Cardinal Python port.")
        print("There will be limited featurs due to the language.")
        print()
        print()
        print("1.Guest Login")
        print("2.Admin Login")
        print("3.Back")
        print()
            
        cin = input("Cardinal/Login/:")
        print()
            
        if cin == "guest login":
                
            Login_V = False
                
            Account_Login_F()
                
        elif cin == "admin login":
                
            Login_V = False
                
            Admin_Login_F()
                
        elif cin == "back":
                
            Login_V = False

def Account_Login_F():
    
    Account_Login_V = True
    
    while Account_Login_V == True:
        
        cinu = input("Enter the username : ")
        print()
        
        if cinu == Account_User:
            
            cinp = input("Enter the password : ")
            print()
            
            if cinp == Account_Pass:
                
                Account_Login_V = False
                
                Account_F()
                
            else:
                
                print("Error wrong password. Please try again.")
                print()
            
        else:
            
            print("Error wrong username. Please try again.")
            print()

def Admin_Login_F():
    
    Admin_Login_V = True
    
    while Admin_Login_V == True:
        
        cindu = input("Enter the username : ")
        print()
        
        if cindu == Admin_User:
            
            cindp = input("Enter the password : ")
            print()
            
            if cindp == Admin_Pass:
                
                Admin_Login_V = False
                
                Admin_Account_F()
            
            else:
                
                print("Error wrong password. Please try agin")
                print()
                
        else:
            
            print("Error wrong username. Please try again.")
            print()

def Account_F():
    
    Account_V = True
    
    while Account_V == True:
        
        print("Welcom", Account_User)
        print()
        print()
        print("1.Calculator")
        print("2.Change Username")
        print("3.Change Password")
        print("4.Logput")
        print("5.Exit")
        print()
        
        cin = input("Cardinal/Guest/:")
        print()
        
        if cin == "calculator":
            
            Account_V = False
            
            Calculator()
            
        elif cin == "change user":
            
            Account_V = False
            
            Change_User()
            
        elif cin == "chang pass":
            
            Account_V = False
            
            Change_Pass()
            
        elif cin == "logout":
            
            Admin_Account_V = False
            Account_V = False
            Commandline = True
            
        elif cin == "exit":
            
            Confirm = True
            Account_V = False
            
            while Confirm == True:
                
                print("Are you sure you want to exit.")
                print("Any altered information may reset uppon restart of program.")
                print()
            
                cin = input("Y or N : ")
                print()
            
                if cin == "Y":
                    
                    print("Exiting to command line.")
                    print()
                    
                    Commandline = False
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
                    
                elif cin == "N":
                    
                    Confirm = False
                    
                    Account_F()

def Change_User():
    
    Change_Gen_User_V = True
    
    while Change_Gen_User_V == True:
        
        cinu = input("Enter current username : ")
        print()
        
        if cinu == Account_User:
            
            cinnu = input("Enter new username : ")
            print()
            
            Confirm = True
            Change_Gen_User_V = False
            
            while Confirm == True:
                
                cin = input("Are you sure you want to continue. y/n : ")
                print()
                
                if cin == "y":
                    
                    print("Changes are commited.")
                    print("Note uppon program restart, the username will reset to : Guest.")
                    
                    global Account_New_User
                    Account_New_User = cinnu
                    
                    Confirm - False
                    Commandline = True
                    
                    Account_F()
                    
                if cin == "n":
                    
                    print("Changes were not commited.")
                    print("Exiting to command line.")
                    
                    Confirm = False
                    Commandline = True
                    
def Change_Pass():
    
    Change_Gen_Pass_V = True
    
    while Change_Gen_Pass_V == True:
        
        cinp = input("Enter current password : ")
        print()
        
        if cinp == Account_Pass:
            
            cinnp = input("Enter new password : ")
            print()
            
            Confirm = True
            Change_Gen_Pass_V = False
            
            while Confirm == True:
                
                cin = input("Are you sure you want to continue. y/n : ")
                print()
                
                if cin == "y":
                    
                    print("Changes were commited.")
                    print("Note uppon program restart, the password will reset to : Password.")
                    
                    global Account_New_Pass
                    Account_New_Pass = cinnp
                    Account_Pass = Account_New_Pass
                    
                    Confirm = False
                    Commandline = True
                    
                elif cin == "n":
                    
                    print("Changes were not commited")
                    print("Exiting to commandline")
                    
                    Confrim = False
                    Commandline = True
                    
                else:
                    
                    print("Error, please try again")
                    print()

def Switch_Users():
    
    Account = False
    Login = True

def Admin_Account_F():
    
    Admin_Account_V = True
    
    while Admin_Account_V == True:
        print("Welcome", Admin_User)
        print()
        print()
        print("1.Change Dev Username")
        print("2.Change Dev Password")
        print("3.Change Gen User")
        print("4.Change Gen Pass")
        print("5.Switch Accounts")
        print("6.Logout")
        print("7.Exit")
        print()
    
        cin = input("Cardinal/Admin/:")
        print()
    
        if cin == "change dev user":
        
            Admin_Account_V = False
        
            Change_Admin_User()
    
        elif cin == "change dev pass":
        
            Admin_Account_V = False
        
            Change_Admin_Pass()
        
        elif cin == "change gen user":
        
            Admin_Account_V = False
        
            Change_Gen_User()
        
        elif cin == "change gen pass":
        
            Admin_Account_V = False
        
            Change_Gen_Pass()
    
        elif cin == "logout":
        
            Logout()
        
        elif cin == "exit":
             
            Confirm = True
            Admin_Account_V = False
            
            while Confirm == True:
                
                print("Are you sure you want to exit.")
                print("Any altered information may reset uppon restart of program.")
                print()
            
                cin = input("Y or N : ")
                print()
            
                if cin == "Y":
                    
                    print("Exiting to commandline.")
                    print()
                    
                    Commandline = False
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
                    
                elif cin == "N":
                    
                    Confirm = False
                
                    Admin_Account_F()

def Change_Admin_User():
    print()

def Change_Admin_Pass():
    print()
    
def Change_Gen_User():
    print()

def Change_Gen_Pass():
    print()
 
def Calculator():
    print()

def Logout():
    
    Admin_Account_V = False
    Account_V = False
    Commandline = True
    
def Exit():
    
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

print()

while Commandline == True:
    
    cin = input("Cardinal/:")
    print()
    
    if cin == "login":
        
        Login_Function()
        
    elif cin == "help":
        
        print("Hello World")
        print()
        
    elif cin == "exit":
        
        Commandline = False
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