import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("housing.csv")

X = df.drop(columns=["Price"])
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "linear_model.pkl": LinearRegression(),

    "random_forest.pkl": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "gradient_boosting.pkl": GradientBoostingRegressor(
        random_state=42
    )
}

for filename, model in models.items():

    model.fit(X_train, y_train)

    with open(filename, "wb") as file:
        pickle.dump(model, file)

    print(f"{filename} trained and saved")

print("\nAll models trained successfully!")