import sys
import os

# Добавляем путь к src, чтобы импортировать library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from library import Book, PrintedBook, EBook, User, Librarian, Library


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
        assert book.is_available() == True
    
    def test_book_mark_as_taken(self):
        """Проверка отметки книги как выданной"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        book.mark_as_taken()
        assert book.is_available() == False
    
    def test_book_mark_as_returned(self):
        """Проверка отметки книги как возвращённой"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        book.mark_as_taken()
        book.mark_as_returned()
        assert book.is_available() == True


class TestPrintedBook:
    """Тесты для класса PrintedBook"""
    
    def test_printed_book_creation(self):
        """Проверка создания печатной книги"""
        book = PrintedBook("Война и мир", "Лев Толстой", 1869, 1225, "хорошая")
        assert book.get_title() == "Война и мир"
        assert book.pages == 1225
        assert book.condition == "хорошая"
    
    def test_printed_book_inherits_from_book(self):
        """Проверка наследования от Book"""
        book = PrintedBook("Война и мир", "Лев Толстой", 1869, 1225, "хорошая")
        assert book.is_available() == True


class TestEBook:
    """Тесты для класса EBook"""
    
    def test_ebook_creation(self):
        """Проверка создания электронной книги"""
        book = EBook("Война и мир", "Лев Толстой", 1966, 5, "epub")
        assert book.get_title() == "Война и мир"
        assert book.filesize == 5
        assert book.format == "epub"
    
    def test_ebook_inherits_from_book(self):
        """Проверка наследования от Book"""
        book = EBook("Война и мир", "Лев Толстой", 1966, 5, "epub")
        assert book.is_available() == True


class TestUser:
    """Тесты для класса User"""
    
    def test_user_creation(self):
        """Проверка создания пользователя"""
        user = User("Иван")
        assert user.name == "Иван"
        assert len(user.get_borrowed_books()) == 0
    
    def test_user_borrow_available_book(self):
        """Проверка выдачи доступной книги"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        user = User("Иван")
        result = user.borrow(book)
        assert result == True
        assert book.is_available() == False
        assert len(user.get_borrowed_books()) == 1
    
    def test_user_cannot_borrow_unavailable_book(self):
        """Проверка невозможности выдачи недоступной книги"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        book.mark_as_taken()
        user = User("Иван")
        result = user.borrow(book)
        assert result == False
        assert len(user.get_borrowed_books()) == 0
    
    def test_user_return_book(self):
        """Проверка возврата книги"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        user = User("Иван")
        user.borrow(book)
        result = user.return_book(book)
        assert result == True
        assert book.is_available() == True
        assert len(user.get_borrowed_books()) == 0
    
    def test_user_cannot_return_book_not_borrowed(self):
        """Проверка невозможности возврата чужой книги"""
        book = Book("Война и мир", "Лев Толстой", 1869)
        user = User("Иван")
        result = user.return_book(book)
        assert result == False


class TestLibrary:
    """Тесты для класса Library"""
    
    def test_library_creation(self):
        """Проверка создания библиотеки"""
        lib = Library()
        assert len(lib.books) == 0
        assert len(lib.users) == 0
    
    def test_library_add_book(self):
        """Проверка добавления книги в библиотеку"""
        lib = Library()
        book = Book("Война и мир", "Лев Толстой", 1869)
        lib.add_book(book)
        assert len(lib.books) == 1
    
    def test_library_find_book(self):
        """Проверка поиска книги по названию"""
        lib = Library()
        book = Book("Война и мир", "Лев Толстой", 1869)
        lib.add_book(book)
        found = lib.find_book("Война и мир")
        assert found == book
    
    def test_library_find_book_not_found(self):
        """Проверка поиска несуществующей книги"""
        lib = Library()
        found = lib.find_book("Война и мир")
        assert found == None
    
    def test_library_remove_book(self):
        """Проверка удаления книги из библиотеки"""
        lib = Library()
        book = Book("Война и мир", "Лев Толстой", 1869)
        lib.add_book(book)
        result = lib.remove_book("Война и мир")
        assert result == True
        assert len(lib.books) == 0
    
    def test_library_add_user(self):
        """Проверка добавления пользователя в библиотеку"""
        lib = Library()
        user = User("Иван")
        lib.add_user(user)
        assert len(lib.users) == 1
    
    def test_library_find_user(self):
        """Проверка поиска пользователя по имени"""
        lib = Library()
        user = User("Иван")
        lib.add_user(user)
        found = lib.find_user("Иван")
        assert found == user
    
    def test_library_lend_book(self):
        """Проверка выдачи книги через библиотеку"""
        lib = Library()
        book = Book("Война и мир", "Лев Толстой", 1869)
        user = User("Иван")
        lib.add_book(book)
        lib.add_user(user)
        result = lib.lend_book("Война и мир", "Иван")
        assert result == True
        assert book.is_available() == False
    
    def test_library_return_book(self):
        """Проверка возврата книги через библиотеку"""
        lib = Library()
        book = Book("Война и мир", "Лев Толстой", 1869)
        user = User("Иван")
        lib.add_book(book)
        lib.add_user(user)
        lib.lend_book("Война и мир", "Иван")
        result = lib.return_book("Война и мир", "Иван")
        assert result == True
        assert book.is_available() == True
