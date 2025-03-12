import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data, target_col, model_path='models/sales_model.pkl'):
    """Trains a RandomForest model and saves it."""
    X = data.drop(columns=[target_col])
    y = data[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, model_path)
    print("Model trained and saved successfully.")
    return model, X_test, y_test