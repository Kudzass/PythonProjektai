try:
    skaicius = input("Įveskite skaičių: ")
    konvertuotas_skaicius = int(skaicius)
except ValueError:
    print("Klaida: įvesta ne skaičiaus reikšmė.")
else:
    print(f"Konversija sėkminga: {konvertuotas_skaicius}")
finally:
    print("Programa baigė darbą.")
