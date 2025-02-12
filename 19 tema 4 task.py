import sqlite3

def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_skaicius):
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("UPDATE mokykla SET mokiniu_skaicius = ? WHERE pavadinimas = ?", (naujas_skaicius, pavadinimas))

        if c.rowcount > 0:
            print("✅ Mokyklos '{}' mokinių skaičius atnaujintas į {}".format(pavadinimas, naujas_skaicius))
        else:
            print("⚠ Mokykla '{}' nerasta duomenų bazėje.".format(pavadinimas))

        conn.commit()

def gauti_visas_mokyklas():
    with sqlite3.connect("mokykla.db") as conn:
        c = conn.cursor()
        c.execute("SELECT pavadinimas, adresas, mokiniu_skaicius FROM mokykla")
        rows = c.fetchall()
        if not rows:
            print("⚠ Duomenų bazėje nėra mokyklų.")
        for row in rows:
            print("Mokykla: {}, Adresas: {}, Mokinių skaičius: {}".format(row[0], row[1], row[2]))


print("\n🔹 Prieš atnaujinimą:")
gauti_visas_mokyklas()

atnaujinti_mokiniu_skaiciu("Vilniaus progimnazija", 550)
atnaujinti_mokiniu_skaiciu("Kauno gimnazija", 850)

print("\n🔹 Po atnaujinimo:")
gauti_visas_mokyklas()
