import os
def create():
    try:
        while True:
            userinput=int(input("Enter Which operation youe want to do: \n 1. List all User \n 2. To add New-User \n 3. Create User With credential \n 4. Exit \n Enter the Value: "))

            if userinput == 1:
                user= os.system("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/{print $1}' /etc/passwd")
                print (user)
            elif userinput == 2:
                useradd = input("Enter the Username You Want to add: ")
                creat = os.system(f"sudo useradd {useradd}" )  
                return "User Created ✌"
            elif  userinput == 3:
                useraddCre = input("Enter the Username You Want to add: ")
                cced = os.system(f"sudo adduser {useraddCre}" )  
                return "User Created ✌"
            elif userinput == 4:
                print("You Have Exited !!!! 🤟")
                break
            else:
                print("enter Proper Value!!! ")
       
    except OSError as error : 
        print(error) 
        print("File descriptor is not associated with any terminal device") 