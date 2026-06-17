#def add(a,b):  # add
#    return a+b

#def sub(a,b):  # sub
#    return a-b

#def mul(a,b):  # mul
#    return a*b

#def div(a,b):  # div
#    return a/b

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("Add =", add(a,b))
#print("Sub =", sub(a,b))
#print("Mul =", mul(a,b))
#print("Div =", div(a,b))

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