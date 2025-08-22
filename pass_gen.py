import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.printable
    password=""
    for _ in range(length):
        password += random.choice(chars)
    return password

print("Welcome to password generator")
leng = int(input("Enter the password length (default is 12)")or 12)
password = generate_password(leng)
print(f"Your generated password is:{password}")