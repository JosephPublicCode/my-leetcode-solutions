# leetcode 596

# Classes more than 5 Students. 

import pandas as pd 

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by='class',as_index = False).agg({'student':'count'})
    df = df[df['student'] >= 5]
    return df[['class']]