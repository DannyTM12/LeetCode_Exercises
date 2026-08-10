import pandas as pd

def fillMissingData(products: pd.DataFrame) -> pd.DataFrame:
    
    newValues = {'quantity': 0} # New values to fill missing data in the 'quantity' column

    products = products.fillna(newValues) # Fill missing values in the 'quantity' column with 0

    return products # Return the modified DataFrame with missing values filled