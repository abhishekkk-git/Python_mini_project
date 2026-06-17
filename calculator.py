# calculator programme

def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = input("Choose (+, -, *, /): ")

if choice == "+":
    print("Result =", add(a, b))

elif choice == "-":
    print("Result =", diff(a, b))

elif choice == "*":
    print("Result =", mult(a, b))

elif choice == "/":
    print("Result =", div(a, b))

else:
    print("Invalid Choice")
