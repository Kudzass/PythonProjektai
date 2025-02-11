class SkaiciuSekosIteratorius:

    def __init__(self, pradinis, galinis):
        self.pradinis = pradinis
        self.galinis = galinis

    def __iter__(self):
        return iter(range(self.pradinis, self.galinis + 1, 2))

    def atgaline_seka(self):
        return list(range(self.galinis, self.pradinis - 1, -2))

iteratorius = SkaiciuSekosIteratorius(2, 10)
for skaicius in iteratorius:
    print(skaicius)

print(iteratorius.atgaline_seka())
