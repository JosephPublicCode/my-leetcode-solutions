import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher
    df.drop_duplicates(subset=['teacher_id','subject_id'],inplace=True)
    df = df.groupby(by='teacher_id', as_index=False).agg({'subject_id':'count'}).rename(columns={'subject_id':'cnt'})
    return df