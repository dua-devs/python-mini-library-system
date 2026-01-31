books = []  # list of dicts (each dict represents one book)
members = []  # list of dicts (each dict represents one member)

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

def add_book():
    book_id = read_int("Enter book id: ")
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "is_available": True
    }

    books.append(book)
    print("Book added successfully!")

    
def list_books():
    if len(books) == 0:
        print("No books found.")
        return

    print("\n--- Books List ---")
    for b in books:
        status = "Available" if b["is_available"] else "Borrowed"
        print(f'ID: {b["book_id"]} | Title: {b["title"]} | Author: {b["author"]} | Status: {status}')

def register_member():
    member_id = read_int("Enter member id: ")
    name = input("Enter member name: ").strip()

    member = {
        "member_id": member_id,
        "name": name
    }

    members.append(member)
    print("Member registered successfully!")

def list_members():
    if len(members) == 0:
        print("No members found.")
        return

    print("\n--- Members List ---")
    for m in members:
        print(f'ID: {m["member_id"]} | Name: {m["name"]}')


def main():
    while True:
        show_menu()
        choice = read_int("Choose an option (1-8): ")

        if choice == 1:
            add_book()
        elif choice == 2:
            list_books()
        elif choice == 3:
            register_member()
        elif choice == 4:
            list_members()
        elif choice == 5:
            print("TODO: Borrow Book")
        elif choice == 6:
            print("TODO: Return Book")
        elif choice == 7:
            print("TODO: Search Book")
        elif choice == 8:
            print("Saving... Goodbye")
            break
        else:
            print("Invalid option. Choose 1-8.")


if __name__ == "__main__":
    main()

