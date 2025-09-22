"""
function main()
    get name

    function display_menu()
        display "(H)ello"
        display "(G)oodbye"
        display "(Q)uit"

    display_menu()
    choice = input(">>> ")

    while choice != "Q":
        if choice == "H":
            display "Hello {name}"
        else if choice == "G":
            display "Goodbye {name}"
        else:
            display "Invalid choice"

        display_menu()
        choice = input(">>> ").upper()

    display "Finished."
"""

def main():
    name = input("Enter name: ")

    def display_menu():
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

        display_menu()
        choice = input(">>> ").upper()

    print("Finished.")

main()