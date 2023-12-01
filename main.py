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





















"""
import qrcode
img = qrcode.make()
type(img)  
img.save("Saurabh Jain-QR.png")

# animated_qrcode.py


import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://github.com/Saurabh234567/python")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)
save("animated_qrcode.gif")
"""