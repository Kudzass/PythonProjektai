# # # print('Hello, world!')
# # #
# # # # print("1. Užduotis")
# # # # numb1 = 15
# # # # numb2 = 27
# # # # numb3 = 50
# # # # numb4 = 23
# # # # numb5 = 12
# # # # numb6 = 8
# # # # numb7 = 144
# # # # numb8 = 12
# # # # numb9 = 100
# # # # numb10 = 9
# # # #
# # # # print('1:', numb1 + numb2)
# # # # print('2:', numb3 - numb4)
# # # # print('3:', numb5 * numb6)
# # # # print('4:', numb7 / numb8)
# # # # print('5:', numb9 % numb10)
# # # #
# # # # print("2. Užduotis")
# # # #
# # # # a = 28
# # # # b = 8
# # # # c = 97
# # # # d = 10
# # # #
# # # # print('1:', a // b)
# # # # print('2:', c // d)
# # # #
# # # # print("3. Užduotis")
# # # #
# # # # x = 3
# # # # z = 2
# # # # v = 10
# # # # q = 0
# # # #
# # # # print('1:', x ** 2)
# # # # print('2:', z ** 5)
# # # # print('3:', v ** q)
# # # #
# # # # print("4. Užduotis")
# # # #
# # # # g = 3
# # # # h = 15
# # # # l = 40
# # # #
# # # # print('1:', q * h)
# # # # print('2:', l // h)
# # # # print('3:', l % h)
# # #
# # # # print("5. Užduotis")
# # # #
# # # # m = 45
# # # # n = 7
# # # # f = 6
# # # # q = 10
# # # # w = 5
# # # # e = 15
# # # # r = 2
# # # # t = 20
# # # # y = 4
# # # #
# # # # print('1:', m % n > 6 )
# # # # print('2:', q + w > w // r )
# # # # print('3:', t / w == y)
# # #
# # # print("6. Užduotis")
# # #
# # # a = 20 + 15
# # # b = 30 // 3
# # # c = 50 % 6
# # #
# # # Rezultatas = (a) * 2 - (b) + (c)
# # # print(Rezultatas)
# # #
# # # num1 = 10
# # # num2 = 1.5
# # # text = "Hello world"
# # #
# # # print(type(num1))
# # # print(type(num2))
# # # print(type(text))
# # #
# # # res = text * 10
# # # print(res)
# #
# # # user_input = input("Iveskite teksta:")
# # # print(type(user_input))
# #
# #
# # # user_input1 = float(input('number 1:'))
# # # user_input2 = float(input('number 2:'))
# # # user_input1 = int(input('number 1:'))
# # # user_input2 = int(input('number 2:'))
# # user_input1 = (input('number 1:'))
# # user_input2 = (input('number 2:'))
# #
# # print(user_input1 + user_input2)
#
# # print(f"Your BMI: {float(input('Mass kg: ')) / ((float(input('Mass kg: ')) / 100) ** 2)}")
#
# # mase = float(input('Mase (kg): '))
# # ugis = float(input('Ugis (cm): '))
# # res = 'Jusu BMI: ' + str(mase / ((ugis / 100) ** 2))
# # print(res)
# #
# print("Užduotis: BMI skaičiavimas su pateiktais duomenimis" )
# # BMI= svoris (kg) / (ūgis (cm) / 100)2
#
# user_input = input("Iveskite vardą:")
# print(user_input)
#
# weight_input = float(input("Iveskite svorį:"))
# print(weight_input)
#
# height_input = float(input("Iveskite ugį:"))
# print(height_input)
#
# bmi =  weight_input / (height_input / 100) ** 2
#
# # index = (bmi > 18.5, "Nepakankamas svoris") + (bmi > 24.9,"Normalus svoris") + (bmi > 29.9, 'Antsvoris') + (bmi > 30.0, "Nutukimas")
#
# print(f'Hello, {user_input}! Your weight: {weight_input} kg., Your height: {height_input} cm., Your BMI: {bmi}')

