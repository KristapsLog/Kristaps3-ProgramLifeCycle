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

def main():
    print(add(5, 3))        # Output: 8
    print(subtract(5, 3))   # Output: 2
    print(multiply(5, 3))   # Output: 15
    print(divide(5, 0))     # Output: Error: Division by zero