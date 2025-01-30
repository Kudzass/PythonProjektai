print('-------------------------7: Įvadas į **kwargs---------------------------------------')

def rodyti_duomenis(**kwargs):
    for raktas, reiksme in kwargs.items():
        print(f"{raktas}: {reiksme}")

rodyti_duomenis(vardas="Tomas", amzius=38, miestas="Vilnius")


print('-------------------------8: **kwargs su numatytaisiais argumentais------------------')

def registruoti_naudotoja(vardas, el_pastas, **kwargs):
    duomenys = {"vardas": vardas, "el_pastas": el_pastas, **kwargs}
    for raktas, reiksme in duomenys.items():
        print(f"{raktas}: {reiksme}")

registruoti_naudotoja("Tomas", "tomas.sipaitis@fasttrack.lt", amzius=38, miestas="Vilnius")


print('-------------------------9: **kwargs naudojimas kitoje funkcijoje-------------------')

def atspausdinti_lista(listas, **kwargs):
    print(*listas, **kwargs)

atspausdinti_lista(["Labas", "pasauli"], sep=" - ", end="!!!\n")