# print(    f"Hello, {input('Name: ')} {input('Surname: ')}!")
# text1 = "ABCDE"
# print(text1[0])
# print(text1[1])
# print(text1[2])
# print(text1[3])
# print(text1[4])
# print("----------")
# print(text1[-1])
# print(text1[-2])
# print(text1[0:2])
# print(text1[1:4])
# print(text1[1:-1])
# print(text1[0:])
# print(text1[2:])
# print(text1[:4])

# task: slice "HELLO WORLD"
# text1 = "HELLO WORLD"
# print(text1[0:5]) # HELLO
# print(text1[:5])# HELLO
# print(text1[6:])# WORLD
# print(text1[:7])# HELLO W
# print(text1[1:7])# ELLO W
# print(text1[1:-1])# ELLO WORL
# print(text1["Task done!"])# "" - tarpas

# text = "hello world"
# text2 = text.upper() # Didina raides
#
# print("text - " + text)
# print("text2 - " + text2)
# print(text.count("l")) # skaičiuoja simbolius
# print(text.count("ll"))
#
# # print(text.index('r')) # randa simboli kurioje vietoje
# # print(text.index('l'))
# # print(text.index('world'))
# # print(text.index('kakutis'))
#
# print(text.find('r')) # randa simboli kurioje vietoje (saugesnis)
# print(text.find('l'))
# print(text.find('world'))
# print(text.find('kakutis'))

# text = "hello world"
# text2 = text.replace("l","w")
# text3 = text.replace("hello", "Kakutis")
#
# print(text2)
# print(text3)
#
# user = '          Tomas Sipaitis        '
# user2 = "Tomas Sipaitis"
#
# user = user.strip()
#
# print(user)
# print(user == user2)


# text2 = "Hello World"
# print(text2[1:10:1])
# print(text2[1:10:2])
# print(text2[::2])
# print(text2[::-1])

# text2 = "Hello World"
#
# print(text2.lower())
# user = "Tomas"
# imported_user = "TOmas"

# 1. Kas yra sąrašas?

# # 1:
# sarasas = []
# print(type(sarasas))
# print(sarasas)
#
# # 2:
#
# men1 = 'Sausis'
# men2 = 'Vasaris'
# metai = '2024'
#
# sarasas = [men1, men2, metai]
#
# print(sarasas)
#
# # 3:
#
# sarasas.append(men1)
# print(sarasas)
#
# sarasas.append(men2)
# print(sarasas)
#
# sarasas.append(2024)
# print(sarasas)
#
# # 2. Sąrašų metodai
#
# # 1:
#
# dog = 'šuo'
# kat = 'katė'
# rabbit = 'zuikis'
# elefant = 'dramblys'
# giraffe = 'zirafa'
#
# sarasas = [dog, kat, rabbit]
# print(sarasas)
#
# menesiai = "Sausis",'Vasaris','Kovas','Balandis'

# #
# # Sukuriame sąrašą su skaičiais
# skaiciai = [3, 8, 12, 5, 10]
#
# # a. Naudojame len(), kad sužinotume elementų skaičių
# elementu_skaicius = len(skaiciai)
# print("Elementų skaičius sąraše:", elementu_skaicius)
#
# # b. Naudojame sum(), kad suskaičiuotume visų elementų sumą
# elementu_suma = sum(skaiciai)
# print("Visų skaičių suma:", elementu_suma)
#
# # c. Naudojame max() ir min(), kad nustatytume didžiausią ir mažiausią skaičių
# didziausias_skaicius = max(skaiciai)
# maziausias_skaicius = min(skaiciai)
# print("Didžiausias skaičius sąraše:", didziausias_skaicius)
# print("Mažiausias skaičius sąraše:", maziausias_skaicius)



# salys = ["Lietuva", "Latvija", "Estija", "Lenkija"]
#
# pirmas = salys[0]
# paskutinis = salys[-1]
# print("Pirmas sąrašo elementas:", pirmas)
# print("Paskutinis sąrašo elementas:", paskutinis)
#
# viduriniai = salys[1:-1]
# print("Viduriniai elementai:", viduriniai)
#
# atvirkstinis = salys[::-1]
# print("Sąrašas atvirkštine tvarka:", atvirkstinis)

