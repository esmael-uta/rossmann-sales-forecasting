# evaluate_model.py
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(model_path, X_test, y_test):
    """Evaluates the trained model using MAE and RMSE."""
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    
    print(f"Mean Absolute Error: {mae}")
    print(f"Root Mean Squared Error: {rmse}")
    return mae, rmse