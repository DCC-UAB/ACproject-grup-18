import pandas as pd
from sklearn.preprocessing import LabelEncoder
class dataset():
    def __init__(self):
        self.path = "dataset_ac/ratings_Electronics.csv"
        self.dataset = pd.DataFrame()
        self.cleaned = False
        self.threshold_1 = 50
        self.threshold_2 = 5

    def set_path(self, new_path):
        if type(new_path) != str:
            raise TypeError('new_path ha de ser un string')
        if new_path == "default":
            return
        self.path = new_path

    def get_path(self):
        return self.path

    def load_dataset(self):
        df = pd.read_csv(self.path)
        df.columns = ["user_id","item_id","rating","timestamp"]
        self.dataset = df

    def clear_dataset(self):
        self.dataset.dropna(inplace=True)
        user_counts = self.dataset['user_id'].value_counts()
        product_counts = self.dataset['item_id'].value_counts()

        self.dataset = (
            self.dataset)[(self.dataset['user_id'].isin(user_counts[user_counts >= self.threshold_1].index)) &
            (self.dataset['item_id'].isin(product_counts[product_counts >= self.threshold_2].index))
            ]

        # Encode user_id and prod_id
        user_encoder = LabelEncoder()
        product_encoder = LabelEncoder()

        self.dataset['user_id_encoded'] = user_encoder.fit_transform(self.dataset['user_id'])
        self.dataset['item_id_encoded'] = product_encoder.fit_transform(self.dataset['item_id'])

        self.cleaned = True

    def get_dataset_raw(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        return self.dataset

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
        return self.dataset['user_id_encoded']

    def get_items(self):
        if self.dataset.empty:
            print('Load a dataset first')
            return None
        if not self.cleaned:
            print('Please clean the dataset first')
            return None
        return self.dataset['item_id_encoded']

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

    def set_threshold(self, new_threshold1, new_threshold2):
        self.threshold_1 = int(new_threshold1)
        self.threshold_2 = int(new_threshold2)


    def __str__(self):
        if self.dataset.empty:
            return 'Dataset is empty'
        return str(self.dataset.head())
