print('-------------------Užduotis 4: Klasės instancijų atvaizdavimas-------------------------')

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(book1)

print('-------------------Užduotis 5: Savų metodų kūrimas klasėje-----------------------------')

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_book_age(self):
        current_year = datetime.now().year
        return current_year - self.year
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)

print(f"Knyga '{book1.title}' yra {book1.get_book_age()} metų senumo.")
print(f"Knyga '{book2.title}' yra {book2.get_book_age()} metų senumo.")

print('-------------------Užduotis 6 : Metodų iškvietimas ir rezultatų naudojimas--------------')

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_book_age(self):
        current_year = datetime.now().year
        return current_year - self.year
book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book_age = book.get_book_age()

print(f"Knyga '{book.title}' yra {book_age} metų senumo.")
