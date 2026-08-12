import pandas as pd
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:

    employees.salary *= 2 # This modifies the salary column by multiplying each value by 2

    return employees # Return the modified DataFrame with the updated salary column