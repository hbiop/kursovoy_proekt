from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLabel
)
from PyQt5.QtCore import Qt

class LoadDataPage(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        hbox_buttons = QHBoxLayout()
        self.btn_load_data = QPushButton("Загрузить данные")
        hbox_buttons.addWidget(self.btn_load_data)
        self.btn_remove_column = QPushButton("Удалить столбец")
        hbox_buttons.addWidget(self.btn_remove_column)
        self.lbl_target_variable = QLabel("Целевая переменная:")
        self.combo_target_variable = QComboBox()
        hbox_buttons.addStretch(1)
        hbox_buttons.addWidget(self.lbl_target_variable)
        hbox_buttons.addWidget(self.combo_target_variable)
        vbox.addLayout(hbox_buttons)
        self.table_data = QTableWidget()
        vbox.addWidget(self.table_data)
        self.table_data.setColumnCount(0)
        self.table_data.setRowCount(0)
        self.submit_button = QPushButton("Подтвердить")
        self.submit_button.setEnabled(False)
        vbox.addWidget(self.submit_button)
        self.setLayout(vbox)


