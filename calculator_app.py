# The Calculator App
#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def addition(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x/y

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
def calculator():
    operation = input("What operation do you want to use? (+, -, *, /): ")
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))

    if operation == "+":
        return addition(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        if num2 != 0:
            return divide(num1, num2)
    else:
        return "Invalid operation"



# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def calculator():
    operation = input("What operation do you want to use? (+, -, *, /): ")
    num1 = float(input("What is the first number? "))
    num2 = float(input("Enter the second number: "))

    if operation == "+":
        return addition(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return  divide(num1, num2)
    else:
        return "Invalid operation"
    

