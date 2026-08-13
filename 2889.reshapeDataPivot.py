import pandas as pd
def  pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    return weather.pivot(index='month', columns='city', values='temperature')

    # pivot works by taking the index, columns and values as arguments. 
    # In this case, we are pivoting the weather dataframe to have 'month' as the index, 
    # 'city' as the columns and 'temperature' as the values.