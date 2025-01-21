from PyQt5.QtWidgets import QApplication
from neural_network.neural_network import NeuralNetwork
from neural_network.layers.layer import Layer
from neural_network.activation_functions.sigmoid import SigmoidFunction
from app.app import App

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()