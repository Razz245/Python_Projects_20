# 🧮 Basic Calculator Program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero not allowed!"

print("=== Basic Calculator ===")
print("Operations: +, -, *, /")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operator == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operator == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operator == '/':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("❌ Invalid operator!")
