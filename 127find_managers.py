import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(by='managerId').agg(
        staff_cnt = ('id', 'size')
    ).reset_index()

    managers = managers[managers['staff_cnt']>=5]
    managers = managers.rename(columns={'managerId':'id'})
    print(managers)
    df = pd.merge(left=managers, right=employee, how='inner')
    print(df)
    return df[['name']]

if __name__ == '__main__':
    data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
    print(find_managers(employee))