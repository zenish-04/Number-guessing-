import random


print("Welcome the dice rolling game !!")
while True:
    print("Enter 'r' to roll the dice")
    a=input()
    if(a=="r" or a=="R"):
        number=random.randint(1,6)
        print("You got: ",number)
        print("Do you want to roll again?(Y?N)")
        again=input()
        if(again=="y"or again=="Y"):
            continue
    else:
        break
print("_____Game over_____")