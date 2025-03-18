import random
class parent1:
    def __init__(self, blood_antigen):
        self.blood_antigen_1 = blood_antigen

    def blood_type(self):
        if self.blood_antigen_1 in ('AO', 'AA'):
            return 'A'
        elif self.blood_antigen_1 in ('BO', 'BB'):
            return 'B'
        elif self.blood_antigen_1 == 'AB':
            return 'AB'
        elif self.blood_antigen_1 == 'OO':
            return 'O'
        
class parent2:
    def __init__(self, blood_antigen):
        self.blood_antigen_2 = blood_antigen

    def blood_type(self):
        if self.blood_antigen_2 in ('AO', 'AA'):
            return 'A'
        elif self.blood_antigen_2 in ('BO', 'BB'):
            return 'B'
        elif self.blood_antigen_2 == 'AB':
            return 'AB'
        elif self.blood_antigen_2 == 'OO':
            return 'O'
    
class child(parent1, parent2):
    def __init__(self, blood_antigen_1, blood_antigen_2):
        parent1.__init__(self, blood_antigen_1)
        parent2.__init__(self, blood_antigen_2)

    def get_blood_antigen(self):
        self.first_antigen = self.blood_antigen_1[random.randint(0, 1)]
        self.second_antigen = self.blood_antigen_2[random.randint(0, 1)]
        self.antigen = self.first_antigen + self.second_antigen
        return self.antigen
    
    def blood_type(self):
        if self.antigen in ('AO', 'AA', 'OA'):
            return 'A'
        elif self.antigen in ('BO', 'BB', 'OB'):
            return 'B'
        elif self.antigen in ('AB', 'BA'):
            return 'AB'
        elif self.antigen == 'OO':
            return 'O'

antigen1 = input("Antigen orang tua 1: ")
antigen2 = input("Antigen orang tua 2: ")

bapak = parent1(antigen1)
print(f"\nGolongan darah bapak adalah {bapak.blood_type()}, dengan antigen {antigen1}")

ibuk = parent2(antigen2)
print(f"Golongan darah ibuk adalah {ibuk.blood_type()}, dengan antigen {antigen2}")

anak = child(antigen1, antigen2)
print(f"\nDengan antigen {anak.get_blood_antigen()}, maka")
print(f"golongan darah anak mereka adalah {anak.blood_type()}")