# Sukuriame tuple
# savaites_dienos = ("pirmadienis", "antradienis", "trečiadienis", "ketvirtadienis")
# 
# antras_elementas = savaites_dienos[1]
# print("Antras elementas:", antras_elementas)
# 
# pirmadienis_kiekis = savaites_dienos.count("pirmadienis")
# print('"pirmadienis" pasikartoja:', pirmadienis_kiekis, "kartą(-us)")
# 
# pirmadienis_indeksas = savaites_dienos.index("pirmadienis")
# print('"pirmadienis" yra indekse:', pirmadienis_indeksas)

# eilute = "obuolys bananai kriaušės"
# sarasas = eilute.split()  # Skirtukas tarp žodžių yra tarpas
#
# print(sarasas)
# sujungta_eilute = "---".join(sarasas)
#
# print(sujungta_eilute)
#
# # 1:
# skaicius1 = int(input("Įveskite pirmą skaičių: "))
# skaicius2 = int(input("Įveskite antrą skaičių: "))
#
# if skaicius1 > skaicius2:
#     print(f"{skaicius1} yra didesnis.")
# elif skaicius1 < skaicius2:
#     print(f"{skaicius2} yra didesnis.")
# else:
#     print("Skaičiai yra vienodi.")
# # 2:
#
# skaicius = int(input("Įveskite skaičių: "))
#
# if skaicius % 2 == 0:
#     print("Skaičius yra lyginis.")
# else:
#     print("Skaičius yra nelyginis.")
#
# # 3:
#
# # sarasas = ["obuolys", "bananas", "kriaušės", "mango"]
# # zodis = input("Įveskite žodį: ")
# #
# # if zodis in sarasas:
# #     print(f"{zodis} yra sąraše.")
# # else:
# #     print(f"{zodis} nėra sąraše.")
#
# age = int(input("Įveskite savo amžių: "))
#
# if age < 18:
#     print("Nepilnametis")
# else:
#     print("Pilnametis")
#
# temperature = float(input("Įveskite temperatūrą: "))
#
# if temperature < 0:
#     print("Šalta")
# elif 0 <= temperature <= 20:
#     print("Vidutiniška")
# else:
#     print("Šilta")
# temperature = float(input("Įveskite temperatūrą: "))
#
# if temperature < 0:
#     print("Šalta")
# elif 0 <= temperature <= 20:
#     print("Vidutiniška")
# else:
#     print("Šilta")

# score = int(input("Įveskite balą: "))
#
# if 0 <= score <= 4:
#     print("Nepatenkinamas")
# elif 5 <= score <= 7:
#     print("Vidutinis")
# elif 8 <= score <= 10:
#     print("Puikus")
# else:
#     print("Neteisingas įvestas balas")
#
#
# season = input("Įveskite metų laiką (Žiema, Pavasaris, Vasara, Ruduo): ").strip().lower()
#
# if season == "žiema":
#     print("Gruodis, Sausis, Vasaris")
# elif season == "pavasaris":
#     print("Kovas, Balandis, Gegužė")
# elif season == "vasara":
#     print("Birželis, Liepa, Rugpjūtis")
# elif season == "ruduo":
#     print("Rugsėjis, Spalis, Lapkritis")
# else:
#     print("Neteisingas metų laikas")

# num1 = float(input("Įveskite pirmą skaičių: "))
# num2 = float(input("Įveskite antrą skaičių: "))
#
# if num1 > 0 and num2 > 0:
#     print("Abu skaičiai yra teigiami")
# elif num1 < 0 or num2 < 0:
#     print("Bent vienas skaičius yra neigiamas")
# else:
#     print("Skaičiai nėra nei abu teigiami, nei bent vienas neigiamas")
# print('--------------------')
# german_brands = ["bmw", "audi", "mercedes", "volkswagen", "porsche"]
# sports_models = ["m", "rs", "911", "amg"]
#
# brand = input("Įveskite automobilio markę: ").strip().lower()
# model = input("Įveskite automobilio modelį: ").strip().lower()
#
# if brand in german_brands:
#     print("Automobilio markė yra vokiška")
# else:
#     print("Automobilio markė nėra vokiška")
#
# if model in sports_models:
#     print("Automobilio modelis yra sportinis")
# else:
#     print("Automobilio modelis nėra sportinis")

