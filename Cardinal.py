# Functions
def Switch_Users():
    
    global Account_V
    global Admin_Account_V
    global Commandline
    
    Account_V = False
    Admin_Account_V = False
    Commandline = True

def Calculator():
    print()

def Logout():
    
    global Account_V
    global Admin_Account_V
    global Commandline
    
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

while Commandline == True:
    
    cin = input("Cardinal/:")
    print()

    if cin == "login":
        print()
        
    elif cin == "help":
        print()
        
    elif cin == "exit":
        
        Exit()