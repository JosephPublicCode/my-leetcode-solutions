# leetcode 1789

# Primary Department for Each Employee

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee 
    df2 = df[df['primary_flag']=="Y"]
    df = df[~df['employee_id'].isin(df2['employee_id'])]
    df = pd.concat([df,df2])
    
    return df.loc[:,['employee_id','department_id']]

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[(~employee.duplicated(subset='employee_id', keep=False))|(employee.primary_flag=="Y")]

    return employee[['employee_id', 'department_id']]