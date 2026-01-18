import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_cnt = (accounts['income']<20000).sum()
    high_cnt = (accounts['income']>50000).sum()
    aver_cnt = len(accounts) - low_cnt - high_cnt
    data = [['Low Salary', low_cnt], ['Average Salary', aver_cnt], ['High Salary', high_cnt]]
    return pd.DataFrame(data, columns=['category', 'accounts_count'])

if __name__ == '__main__':
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
    accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
    print(count_salary_categories(accounts))