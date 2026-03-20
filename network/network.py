from layer.layer import Layer

# réseau simple 
class NeuralNetwork:
    def __init__(self):
        self.layer1 = Layer(2, 2)
        self.layer2 = Layer(1, 2)

    def forward(self, inputs):
        out1 = self.layer1.forward(inputs)
        out2 = self.layer2.forward(out1)

        return out2

    # entraînement
    def train(self, dataset, epochs=1000, lr=0.1):
        for _ in range(epochs):
            for inputs, target in dataset.data:
                output = self.forward(inputs)[0]

                error = target - output

                # mise à jour des poids de la couche 2
                for neuron in self.layer2.neurons:
                    for i in range(len(neuron.weights)):
                        neuron.weights[i] = neuron.weights[i] + lr * error

                    neuron.bias = neuron.bias + lr * error
