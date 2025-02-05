import datetime

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.borrow_date = None
    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) {'[Pasiskolinta]' if not self.available else '[Laisva]'}"
    def is_classic(self):
        return (datetime.datetime.now().year - self.year) > 50
    def due_date(self):
        if self.borrow_date:
            return self.borrow_date + datetime.timedelta(days=14)
        return None
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Knyga pridėta į biblioteką.")
    def display_books(self):
        if not self.books:
            print("Bibliotekoje nėra knygų.")
        else:
            for book in self.books:
                print(book)
    def borrow_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower() and book.available:
                    book.available = False
                    book.borrow_date = datetime.datetime.now()
                    print(f"Knyga '{book.title}' pasiskolinta. Grąžinti iki: {book.due_date().date()}")
                    return
            print("Knyga nerasta arba jau pasiskolinta.")
        except Exception as e:
            print("Įvyko klaida bandant pasiskolinti knygą.")
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                book.borrow_date = None
                print(f"Knyga '{book.title}' sėkmingai grąžinta.")
                return

        print("Knyga nerasta arba ji nebuvo pasiskolinta.")

    def filter_books(self, *args, **kwargs):
        filtered = self.books
        if 'author' in kwargs:
            filtered = [book for book in filtered if book.author.lower() == kwargs['author'].lower()]
        if 'year' in kwargs:
            filtered = [book for book in filtered if book.year == kwargs['year']]
        if 'title' in kwargs:
            filtered = [book for book in filtered if kwargs['title'].lower() in book.title.lower()]
        if filtered:
            for book in filtered:
                print(book)
        else:

            print("Atitikimų nerasta.")

library = Library()

library.add_book(Book("Ponos ir nusikaltėliai", "Maironis", 1912))
library.add_book(Book("Meilė ir mirtis", "Antanas Baranauskas", 1885))
library.add_book(Book("Baltaragio malūnas", "Vincas Kudirka", 1900))
library.add_book(Book("Raudoni žiedai", "Jurgis Savickis", 1912))
library.add_book(Book("Altorių šešėly", "Jurgis Kunčinas", 1909))

while True:
    print("\n1. Pridėti knygą")
    print("2. Rodyti knygas")
    print("3. Pasiskolinti knygą")
    print("4. Grąžinti knygą")
    print("5. Filtruoti knygas")
    print("6. Išeiti")

    pasirinkimas = input("Pasirinkite veiksmą: ")

    if pasirinkimas == "1":
        title = input("Įveskite pavadinimą: ")
        author = input("Įveskite autorių: ")
        try:
            year = int(input("Įveskite išleidimo metus: "))
            library.add_book(Book(title, author, year))
        except ValueError:
            print("Neteisingai įvesti metai!")
    elif pasirinkimas == "2":
        library.display_books()
    elif pasirinkimas == "3":
        title = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
        library.borrow_book(title)
    elif pasirinkimas == "4":
        title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
        library.return_book(title)
    elif pasirinkimas == "5":
        kriterijus = input("Filtruoti pagal (author/year/title): ")
        value = input("Įveskite reikšmę: ")
        if kriterijus == "year":
            try:
                value = int(value)
            except ValueError:
                print("Metai turi būti skaičius!")
                continue

        library.filter_books(**{kriterijus: value})

    elif pasirinkimas == "6":
        print("Programa baigta.")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
