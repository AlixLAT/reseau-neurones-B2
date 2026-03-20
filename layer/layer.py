from neurone.neurone import Neuron

# une couche avec plusieurs neurones
class Layer:
    def __init__(self, nb_neurons, input_size):
        self.neurons = []

        # création des neurones
        for i in range(nb_neurons):
            n = Neuron(input_size)
            self.neurons.append(n)

    def forward(self, inputs):
        res = []

        # on passe dans chaque neurone
        for n in self.neurons:
            val = n.forward(inputs)
            res.append(val)

        return res