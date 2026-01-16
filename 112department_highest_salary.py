import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(by='salary', ascending=False, inplace=True)

    has_occurred = {}    # 记录已出现的 {department:salary}
    matched_rows = []
    for row in employee.itertuples(index=False):
        if row.departmentId not in has_occurred:
            has_occurred[row.departmentId] = row.salary
            matched_rows.append([row.name, row.salary, row.departmentId])
        elif has_occurred[row.departmentId] == row.salary:
            matched_rows.append([row.name, row.salary, row.departmentId])

    df = pd.DataFrame(data=matched_rows, columns=['Employee', 'Salary', 'departmentId'])

    department.rename(columns={'id':'departmentId', 'name':'Department'}, inplace=True)

    return pd.merge(left=df, right=department, on='departmentId')[['Department', 'Employee', 'Salary']]





if __name__ =='__main__':
    data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    print(department_highest_salary(employee, department))