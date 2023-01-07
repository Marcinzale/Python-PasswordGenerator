import random, string
import pyperclip

print()
password_length = int(input("How long should the password be? "))
print()
password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(password_length):
    password.append(random.choice(password_characters))

password = "".join(password)

print("Your password is: " + "".join(password) + "\n")

answer = str.lower(input("Copy password to clipboard? Yes (y) or not (n): "))
if answer == 'y':
    pyperclip.copy(password)
    print("Password copied to system clipboard\n")
    
else:
    print()
    print("Bye!\n")
    
input("Press any key to exit...\n\n")




