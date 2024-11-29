from load_csv import dataset

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

print(dataset)