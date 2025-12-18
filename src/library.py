class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def is_available(self):
        return self.available

    def mark_as_taken(self):
        self.available = False

    def mark_as_returned(self):
        self.available = True

    def __str__(self):
        status = "в наличии" if self.available else "выдана"
        return f"{self.title} - {self.author} ({self.year}) - {status}"


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "отличная"
        print(f"{self.get_title()} отремонтирована. Состояние: {self.condition}")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.pages} стр., {self.condition}"


class EBook(Book):
    def __init__(self, title, author, year, filesize, format):
        super().__init__(title, author, year)
        self.filesize = filesize
        self.format = format

    def download(self):
        print(f"{self.get_title()} загружается...")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.filesize} МБ, {self.format}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.borrowed_books.append(book)
            print(f"{self.name} взял {book.get_title()}")
            return True
        else:
            print(f"{book.get_title()} недоступна")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} вернул {book.get_title()}")
            return True
        else:
            print(f"{self.name} не брал {book.get_title()}")
            return False

    def show_books(self):
        if not self.borrowed_books:
            print(f"У {self.name} нет книг")
        else:
            print(f"Книги {self.name}:")
            for book in self.borrowed_books:
                print(f"  - {book.get_title()}")

    def get_borrowed_books(self):
        return self.borrowed_books.copy()


class Librarian(User):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} добавил книгу: {book.get_title()}")

    def remove_book(self, library, title):
        library.remove_book(title)
        print(f"{self.name} удалил книгу: {title}")

    def register_user(self, library, user):
        library.add_user(user)
        print(f"{self.name} зарегистрировал пользователя: {user.name}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                return True
        return False

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None

    def show_all_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            print("Все книги в библиотеке:")
            for book in self.books:
                print(f"  - {book}")

    def show_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if not available_books:
            print("Нет доступных книг")
        else:
            print("Доступные книги:")
            for book in available_books:
                print(f"  - {book}")

    def lend_book(self, title, username):
        book = self.find_book(title)
        user = self.find_user(username)
        if not book:
            print(f"Книга '{title}' не найдена")
            return False
        if not user:
            print(f"Пользователь '{username}' не найден")
            return False
        if user.borrow(book):
            return True
        return False

    def return_book(self, title, username):
        book = self.find_book(title)
        user = self.find_user(username)
        if not book:
            print(f"Книга '{title}' не найдена")
            return False
        if not user:
            print(f"Пользователь '{username}' не найден")
            return False
        if user.return_book(book):
            return True
        return False

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
