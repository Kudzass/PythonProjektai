import datetime
import locale
locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')

print("---------Užduotis 5: Datos ir laiko įvedimas naudojant str formatą-----------")

user_input = input("Įveskite datą (YYYY-MM-DD): ")
input_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")

print("Jūsų įvesta data datetime formatu:", input_date)

print("---------Užduotis 6: Datos ir laiko išvedimas naudojant strftime formatą------")

datetime_obj = datetime.datetime(2022, 12, 31, 23, 59, 59)

formatted_date_1 = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
formatted_date_2 = datetime_obj.strftime("%Y metų %B %d diena")
formatted_date_2 = formatted_date_2.replace("metu", "metų")
formatted_date_2 = formatted_date_2.replace("gruodis", "gruodžio")

print(formatted_date_1)
print(formatted_date_2)
