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
