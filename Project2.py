import random
import string
password_length=int(input("Enter the length of pasword you want to generate:"))
randomword=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(password_length):
    password+=random.choice(randomword)
print("Your generated password is:", password)

