import pandas as pd

def check_data(data):
    """Performs basic exploratory data analysis."""
    print("\nData shape:\n", data.shape)
    print("\nData Info:\n", data.info())
    print("\nMissing Values:\n", data.isnull().sum())
    print("\nSummary Statistics:\n", data.describe())
