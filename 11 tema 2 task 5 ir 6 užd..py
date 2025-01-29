print('-------------5: Kelių argumentų tipų derinimas----------------------')

def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    """
    Pakartotinai atspausdina kiekvieną pateiktą žinutę nurodytą skaičių kartų,
    o pabaigoje prideda nurodytą pabaigos simbolį.

    Argumentai:
    kartai (int): Kiek kartų kartoti kiekvieną žinutę.
    *args (str): Žinutės, kurias reikia pakartoti.
    pabaiga (str, optional): Simbolis, kuris bus pridėtas kiekvienos žinutės gale (numatyta "!").

    Grąžina:
    list: Sąrašas su pakartotomis žinutėmis.

    Pavyzdys:
    >>> spausdinti_zinutes(2, "Labas", "Pasauli", pabaiga="!!!")
    ['Labas Labas!!!', 'Pasauli Pasauli!!!']
    """
    return [(" ".join([msg] * kartai) + pabaiga) for msg in args]

print(spausdinti_zinutes(2, "Labas", "Pasauli", pabaiga="!!!"))
print(spausdinti_zinutes(3, "Sveiki", "Kaip sekasi"))

print('-------------6: Rezultatų grąžinimas naudojant *args-------------------')

def dauginti_skaicius(n, *args):
    """
    Padaugina kiekvieną pateiktą skaičių iš n ir grąžina rezultatų sąrašą.

    Argumentai:
    n (int, float): Skaičius, iš kurio dauginama.
    *args (int, float): Skaičiai, kuriuos reikia padauginti iš n.

    Grąžina:
    list: Sąrašas su rezultatais.

    Pavyzdys:
    >>> dauginti_skaicius(2, 3, 4, 5)
    [6, 8, 10]

    >>> dauginti_skaicius(5, 1, 2, 3, 4)
    [5, 10, 15, 20]
    """
    return [n * x for x in args]

print(dauginti_skaicius(2, 3, 4, 5))
print(dauginti_skaicius(5, 1, 2, 3, 4))

