#Script python dades dataset Amazon Products
#Importem llibreries
import pandas as pd

#Careguem les dades
df = pd.read_csv("ratings_Electronics (1).csv",
                             names=['userId', 'productId','rating','timestamp'])
#Mostrem les primeres 5 linies
print(df.head)

#Analitzem dades
#   Dimensió
print("Nombre files:", df.shape[0])
print("Nombre columnes",df.shape[1])

#   Hi ha alguna valor null a alguna columna?
print(df.isnull().sum(), "No hi ha valors nulls") #No hi ha valors nulls

#Tenen les columnes els valors corresponents de dades?
print(df.info())


#   Hi ha alguna fila duplicada? --> 
#   Hi ha outliers? --> No
#RATINGS
#   Els ratings recorren tots els valors possibles? Hi ha algun outlier?
print('Minimum rating:', df["rating"].min())
print('Maximum rating:', df["rating"].max())

#Quantitat de valors
total_productes = df['productId'].nunique()
total_usuaris = df['userId'].nunique()

print("Total productes:", total_productes)
print("Total usuaris:", total_usuaris)

#Hi ha files duplicades?
files_duplicades = df[df.duplicated()]
print("Total files duplicades:",files_duplicades)
print("No hi ha files duplicades")

#Usuari ha votat més d'un cop el mateix rating?
duplicados_usuario_producto = df.duplicated(subset=['userId', 'productId'])
#   Contar cuántas combinaciones duplicadas existen
total_duplicados_usuario_producto = duplicados_usuario_producto.sum()
print("Total de combinacions duplicades (usuaris-producte):",total_duplicados_usuario_producto)

#ENTRENEM UN MODEL Collaborative Filtering (CF) User-to-User
# Crear una matriz pivote de usuarios y productos
#puede ser que no todos los usuarios hayan votado todo.
#podemos recomendar
#tenemos muchas variables y la matriu llegará a ser de 2000015699392 cells es mucho. Recomendable hacer subset?
user_product_matrix = df.pivot_table(values='rating', index='userId', columns='productId', fill_value=0)

print("MATRIU",user_product_matrix.head())

#Potser podem només agafar els usuaris que tinguin valors significatius en cuant a vot

