print('--------------------Užduotis 7: Laiko skirtumo objekto gavimas atliekant datų atimtį---------------------------')

from datetime import datetime

date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)
time_difference = date2 - date1

print("Laiko skirtumas dienomis:", time_difference.days)

print('--------------------Užduotis 8: Skaičiavimai su timedelta objektais---------------------------')

from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date + timedelta(days=90)

print("Data po 90 dienų bus:", new_date.strftime('%Y-%m-%d'))

print('--------------------Užduotis 9: timedelta objekto laukų prieiga---------------------------')

from datetime import datetime

date1 = datetime(2000, 1, 1)
current_date = datetime.now()
time_difference = current_date - date1

print("Dienų skaičius:", time_difference.days)
print("Valandų skaičius:", time_difference.seconds // 3600)
print("Bendras sekundžių skaičius:", time_difference.total_seconds())
