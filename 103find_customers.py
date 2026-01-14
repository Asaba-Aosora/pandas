import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.rename(columns={'id':'order_id'})
    customers = customers.rename(columns={'name':'Customers'})
    df = pd.merge(left=customers, right=orders, how='left', left_on='id', right_on='customerId')
    print(df)
    return df[df['order_id'].isna()][['Customers']]