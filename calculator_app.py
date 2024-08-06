#Defining the functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2
        
def calculator():
    while True:
        print("Calculator App")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("What operation would you like to perform? (1, 2, 3, 4, or 5) ")

        if choice == "5":
            print("Goodbye!")
            break

        elif choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid choice. Please try again.")

# Call the calculator function
calculator() 
