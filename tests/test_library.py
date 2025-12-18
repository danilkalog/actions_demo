import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from library import Book, PrintedBook, EBook, User, Library


class TestBook:
    """Тесты для класса Book"""

    def test_book_creation(self):
        """Проверка создания книги"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        assert book.get_title() == "Война и мир"
        assert book.get_author() == "Лев Толстой"
        assert book.get_year() == 1869

    def test_book_available_by_default(self):
        """Проверка, что книга доступна при создании"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        assert book.is_available()

    def test_book_mark_as_taken(self):
        """Проверка отметки книги как выданной"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        book.mark_as_taken()
        assert not book.is_available()

    def test_book_mark_as_returned(self):
        """Проверка отметки книги как возвращённой"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        book.mark_as_taken()
        book.mark_as_returned()
        assert book.is_available()


class TestPrintedBook:
    """Тесты для класса PrintedBook"""

    def test_printed_book_creation(self):
        """Проверка создания печатной книги"""
        book = PrintedBook("Война и мир", "Лев Толстой", 1869,
                           1225, "хорошая")
        assert book.get_title() == "Война и мир"
        assert book.pages == 1225
        assert book.condition == "хорошая"

    def test_printed_book_
