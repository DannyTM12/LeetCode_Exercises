import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df_eliminados = students.dropna(subset= 'name') # Drop rows where the 'name' column has missing values

    return df_eliminados # Return the DataFrame after dropping rows with missing 'name' values