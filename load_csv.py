import pandas as pd
from sklearn.preprocessing import LabelEncoder
class dataset():
    def __init__(self):
        self.path_1 = "/Users/lauragispertcortes/Documents/UAB/3 curs/1s/Aprenetatge computacional/Projecte/ratings_Electronics.csv"
        self.path_2 = "C:/Users/Joel/Documents/UAB/Tercer/Primer_Semestre/AC - Aprenentatge Computacional/Projecte/ratings_Electronics.csv"
        self.path_3 = "C:/Users/guill/Downloads/ratings_Electronics.csv"
        self.dataset = pd.DataFrame()
        self.cleaned = False
        self.threshold_1 = 50
        self.threshold_2 = 5

    def load_dataset(self):
        for path in [self.path_1, self.path_2, self.path_3]:
            try:
                df = pd.read_csv(path)
                df.columns = ["user_id", "item_id", "rating", "timestamp"]
                self.dataset = df
                print(f"Data loaded successfully from: {path}")
                return
            except FileNotFoundError:
                print(f"Failed to load data from: {path}")
        print("Error: File not found in all specified paths.")

    def clear_dataset(self):
        user_counts = self.dataset['user_id'].value_counts()
        valid_users = user_counts[user_counts >= self.threshold_1].index
        self.dataset = self.dataset[self.dataset['user_id'].isin(valid_users)]

        item_counts = self.dataset['item_id'].value_counts()
        valid_items = item_counts[item_counts >= self.threshold_2].index
        self.dataset = self.dataset[self.dataset['item_id'].isin(valid_items)]

        self.cleaned = True

    def get_dataset(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset

    def get_users(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset['user_id']

    def get_items(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset['item_id']

    def get_ratings(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset['rating']

    def get_timestamp(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset['timestamp']

    def __str__(self):
        if self.dataset.empty:
            return 'Dataset is empty'
        return str(self.dataset.head())
