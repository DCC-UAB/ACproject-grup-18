import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split , KFold
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, roc_curve, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("C:/Users/Joel/Documents/UAB/Tercer/Primer_Semestre/AC - Aprenentatge Computacional/ratings_Electronics (1).csv", names = ['userId', 'productId', 'ratings', 'timestamp'])

df = df.head(1000)
print(df.head)

df['userId'] = df['userId'].astype('category').cat.codes
df['productId'] = df['productId'].astype('category').cat.codes


train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)


from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

reader = Reader(rating_scale=(df['ratings'].min(), df['ratings'].max()))
data = Dataset.load_from_df(df[['userId', 'productId', 'ratings']], reader)

# Crear el modelo SVD
model = SVD()

# Validación cruzada
cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Entrenar el modelo en todo el dataset
trainset = data.build_full_trainset()
model.fit(trainset)

# Predecir para un usuario y un producto específicos
user_id = 1  # ID de usuario
product_id = 2  # ID de producto
prediction = model.predict(user_id, product_id)
print(prediction)


from load_csv import dataset
from split import split_random, split_priority, train_test_split

df = dataset()

df.load_dataset()
df.clear_dataset()
dataset_ = df.get_dataset()
# Matriu user-item
user_item_matrix = dataset_.pivot_table(values='rating', index='user_id', columns='item_id', fill_value=0)
# Per cada fila es contan els valors diferents de 0 i filtrem els usuaris que tenen al menys 50 interaccions
non_zero_counts_rows = user_item_matrix.apply(lambda row: (row != 0).sum(), axis=1)
valid_users = non_zero_counts_rows[non_zero_counts_rows >= 50].index
# Filtrar la matriz para mantener solo los usuarios válidos
user_item_matrix_filtered_rows = user_item_matrix.loc[valid_users]

# Contar valores diferentes de 0 por columna (producto)# Filtrar productos que tienen al menos 50 interacciones
non_zero_counts_columns = user_item_matrix_filtered_rows.apply(lambda col: (col != 0).sum(), axis=0)
valid_items = non_zero_counts_columns[non_zero_counts_columns >= 5].index
# Filtrar la matriz para mantener solo los productos válidos
user_item_matrix_filtered = user_item_matrix_filtered_rows[valid_items]

# Ver el resultado
print(user_item_matrix_filtered.shape)  # Dimensiones de la matriz filtrada