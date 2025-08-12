"""
Library Management System - Part 1
Classes: Book, Member
"""

class Book:
    """Represents a single book in the library."""

    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author.strip():
            raise ValueError("Author cannot be empty.")
        if not isbn.strip():
            raise ValueError("ISBN cannot be empty.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_info(self):
        """Display book details."""
        status = "Available" if self.available else "Not Available"
        print(f"[{self.isbn}] '{self.title}' by {self.author} - {status}")


class Member:
    """Represents a library member."""

    def __init__(self, name: str, member_id: str):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if not member_id.strip():
            raise ValueError("Member ID cannot be empty.")

        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List of Book objects

    def borrow_book(self, book: Book):
        """Borrow a book if available."""
        if not isinstance(book, Book):
            raise TypeError("Can only borrow a Book object.")
        if not book.available:
            print(f"❌ '{book.title}' is currently not available.")
            return
        book.available = False
        self.borrowed_books.append(book)
        print(f"✅ {self.name} borrowed '{book.title}'.")

    def return_book(self, book: Book):
        """Return a borrowed book."""
        if book not in self.borrowed_books:
            print(f"⚠️ {self.name} does not have '{book.title}' borrowed.")
            return
        book.available = True
        self.borrowed_books.remove(book)
        print(f"🔄 {self.name} returned '{book.title}'.")

    def display_info(self):
        """Display member details."""
        print(f"Member: {self.name} (ID: {self.member_id})")
        if self.borrowed_books:
            print("  Borrowed books:")
            for b in self.borrowed_books:
                print(f"   - {b.title} by {b.author}")
        else:
            print("  No books borrowed.")
