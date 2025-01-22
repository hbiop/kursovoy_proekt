import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from PyQt5.QtCore import pyqtSignal, QObject

class DataPreprocessor(QObject):
    data_signal: pyqtSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.cleaning_nullable_values: str = "delete"
        self.data : pd.DataFrame = pd.DataFrame()
        self.Y : pd.DataFrame = pd.DataFrame()
        self.column_for_prediction = None
        self.labels_values = dict()

    def read_data(self, url):
        self.data : pd.DataFrame = pd.read_csv(url)

    def set_column_for_prediction(self, value):
        self.column_for_prediction = value
        data = self.data
        self.data = data.drop([self.column_for_prediction], axis=1)
        self.Y = data[self.column_for_prediction]

    def print_data(self):
        print(self.data)

    def get_data(self):
        return self.data

    def fill_missing_values(self):
        if hasattr(self, 'data'):
            self.data.fillna(self.data.mean(), inplace=True)

    def normalize_data(self):
        if hasattr(self, 'data'):
            from sklearn.preprocessing import MinMaxScaler
            scaler = MinMaxScaler()
            scaled_data = scaler.fit_transform(self.data.select_dtypes(include=['float64', 'int64']))
            self.data[self.data.select_dtypes(include=['float64', 'int64']).columns] = scaled_data

    def prepare_data(self):
        self.encode_categorical_variables()
        self.fill_missing_values()
        self.normalize_data()
        self.data_signal.emit("")

    def encode_categorical_variables(self):
        if hasattr(self, 'data'):
            columns = self.data.columns
            for col in columns:
                if self.data[col].dtype == 'object' :
                    le = LabelEncoder()
                    self.data[col] = le.fit_transform(self.data[col])

    def drop_columns(self, column_name : str):
        if hasattr(self, 'data'):
            self.data.drop(columns=column_name, inplace=True, errors='ignore')

    def split_data(self):
        return train_test_split(self.data, self.Y, test_size=0.2, random_state=42)


