from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLabel
)
from PyQt5.QtCore import Qt

class LoadDataPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # Общий вертикальный макет
        vbox = QVBoxLayout(self)

        # Горизонтальная панель для кнопок загрузки и удаления столбца
        hbox_buttons = QHBoxLayout()

        # Кнопка загрузки данных
        self.btn_load_data = QPushButton("Загрузить данные")
        hbox_buttons.addWidget(self.btn_load_data)

        # Кнопка удаления столбца
        self.btn_remove_column = QPushButton("Удалить столбец")
        hbox_buttons.addWidget(self.btn_remove_column)

        # Поле для выбора целевой переменной
        self.lbl_target_variable = QLabel("Целевая переменная:")
        self.combo_target_variable = QComboBox()
        hbox_buttons.addStretch(1)  # Растягивание пустого пространства
        hbox_buttons.addWidget(self.lbl_target_variable)
        hbox_buttons.addWidget(self.combo_target_variable)

        vbox.addLayout(hbox_buttons)

        # Таблица для вывода данных
        self.table_data = QTableWidget()
        vbox.addWidget(self.table_data)

        # Настройка таблицы
        self.table_data.setColumnCount(0)  # Начальное количество колонок
        self.table_data.setRowCount(0)     # Начальное количество строк

        # Подключение сигналов к слотам
        self.btn_load_data.clicked.connect(self.load_data)
        self.btn_remove_column.clicked.connect(self.remove_column)

    def load_data(self):
        # Пример загрузки данных
        headers = ["Колонка 1", "Колонка 2", "Колонка 3"]
        rows = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.table_data.setColumnCount(len(headers))
        self.table_data.setHorizontalHeaderLabels(headers)
        self.table_data.setRowCount(len(rows))

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_data.setItem(i, j, item)

        # Заполнение выпадающего списка целевых переменных
        self.combo_target_variable.clear()
        self.combo_target_variable.addItems(headers)

    def remove_column(self):
        # Удаление выбранного столбца
        column_to_delete = self.table_data.currentColumn()
        self.table_data.removeColumn(column_to_delete)

        # Обновление выпадающего списка целевых переменных
        headers = [self.table_data.horizontalHeaderItem(i).text() for i in range(self.table_data.columnCount())]
        self.combo_target_variable.clear()
        self.combo_target_variable.addItems(headers)