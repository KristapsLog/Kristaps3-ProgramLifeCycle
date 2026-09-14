print("Kalkulatora Izveide")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0 or x == 0:
        return "Error: Division by zero"
    return x / y

def menu():
    print("1. Saskaitīt")
    print("2. Atņemt")
    print("3. Reizināt")
    print("4. Dalīt")
    print("5. Iziet")
