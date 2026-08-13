import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(['weight'], ascending=False) [['name']]

    # Explanation part by part:
    # 1. animals['weight'] > 100: This creates a boolean mask that checks which rows in the 'weight' column have values greater than 100.
    # 2. animals[animals['weight'] > 100]: This filters the original DataFrame to include only the rows where the 'weight' is greater than 100.
    # 3. .sort_values(['weight'], ascending=False): This sorts the filtered DataFrame by the 'weight' column in descending order (from heaviest to lightest).
    # 4. [['name']]: This selects only the 'name' column from the sorted DataFrame, resulting in a DataFrame that contains