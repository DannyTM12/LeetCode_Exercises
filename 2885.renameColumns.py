import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Rename the columns of the DataFrame to more descriptive names
    students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace=True) # Rename columns, inplace=True modifies the original DataFrame
    return students # Return the modified DataFrame with renamed columns