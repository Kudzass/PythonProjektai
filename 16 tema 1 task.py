class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f"{self.vardas} juda.")

class Kate(Gyvunas):
    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!")

class Suo(Gyvunas):
    def loti(self):
        print(f"{self.vardas} sako AU AU!")

kate = Kate("Robustas", 9)
suo = Suo("Anri", 11)

kate.judeti()
kate.miaukseti()
suo.judeti()
suo.loti()
