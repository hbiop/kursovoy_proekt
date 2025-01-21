import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self):
        self.cleaning_nullable_values: str = "delete"
        self.data : pd.DataFrame = pd.DataFrame()
        self.Y : pd.DataFrame = pd.DataFrame()
        self.column_for_prediction = 0

    def read_data(self, url):
        data : pd.DataFrame = pd.read_csv(url)
        self.data = data.drop(['NObeyesdad'], axis=1)
        self.Y = data['NObeyesdad']

    def print_data(self):
        print(self.data)

    def get_data(self):
        return self.data

    def delete_duplicates(self):
        self.data = self.data.drop_duplicates(inplace=True)

    def clear_nullable_values(self):
        match self.cleaning_nullable_values:
            case "delete":
                self.data = self.data.dropna()
            case "fill":
                self.data = self.data.fillna(0)

    def fill_missing_values(self):
        if hasattr(self, 'data'):
            self.data.fillna(self.data.mean(), inplace=True)  # Заполнение средним значением

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

    def encode_categorical_variables(self):
        if hasattr(self, 'data'):
            columns = self.data.columns
            for col in columns:
                if self.data[col].dtype == 'object' :
                    le = LabelEncoder()
                    self.data[col] = le.fit_transform(self.data[col])

    def drop_columns(self, column_name : str):
        if hasattr(self, 'data'):
            columns = self.data.columns
            self.data.drop(columns=column_name, inplace=True, errors='ignore')

    def split_data(self):
        return train_test_split(self.data, self.Y, test_size=0.2, random_state=42)


