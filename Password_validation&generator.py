from random import randint
from time import sleep
import re


error = []
mistakes = 0
name = ""
new_pasw = ""
char = [ "@", "$", "_"]


def validation(pasw):
    global error
    global mistakes
    global name

    for c in pasw:
        if (c.islower()) == True:
            name += c



    if len(pasw) < 8:
        error.append("Lenght")
        mistakes += 1

    if not re.search("[a-z]", pasw):
        error.append("Alphabet")
        mistakes += 1

    if not re.search("[A-Z]", pasw):
        error.append("Upper case")
        mistakes += 1

    if not re.search("[0-9]", pasw):
        error.append("Number")
        mistakes += 1

    if not re.search("[_@$]", pasw):
        error.append("Character")
        mistakes += 1


def password_conditions():
    lenght = "Minimum 8 characters"
    alphabet = "The alphabets must be between [a-z]"
    upper = "At least one alphabet should be of Upper Case [A-Z]"
    number = "At least 1 number or digit between [0-9]"
    char = "At least 1 character from [ _ or @ or $ ]"
    if "Lenght" in error:
        print(f"\t{lenght}")
    if "Alphabet" in  error:
        print(f"\t{alphabet}")
    if "Upper case" in error:
        print(f"\t{upper}")
    if "Number" in error:
        print(f"\t{number}")
    if "Character" in error:
        print(f"\t{char}")


def password_generator():
    global new_pasw
    num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    new_pasw += name[0].upper()
    new_pasw += name[1:]
    new_pasw += char[randint(0, 2)]
    while len(new_pasw) < 8:
        new_pasw += num[randint(0, 9)]
    print(new_pasw)


print("This is a password validation program")
validation(input("Type your password: ").strip())
sleep(0.5)
if mistakes > 0:
    print(f"Your password is too weak")
    sleep(0.5)
    print(f"Mistakes:")
    password_conditions()
    while True:
        opc = input("You want a new password? ").strip().upper()
        if opc[0] == "Y":
            print("Ok the wait a second so I can make one")
            sleep(1)
            password_generator()
            break
        elif opc[0] == "N":
            print("Ok, see you later.")
            break
        else:
            print("Type your answer with YES or NO.")
else:
    print("You have a perfec password, nice work.")