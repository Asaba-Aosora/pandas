import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.sort_values(by='salary', ascending=False)
    df.drop_duplicates(subset='salary', inplace=True)
    title = f"getNthHighestSalary({N})"

    # 还要避免传入负数
    return df.iloc[[N-1]][['salary']].rename(columns={'salary':title}) if len(df)>=N and N>0 else pd.DataFrame({title:[None]})

if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id':'Int64', 'salary':'Int64'})
    n = -1
    print(nth_highest_salary(employee, n))