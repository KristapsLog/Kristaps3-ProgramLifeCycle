print("Kalkulatora Izveide")

history = []

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

def power(x, y):
    return x ** y

def menu():
    print("1. Saskaitīt")
    print("2. Atņemt")
    print("3. Reizināt")
    print("4. Dalīt")
    print("5. Kāpināt")
    print("6. Iziet")

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
        if choice == "6":
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
            a = get_number("Pirmais skaitlis: ")
            b = get_number("Otrais skaitlis: ")
            print("Rezultāts:", divide(a, b))
        elif choice == "5":
            a = get_number("Pamats: ")
            b = get_number("Kāpinātājs: ")
            print("Rezultāts:", power(a, b))
        else:
            print("Nepareiza izvēle, mēģini vēlreiz!")
main()