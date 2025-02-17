import sqlite3

conn = sqlite3.connect('mokykla.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS mokiniai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT,
                    pavarde TEXT,
                    klase TEXT,
                    vidurkis REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS mokytojai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT,
                    pavarde TEXT,
                    dalykas TEXT)''')

conn.commit()

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Vykdoma operacija: {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def prideti_mokini(vardas, pavarde, klase, vidurkis):
    try:
        cursor.execute("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)",
                       (vardas, pavarde, klase, vidurkis))
        conn.commit()
        print("Mokinys pridėtas!")
    except sqlite3.Error as e:
        print("Klaida pridedant mokinį:", e)

@log_decorator
def prideti_mokytoja(vardas, pavarde, dalykas):
    try:
        cursor.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
                       (vardas, pavarde, dalykas))
        conn.commit()
        print("Mokytojas pridėtas!")
    except sqlite3.Error as e:
        print("Klaida pridedant mokytoją:", e)

@log_decorator
def rodyti_mokinius():
    cursor.execute("SELECT * FROM mokiniai")
    mokiniai = cursor.fetchall()
    for m in mokiniai:
        print(m)

@log_decorator
def ieskoti_mokinio(vardas, pavarde):
    try:
        cursor.execute("SELECT * FROM mokiniai WHERE vardas = ? AND pavarde = ?", (vardas, pavarde))
        mokinys = cursor.fetchone()
        if mokinys:
            print(mokinys)
        else:
            print("Mokinys nerastas.")
    except sqlite3.Error as e:
        print("Klaida ieškant mokinio:", e)

@log_decorator
def atnaujinti_mokinio_klase(id, nauja_klase):
    try:
        cursor.execute("UPDATE mokiniai SET klase = ? WHERE id = ?", (nauja_klase, id))
        conn.commit()
        print("Mokinys atnaujintas!")
    except sqlite3.Error as e:
        print("Klaida atnaujinant mokinį:", e)

@log_decorator
def pasalinti_mokini(id):
    try:
        cursor.execute("DELETE FROM mokiniai WHERE id = ?", (id,))
        conn.commit()
        print("Mokinys pašalintas!")
    except sqlite3.Error as e:
        print("Klaida šalinant mokinį:", e)

class MokiniaiIteratorius:
    def __init__(self, mokiniai):
        self.mokiniai = mokiniai
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.mokiniai):
            raise StopIteration
        id_, vardas, pavarde, klase, vidurkis = self.mokiniai[self.index]
        self.index += 1
        return f"{vardas} {pavarde} ({klase}) - Vidurkis: {vidurkis}"

prideti_mokini("Jonas", "Jonaitis", "10B", 8.5)
prideti_mokini("Petras", "Petraitis", "9A", 7.2)
prideti_mokytoja("Ona", "Onaitienė", "Matematika")

rodyti_mokinius()

ieskoti_mokinio("Jonas", "Jonaitis")
atnaujinti_mokinio_klase(1, "11A")
pasalinti_mokini(2)

cursor.execute("SELECT * FROM mokiniai")
mokiniu_sarasas = cursor.fetchall()
iteratorius = MokiniaiIteratorius(mokiniu_sarasas)

for mokinys in iteratorius:
    print(mokinys)

conn.close()
