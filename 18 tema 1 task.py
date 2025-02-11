class Matematika:
    @staticmethod
    def sudeti(a, b):
        return a + b

    @staticmethod
    def atimti(a, b):
        return a - b

    @staticmethod
    def dauginti(a, b):
        return a * b

    @staticmethod
    def dalinti(a, b):
        if b == 0:
            raise ValueError("Dalyba iš nulio negalima")
        return a / b

    @staticmethod
    def ar_lyginis(skaicius):
        return skaicius % 2 == 0


class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    @classmethod
    def sukurti_is_string(cls, eilute):
        dalys = eilute.split(" ")
        marke = dalys[0]
        modelis = dalys[1]
        metai = int(dalys[2])
        return cls(marke, modelis, metai)

    @classmethod
    def naujausias_modelis(cls, automobiliai):
        return max(automobiliai, key=lambda auto: auto.metai)


print(Matematika.sudeti(3, 5))
print(Matematika.ar_lyginis(4))

auto1 = Automobilis.sukurti_is_string("Toyota Prius 2023")
auto2 = Automobilis.sukurti_is_string("Audi A6 2020")
auto3 = Automobilis.sukurti_is_string("Citroen DS5 2018")

naujausias = Automobilis.naujausias_modelis([auto1, auto2, auto3])
print(f"Naujausias automobilis: {naujausias.marke} {naujausias.modelis} {naujausias.metai}")
