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
    a = int(input("Ievadiet pirmo skaitli: "))
    b = int(input("Ievadiet otro skaitli: "))
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))