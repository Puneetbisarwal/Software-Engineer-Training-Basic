from task1library import Book, Member

# Create book objects
book1 = Book("Python 101", "Jatin Malhotra", "1234567890123")
book2 = Book("Basic of Mathematics", "RS Malhotra", "9876543210123")

# Create member
member1 = Member("Prakhar Kapoor", "M001")

# Borrow a book
print(member1.borrow_book(book1))
print(member1.borrow_book(book2))

# Return a book
print(member1.return_book(book1))

# Display book info
print(book1.display_info())

# Get totals
print("Total books:", Book.get_total_books())
print("Total members:", Member.get_total_members())

# Validate IDs
print(Book.validate_isbn("1234567890123"))
print(Member.validate_member_id("M001"))
