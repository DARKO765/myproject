import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("🔐 Password Generator")

try:
    length = int(input("Enter password length: "))
    if length < 4:
        print("Password too short! (min 4)")
    else:
        print("Generated Password:", generate_password(length))
except:
    print("Please enter a valid number")
