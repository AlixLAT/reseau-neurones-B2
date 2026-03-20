import random

# classe pour créer des données 
class Dataset:
    def __init__(self, size=50):
        self.data = []
        self.generate(size)

    def generate(self, size):
        for i in range(size):
            x1 = random.random()
            x2 = random.random()

            # on définit la règle de classification : si la somme des deux entrées est supérieure à 1, alors la classe est 1, sinon c'est 0
            if x1 + x2 > 1:
                y = 1
            else:
                y = 0

            # on stocke entrée + résultat
            self.data.append(([x1, x2], y))