from load_csv import dataset
from split import split_random, split_priority

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

train_r.head()



#print(dataset)