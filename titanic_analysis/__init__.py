# This file makes the folder a packag
import pandas as pd
from data_loader import load_titanic_data
from feature_type_dict import create_feature_type_dict
from categorical_unique_values import display_unique_values
from numerical_df import get_numerical_df
from summary_table import create_summary_table

df = load_titanic_data("data/titanic.csv")
print(isinstance(df, pd.DataFrame))
print(not df.empty)

# Mock a DataFrame
mock_df = pd.DataFrame(data={
    'Sex': ['male', 'female', 'female', 'male'],
    'Embarked': ['S', 'C', 'S', 'Q']
})
categorical_features = ['Sex', 'Embarked']
    
unique_values = display_unique_values(mock_df, categorical_features)
    
print(isinstance(unique_values, dict), "The result should be a dictionary")
print('Sex' in unique_values and 'Embarked' in unique_values, "Both categorical features should be in the result")

# Mock a DataFrame
mock_df = pd.DataFrame(data={
    'Age': [22, 38, 26, 35],
    'Sex': ['male', 'female', 'female', 'male'],
    'Survived': [0, 1, 1, 0]
})
feature_types = create_feature_type_dict(mock_df)
    
print('numerical' in feature_types, "The dictionary should have a 'numerical' key")
print('categorical' in feature_types, "The dictionary should have a 'categorical' key")

# Mock a DataFrame
mock_df = pd.DataFrame(data={
    'Age': [22, 38, 26, 35],
    'Fare': [7.25, 71.83, 7.92, 53.10],
    'Survived': [0, 1, 1, 0]
})
numerical_features = ['Age', 'Fare']
    
numerical_df = get_numerical_df(mock_df, numerical_features)
    
print(not numerical_df.empty, "Numerical DataFrame should not be empty")
print(all(col in numerical_df.columns for col in numerical_features), "All numerical features should be present")

mock_df = pd.DataFrame(data={
    'Age': [22, 38, 26, 35, None],
    'Sex': ['male', 'female', 'female', 'male', 'male'],
    'Survived': [0, 1, 1, 0, 1]
})
    
summary_df = create_summary_table(mock_df)
    
print('Feature Name' in summary_df.columns, f"Summary should include 'Feature Name'. Found columns: {summary_df.columns.tolist()}")
print('Data Type' in summary_df.columns, f"Summary should include 'Data Type'. Found columns: {summary_df.columns.tolist()}")
print('Has Missing Values?' in summary_df.columns, f"Summary should include 'Has Missing Values?'. Found columns: {summary_df.columns.tolist()}")
print('Number of Unique Values' in summary_df.columns, f"Summary should include 'Number of Unique Values'. Found columns: {summary_df.columns.tolist()}")
