import random
import time

class Book:
    def __init__(self,title,author,genre,publish_year,isbn=None,available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publish_year = publish_year
        self.isbn = isbn if isbn else str(random.randint(100,1000))
        self.available = available
        self.borrower = None
        self.borrowed_time = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower} (since {self.borrowed_time})"
        return f"'{self.title}' by {self.author} ({self.genre}, {self.publish_year}) - {status} - ISBN: {self.isbn}"

    def borrow(self,borrower):
        if self.available:
            self.available = False
            self.borrower = borrower
            self.borrowed_time =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"{borrower} has borrowed '{self.title}' at {self.borrowed_time}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed by {self.borrower}.")

    def return_book(self):
        if not self.available:
            print(f"'{self.title}' has been returned by {self.borrower}. It was borrowed at {self.borrowed_time}.")
            self.available = True
            self.borrower = None
            self.borrowed_time = None
        else:
            print(f"'{self.title}' is not currently borrowed.")


