import os
import math

# For clean

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# For asthetics

def border():
    print("╔══════════════════════╗")

def mid():
    print("╠══════════════════════╣")

def end():
    print("╚══════════════════════╝")

def line():
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

# Secondary Menus

def SecMenu():
    while True:
        border()
        print(" 1. Back to menu.")
        print(" 2. Exit.")
        end()

        try:
            choice = int(input("What would you like to do? \n :"))

            match choice:
                case 1:
                    return 1

                case 2:
                    return 2

        except ValueError:
            print("Enter valid option.")

def AdvMath():
    while True:
        clear()
        border()
        print("║    Advance Maths     ║")
        mid()
        print(" 1. Factorial")
        print(" 2. Square")
        print(" 3. Cube")
        print(" 4. Root")
        print(" 5. Log")
        print(" 6. Back/Exit")
        end()

        try:
            choice = int(input("What would you like to do? \n :"))

            match choice:
                case 1:
                    line()
                    num = int(input("Enter a number: "))
                    line()
                    while num < 0:
                        print("Factorial of negative number doesn't exit.")
                        line()
                        num = int(input("Enter a number :"))
    
                    line()
                    Factorial(num)
                    result = SecMenu()
                    if result == 2:
                        return 2


                case 2:
                    pass

                case 3:
                    pass
                
                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    pass

        except ValueError:
            print("Enter a valid option.")




# Math Func

def Add(num1, num2):
     print(f"{num1} + {num2} = {num1 + num2}.")

def Sub(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}.")

def Mult(num1, num2):
    print(f"{num1} × {num2} = {num1 * num2}.")

def Div(num1, num2):
    print(f"{num1} / {num2} = {num1 / num2}.")

# Advance Math Func

def Factorial(num):
    print(f"{num}! = {math.factorial(num)}.")

def Root(num):
    print(f"√{num} = {math.sqrt(num)}.")

def Square(num):
    num_sqr = num ** 2
    print(f"{num}² = {num_sqr}.")

def Cube(num):
    num_cube = num ** 3
    print(f"{num}³ = {num_cube}.")

def Log(num):
    print(f"Log{num} to base e = {math.log(num)}.")
    print(f"Log{num} to base 10 = {math.log10(num)}.")

# Main function

def main():
    while True:
        clear()
        border()
        print("║    CLI Calculator    ║")
        mid()
        print(" 1. Addition")
        print(" 2. Substraction")
        print(" 3. Multiplication")
        print(" 4. Division")
        print(" 5. Exit")
        end()

        try:
            choice = int(input("What would you like to do? \n :"))

            match choice:
                case 1:
                    line()
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    line()
                    Add(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 2:
                    line()
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    line()
                    Sub(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 3:
                    line()
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    line()
                    Mult(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 4:
                    line()
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    line()
                    if num2 == 0:
                        print("Can't divide by zero, Enter a Valid number!")
                        line()
                        num2 = int(input("Enter the second number: "))
                        line()
                        Div(num1, num2)
                        result = SecMenu()
                        if result == 2:
                            break
                    else:
                         line()
                         Div(num1, num2)
                         result = SecMenu()
                         if result == 2:
                             break

                case 5:
                    border()
                    print("║  Thanks for using    ║")
                    print("║   CLI Calculator.    ║")
                    end()

                    break

        except ValueError:
               print("Enter a valid option.")

if __name__ == "__main__":
    main()
