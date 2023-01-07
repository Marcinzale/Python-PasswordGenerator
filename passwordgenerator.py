import random, string
print()
password_length = int(input("How long should the password be? "))
print()
password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(password_length):
    password.append(random.choice(password_characters))

print("Your password is: " + "".join(password))

print()
print("Bye!\n")
input('Press any key to exit...')
