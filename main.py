from load_csv import Dataset
from split import split_random, split_priority, train_test_split
from surprise import KNNBasic, accuracy
import pandas as pd

#print('Introduce path: ')
#print('\n')
#print("(type 'default' for predetermined path)")
#path = input("Introduce path:")

df = Dataset()
df.load_dataset()
df.clear_dataset()





dataset_ = df.get_dataset()
print("gfgf",dataset_.shape)
num_unique_users = dataset_['user_id'].nunique()
print(f"Usuarios únicos: {num_unique_users}")

"""dataset_ = df.get_dataset()

no_of_rated_products_per_user = dataset_.groupby(by='user_id')['rating'].count().sort_values(ascending=False)
no_of_rated_products_per_user.head()


print("/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n")"""

# Contar ítems únicos
num_unique_items = dataset_['item_id'].nunique()
print(f"Ítems únicos: {num_unique_items}")

'''user_item_matrix = dataset_.pivot_table(values='rating', index='user_id', columns='item_id', fill_value=0)
non_zero_counts = user_item_matrix.apply(lambda row: (row != 0).sum(), axis=1)
print(non_zero_counts.shape)
non_zero_counts = non_zero_counts[non_zero_counts>=50]
print(non_zero_counts.shape)
print(user_item_matrix.head())'''


# Crear la matriz usuario-item (ya lo has hecho)
user_item_matrix = dataset_.pivot_table(values='rating', index='user_id', columns='item_id', fill_value=0)

# Contar valores diferentes de 0 por fila (usuario)
non_zero_counts_rows = user_item_matrix.apply(lambda row: (row != 0).sum(), axis=1)

# Filtrar usuarios que tienen al menos 50 interacciones
valid_users = non_zero_counts_rows[non_zero_counts_rows >= 50].index

# Filtrar la matriz para mantener solo los usuarios válidos
user_item_matrix_filtered_rows = user_item_matrix.loc[valid_users]

# Contar valores diferentes de 0 por columna (producto)
non_zero_counts_columns = user_item_matrix_filtered_rows.apply(lambda col: (col != 0).sum(), axis=0)

# Filtrar productos que tienen al menos 50 interacciones
valid_items = non_zero_counts_columns[non_zero_counts_columns >= 5].index

# Filtrar la matriz para mantener solo los productos válidos
user_item_matrix_filtered = user_item_matrix_filtered_rows[valid_items]

# Ver el resultado
print(user_item_matrix_filtered.shape)  # Dimensiones de la matriz filtrada

####500#### users (com que després de filtrar només ens queden 1320 usuaris agafem una tercera part)
df_13 = user_item_matrix_filtered.sample(frac=1/3, random_state=42)
 #      1. Dividim train i test 80/20
train, test = train_test_split(df_13, test_size=0.2, random_state=42)
print("Mida train",train.shape)






import pandas as pd
from surprise import Dataset, Reader

# Supongamos que user_item_matrix es tu matriz de usuarios e ítems
user_item_matrix = user_item_matrix_filtered  # Esta es tu matriz filtrada de usuarios e ítems

# Convertir la matriz a formato "long" (user_id, item_id, rating)
long_format_df = user_item_matrix.stack().reset_index()
long_format_df.columns = ['user_id', 'item_id', 'rating']

# Mostrar un ejemplo de la transformación
print(long_format_df.head())

# Definir el formato de lectura para Surprise
reader = Reader(rating_scale=(1, 5))  # Asegúrate de que el rating_scale coincide con los valores que usas

# Cargar el dataframe a Surprise
data = Dataset.load_from_df(long_format_df[['user_id', 'item_id', 'rating']], reader)

# Ahora puedes usar data con los modelos de Surprise


from surprise import KNNBasic
from surprise import accuracy

# Dividir los datos en conjunto de entrenamiento y prueba
trainset = data.build_full_trainset()
testset = trainset.build_testset()  # Puedes ajustar la prueba según lo que necesites (por ejemplo, validación cruzada)

# Crear el modelo KNN basado en usuarios
sim_options = {'name': 'cosine', 'user_based': True}
model = KNNBasic(sim_options=sim_options)
model.fit(trainset)

# Hacer predicciones
predictions = model.test(testset)

# Evaluar el modelo con RMSE
print("RMSE:", accuracy.rmse(predictions))








#USER-TO-USER
#dataset amb 500
print(type(dataset_))
data_500 = dataset_[:500]
print(data_500.shape)
print(data_500.head())

#Dividim data
#train_data, test_data = train_test_split(data_500, test_size=0.2, random_state=42)
#user_product_matrix = data_500.pivot_table(values='rating', index='user_id_encoded', columns='item_id_encoded', fill_value=0)
#shape de 321, 242
#print("MATRIU",user_product_matrix.head())

#Creem matriu
user_item_matrix2 = data_500.pivot_table(values='rating', index='user_id', columns='item_id', fill_value=0)
print("SHAPE",user_item_matrix2.iloc[0].sum())
# CALCULAR SIMILITUD COEFICIENT CORRELACIO PEARSON
user_similarity_train_pearson = user_item_matrix2.corr(method='pearson')
#user_similarity_train_pearson = user_item_matrix2.T.corr(method='pearson')
print(user_similarity_train_pearson.head())
#filtrar usuario que más se parece
#predecir ratings
#evaluar modelo

