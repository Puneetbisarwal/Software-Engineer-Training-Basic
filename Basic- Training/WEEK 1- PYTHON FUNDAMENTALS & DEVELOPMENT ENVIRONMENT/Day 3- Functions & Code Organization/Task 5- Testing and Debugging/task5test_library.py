import unittest
from task5library import Book, Member

class task5test_library(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python 101", "John Doe", "12345", True)
        self.member = Member("Abhishek", "M001")

    def test_borrow_book(self):
        self.member.borrow_book(self.book)
        self.assertFalse(self.book.available)
        self.assertIn(self.book, self.member.borrowed_books)

    def test_return_book(self):
        self.member.borrowed_books.append(self.book)
        self.book.available = False
        self.member.return_book(self.book)
        self.assertTrue(self.book.available)
        self.assertNotIn(self.book, self.member.borrowed_books)

if __name__ == '__main__':
    unittest.main()
