# Switching Variables

Commandline = True
Login = False
Account_Login = False
Account = False
Dev_Login = False
Dev_Account = False
Dev_Comfirm = False
Dev_Confirm_User = False
Dev_Confirm_Pass = False

# Account Info

Account_User = "Person"
Account_Pass = "Password"
Dev_User = "JY48572"
Dev_Pass = "11323535892207jY"

print()

while Commandline == True:

    cin = input("Cardinal/: ")
    print()

    if cin == "login":

        Commandline = False
        Login = True

        while Login == True:
        
            print("Welcome to Cardinal")
            print("This is the python port, so there is going to be fewer fetures")
            print()
            print()
            print("1.Login")
            print("2.Dev Login")
            print("3.Back")
            print()

            cin = input("Cardinal/Login/: ")
            print()

            if cin == "login":
            
                Login = False
                Account_Login = True
                
                print()

                while Account_Login == True:
            
                    cinu = input("Enter the username : ")
                    print()

                    if cinu == Account_User:

                        cinp = input("Enter the password : ")
                        print()

                        if cinp == Account_Pass:

                            Account_Login = False
                            Account = True
                
                            while Account == True:
                  
                                print("Welcome", Account_User)
                                print()
                                print()
                                print("1.Change Username")
                                print("2.Change Password")
                                print("3.Switch Users")
                                print("4.Logout")
                                print("5.Log Off")
                                print()

                                cin = input("Cardinal/User/: ")
                                print()

                                if cin == "change users":
                      
                                    cinu = input("Enter current username : ")
                                    print()

                                    if cinu == Account_User:

                                        cinnu = input("Enter new username : ")
                                        print()

                                        Account_User = cinnu
                                        print("Username has been changed")
                                        print()
                                        print("Please note that the new username is temporary.")
                                        print("It will default to Person uppon Restart of Cardinal")
                                        print()

                                        Account = True

                                elif cin == "change pass":

                                    cinp = input("Enter current password : ")
                                    print()

                                    if cinp == Account_Pass:

                                        cinnp = input("Enter new password : ")
                                        print()

                                        Account_Pass = cinnp
                                        print("Password has been changed")
                                        print()
                                        print("Please not that the new password is temporary.")
                                        print("It will default to Password uppon restart of Cardinal")
                                        print()

                                        Account = True

                                elif cin == "switch user":

                                    Account = False
                                    Login = True

                                elif cin == "logout":

                                    Account = False
                                    Commandline = True

                                elif cin == "log off":

                                    print("Cardinal is closing.")
                                    print()
                                    print("Good Bye")
                                    print()
                                    Commandline = False
                                    Login = False
                                    Account = False
                                    Dev_Login = False

                                else:

                                    print("Choice not availiable. Please try again")
                                    print()
                  
                  
                        else:
                            
                            print("Error wrong password. Please try again.")
                            print()
                            
                            Account_Login = True

                    else:
                        
                        print("Error wrong username. Please try again.")
                        print()
                        
                        Account_Login = True

            elif cin == "dev login":

                Login = False
                Dev_Login = True

                while Dev_Login == True:

                    cindu = input("Enter dev username : ")
                    print()

                    if cindu == Dev_User:

                        cindp = input("Enter dev password : ")
                        print()

                        if cindp == Dev_Pass:
              
                            Dev_Login = False
                            Dev_Account = True

                            while Dev_Account == True:

                                print("Welcome", Dev_User)
                                print("How may I assit you today")
                                print()
                                print()
                                print("1.Change Dev Username")
                                print("2.Change Dev Password")
                                print("3.Change General Username")
                                print("4.Change General Password")
                                print("5.Switch Accounts")
                                print("6.Logout")
                                print("7.Log Off")
                                print()

                                cin = input("Cardinal/Dev/User/: ")
                                print()

                                if cin == "change dev user":

                                    Dev_Account = False

                                    cindu = input("Enter current dev username : ")
                                    print()

                                    if cindu == Dev_User:

                                        cinndu = input("Enter new username : ")
                                        print()

                                        print()
                                        print("WARNING!!")
                                        print()
                                        print("Note that this new username is temporary.")
                                        print("It will default to JY48572 uppon restart")
                                        print()

                                        Dev_Confirm = True

                                        while Dev_Confirm == True:

                                            Dev_Confirm_User = True

                                            while Dev_Confirm_User == True:

                                                Dev_Confirm = False

                                                cin = input("Are you sure you want to continue Y/N : ")
                                                print()
                    
                                                if cin == "Y":

                                                    Dev_User = cinndu

                                                    print("New username saved")
                                                    print()

                                                    Dev_Confirm_User = False
                                                    Dev_Account = True

                                                elif cin == "N":

                                                    Dev_User = Dev_User

                                                    print("New username not saved")
                                                    print()
                                                    print("Aborting")
                                                    print()

                                                    Dev_Confirm_User = False
                                                    Dev_Account = True

                                                else:

                                                    print("Error, please try again")
                                                    print()

                                                    Dev_Confirm_User = True

                                elif cin == "change dev pass":

                                    Dev_Account = False

                                    cindp = input("Enter current dav password : ")
                                    print()

                                    if cindp == Dev_Pass:

                                        cinndp = input("Enter new dev password : ")
                                        print()

                                        print()
                                        print("WARNING!!")
                                        print()
                                        print("Note that this new password is temporary")
                                        print("It will default to 11323535892207jY uppon restart")
                                        print()

                                        Dev_Confirm = True

                                        while Dev_Confirm == True:

                                            Dev_Confirm_Pass = True

                                            while Dev_Confirm_Pass == True:

                                                Dev_Confirm = False

                                                cin = input("Are you sure you want to continue Y/N : ")
                                                print()

                                                if cin == "Y":

                                                    Dev_Pass = cinndp

                                                    print("New username saved")
                                                    print()

                                                    Dev_Confirm_Pass = False
                                                    Dev_Account = True

                              elif cin == "N":

                                print("New username not saved")
                                print()
                                print("Aborting")
                                print()

                                Dev_Confirm_Pass = False
                                Dev_Account = True

                              else:

                                print("Error please try again")
                                print()

                                Dev_Confirm_Pass = True

                      elif cin == "change gen user":

                        Dev_Account = False

                        cinnu = input("Enter new general username : ")
                        print()

                  

                      elif cin == "logout":

                        Dev_Account = False
                        Commandline = True

                      elif cin == "log off":

                        print("Cardinal is closing")
                        print()
                        print("Good Bye")
                        print()

                    Commandline = False
                    Login = False
                    Account_Login = False
                    Account = False
                    Dev_Login = False
                    Dev_Account = False
                    Dev_Comfirm = False
                    Dev_Confirm_User = False
                    Dev_Confirm_Pass = False
                  
                  else:

                    print("Error wrong dev password. Please try again.")
                    print()
                    print("Exiting to login.")
                    print()

                    Dev_Login = False
                    Login = True
            
                else:

                  print("Error wrong dev userneame. PLease try again.")
                  print()
                  print("Exiting to login.")
                  print()

                  Dev_Login = False
                  Login = True

            elif cin == "back":

              print("Exiting to commandline.")
              print()
                
              Login = False
              Commandline = True

            else:

              print("Choice not availiable. Please try again")
              print()
                
              login = False
              Commandline = True

        else:

          print("Command not availiable. Please try again")
          print()
        
          Commandline = True
