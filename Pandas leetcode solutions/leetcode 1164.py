# leetcode 1164

# Product Price at a Given Date 

import pandas as pd

import pandas as pd
def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
   df = products
   df = df[df['change_date'] <= '2019-08-16']
   df = df.groupby(by='product_id',as_index=False).agg({'change_date':'max'})
   df = df.merge(products, on=['product_id','change_date'],how='left')


   df['price'] = df['new_price']
   df = df[['product_id', 'price']]

   distinct_product = products['product_id'].unique()
   default_price = [10]*len(distinct_product)
   default_df =  pd.DataFrame({
    "product_id": distinct_product, 
    "price": default_price
   })
   products = pd.concat([df,default_df]).drop_duplicates(subset="product_id",keep='first')
   return products


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    updated = products[products.change_date <= '2019-08-16'].groupby('product_id').agg({'change_date':'max'}).reset_index()
    updated = updated.merge(products,on=['product_id', 'change_date'],how='left')
    
    not_updated = products[~products.product_id.isin(updated['product_id'])].drop_duplicates(subset='product_id')
    not_updated['new_price'] = 10

    return pd.concat([updated,not_updated])[['product_id','new_price']].rename(columns={'new_price':'price'})
