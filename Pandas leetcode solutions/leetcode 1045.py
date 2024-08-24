# leetcode 1045

# Customers who bought all products

import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer 
    df = df.groupby(by=['customer_id'],as_index=False).agg({'product_key':pd.Series.nunique})
    counter = product['product_key'].count()
    df = df[df['product_key'] == counter]
    return df[['customer_id']]


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    #customer.drop_duplicates(inplace=True)
    result= customer.groupby('customer_id')['product_key'].nunique().reset_index(name='count')
    result=result.loc[result['count']==len(product)]
    return pd.DataFrame(result['customer_id'])