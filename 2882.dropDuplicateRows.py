import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:

    customers_unique = customers.drop_duplicates(subset='email') # Delete all duplicates in emails column, just conserving the firts one

    return customers_unique # return the new DataFrame