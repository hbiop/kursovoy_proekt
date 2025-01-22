from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QStackedLayout, QVBoxLayout, QWidget

from app.controllers.data_preview_controller import DataPreviewPageController
from app.controllers.load_data_window_controller import LoadDataWindowController
from app.controllers.main_window_controller import MainWindowController
from app.controllers.prediction_results_page_controller import PredictionResultsPageController
from app.view.layouts.data_preview_page import DataPreviewPage
from app.view.layouts.load_data_page import LoadDataPage
from app.view.layouts.main_page import MainPage
from app.view.layouts.prediction_results_page import PredictionResultsPage
from data_preprocessing.data_cleaning.data_preprocessor import DataPreprocessor
from neural_network.neural_network import NeuralNetwork


class App(QWidget, QObject):
    data_signal: pyqtSignal = pyqtSignal(NeuralNetwork)
    def __init__(self):
        super().__init__()
        self.neural_network = NeuralNetwork()
        self.data_preprocessor = DataPreprocessor()
        vbox = QVBoxLayout(self)
        self.stacked_layout = QStackedLayout()

        self.main_page = MainPage()
        self.main_page_controller = MainWindowController(self.main_page, self.data_preprocessor, self.neural_network, self.stacked_layout, self.data_signal)

        self.load_data_page = LoadDataPage()
        self.load_data_page_controller = LoadDataWindowController(self.data_preprocessor, self.load_data_page, self.stacked_layout, self.data_signal)

        print(self.data_preprocessor.data)
        self.data_preview = DataPreviewPage()
        self.data_preview_page_controller = DataPreviewPageController(self.data_preprocessor, self.data_preview, self.stacked_layout, self.neural_network, self.data_signal)

        self.predictions_page = PredictionResultsPage()
        self.predictions_page_controller = PredictionResultsPageController(self.data_preprocessor,self.predictions_page,self.stacked_layout,self.data_signal)
        self.stacked_layout.addWidget(self.main_page)
        self.stacked_layout.addWidget(self.load_data_page)
        self.stacked_layout.addWidget(self.data_preview)
        self.stacked_layout.addWidget(self.predictions_page)

        self.stacked_layout.setCurrentIndex(0)

        vbox.addLayout(self.stacked_layout)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Нейронная сеть')
        self.show()

