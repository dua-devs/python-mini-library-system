def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Please enter a number: ")


def show_menu():
    print("\n Mini Library System (V1 - Collections) : ")
    print("1) Add Book")
    print("2) List Books")
    print("3) Register Member")
    print("4) List Members")
    print("5) Borrow Book")
    print("6) Return Book")
    print("7) Search Book")
    print("8) Save & Exit")


def main():
    while True:
        show_menu()
        choice = read_int("Choose an option (1-8): ")

        if choice == 1:
            print("TODO: Add Book")
        elif choice == 2:
            print("TODO: List Books")
        elif choice == 3:
            print("TODO: Register Member")
        elif choice == 4:
            print("TODO: List Members")
        elif choice == 5:
            print("TODO: Borrow Book")
        elif choice == 6:
            print("TODO: Return Book")
        elif choice == 7:
            print("TODO: Search Book")
        elif choice == 8:
            print(" Saving... Goodbye")
            break
        else:
            print("Invalid option. Choose 1-8.")


if __name__ == "__main__":
    main()

