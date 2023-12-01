import os

def delete():
    try:
        while True:
            userinput=int(input("Enter Which operation youe want to do: \n 1. List all User \n 2. To Delete User-Name \n 3. Exit \n Enter the Value: "))

            if userinput == 1:
                user= os.system("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/{print $1}' /etc/passwd")
                print (user)
            elif userinput == 2:
                userdel = input("Enter the Username You Want to delete: ")
                creat = os.system(f"sudo userdel {userdel}" )   
                print(f"Selected User: {userdel} is deleted ☠ ")
            elif userinput == 3:
                print("You Have Exited !!!!")
                break
            else:
                print("enter Proper Value!!! ")
       
    except OSError as error : 
        print(error) 
        print("File descriptor is not associated with any terminal device") 
