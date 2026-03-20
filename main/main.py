import sys
sys.path.insert(0, '.')
from dataset.dataset import Dataset
from network.network import NeuralNetwork

# probleme de chemin d'importation, il ne trouvait pas les modules

# création dataset
dataset = Dataset(100)

# création réseau
reseau = NeuralNetwork()  

print("réseau créé")  

# entraînement
reseau.train(dataset)

# test
test_input = [0.8, 0.5]
res = reseau.forward(test_input) 

print("entrée =", test_input)
print("résultat =", res)

print("fin du programme") 