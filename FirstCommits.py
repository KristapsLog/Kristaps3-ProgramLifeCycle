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

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli!")

def main():
    while True:
        menu()
        choice = input("Izvēle: ")
        if choice == "5":
            break
        if choice == "1":
            a = get_number("Pirmais skaitlis: ")
            b = get_number("Otrais skaitlis: ")
            print("Rezultāts:", add(a, b))
        elif choice == "2":
            a = get_number("Pirmais skaitlis: ")
            b = get_number("Otrais skaitlis: ")
            print("Rezultāts:", subtract(a, b))
        elif choice == "3":
            a = get_number("Pirmais skaitlis: ")
            b = get_number("Otrais skaitlis: ")
            print("Rezultāts:", multiply(a, b))
        elif choice == "4":
            a = float(input("Pirmais skaitlis: "))
            b = float(input("Otrais skaitlis: "))
            print("Rezultāts:", divide(a, b))

main()