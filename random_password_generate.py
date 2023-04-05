# ask user is they want to generate a password ot not
# if yes, ask for password lenth
# Genarate password
# print password
# if answer is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + string.hexdigits + string.octdigits +"!@#$%^&*(){}[]:<>?,./")

def generate_password():
    password_length = int(input("How long would you like your password to be ? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)
    
option = input("Do you want to generate a password ? ")

if option == "Yes" or option == "yes":
    generate_password()
elif option == "No" or option == "no":
    print("Program Ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()