# numb = float(input("Iveskite skaiciu: "))
# print("Teigiamas" if numb > 0 else "Neigiamas")
#
# print('------------------------------------------')
#
# string = input("Iveskite simboliu eilute: ")
# print("Didzioji raide" if string[0].isupper() else "Mazoji raide")
#
# print('------------------------------------------')
#
# word = input("Iveskite zodi: ")
# print("Zodis prasideda didziaja raide" if word[0].isupper() else "Zodis neprasideda didziaja raide")
# print("Visi simboliai mazosios raides" if word.islower() else "Ne visi simboliai mazosios raides")
#
# print('------------------------------------------')
#
# sentence = input("Iveskite sakini: ")
# print("Eilute prasideda simboliu 'A'" if sentence.startswith("A") else "Eilute neprasideda simboliu 'A'")
# print("Eilute parasyta tik didziosiomis raidemis" if sentence.isupper() else "Eilute nėra parasyta tik didziosiomis raidemis")

# name = input('Iveskite savo varda:')
# age = int(input('Kiek jums metu:'))
#
# print("-------------------------------")
#
# print(f'Sveikas {name}! Tau, {age} metai!')
#
# print('-----------------------------')
#
# name_lenght = len(name.strip())
# print(f'Tavo varda sudaro {name_lenght} simboliai!')
#
# print("--------------------------------")
#
# if age > 18:
#     print("Pilnametis!")
# else:
#     print("Nepilnametis")


# print("-------------------------")
# for num in  range(2, 21, 2):
#     print(num, end=' ')
# print("\n-------------------------")
# sum_kvadratu = 0
# for num in range(2, 21, 2):
#     sum_kvadratu =  sum_kvadratu + (num ** 2)
# print("\nKvadratu suma:", sum_kvadratu)
# print("---------------------------")
# for num in range(10, 0, -1):
#     print(num, end=" ")
# print("\n----------------------------")
# print('-------------------')
#
# print("1/1:")
# words = ['Obuolys', 'Kriause', 'Bananas', 'Vysnia']
# print(" | ".join(words))
#
# print('-------------------')
# print('1/2:')
#
# words = ['Obuolys', 'Kriause', 'Bananas', 'Vysnia']
# index = 1
#
# for word in words:
#     if words[-1] != word:
#         print(f'{index}) {word}', end=", ")
#         index += 1
#     else:
#         print(f'{index}) {word}')
#
# print('-------------------')
# print('1/3:')
#
# print("Pirmas", end=' ')
# print("Antras", end=' ')
# print("Trečias")
#
# print('-------------------')
#
# def process_list(data_list):
#     processed_results = []
#
#     for item in data_list:
#         if isinstance(item, int):
#             processed_results.append(item * 10)
#         elif isinstance(item, str):
#             processed_results.append(item.upper())
#         elif isinstance(item, bool):
#             processed_results.append("True arba False aptikta")
#         elif isinstance(item, float):
#             processed_results.append(round(item, 2))
#         else:
#             processed_results.append("Neatpažintas tipas")
#
#     for result in processed_results:
#         print(result)
#
# data = [123, 'Labas', True, 45.6, None]
# process_list(data)
#
# numbers = [1.234, 3.14159, 2.71828, 0.57721]
# rounded_numbers = [round(num, 3) for num in numbers]
# print("Apvalinti skaičiai:", rounded_numbers)
#
# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT.UTF-8')
#
# words = ["Žalgiris", "Ąžuolas", "Lietuva", "Vilnius"]
# sorted_words = sorted(words, key=locale.strxfrm)
# print("Surikiuoti žodžiai:", sorted_words)
#
# number_list = [10, 3, 7, 1, 15]
# sorted_numbers_desc = sorted(number_list, reverse=True)
# print("Skaičiai mažėjimo tvarka:", sorted_numbers_desc)

