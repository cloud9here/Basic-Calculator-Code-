import math

def calculator(num1, num2, operation):
    operation = operation.lower()  # Make operation case-insensitive

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    elif operation == "modulus":
        return num1 % num2
    elif operation == "power":
        return num1 ** num2
    elif operation == "sqrt":
        if num1 < 0:
            return "Error: Square root of a negative number is undefined for real numbers."
        return math.sqrt(num1)
    elif operation == "log":
        if num1 <= 0:
            return "Error: Logarithm is undefined for zero or negative numbers."
        return math.log(num1)
    else:
        return f"Invalid operation: {operation}. Please use one of these: add, subtract, multiply, divide, modulus, power, sqrt, log."

# User Input
print("Welcome to the Calculator!")
print("Available operations: add, subtract, multiply, divide, modulus, power, sqrt, log")

while True:
    operation = input("Enter the operation you want to perform (or type 'exit' to quit): ").strip()
    if operation.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    if operation.lower() in ["add", "subtract", "multiply", "divide", "modulus", "power"]:
        num2 = float(input("Enter the second number: "))
    else:
        num2 = 0  # Second number is not usually need for sqrt or log

    result = calculator(num1, num2, operation)
    print(f"The result of {operation} is: {result}\n")
