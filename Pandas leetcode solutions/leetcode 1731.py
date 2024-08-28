# leetcode 1731

# The Number of Employees which report to each employee. 


import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    name = df[['employee_id','name']]
    reports = df
    reports['employee_id'] = reports['reports_to']
    reports = reports.groupby(by='employee_id',as_index=False).agg({'reports_to':'count','age':'mean'})
    reports['age'] = reports['age'].apply(lambda x: Decimal(str(x)).quantize(Decimal('0'),        rounding=ROUND_HALF_UP))
    df = pd.merge(name, reports,on='employee_id')
    df.sort_values(by='employee_id',inplace=True)
    df = df.rename(columns={'reports_to':'reports_count','age':'average_age'})
    return df
