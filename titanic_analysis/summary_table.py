import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_table_dic = {'Feature Name': [], 'Data Type': [], 'Has Missing Values?': [], 'Number of Unique Values': []}
    for key_name in df:
        summary_table_dic['Feature Name'].append(key_name)
    for key_dtypes in df:
        summary_table_dic['Data Type'].append(df[key_dtypes].dtypes)
    for key_missing in df:
        summary_table_dic['Has Missing Values?'].append(pd.isnull(df[key_missing].any()))
    for key_uni in df:
        summary_table_dic['Number of Unique Values'].append(len(df[key_uni]))
    print(summary_table_dic)   
    return pd.DataFrame(summary_table_dic)
    pass  # Implement the logic here
