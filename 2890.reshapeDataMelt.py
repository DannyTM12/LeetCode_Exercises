import pandas as pd
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

    # Explanation: 
    # The melt function is used to reshape the report dataframe from wide format to 
    # long format.
    # The id_vars parameter specifies the column(s) to keep as identifier variables,
    # in this case, 'product'.
    # The var_name parameter specifies the name of the new column that will contain
    # the variable names, in this case, 'quarter'.
    # The value_name parameter specifies the name of the new column that will contain
    # the values, in this case, 'sales'.