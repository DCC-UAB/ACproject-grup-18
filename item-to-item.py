from load_csv import Dataset
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


df = Dataset()
df.load_dataset()
df.clear_dataset()

dataset = df.get_dataset()

def predict_rating(user_id, item_id, user_item_matrix, similarity_matrix):
    if item_id not in similarity_matrix.index or user_id not in user_item_matrix.columns:
        return 0

    user_ratings = user_item_matrix.loc[:, user_id]
    rated_items = user_ratings[user_ratings > 0].index

    similarities = similarity_matrix.loc[item_id, rated_items]

    weighted_sum = np.dot(similarities, user_ratings[rated_items])
    sum_of_weights = np.abs(similarities).sum()

    if sum_of_weights == 0:
        return 0
    return weighted_sum / sum_of_weights

#ITEM-TO-ITEM

train = dataset[:500]
test = dataset[501]

item_user_matrix_train =train.pivot_table(values='rating', index='item_id', columns='user_id', fill_value=0)
item_similarity_pearson = item_user_matrix_train.T.corr(method='pearson')

predicted_ratings = []
for _, row in test.iterrows():
    user_id = row['user_id']
    item_id = row['item_id']

    predicted_rating = predict_rating(user_id, item_id, item_user_matrix_train, item_similarity_pearson)
    predicted_ratings.append(predicted_rating)

test['predicted_rating'] = predicted_ratings

print(test['rating'])
print(test['predicted_rating'])

mae = mean_absolute_error(test['rating'], test['predicted_rating'])
rmse = np.sqrt(mean_squared_error(test['rating'], test['predicted_rating']))

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")

