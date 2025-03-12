# rossmann-sales-forecasting
This repository contains a modular and well-structured pipeline for training, evaluating, and deploying a machine learning model to predict sales six weeks in advance. The project follows best practices in software engineering, including modularization, unit testing, and CI/CD integration.

## 📂 Project Structure

├── scripts/ # Data processing & model training scripts │ ├── load_data.py │ ├── check_data.py │ ├── clean_data.py │ ├── train_model.py │ ├── evaluate_model.py │ ├── requirements.txt │ ├── api.py # FastAPI deployment script │ ├── Dockerfile # Docker configuration │ ├── artifacts/ # Saved models & preprocessors │ ├── tests/ # Unit & Integration Tests │ ├── test_clean_data.py │ ├── test_train_model.py │ ├── test_api.py │ ├── README.md # General project documentation ├── requirements.txt # Python dependencies ├── .gitignore # Ignored files


## 📜 Features

- **Data Loading & Preprocessing**: Handling missing values, feature encoding, and outlier detection.
- **Model Training & Evaluation**: Training with Scikit-learn, logging metrics, and hyperparameter tuning.
- **Unit & Integration Testing**: Automated tests for each component.
- **API Deployment**: Exposing the trained model via FastAPI.
- **Docker Integration**: Easily deployable with Docker.

## 🚀 Getting Started

### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt