import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3) # Use the head() method to select the first three rows of the DataFrame and return them