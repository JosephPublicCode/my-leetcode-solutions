#leetcode 1141

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df = df.groupby('activity_date', as_index=False)[['user_id']].nunique()
    df = df.rename(columns={'activity_date':'day','user_id':'active_users'})
    df = df[(df['day'] <= '2019-07-27') & (df['day'] >= '2019-06-28')]
    return df
