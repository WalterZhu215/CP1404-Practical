"""
MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

function main()
    print(MENU)
    get choice
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        else if choice == "F":
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        display (MENU)
        get choice
    print("Thank you.")

function celsius_to_fahrenheit():
    get celsius
    fahrenheit = celsius * 9.0 / 5 + 32
    display "Result: {fahrenheit:.2f} F"

def fahrenheit_to_celsius():
    get fahrenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    display "Result: {celsius:.2f} C"
"""



MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

main()