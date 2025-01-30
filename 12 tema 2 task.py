# try:
#     a = float(input("Įveskite pirmą skaičių: "))
#     b = float(input("Įveskite antrą skaičių: "))
#
#     try:
#         rezultatas = a / b
#         print("Rezultatas:", rezultatas)
#     except ZeroDivisionError:
#         print("Klaida: Dalyba iš nulio negalima.")
#
# except ValueError:
#     print("Klaida: Įvestas ne skaičius.")

def gauti_skaiciu(pranesimas):
    while True:
        try:
            return float(input(pranesimas))
        except ValueError:
            print("Klaida: Įvestas ne skaičius. Bandykite dar kartą.")


def dalinti():
    while True:
        a = gauti_skaiciu("Įveskite pirmą skaičių: ")
        b = gauti_skaiciu("Įveskite antrą skaičių: ")

        try:
            rezultatas = a / b
            print("Rezultatas:", rezultatas)
            break
        except ZeroDivisionError:
            print("Klaida: Dalyba iš nulio negalima. Bandykite dar kartą.")


dalinti()
