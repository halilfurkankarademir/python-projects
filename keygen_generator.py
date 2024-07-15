##A simple Keygen Generator and Validator by Halil Furkan Karademir
##You can find keygens.txt where your project is located.
##Don't forget the star project if you liked the project :)

import string
import random
from termcolor import colored

error_message=colored("Invalid choice, please enter 1, 2, or 3.","red",attrs=['bold'])
validSuccess_message=colored("Keygen validation successfull!","green",attrs=['bold'])
validFail_message=colored("Keygen validation failed!","red",attrs=['bold'])
writedSuccess_message=colored("\nKeygens writed successfully!\n","green",attrs=['bold'])
invalidNumber_message=colored("Please enter a valid number.","red",attrs=['bold'])

def main():
    while True:
        choice=input("Welcome to the Keygen Generator!\n1.Generate Keygen\n2.Validate Keygen\n3.Exit\n")
        if choice=="1":
            keygenGenerator()
        elif choice=="2":
            keygenValidator()
        elif choice=="3":
            print("Exiting...")
            break
        else:
            print(error_message)

def keygenGenerator():
    characters=string.ascii_letters+string.digits
    keygen=""
    keygenList=[]
    while True:
        try:
            numberOfKeygens = int(input("How many keygens do you want to generate?:"))
            break
        except ValueError:
            print(invalidNumber_message)
    for i in range(numberOfKeygens):
        for j in range(16):
            randomChar=random.choice(characters)
            keygen+=randomChar
            if(j==3 or j==7 or j==11 and j!=0):
                keygen+="-" 
        keygenList.append(keygen)
        keygen=""      
        print("\n%d.keygen is: %s"%(i+1,keygenList[i]))
    choice=input("\nDo you want to write keygens into a text file? (Y/N):")
    if choice.lower()=="y":
        with open("keygens.txt","w") as f:
            for keygen in keygenList:
                f.write(keygen+"\n")
            print(writedSuccess_message)
    else:
        return False

def keygenValidator():
    keygen=input("Please type your keygen to be checked:")
    try:
        with open("keygens.txt","r") as fileToControl:
            if keygen in fileToControl.read().splitlines():
                print(validSuccess_message)
            else:
                print(validFail_message)
    except FileNotFoundError:
        print("The keygens.txt file does not exist. Please generate keygens first.")
                     
if __name__=="__main__":
    main()