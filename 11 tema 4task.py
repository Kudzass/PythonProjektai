print('--------------------11: Įvadas į lambda funkcijas----------------------------')

pakelti_kvadratu = lambda x: x ** 2
print(pakelti_kvadratu(5))

print('--------------------12: Lambda funkcijos ir rūšiavimas-----------------------')

darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
surusiuoti_darbuotojai = sorted(darbuotojai, key=lambda x: x[1])
print(surusiuoti_darbuotojai)

print('--------------------13: Lambda funkcija su filter()--------------------------')

skaiciai = [5, 10, 15, 20, 25, 30]
dalinasi_is_10 = list(filter(lambda x: x % 10 == 0, skaiciai))
print(dalinasi_is_10)

