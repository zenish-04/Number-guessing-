import random
expected=random.randit(1,100)
print("Welcome to the number guessing game!")
print("Enter 'Q' or 'q' to quit the game at any time.")
while True:
    attempt=0
    guess=input("Enter your guess number between 1 and 100:")
    if guess.lower()=='q':
        print("Thanks for playing! Have a great day!")
        break
    if not guess.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    guess=int(guess)
    if guess<1 or guess>100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    attempt=attempt+1
    if guess<expected:
        print("Too low! Try again.")
    elif guess>expected:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in ",attempt,"attempts!")
        break
print("The expected number was:",expected)
print("Game over. Thanks for playing!")