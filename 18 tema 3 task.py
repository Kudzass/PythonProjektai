def sekimo_dekoratorius(funkcija):
    def vidine_funkcija(*args, **kwargs):
        print(f"Vykdoma funkcija: {funkcija.__name__}")
        rezultatas = funkcija(*args, **kwargs)
        print("Funkcija baigta!")
        return rezultatas
    return vidine_funkcija

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return "Klaida: dalyba iš nulio negalima!"
    return a / b

print(dauginti(2, 2))
print(dalinti(100, 50))
print(dalinti(77, 0))
