def Add(num1, num2):
     print(f"The Addition of {num1} and {num2} is {num1 + num2}.")

def Sub(num1, num2):
    print(f"The Substraction of {num1} and {num2} is {num1 - num2}.")

def Mult(num1, num2):
    print(f"The Multiplication of {num1} and {num2} is {num1 * num2}.")

def Div(num1, num2):
    print(f"The Division of {num1} and {num2} is {num1 / num2}")

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
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Add(num1, num2)

                case 2:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Sub(num1, num2)

                case 3:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    Mult(num1, num2)

                case 4:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    if num2 == 0:
                        print("Enter a Valid number!")
                        num2 = int(input("Enter the second number: "))
                    else:
                         Div(num1, num2)

                case 5:
                    break

        except ValueError:
               print("Enter valid option.")

if __name__ == "__main__":
    main()
