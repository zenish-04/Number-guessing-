import random

expected=random.randint(1,100)
print("Lets start the game!!")
while True:
 if(quit=="Y" or quit=="y"):
    print("You have quit the game")
    break
 while True:
    guess=int(input("Enter your guess between 1 to 100:"))
    if guess<expected:
        print("Your guess is low")
    elif guess>expected:
        print("Your guess is high")
    else:
        print("Congratulations You  have guessed it right:")
        break

print("-----Game over:-------")