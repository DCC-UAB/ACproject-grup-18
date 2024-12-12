from load_csv import dataset
from surprise import Dataset,Reader
from surprise import KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy



df = dataset()
df.load_dataset()
df.clear_dataset()

dataset = df.get_dataset()


reader = Reader(rating_scale=(0, 5))
dataset1 = Dataset.load_from_df(dataset[['user_id', 'item_id', 'rating']], reader)

train, test = train_test_split(dataset1, test_size=0.2)

sim_options = {
    "name": "cosine",  # Mètrica de similitud (també pot ser 'pearson')
    "user_based": False  # False indica que és item-to-item
}

model = KNNBasic(sim_options=sim_options)

# Entrenar el model
model.fit(train)

# Predir sobre el conjunt de test
prediccions = model.test(test)

# Avaluar el model
rmse = accuracy.rmse(prediccions)
print(f"RMSE del model: {rmse}")


def recomana_items(usuari_id, model, trainset, top_n=3):
    # Obtenir tots els items del dataset
    item_ids = trainset.all_items()
    items = [trainset.to_raw_iid(i) for i in item_ids]

    # Obtenir els items ja puntuats per l'usuari
    puntuacions_usuari = trainset.ur[trainset.to_inner_uid(usuari_id)]
    items_puntuats = [trainset.to_raw_iid(iid) for (iid, _) in puntuacions_usuari]

    # Generar prediccions per a items no puntuats
    recomanacions = []
    for item in items:
        if item not in items_puntuats:
            prediccio = model.predict(usuari_id, item)
            recomanacions.append((item, prediccio.est))

    # Retornar els top N items
    recomanacions = sorted(recomanacions, key=lambda x: x[1], reverse=True)
    return recomanacions[:top_n]

# Exemple de recomanacions per l'usuari 1
recomanacions = recomana_items(dataset.iloc[0]['user_id'], model, train)
print("Recomanacions:", recomanacions)


