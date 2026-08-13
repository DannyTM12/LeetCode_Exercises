import pandas as pd
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]
    # Explanation:
    # students.loc is used to select rows and columns from the DataFrame.
    # students['student_id'] == 101 is a condition that filters the rows where the 'student_id' column is equal to 101.
    # ['name', 'age'] specifies the columns to be selected from the filtered rows, which are 'name' and 'age'.