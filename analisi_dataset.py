# Importem llibreries necessàries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
##Falta df.describe
# Carreguem les dades
df = pd.read_csv("/Users/lauragispertcortes/Documents/UAB/3 curs/1s/Aprenetatge computacional/Projecte/ratings_Electronics.csv",
                 names=['userId', 'productId', 'rating', 'timestamp'])

# Mostrem les primeres 5 línies
print("Primeres 5 files del dataset:")
print(df.head())

# Analitzem les dades
# Dimensió
print("Nombre files:", df.shape[0])
print("Nombre columnes:", df.shape[1])

# Hi ha algun valor null a alguna columna?
print("\nValors nulls per columna:")
print(df.isnull().sum())

# Informació de les columnes
print("\nTipus de dades:")
print(df.info())

# Estadístiques dels ratings
print("\nEstadístiques dels ratings:")
print("Minimum rating:", df["rating"].min())
print("Maximum rating:", df["rating"].max())

# Quantitat de productes i usuaris únics
total_productes = df['productId'].nunique()
total_usuaris = df['userId'].nunique()
print("\nTotal productes únics:", total_productes)
print("Total usuaris únics:", total_usuaris)

# Files duplicades
files_duplicades = df[df.duplicated()]
print("\nTotal files duplicades:", len(files_duplicades))
if len(files_duplicades) > 0:
    print(files_duplicades.head())
else:
    print("No hi ha files duplicades")

# Combinacions duplicades usuari-producte
duplicados_usuario_producto = df.duplicated(subset=['userId', 'productId'])
total_duplicados_usuario_producto = duplicados_usuario_producto.sum()
print("\nTotal de combinacions duplicades (usuari-producte):", total_duplicados_usuario_producto)

# Distribució dels ratings
print("\nDistribució dels ratings:")
sns.countplot(data=df, x="rating", palette="viridis")
plt.title("Distribució dels ratings")
plt.xlabel("Rating")
plt.ylabel("Nombre de ratings")
plt.show()

data_500 = df[:500]
print(data_500)
# Matriu usuari-producte
user_product_matrix = data_500.pivot_table(values='rating', index='userId', columns='productId', fill_value=0)
print("\nMatriu usuari-producte:")
print(user_product_matrix.head())

# Visualització de la matriu pivotada (subset)
subset_matrix = user_product_matrix.iloc[:10, :10]
sns.heatmap(subset_matrix, cmap="YlGnBu", annot=True, cbar=True)
plt.title("Visualització de la matriu pivotada (subset)")
plt.xlabel("ProductId")
plt.ylabel("UserId")
plt.show()
