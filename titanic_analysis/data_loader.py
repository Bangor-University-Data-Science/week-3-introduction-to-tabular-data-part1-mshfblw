import pandas as pd

def load_titanic_data(filepath):
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    df = pd.read_csv(filepath)
    return df
    pass  # Implement the loading logic here
