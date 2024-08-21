# leetcode 1792 

# Find Followers Count 

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers 
    df = df.groupby(by='user_id',as_index=False).agg({'follower_id':'count'})
    df = df.sort_values(by='user_id')
    df = df.rename(columns={'follower_id':'followers_count'})
    return df