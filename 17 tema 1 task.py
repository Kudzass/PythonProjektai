class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if pazymys > 0 and pazymys < 11:
            self._pazymiai.append(pazymys)
        else:
            print("Pažymys turi būti tarp 1 ir 10.")

    def rodyti_vidurki(self):
        return sum(self._pazymiai) / len(self._pazymiai) if self._pazymiai else 0

class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus=0):
        super().__init__(vardas, pavarde)
        self.bonus = bonus

    def rodyti_vidurki(self):
        return super().rodyti_vidurki() + self.bonus if self._pazymiai else 0

class BankoSaskaita:
    def __init__(self, savininkas, pradinis_balansas=0):
        self.savininkas = savininkas
        self.__balansas = pradinis_balansas

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma

    def nuskaičiuoti_pinigus(self, suma):
        if 0 < suma <= self.__balansas:
            self.__balansas -= suma

studentas1 = Studentas("Tomas", "Sipaitis")
studentas1.prideti_pazymi(8)
studentas1.prideti_pazymi(10)
print(f"{studentas1.vardas} vidurkis: {studentas1.rodyti_vidurki()}")

lyderis = StudentasLyderis("Mantas", "Mantauskas", bonus=0.5)
lyderis.prideti_pazymi(9)
lyderis.prideti_pazymi(10)
print(f"{lyderis.vardas} su bonusu vidurkis: {lyderis.rodyti_vidurki()}")

saskaita = BankoSaskaita("Remygijus", 100)
saskaita.prideti_pinigus(50)
saskaita.nuskaičiuoti_pinigus(30)
print(f"{saskaita.savininkas} balansas: {saskaita.gauti_balansa()}")
