class Library:
    def __init__(self):
        self.books = {
            "The Alchemist": True,
            "Harry Potter": True,
            "Atomic Habits": True,
            "Clean Code": True,
            "Deep Work": True
        }

    def display_books(self):
        print("\nAvailable Books:")
        for book, status in self.books.items():
            if status == True:
                status_text = "Available"
            else:
                status_text = "Borrowed"
            print(f" - {book} [{status_text}]")

    def borrow_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] == True:
                self.books[book_name] = False
                print(f"\nYou have successfully borrowed '{book_name}'.")
            else:
                print(f"\nSorry, '{book_name}' is currently borrowed by someone else.")
        else:
            print(f"\nSorry, the book '{book_name}' does not exist in the library.")

    def return_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] == False:
                self.books[book_name] = True
                print(f"\nThank you for returning '{book_name}'.")
            else:
                print(f"\nThe book '{book_name}' was not borrowed.")
        else:
            print(f"\nThe book '{book_name}' does not belong to this library.")

    def add_book(self, book_name):
        if book_name in self.books:
            print(f"\nThe book '{book_name}' already exists in the library.")
        else:
            self.books[book_name] = True
            print(f"\nThe book '{book_name}' has been added to the library.")

def main():
    print('Welcome to EXL library management ')
    library = Library()
    while True:
        print("\n===== Library Menu =====")
        print("Choose an option:")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book = input("Enter the name of the book : ")
            library.borrow_book(book)
        elif choice == '3':
            book = input("Enter the name of the book : ")
            library.return_book(book)
        elif choice == '4':
            book = input("Enter the name of the book : ")
            library.add_book(book)
        elif choice == '5':
            print("\nExiting Library System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()