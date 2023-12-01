import os
def list():
    try:
        user= os.system("awk -F: '$NF!~/\/false$/ && $NF!~/\/nologin$/{print $1}' /etc/passwd")
        print ("Following is the List of All Active User in system",user)
    except OSError as error : 
        print(error) 
        print("File descriptor is not associated with any terminal device") 
