import pandas as pd
from sklearn.preprocessing import LabelEncoder
class dataset():
    def __init__(self):
        self.path = "dataset_ac/ratings_Electronics.csv"
        self.dataset = pd.DataFrame()
    def set_path(self,new_path):
        self.path = new_path
    def get_path(self):
        return self.path
    def load_dataset(self):
        df = pd.read_csv(self.path)
        df.columns = ["user_id","item_id","rating","timestamp"]
        self.dataset = df

    def clear_dataset(self):
        self.dataset.dropna()
        user_counts = self.dataset['user_id'].value_counts()
        product_counts = self.dataset['item_id'].value_counts()

        self.dataset = (
            self.dataset)[(self.dataset['user_id'].isin(user_counts[user_counts >= 50].index)) &
            (self.dataset['item_id'].isin(product_counts[product_counts >= 5].index))
            ]

        # Encode user_id and prod_id
        user_encoder = LabelEncoder()
        product_encoder = LabelEncoder()

        self.dataset['user_id_encoded'] = user_encoder.fit_transform(self.dataset['user_id'])
        self.dataset['item_id_encoded'] = product_encoder.fit_transform(self.dataset['item_id'])
    def get_users(self):
        try:
            if not(self.dataset['user_id_encoded']):
                print('Please clean the dataset first')
                return
            return self.dataset['user_id']
        except:
            if self.dataset.empty:
                print('Load a dataset first')
            print('An error has occurred')

    def get_items(self):
        try:
            if not(self.dataset['item_id_encoded']):
                print('Please clean the dataset first')
                return
            return self.dataset['item_id']
        except:
            if self.dataset.empty:
                print('Load a dataset first')
            print('An error has occurred')
    def get_ratings(self):
        try:
            return self.dataset['rating']
        except:
            if self.dataset.empty:
                print('Load a dataset first')
            print('An error has occurred')

    def __str__(self):
        print(self.dataset.head())