#
# print('------------------------------------------------------------------------------------')
#
# mokykla = {
#     "pavadinimas": "Vilniaus Senvagės Gimnazija",
#     "mokytojai": [
#         {"vardas": "Tomas", "pavardė": "Sipaitis", "mokomas_dalykas": "Chemija"},
#         {"vardas": "Darius", "pavardė": "Daraitis", "mokomas_dalykas": "Dailė"}
#     ],
#     "mokinių_skaičius": 1000
# }
#
# print("Pirmas mokytojas:", mokykla["mokytojai"][0]["vardas"], "-", mokykla["mokytojai"][0]["mokomas_dalykas"])
#
# if mokykla["mokinių_skaičius"] > 500:
#     print("Mokykloje yra daugiau nei 500 mokinių.")
# else:
#     print("Mokykloje yra 500 ar mažiau mokinių.")
#
# print('------------------------------------------------------------------------------------')
#
# company = {
#     "name": "TechCorp",
#     "employees": [
#         {"name": "Darius", "role": "Developer", "salary": 3000},
#         {"name": "Laura", "role": "Designer", "salary": 2500},
#         {"name": "Tomas", "role": "Manager", "salary": 4000}
#     ],
#     "location": "Kaunas",
#     "industry": "IT"
# }
#
# for employee in company["employees"]:
#     print(f"{employee['name']} - {employee['role']}")
#
# avg_salary = sum(emp["salary"] for emp in company["employees"]) / len(company["employees"])
# print("Vidutinis atlyginimas:", round(avg_salary, 2))
#
# if "location" in company:
#     print("Įmonės vieta:", company["location"])
#
# print('------------------------------------------------------------------------------------')
#
# library = {
#     "books": [
#         {"title": "1984", "author": "George Orwell", "copies": 3},
#         {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5},
#         {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}
#     ],
#     "location": "Kaunas",
#     "open_hours": {"start": "8:00", "end": "20:00"}
# }
#
# for book in library["books"]:
#     print(f"{book['title']} - {book['author']}")
#
# min_copies_book = min(library["books"], key=lambda b: b["copies"])
# print("Knyga su mažiausiai kopijų:", min_copies_book["title"])
#
#
# import pprint
# store = {
#     "name": "E-Shop",
#     "categories": ["Electronics", "Books", "Clothing"],
#     "products": [
#         {"name": "Laptop", "price": 1000, "stock": 10},
#         {"name": "Book", "price": 20, "stock": 50},
#         {"name": "T-shirt", "price": 15, "stock": 100}
#     ],
#     "rating": 4.5
# }
# if "Clothing" in store["categories"]:
#     store["categories"].remove("Clothing")
#
# for product in store["products"]:
#     if product["price"] > 50:
#         product["price"] *= 0.95
#
# for product in store["products"]:
#     if product["name"] == "Laptop":
#         product["stock"] = 15
# if store["rating"] < 4.6:
#     store["rating"] += 0.1
#
# pprint.pprint(store)
#
#
# total_sum = 0
# while True:
#     try:
#         num = int(input("Įveskite skaičių nuo 1 iki 10: "))
#         if num < 1 or num > 10:
#             print("Neteisinga reikšmė! Bandykite dar kartą.")
#             continue
#         if num == 5:
#             break
#         total_sum += num
#     except ValueError:
#         print("Prašome įvesti tik skaičių!")
# print("Visų įvestų skaičių suma (be 5):", total_sum)

# skaiciai = [-10, -5, 0, 5, 10, 15, 20]
#
# teigiama_suma = 0
# neigiama_suma = 0
# for skaicius in skaiciai:
#     if skaicius > 0:
#         teigiama_suma += skaicius
#     elif skaicius < 0:
#         neigiama_suma += skaicius
# didziausias = max(skaiciai)
# maziausias = min(skaiciai)
# print("Teigiamų skaičių suma:", teigiama_suma)
# print("Neigiamų skaičių suma:", neigiama_suma)
# print("Didžiausias skaičius sąraše:", didziausias)
# print("Mažiausias skaičius sąraše:", maziausias)

