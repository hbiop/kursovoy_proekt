from PyQt5.QtWidgets import QStackedLayout, QVBoxLayout, QWidget

from app.controllers.main_window_controller import MainWindowController
from app.view.layouts.main_page import MainPage
from data_preprocessing.data_cleaning.data_preprocessor import DataPreprocessor
from neural_network.neural_network import NeuralNetwork


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.neural_network = NeuralNetwork()
        self.data_preprocessor = DataPreprocessor()
        vbox = QVBoxLayout(self)
        self.main_page = MainPage()
        self.main_page_controller = MainWindowController(self.main_page, self.data_preprocessor, self.neural_network)
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.main_page)
        vbox.addLayout(self.stacked_layout)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Пример QStackedLayout')
        self.show()

