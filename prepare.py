import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def prepare():
    # Load the dataset
    house_df = pd.read_csv('USA_Housing.csv')

    # Check for categorical columns
    categorical_columns = house_df.select_dtypes(include=['object']).columns
    print("Categorical columns:", categorical_columns)

    # Label Encoding
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        house_df[f'{col}_encoded'] = label_encoder.fit_transform(house_df[col])

    return house_df

