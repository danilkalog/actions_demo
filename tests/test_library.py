import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Book, User, Library


def test_book_creation():
    book = Book("Война и мир", "Лев Толстой", 1869)
    assert book.get_title() == "Война и мир"
    assert book.is_available()


def test_user_borrow():
    book = Book("Война и мир", "Лев Толстой", 1869)
    user = User("Иван")
    assert user.borrow(book)
    assert not book.is_available()


def test_library_add_book():
    lib = Library()
    book = Book("Война и мир", "Лев Толстой", 1869)
    lib.add_book(book)
    assert len(lib.books) == 1
    assert lib.find_book("Война и мир") == book
