# leetcode 1174 

# Immediate Food Delivery II 

import pandas as pd
import numpy as np
def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery
    df_min = df.groupby(by='customer_id',as_index=False).agg({'order_date':'min'})
    df_merge = pd.merge(df_min,df, how='left', left_on=['order_date','customer_id'],
                right_on=['order_date','customer_id'])
    df_merge['imm_bool'] = np.where(df_merge['order_date'] == df_merge['customer_pref_delivery_date'],\
                            1,0)
    count = len(df_merge)
    summation =  100*sum(df_merge['imm_bool'])
    df_value = pd.DataFrame(data=[summation/count],columns=['immediate_percentage'])
    df_value = df_value.round(2)
    return df_value

# shorter Solution

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery.sort_values(by=['customer_id','order_date'])\
                .drop_duplicates(subset='customer_id',keep='first')
    value = round(
        100*sum(np.where(df['order_date']==df['customer_pref_delivery_date'],1,0))/
            len(df)
        ,2
    )
    df = pd.DataFrame([value],columns=['immediate_percentage'])
    return df 
