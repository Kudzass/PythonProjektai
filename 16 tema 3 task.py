print('---------------------------------4. Konstruktoriaus Perrašymas------------------------------------------')
class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
    def informacija(self):
        return f"Vardas: {self.vardas}, Amžius: {self.amzius}"
class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos
    def informacija(self):
        return f"Vardas: {self.vardas}, Amžius: {self.amzius}, Pareigos: {self.pareigos}"

darbuotojas = Darbuotojas("Tomas", 38, "Motociklų serviso meistras")

print(darbuotojas.informacija())

print('---------------------------------5. Kitų Metodų Perrašymas (Overriding)----------------------------------')

class TransportoPriemone:
    def judeti(self):
        print("Transporto priemonė juda")

class Dviratis(TransportoPriemone):
    def judeti(self):
        print("Dviratis važiuoja pedalais")

transportas = TransportoPriemone()
dviratis = Dviratis()

transportas.judeti()
dviratis.judeti()
