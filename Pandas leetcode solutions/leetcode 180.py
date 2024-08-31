# leetcode 180

# Consecutive Numbers

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs.sort_values(by='id',inplace=True)
    logs['diff1'] = logs['num'].diff()
    logs['diff2'] = logs['num'].diff().diff()
    logs['id1'] = logs['id'].diff()
    logs['id2'] = logs['id'].diff().diff()
    logs = logs[(logs['diff1'] == 0 ) & (logs['diff2']== 0) &
    (logs['id1'] == 1) & (logs['id2'] == 0)][['num']]
    logs = logs.drop_duplicates().rename(columns={'num':'ConsecutiveNums'})
    return logs

