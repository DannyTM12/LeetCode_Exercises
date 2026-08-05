import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape) # Return the size of the DataFrame as a list containing the number of rows and columns