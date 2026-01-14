import pandas as pd

def valid_rules(row):
    conditions = row['conditions']
    lst = conditions.split()
    print(lst)
    rule = any(condition.startswith('DIAB1') for condition in lst)
    return rule

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients.apply(valid_rules, axis=1)]
    return df

if __name__ == '__main__':
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
    patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})
    print(find_patients(patients))