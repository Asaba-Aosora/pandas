import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.drop_duplicates(subset='salary').sort_values(by='salary', ascending=False)
    return df.iloc[[1]][['salary']].rename(columns={'salary':'SecondHighestSalary'}) if len(df)>=2 else pd.DataFrame({'SecondHighestSalary':[None]})

if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(second_highest_salary(employee))