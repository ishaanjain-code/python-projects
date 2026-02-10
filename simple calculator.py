def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y): 
    return x*y 
def divide(x, y):
    return x/y
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
operation=input("Choose operation (+, -, *, /): ")
if operation=='+':
    print(f"{a} + {b} = {add(a, b)}")
elif operation=='-':
    print(f"{a} - {b} = {subtract(a, b)}")
elif operation=='*':
    print(f"{a} * {b} = {multiply(a, b)}")
elif operation=='/':
    print(f"{a} / {b} = {divide(a, b)}")