import book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, publish_year):
        new_book = book.Book(title, author, genre, publish_year)
        self.books.append(new_book)
        print(f"Book '{title}' has been added to the library with ISBN: {new_book.isbn}.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                break

        print("Book not found.")

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"Books found with title '{title}':")
            for book in results:
                print(book)
        else:
            print(f"No books found with title '{title}'.")

    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        if results:
            print(f"Books by {author}:")
            for book in results:
                print(book)
        else:
            print(f"No books found by {author}.")

    def filter_by_genre(self, genre):
        results = [book for book in self.books if genre.lower() == book.genre.lower()]
        if results:
            print(f"Books in the genre '{genre}':")
            for book in results:
                print(book)
        else:
            print(f"No books found in the genre '{genre}'.")

    def filter_by_year(self, start_year, end_year):
        results = [book for book in self.books if start_year <= book.publish_year <= end_year]
        if results:
            print(f"Books published between {start_year} and {end_year}:")
            for book in results:
                print(book)
        else:
            print(f"No books found from {start_year} to {end_year}.")

    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def borrow_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                book.borrow(borrower)
                break
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                break
        print("Book not found.")

    def user_panel(self, user_name):
        while True:
            print(f"Welcome to the library, {user_name}!")
            print("""
               1. List all books
               2. Search by title
               3. Search by author
               4. Filter by genre
               5. Filter by year
               6. Borrow a book
               7. Return a book
               8. Exit
               """)

            choice = input("Select an option: ")

            if choice == "1":
                self.list_books()
            elif choice == "2":
                title = input("Enter the title to search: ")
                self.search_by_title(title)
            elif choice == "3":
                author = input("Enter the author to search: ")
                self.search_by_author(author)
            elif choice == "4":
                genre = input("Enter the genre to filter by: ")
                self.filter_by_genre(genre)
            elif choice == "5":
                try:
                    start_year = int(input("Enter the start year: "))
                    end_year = int(input("Enter the end year: "))
                    self.filter_by_year(start_year, end_year)
                except Exception as e:
                    print("Hata: ", e)
            elif choice == "6":
                isbn = input("Enter the ISBN of the book you want to borrow: ")
                self.borrow_book(isbn, user_name)
            elif choice == "7":
                isbn = input("Enter the ISBN of the book you want to return: ")
                self.return_book(isbn)
            elif choice == "8":
                print(f"Goodbye, {user_name}!")
                break
            else:
                print("Invalid option. Please try again.")
