import sqlite3

conn = sqlite3.connect("mokykla.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS mokykla (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pavadinimas TEXT NOT NULL,
        adresas TEXT NOT NULL,
        mokiniu_skaicius INTEGER NOT NULL
    )
""")
mokyklos = [
    ("Vilniaus licėjus", "Vilnius, Žirmūnų g. 1", 500),
    ("Kauno Jėzuitų gimnazija", "Kaunas, Rotušės a. 9", 600),
    ("Klaipėdos Ąžuolyno gimnazija", "Klaipėda, Taikos pr. 20", 450)
]
c.executemany("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)", mokyklos)

conn.commit()
conn.close()

print("✅ Mokyklų duomenys sėkmingai įrašyti į 'mokykla.db'.")

conn = sqlite3.connect("mokykla.db")
c = conn.cursor()

c.execute("SELECT * FROM mokykla")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
