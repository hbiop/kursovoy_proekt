from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pickle
from app.view.layouts.main_page import MainPage
from data_preprocessing.data_cleaning.data_preprocessor import DataPreprocessor
from neural_network.neural_network import NeuralNetwork


class MainWindowController:
    def __init__(self, view, data_preprocessor, neural_network_model):
        super().__init__()
        self.view:MainPage= view
        self.view.controller = self
        self.data_preprocessor : DataPreprocessor = data_preprocessor
        self.neural_network : NeuralNetwork = neural_network_model
        self.view.button_load_from_file.clicked.connect(self.load_data)

    def load_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            None, "Open pkl File", "", "PKL Файлы (*.pkl);;All Files (*)",
            options=options
        )
        if file_name:
            try:
                with open(file_name, "rb") as file:
                    self.neural_network = pickle.load(file)

            except Exception as e:
                self.show_error_message(f"Ошибка при открытии файла: {e}")

    def show_error_message(self, message):
        QMessageBox.critical(self.view, "Ошибка", message)
