import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by=['class'])['student'].nunique().reset_index()
    return df[df['student']>=5][['class']]

if __name__ == '__main__':
    data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
    courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})   
    print(find_classes(courses))