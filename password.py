##A password generator using python

import string
import random

chars= string.ascii_letters+string.digits+'.'+'!'+'%'+'&'+'#'

def PasswordGenerator():
    while True:
        length=int(input("Enter password length to generate:"))
        password=""
        for i in range(length):
            randomChar=random.choice(chars)
            password+=randomChar
        print("Password is:%s"%(password))
        choice=input("Do you want to save it in txt file? (Y/N):\n")
        
        if choice.lower()=="y":
            name=input("Type password name:")
            saveFile(password,name)
        else:
            return False
    
def saveFile(password,name):
    with open("passwords.txt","a") as file1:
        file1.write(f"Name: {name} Password: {password}\n")
        print("Password saved.")
PasswordGenerator()    
