from load_csv import dataset

print('Introduce path: ')
print('\n')
print("(type 'default' for predetermined path)")
path = input("Introduce path:")

dataset.set_path(path)

dataset.load_dataset()
dataset.clear_dataset()

items = dataset.get_items()
users = dataset.get_users()
ratings = dataset.get_ratings()
timestamp = dataset.get_timestamp()

