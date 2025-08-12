from task4library import Book, Member

# Create sample books
book1 = Book("The Hobbit", "J.R.R. Tolkien", "ISBN001")
book2 = Book("1984", "George Orwell", "ISBN002")
book3 = Book("Python Programming", "John Zelle", "ISBN003")

# Create member
member1 = Member("Akash", "M001")

# Display initial info
book1.display_info()
book2.display_info()
member1.display_info()

print("\n--- Borrowing Books ---")
member1.borrow_book(book1)  # Available
member1.borrow_book(book2)  # Available

print("\n--- Trying to Borrow Again ---")
member1.borrow_book(book1)  # Already borrowed

print("\n--- Returning Books ---")
member1.return_book(book1)  # Return
member1.return_book(book3)  # Not borrowed

print("\n--- Final Status ---")
book1.display_info()
book2.display_info()
member1.display_info()
