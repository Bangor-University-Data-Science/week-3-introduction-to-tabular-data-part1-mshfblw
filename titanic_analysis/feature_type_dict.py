import pandas as pd
def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    if isinstance(df, pd.DataFrame):
        feature_types = {
            'numerical': {
                'continuous': df.select_dtypes(include=['float64']).columns.to_list(),  # Fill with continuous numerical features
                'discrete': df.select_dtypes(include=['int64']).columns.to_list()  # Fill with discrete numerical features
            },
            'categorical': {
                'nominal': df.select_dtypes(include=['object', 'category', 'bool']).columns.to_list(),  # Fill with nominal categorical features
                'ordinal': []  # Fill with ordinal categorical features
            }
        }
        return feature_types
    else:
        df = pd.DataFrame(df)
        feature_types_input_dic = {
            'numerical': {
                'continuous': df.select_dtypes(include=['float64']).columns.to_list(),  # Fill with continuous numerical features
                'discrete': df.select_dtypes(include=['int64']).columns.to_list()  # Fill with discrete numerical features
            },
            'categorical': {
                'nominal': df.select_dtypes(include=['object', 'category', 'bool']).columns.to_list(),  # Fill with nominal categorical features
                'ordinal': []  # Fill with ordinal categorical features
            }
        }
        return feature_types_input_dic
