import os
from Delete import delete
from create import create
from list import list

try:
    while True:
        userinput=int(input("Enter Which operation youe want to do:\n 1. List All UserName \n 2. Create New User-Name \n 3. Delete A Username \n 4. Exit The Program \n Enter your Value: "))

        if userinput == 1:
            print (list())
        elif userinput == 2:
            print (create())
        elif userinput == 3:
            print (delete())
        elif userinput == 4:
            print("GoodBye Adios ❅ ")
            break
        else:
            print("enter Proper Value!!! ")
except KeyboardInterrupt :
    print("\n Code Exited From Backdoor Secrectly o_o")





















