import datetime

now = datetime.datetime.today()

print("Metai:", now.year)
print("Mėnuo:", now.month)
print("Diena:", now.day)
print("Valanda:", now.hour)
print("Minutė:", now.minute)
print("Sekundė:", now.second)


print(f"Dabar yra {now.hour}:{now.minute}, {now.day}-{now.month}-{now.year}")
