import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ['student_id', 'age'] # Define the column names for the DataFrame
    df = pd.DataFrame(student_data, columns=column_names) # Create a DataFrame using the provided student data and column names
    return df # Return the created DataFrame