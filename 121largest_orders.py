import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(by='customer_number')['order_number'].size().reset_index()
    df = df.sort_values(by='order_number', ascending=False).reset_index(drop=True)
    return df.loc[[0], ['customer_number']]

if __name__ == '__main__':
    data = [[1, 1], [2, 2], [3, 3], [4, 3]]
    orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})
    print(largest_orders(orders))