# leetcode 1070

# Product Sales Analysis III 
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby(by=['product_id'],as_index = False).agg({'year':'min'})

    df = pd.merge(df,sales,on=['product_id','year'],how="left")
    df = df.rename(columns={'year':'first_year'})
    return df.iloc[:,[0,1,3,4]]


import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales["first_year"] = sales.groupby("product_id")["year"].transform("min")
    return sales.loc[
        sales["year"] == sales["first_year"],
        ["product_id", "first_year", "quantity", "price"]
    ]
