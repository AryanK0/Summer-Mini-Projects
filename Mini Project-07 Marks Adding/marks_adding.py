import pandas as pd

def calculate_grades(data):
    df = pd.DataFrame(data)
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    df['Average'] = df['Total'] / 3
    df['Grade'] = df['Average'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C'))
    return df

if __name__ == '__main__':
    students = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [95, 80, 75],
        'Science': [90, 85, 70],
        'English': [92, 88, 80]
    }
    print(calculate_grades(students))