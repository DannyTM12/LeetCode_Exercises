import pandas as pd

def changeDataType(students: pd.DataFrame) -> pd.DataFrame:

    students['grade'] = students[['grade']].astype(int) # Convert grade column to integer type
    return students