import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']==101, ['name', 'age']]

if __name__ == '__main__':
    students_list = [
        [101, 'Ulysses', 13],
        [53, 'William', 10]
    ]

    students = pd.DataFrame(students_list, columns=['student_id', 'name', 'age'])
    print(selectData(students))