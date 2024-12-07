from sklearn.model_selection import train_test_split

def split_user_random(df):
    sampled_users = df['user_id'].drop_duplicates().sample(n=500, random_state=42)
    sampled_df = df[df['user_id'].isin(sampled_users)]
    train, test = train_test_split(sampled_df, test_size=0.2, random_state=42)
    return train, test

def split_user_priority(df):
    user_counts = df.groupby('user_id').size().reset_index(name='count')
    top_users = user_counts.nlargest(500, 'count')
    filtered_df = df[df['user_id'].isin(top_users['user_id'])]
    train, test = train_test_split(filtered_df, test_size=0.2, random_state=42)
    return train, test

def split_item_random(df):
    sampled_users = df['item_id'].drop_duplicates().sample(n=500, random_state=42)
    sampled_df = df[df['item_id'].isin(sampled_users)]
    train, test = train_test_split(sampled_df, test_size=0.2, random_state=42)
    return train, test

def split_item_priority(df):
    user_counts = df.groupby('item_id').size().reset_index(name='count')
    top_users = user_counts.nlargest(500, 'count')
    filtered_df = df[df['item_id'].isin(top_users['item_id'])]
    train, test = train_test_split(filtered_df, test_size=0.2, random_state=42)
    return train, test