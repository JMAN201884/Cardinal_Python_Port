# Functions

def Login_F():
    print("Hello World")
    print()
    
def Account_Login_F():
    print()
    
def Admin_Login_F():
    print()

def Account_F():
    print()
    
def Change_User():
    print()
    
def Change_Pass():
    print()
    
def Switch_Users():
    
    Account = False
    Login = True

def Logout():
    
    Account = False
    Commandline = True
    
def Admin_Account_F():
    print()

def Change_Dev_User():
    print()
    
def Change_Dev_Pass():
    print()
    
def Change_Gen_User():
    print()
    
def Change_Gen_Pass():
    print()
    
def Logout_Admin():
    
    Admin_Account = False
    Commandline = True
    
def Exit():
    
    Commandline = True
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

# Switching Variables

Commandline = True
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

# Variables

a_number = 0
b_number = 0
c_number = 0
x_number = 0
y_number = 0
z_number = 0

# Account Info

Account_User = "Person"
Account_Pass = "Password"
Admin_User = "Admin"
Admin_Pass = "Testing"

print()

while Commandline == True:
    
    cin = input("Cardinal/:")
    print()
    
    if cin == "login":
        
        Login = True
        
        Login_F()
        
    elif cin == "help":
        
        print("Hello World")
        print()
        
    elif cin == "exit":
        
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