def SecMenu():
    while True:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(" 1. Back to menu.")
        print(" 2. Exit.")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        try:
            choice = int(input("What would you like to do? \n :"))

            match choice:
                case 1:
                    return 1

                case 2:
                    return 2

        except ValueError:
            print("Enter valid option.")

def Add(num1, num2):
     print(f"{num1} + {num2} = {num1 + num2}.")

def Sub(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}.")

def Mult(num1, num2):
    print(f"{num1} × {num2} = {num1 * num2}.")

def Div(num1, num2):
    print(f"{num1} / {num2} = {num1 / num2}")

def main():
    while True:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("︱ CLI Calculator ︱")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(" 1. Addition")
        print(" 2. Substraction")
        print(" 3. Multiplication")
        print(" 4. Division")
        print(" 5. Exit")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        try:
            choice = int(input("What would you like to do? \n :"))

            match choice:
                case 1:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Add(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 2:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Sub(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 3:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Mult(num1, num2)
                    result = SecMenu()
                    if result == 2:
                        break

                case 4:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    if num2 == 0:
                        print("Enter a Valid number!")
                        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                        num2 = int(input("Enter the second number: "))
                        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                        Div(num1, num2)
                        result = SecMenu()
                        if result == 2:
                            break
                    else:
                         print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                         Div(num1, num2)
                         result = SecMenu()
                         if result == 2:
                             break

                case 5:
                    break

        except ValueError:
               print("Enter valid option.")

if __name__ == "__main__":
    main()
