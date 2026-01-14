import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'][(employees['employee_id']%2==1) & (employees['name'].str[0]!='M')]
    employees.fillna(value=0, inplace=True)
    return employees[['employee_id', 'bonus']].astype({'bonus':int}).sort_values(by='employee_id')



if __name__ == '__main__':
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
    print(calculate_special_bonus(employees))