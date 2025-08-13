class Book:
    """Represents a book in the library."""

    # Class attribute (shared by all books)
    total_books = 0

    def __init__(self, title, author, isbn, available=True):
        """Initialize a new Book object."""
        self.title = title                  # Instance attribute
        self.author = author                # Instance attribute
        self.__isbn = isbn                   # Private instance attribute
        self.available = available           # Instance attribute
        Book.total_books += 1                # Track number of books

    # Instance method
    def display_info(self):
        """Return a formatted string with book details."""
        return f"{self.title} by {self.author}, ISBN: {self.__isbn}, Available: {self.available}"

    # Getter method for private attribute
    def get_isbn(self):
        """Return the ISBN of the book."""
        return self.__isbn

    # Class method
    @classmethod
    def get_total_books(cls):
        """Return the total number of books created."""
        return cls.total_books

    # Static method
    @staticmethod
    def validate_isbn(isbn):
        """Validate that an ISBN is numeric and has 13 digits."""
        return isinstance(isbn, str) and isbn.isdigit() and len(isbn) == 13


class Member:
    """Represents a library member."""

    # Class attribute (shared by all members)
    total_members = 0

    def __init__(self, name, member_id):
        """Initialize a new Member object."""
        self.name = name                    # Instance attribute
        self.__member_id = member_id         # Private instance attribute
        self.borrowed_books = []             # Instance attribute
        Member.total_members += 1

    # Instance method
    def borrow_book(self, book):
        """Allow member to borrow a book if available."""
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'"
        return f"'{book.title}' is not available."

    def return_book(self, book):
        """Allow member to return a borrowed book."""
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'"
        return f"{self.name} did not borrow '{book.title}'"

    # Getter method for private attribute
    def get_member_id(self):
        """Return the member ID."""
        return self.__member_id

    # Class method
    @classmethod
    def get_total_members(cls):
        """Return the total number of members."""
        return cls.total_members

    # Static method
    @staticmethod
    def validate_member_id(member_id):
        """Validate that member ID starts with 'M' and has 4 digits."""
        return isinstance(member_id, str) and member_id.startswith("M") and member_id[1:].isdigit()
