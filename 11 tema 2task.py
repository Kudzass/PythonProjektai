print('---------------------1: *args naudojimas funkcijose----------------------------')

def sudeti_skaicius(*args):
    """
    Apskaičiuoja ir grąžina visų pateiktų skaičių sumą.

    Argumentai:
    *args (int, float): Neribotas skaičių kiekis.

    Grąžina:
    int arba float: Skaičių suma.

    Pavyzdys:
    >>> sudeti_skaicius(5, 10, 15)
    30
    >>> sudeti_skaicius(100, 200, 300, 400)
    1000
    """
    return sum(args)

print(sudeti_skaicius(5, 10, 15))
print(sudeti_skaicius(100, 200, 300, 400))

print('---------------------2: Funkcija su daugybe vardų------------------------------')

def sveikinti_vardus(*args):
    """
    Sugeneruoja pasisveikinimo žinutę kiekvienam pateiktam vardui.

    Argumentai:
    *args (str): Neribotas skaičius vardų.

    Grąžina:
    str: Pasisveikinimo žinutės kiekvienam vardui.

    Pavyzdys:
    >>> sveikinti_vardus("Tomas", "Laura", "Linas")
    'Labas, Tomas! Labas, Laura! Labas, Linas!'
    """
    return " ".join([f"Labas, {vardas}!" for vardas in args])

print(sveikinti_vardus("Tomas", "Laura", "Linas"))
print(sveikinti_vardus("Lina", "Darius", "Mantas", "Ugnė"))

print('---------------------3: Argumentų derinimas su *args---------------------------')

def pakelti_laipsniu(n, *args):
    """
    Pakelia kiekvieną iš pateiktų skaičių n laipsniu.

    Argumentai:
    n (int, float): Laipsnio pagrindas.
    *args (int, float): Skaičiai, kuriuos reikia pakelti n laipsniu.

    Grąžina:
    list: Sąrašas skaičių, pakeltų n laipsniu.

    Pavyzdys:
    >>> pakelti_laipsniu(2, 3, 4, 5)
    [9, 16, 25]

    >>> pakelti_laipsniu(3, 2, 3)
    [8, 27]
    """
    return [x ** n for x in args]

print(pakelti_laipsniu(2, 3, 4, 5))
print(pakelti_laipsniu(3, 2, 3))
