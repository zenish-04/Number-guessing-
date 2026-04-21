import math
print("Welcome to the 2 number calculator!")
print("****Menu****")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")
print("10. Log base 10")
print("11. Log base e")
print("12. Log base 2")
print("13. Quit")

choice = int(input("Enter your choice: "))

while True:
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", num1 / num2)
    elif choice == 5:
        print("Enter the number to find the square root:")
        num = float(input())
        print("Square root of", num, "is", math.sqrt(num))
    elif choice == 6:
        print("Enter the base number:")
        base = float(input())
        print("Enter the exponent:")
        exponent = float(input())
        print(base, "raised to the power of", exponent, "is", math.pow(base, exponent))
    elif choice == 7:
        print("Enter the angle in degrees:")
        angle = float(input())
        print("Sine of", angle, "is", math.sin(math.radians(angle)))
    elif choice == 8:
        print("Enter the angle in degrees:")
        angle = float(input())
        print("Cosine of", angle, "is", math.cos(math.radians(angle)))
    elif choice == 9:
        print("Enter the angle in degrees:")
        angle = float(input())
        print("Tangent of", angle, "is", math.tan(math.radians(angle)))
    elif choice == 10:
        print("Enter the number to find the log base 10:")
        num=float(input())
        print("Log base 10 of ",num,"is ",math.log10(num))
    elif choice == 11:
        print("Enter the number to find the log base e:")
        num=float(input())
        print("Log base e of ",num,"is ",math.log(num))
    elif choice == 12:
        print("Enter the number to find the log base 2:")
        num=float(input())
        print("Log base 2 of ",num,"is ",math.log2(num))
    elif choice == 13:
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice")
    
    choice = int(input("Enter your choice: "))


