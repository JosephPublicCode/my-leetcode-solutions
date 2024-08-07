# leetcode 550

# Game Play Analysis IV

import pandas as pd
import numpy as np 
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df_min = df.groupby(by=['player_id'],as_index=False).agg({'event_date':'min'})
    length = len(df_min)
    df_join = pd.merge(df,df_min,left_on='player_id',right_on='player_id',how='left')
    df_join = df_join[df_join['event_date_x'] != df_join['event_date_y'] ]
    df_join['bool'] = np.where(df_join['event_date_x'] == df_join['event_date_y']+ pd.Timedelta(days=1),1,0)
    summation = sum(df_join['bool'])
    df = pd.DataFrame(data = [summation/length],columns=['fraction']).round(2)
    return df 
