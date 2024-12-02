from load_csv import dataset
from split import split_random, split_priority, train_test_split

#print('Introduce path: ')
#print('\n')
#print("(type 'default' for predetermined path)")
#path = input("Introduce path:")

df = dataset()

dataset.load_dataset(df)
dataset.clear_dataset(df)

items = dataset.get_items(df)
users = dataset.get_users(df)
ratings = dataset.get_ratings(df)
timestamp = dataset.get_timestamp(df)
dataset = dataset.get_dataset(df)

#dataset.set_threshold(df, 30, 2)

train_r, test_r = split_random(dataset)
train_p, test_p = split_priority(dataset)

print(train_r.head())



#print(dataset)

#USER-TO-USER
#dataset amb 500
print(type(dataset))
data_500 = dataset[:500]
print(data_500.shape)
print(data_500.head())

#Dividim data
train_data, test_data = train_test_split(data_500, test_size=0.2, random_state=42)
#user_product_matrix = data_500.pivot_table(values='rating', index='user_id_encoded', columns='item_id_encoded', fill_value=0)
#shape de 321, 242
#print("MATRIU",user_product_matrix.head())

#Creem matriu
user_item_matrix = train_data.pivot_table(values='rating', index='user_id', columns='item_id', fill_value=0)

# CALCULAR SIMILITUD COEFICIENT CORRELACIO PEARSON
#user_similarity_pearson = user_product_matrix.corr(method='pearson')
user_similarity_train_pearson = user_item_matrix.T.corr(method='pearson')
print(user_similarity_train_pearson.head())
#filtrar usuario que más se parece
#predecir ratings
#evaluar modelo