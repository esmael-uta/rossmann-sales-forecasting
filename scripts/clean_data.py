import pandas as pd

def clean_data(data):
    """
    Cleans the dataset by handling missing values, encoding categorical features, 
    and removing duplicates.
    
    Steps:
    1. Forward fills missing values for numerical columns.
    2. Fills missing categorical values with the mode.
    3. Removes duplicate rows.
    4. Encodes categorical variables using one-hot encoding.
    
    :param data: Pandas DataFrame
    :return: Cleaned DataFrame
    """
    # Handle missing values
    for col in data.columns:
        if data[col].dtype == 'object':  # Categorical column
            data[col].fillna(data[col].mode()[0], inplace=True)
        else:  # Numerical column
            data[col].fillna(method='ffill', inplace=True)

    # Remove duplicate rows
    data.drop_duplicates(inplace=True)

    # Convert categorical variables to one-hot encoding
    data = pd.get_dummies(data, drop_first=True)

    print("Data cleaned successfully.")
    return data