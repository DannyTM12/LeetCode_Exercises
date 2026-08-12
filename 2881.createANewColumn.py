import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    employees['bonus'] = employees['salary'] * 2 # This creates a new column called 'bonus' which is double the salary of each employee.

    return employees # returns the updated DataFrame with the new 'bonus' column added.