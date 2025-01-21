import numpy as np
from neural_network.activation_functions.sigmoid import SigmoidFunction

class Layer:
    def __init__(self, input_size, output_size, activation_function):
        self.weights = np.random.randn(input_size, output_size)
        self.biases = np.zeros((1, output_size))
        if activation_function == "sigmoid":
            self.activation_function = SigmoidFunction()

    def forward(self, input_data):
        self.input_data = input_data
        self.z = np.dot(self.input_data, self.weights) + self.biases
        return self.activation_function.function(self.z)

    def backward(self, output_gradient, learning_rate):
        activation_gradient = self.activation_function.backward(self.z)
        grad_z = output_gradient * activation_gradient
        self.weights -= np.dot(self.input_data.T, grad_z) * learning_rate
        self.biases -= np.sum(grad_z, axis=0, keepdims=True) * learning_rate
        return np.dot(grad_z, self.weights.T)