# 🏠 House Price Prediction System

## Overview

The House Price Prediction System is an end-to-end Machine Learning application that predicts housing prices based on property-related features. The project trains multiple regression models, evaluates their performance, automatically identifies the best-performing model, and provides an interactive web interface for real-time predictions.

The application is designed to be flexible and scalable. Unlike many traditional implementations that depend on fixed feature sets, this project automatically adapts to changes in the dataset structure, making it easy to experiment with different housing attributes without modifying the source code.

---

## Features

- Predict house prices using Machine Learning
- Train and compare multiple regression models
- Automatic best-model selection
- Interactive Streamlit web application
- Dynamic feature handling
- Flexible dataset structure
- Model persistence using Pickle
- RMSE and R² based evaluation
- User-selectable prediction model

---

## Machine Learning Models Used

The project trains and evaluates the following regression algorithms:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

The model with the highest R² score is automatically selected as the best model.

---

## Dataset Structure

The project uses a dataset stored in a file named **housing.csv**.

The dataset must contain:

- One target column named **Price**
- Any number of numerical feature columns

A key feature of this project is its dynamic feature handling. During training and prediction, the application automatically treats every column except **Price** as an input feature. This allows users to customize the dataset by adding, removing, or modifying feature columns without changing the source code.

As long as the dataset file is named **housing.csv**, the target column is named **Price**, and all feature columns contain numerical values, the complete workflow—including training, evaluation, model selection, and Streamlit-based prediction—will function correctly without any modifications to the application.

---

## Project Workflow

### Step 1: Dataset Preparation

The housing dataset is stored in:

```text
housing.csv
```

The dataset contains housing features and the corresponding property prices.

---

### Step 2: Model Training

Run:

```bash
python3 train.py
```

This script:

- Loads the dataset
- Splits data into training and testing sets
- Trains all machine learning models
- Saves trained models as:

```text
linear_model.pkl
random_forest.pkl
gradient_boosting.pkl
```

---

### Step 3: Model Evaluation

Run:

```bash
python3 evaluate.py
```

This script:

- Loads all trained models
- Evaluates performance using RMSE and R² Score
- Compares all models
- Selects the best-performing model
- Saves:

```text
best_model.pkl
best_model_name.txt
```

---

### Step 4: Launch Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will:

- Automatically load available features
- Allow users to select a trained model
- Display the best-performing model
- Predict house prices based on user inputs

---

## Evaluation Metrics

### RMSE (Root Mean Squared Error)

RMSE measures the average prediction error made by the model.

Lower RMSE indicates better prediction accuracy.

---

### R² Score (Coefficient of Determination)

R² measures how well the model explains the variance in housing prices.

Higher R² values indicate better model performance.

---

## Project Structure

```text
Housing-Price-Prediction/
│
├── housing.csv
│
├── train.py
├── evaluate.py
├── app.py
│
├── linear_model.pkl
├── random_forest.pkl
├── gradient_boosting.pkl
│
├── best_model.pkl
├── best_model_name.txt
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Housing-Price-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Required Libraries

- pandas
- numpy
- scikit-learn
- streamlit
- pickle

Install manually if required:

```bash
pip install pandas numpy scikit-learn streamlit
```

---

## Usage

### Train Models

```bash
python3 train.py
```

### Evaluate Models

```bash
python3 evaluate.py
```

### Launch Application

```bash
streamlit run app.py
```

---

## Advantages of This Project

- Supports multiple regression models
- Automatically identifies the best model
- Dynamic feature detection
- Easily adaptable to new datasets
- User-friendly web interface
- Clean and modular project structure
- Suitable for learning end-to-end Machine Learning workflows

---

## Future Improvements

- Hyperparameter tuning using GridSearchCV
- Feature importance visualization
- Interactive performance dashboard
- Real-world housing datasets
- Cloud deployment
- REST API integration
- Prediction history tracking

---

## Conclusion

This project demonstrates a complete Machine Learning pipeline, including data processing, model training, model evaluation, model selection, persistence, and deployment through a Streamlit-based web application. The flexible dataset design and dynamic feature handling make it easy to experiment with different housing datasets while maintaining a clean and scalable architecture.
