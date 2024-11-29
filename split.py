import pandas as pd
from sklearn.model_selection import train_test_split



class split():
    def __init__(self, dataset):
        self.df = dataset

    def split_random(self):
        #Ens quedem amb 500 línies aleatòries
        sampled_df = self.df.sample(n=500, random_state=42)
        train, test = train_test_split(sampled_df, test_size=0.2, random_state=42)

        return train, test

    def split_priority(self):
        #Ens quedem amb els 500 Usuaris que més items han valorat
        user_counts = self.df.groupby('user_id').size().reset_index(name='Count')
        top_users = user_counts.nlargest(500, 'Count')
        filtered_df = self.df[self.df['user_id'].isin(top_users['user_id'])]

        train, test = train_test_split(filtered_df, test_size=0.2, random_state=42)


        return train, test

