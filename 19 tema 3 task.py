import sqlite3

def sukurti_lentele():
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS mokykla (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pavadinimas TEXT NOT NULL,
                adresas TEXT NOT NULL,
                mokiniu_skaicius INTEGER NOT NULL,
                UNIQUE(pavadinimas, adresas)
            )
        """)
        conn.commit()

def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM mokykla WHERE pavadinimas = ? AND adresas = ?", (pavadinimas, adresas))
        if c.fetchone()[0] == 0:
            c.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)",
                      (pavadinimas, adresas, mokiniu_skaicius))
            conn.commit()
        else:
            print("⚠ Mokykla '{}' jau egzistuoja ir nebuvo pridėta.".format(pavadinimas))

def pasalinti_dublikatus():
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("""
            DELETE FROM mokykla
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM mokykla
                GROUP BY pavadinimas, adresas
            )
        """)
        conn.commit()
        print("🗑️ Pasikartojantys įrašai buvo pašalinti.")

def gauti_visas_mokyklas():
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("SELECT pavadinimas, adresas, mokiniu_skaicius FROM mokykla")
        rows = c.fetchall()
        for row in rows:
            print("Mokykla: {}, Adresas: {}, Mokinių skaičius: {}".format(row[0], row[1], row[2]))

def gauti_filtruotas_mokyklas(min_mokiniu):
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("SELECT pavadinimas, adresas, mokiniu_skaicius FROM mokykla WHERE mokiniu_skaicius > ?", (min_mokiniu,))
        rows = c.fetchall()
        for row in rows:
            print("Mokykla: {}, Adresas: {}, Mokinių skaičius: {}".format(row[0], row[1], row[2]))

sukurti_lentele()
prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)
pasalinti_dublikatus()

print("\n✅ Visos mokyklos duomenų bazėje:")
gauti_visas_mokyklas()
print("\n✅ Mokyklos su daugiau nei 600 mokinių:")
gauti_filtruotas_mokyklas(600)
