import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['trans_date'] = transactions['trans_date'].astype(str).str[0:7:1]
    transactions = transactions.rename(columns=
                {'trans_date':'month'})
    transactions = transactions.drop(columns=['id'])
    transactions['approved_count'] = transactions['state'].apply(lambda x: 1 if x == 'approved' else 0)
    transactions['approved_total_amount'] = transactions['amount'].where(transactions['state'] == 
    'approved',0)
    transactions['state'] = transactions['state'].apply(lambda x: 1)
    transactions = transactions.groupby(by=['month','country'], dropna=False, as_index=False).agg({
        'state':'sum',
        'approved_count':'sum',
        'amount':'sum',
        'approved_total_amount':'sum'
    })
    transactions = transactions.rename(columns=
                {'state':'trans_count','amount':'trans_total_amount'})
    return transactions

