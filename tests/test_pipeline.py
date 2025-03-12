import pytest
import pandas as pd
from scripts import load_data, check_data, clean_data, train_model, evaluate_model

from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def sample_csv(tmp_path):
    """Creates a temporary CSV file for testing the pipeline."""
    data = pd.DataFrame({
        'numerical': [1, 2, None, 4, 5, 5],
        'categorical': ['A', None, 'B', 'B', 'A', 'A'],
        'target': [0, 1, 1, 0, 1, 0]
    })
    file_path = tmp_path / "test_data.csv"
    data.to_csv(file_path, index=False)
    return file_path

def test_pipeline(sample_csv):
    """Test the full pipeline from loading to evaluation."""
    
    # Step 1: Load data
    data = load_data.load_data(sample_csv)
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

    # Step 2: Check data
    initial_shape = data.shape
    assert check_data.check_data(data) is None  # check_data prints info, does not modify data

    # Step 3: Clean data
    cleaned_data = clean_data.clean_data(data)
    assert cleaned_data.shape[0] <= initial_shape[0]  # No extra rows added
    assert cleaned_data.isnull().sum().sum() == 0  # No missing values left

    # Step 4: Train model
    X = cleaned_data.drop(columns=['target'])
    y = cleaned_data['target']
    model = train_model.train_model(X, y, model_type="random_forest")
    assert isinstance(model, RandomForestClassifier)  # Ensuring model was trained

    # Step 5: Evaluate model
    accuracy = evaluate_model.evaluate_model(model, X, y)
    assert 0.0 <= accuracy <= 1.0  # Accuracy should be a valid percentage

if __name__ == "__main__":
    pytest.main()