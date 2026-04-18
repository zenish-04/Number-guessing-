import random

expected=random.randint(1,100)
print("Lets start the game!!")
while True:
    quit=input("Do you want to quit the game.(Y/N):")
    if(quit=="Y" or quit=="y"):
     break
    guess=int(input("Enter your guess between 1 to 100:"))
    if guess<expected:
        print("Your guess is low")
    elif guess>expected:
        print("Your guess is high")
    else:
        print("Congratulations You  have guessed it right:")
        break

print("-----Game over:-------")