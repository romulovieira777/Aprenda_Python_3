class Father:  # Pai
    def __init__(self, name, weight):  # Nome, Peso
        self.name = name
        self.weight = weight


class Daughter(Father):
    def __init__(self, name, weight, hair):  # Cabelo
        super().__init__(name, weight)
        self.hair = hair


person_01 = Father('Alcimar', 95)
daughter_01 = Daughter('Mirella', 13, 'Blonde')

print(daughter_01.name)
print(daughter_01.weight)
print(daughter_01.hair)
