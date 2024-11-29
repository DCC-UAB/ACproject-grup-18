import pandas as pd
from sklearn.model_selection import train_test_split



class split():
    def __init__(self, df):
        self.dataset = df

    def split_random(self, df):
        #Ens quedem amb 500 línies aleatòries
        sampled_df = df.sample(n=500, random_state=42)
        train, test, validation = train_test_split(sampled_df, random_state=42)

        return train, test, validation

    def split_priority(self, df):
        #Ens quedem amb els 500 Usuaris que més items han valorat
        user_counts = df.groupby('user_id').size().reset_index(name='Count')
        top_users = user_counts.nlargest(500, 'Count')
        filtered_df = df[df['user_id'].isin(top_users['user_id'])]

        train, test, validation = train_test_split(filtered_df, random_state=42)


        return train, test, validation

