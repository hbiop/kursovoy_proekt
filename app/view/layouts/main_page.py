from PyQt5.QtWidgets import QWidget, QVBoxLayout

from app.view.widgets.buttons.orange_custom_button import OrangeCustomButton

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.button_load_model = OrangeCustomButton("Обучить модель")
        self.button_load_from_file : OrangeCustomButton = OrangeCustomButton("Загрузить из файла")
        self.layout.addWidget(self.button_load_model)
        self.layout.addWidget(self.button_load_from_file)
        self.setLayout(self.layout)
