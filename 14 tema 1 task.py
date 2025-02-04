print('----------Užduotis 1: Klasės kūrimas ir statiniai laukai------------------------------')

class Car:
    manufacturer = "Toyota"

print("Car manufacturer:", Car.manufacturer)

class Bike:
    manufacturer = "Yamaha"

print("Bike manufacturer:", Bike.manufacturer)

print('----------Užduotis 2: Konstruktorius __init__ ir instancijos laukų inicializavimas----')

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)

print(f"Book 1: {book1.title}, {book1.author}, {book1.year}")
print(f"Book 2: {book2.title}, {book2.author}, {book2.year}")

print('----------Užduotis 3: Statinio lauko ir instancijų naudojimas-------------------------')

class Book:
    publisher = "Penguin"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)

print("Publisher:", Book.publisher)
print(f"Book 1: {book1.title}, {book1.author}")
print(f"Book 2: {book2.title}, {book2.author}")
