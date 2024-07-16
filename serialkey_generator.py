##A simple Serial Key Generator and Validator by Halil Furkan Karademir
##You can find serialkeys.txt where your project is located.
##Don't forget the star project if you liked the project :)

import string
import random
from termcolor import colored

error_message=colored("Invalid choice, please enter 1, 2, or 3.","red",attrs=['bold'])
validSuccess_message=colored("Key validation successfull!","green",attrs=['bold'])
validFail_message=colored("Key validation failed!","red",attrs=['bold'])
writedSuccess_message=colored("\nKeys writed successfully!\n","green",attrs=['bold'])
invalidNumber_message=colored("Please enter a valid number.","red",attrs=['bold'])

def main():
    while True:
        choice=input("Welcome to the Serial Key Generator!\n1.Generate Key\n2.Validate Key\n3.Exit\n")
        if choice=="1":
            keyGenerator()
        elif choice=="2":
            keyValidator()
        elif choice=="3":
            print("Exiting...")
            break
        else:
            print(error_message)

def keyGenerator():
    characters=string.ascii_letters+string.digits
    key=""
    keyList=[]
    while True:
        try:
            numberOfKeys = int(input("How many keys do you want to generate?:"))
            break
        except ValueError:
            print(invalidNumber_message)
    for i in range(numberOfKeys):
        for j in range(16):
            randomChar=random.choice(characters)
            key+=randomChar
            if(j==3 or j==7 or j==11 and j!=0):
                key+="-" 
        keyList.append(key)
        key=""      
        print("\n%d.key is: %s"%(i+1,keyList[i]))
    choice=input("\nDo you want to write keys into a text file? (Y/N):")
    if choice.lower()=="y":
        with open("serialkeys.txt","w") as f:
            for key in keyList:
                f.write(key+"\n")
            print(writedSuccess_message)
    else:
        return False

def keyValidator():
    key=input("Please type your key to be checked:")
    try:
        with open("serialkeys.txt","r") as fileToControl:
            if key in fileToControl.read().splitlines():
                print(validSuccess_message)
            else:
                print(validFail_message)
    except FileNotFoundError:
        print("The serialkeys.txt file does not exist. Please generate keys first.")
                     
if __name__=="__main__":
    main()