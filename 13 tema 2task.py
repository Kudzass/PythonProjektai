import datetime

print('------------------------Užduotis 2: Sukurti datetime objektą-----------------------------')
datetime_obj1 = datetime.datetime(1995, 7, 14, 15, 30, 0)

print("Pirmas datetime objektas:", datetime_obj1)

print('-----------------------------------------------------')

datetime_obj2 = datetime.date(2023, 1, 1)

print("Antras datetime objektas:", datetime_obj2)

print("---------------------Užduotis 3: Laiko skirtumo tarp datų skaičiavimas---------------------")

start_date = datetime.date(2000, 1, 1)
today_date = datetime.date.today()
delta = today_date - start_date

print(f"Praėjo {delta.days} dienų nuo 2000-01-01.")

print('-----------------------------------------------------')