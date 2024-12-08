from load_csv import Dataset
import numpy as np

df = Dataset()
df.load_dataset()
df.clear_dataset()

dataset = df.get_dataset()

def predict_rating(target_item, user_item_matrix, similarity_matrix):
    target_ratings = user_item_matrix.loc[target_item]

    rated_items = user_item_matrix.columns[target_ratings > 0]

    if target_item not in similarity_matrix.index:
        return 0

    similarities = similarity_matrix.loc[target_item, rated_items]
    rated_values = user_item_matrix.loc[rated_items].mean(axis=1)

    weighted_sum = np.dot(similarities, rated_values)
    sum_of_weights = np.abs(similarities).sum()

    if sum_of_weights == 0:
        return 0

    return weighted_sum / sum_of_weights

#ITEM-TO-ITEM

ratings = dataset[:500]

item_user_matrix_train =ratings.pivot_table(values='rating', index='item_id', columns='user_id', fill_value=0)
item_similarity_pearson = item_user_matrix_train.T.corr(method='pearson')
target_item = item_user_matrix_train.index[0]

predicted_rating = predict_rating(target_item, item_user_matrix_train, item_similarity_pearson)

print(f"Valoració predita per l'ítem {target_item}: {predicted_rating}")
