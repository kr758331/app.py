import random

print("Your Password: ")

char = "abcdefghijklmnopqrstuvwxyz1234567890#!@$%^&()*?"

password = ''

for x in range (16):
    password += random.choice(char)

    print(password)