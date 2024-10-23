import pandas as pd
def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    if isinstance(df, pd.DataFrame) == False:
        df = pd.DataFrame(df)
        dic_numerical = {}
        for item in numerical_features:
            dic_numerical[item] = list(set(df[item]))
        return pd.DataFrame(dic_numerical)
    else:
        dic_numerical = {}
        for item in numerical_features:
            dic_numerical[item] = list(set(df[item]))
        return pd.DataFrame(dic_numerical)
    pass  # Implement the logic here
