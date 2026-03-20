import random
import math

# neurone simple 
class Neuron:
    def __init__(self, input_size):
        self.weights = []
        
        # poids au hasard
        for i in range(input_size):
            self.weights.append(random.random())

        self.bias = random.random()  

    def activate(self, x):
        # fonction d'activation
        return 1 / (1 + math.exp(-x))

    def forward(self, inputs):
        total = 0

        # somme des produits
        for i in range(len(inputs)):
            total = total + inputs[i] * self.weights[i]

        total = total + self.bias


        return self.activate(total)