# numbers = [1, 3, 5, 7, 8, 10, 11]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"Pirmas lyginis skaičius: {num}")
#         break
# else:
#     print("Lyginių skaičių nėra")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# doubled_numbers = [num * 2 for num in numbers]
# print("Padvigubinti skaiciai:", doubled_numbers)
#
# print('-------------------------------------------')
#
# squared_numbers = [num ** 2 for num in numbers]
# print("Kvadratu pakelti skaiciai:", squared_numbers)
#
# print('-------------------------------------------')
#
# prices_eur = [10, 15, 20, 25, 30]
# exchange_rate = 1.1
#
# prices_usd = [round(price * exchange_rate, 2) for price in prices_eur]
# print("Kainos doleriais:", prices_usd)
#
# print('-------------------------------------------')
#
# price_messages = [f"Kaina: {price} EUR" for price in prices_eur]
# print("Pranesimai apie kainas:", price_messages)
#
# print('----------------------------------------------------------------------------------------------------------------')
#
# skaiciu_informacija = [[num, num**2, num**3, num % 2 == 0] for num in [1, 2, 3, 4, 5]]
# print("Skaiciu informacija:", skaiciu_informacija)
#
# print('----------------------------------------------------------------------------------------------------------------')
#
# skaiciu_sarasas = [5, 8, 12, 18, 25, 30, 35, 40]
#
# filtruoti_skaiciai = [skaicius for skaicius in skaiciu_sarasas if skaicius > 20]
# print("Skaiciai didesni nei 20:", filtruoti_skaiciai)
#
#
# print('----------------------------------------------------------------------------------------------------------------')
#
# dalijasi_is_5 = [skaicius for skaicius in skaiciu_sarasas if skaicius % 5 == 0]
# print("Skaiciai dalijami is 5:", dalijasi_is_5)
#
# print('----------------------------------------------------------------------------------------------------------------')
#
# lyg_nelyg = ["Lyginis" if skaicius % 2 == 0 else "Nelyginis" for skaicius in skaiciu_sarasas]
# print("Lyginiai/Nelyginiai skaiciai:", lyg_nelyg)
#
# print('----------------------------------------------------------------------------------------------------------------')

# print('Užduootis 5: -----------------------------------------------------------------------------------------------------')
# raides = ['A', 'B', 'C']
# skaiciai = [1, 2, 3]
#
# deriniai = [r + str(s) for r in raides for s in skaiciai]
# print("Raidziu ir skaiciu deriniai:", deriniai)
#
# print('---------------------------------------------------')
#
# deriniai_filtruoti = [r + str(s) for r_index, r in enumerate(raides) for s in skaiciai if r_index + s > 3]
# print("Deriniai su indeksu ir suma > 3:", deriniai_filtruoti)
#
# print('---------------------------------------------------')
#
# deriniai_lyginiai = [r.lower() + str(s) for r in raides for s in skaiciai if s % 2 == 0]
# print("Lyginiu skaiciu ir mazuju raidziu deriniai:", deriniai_lyginiai)
#
# print('Užduootis 6: -----------------------------------------------------------------------------------------------------')
# skaiciai_sarasas = [1, 2, 3, 2, 1, 4, 5, 5]
#
# unikalios_reiksmes = {skaicius for skaicius in skaiciai_sarasas}
# print("Unikalios reiksmes:", unikalios_reiksmes)
#
# print('---------------------------------------------------')
#
# padidinti_skaiciai = tuple(skaicius + 1 for skaicius in skaiciai_sarasas)
# print("Padidinti skaiciai:", padidinti_skaiciai)
#
# print('---------------------------------------------------')
#
# skaiciu_kvadratai = {skaicius: skaicius**2 for skaicius in skaiciai_sarasas}
# print("Skaiciu kvadratai:", skaiciu_kvadratai)
#
# print('---------------------------------------------------')

