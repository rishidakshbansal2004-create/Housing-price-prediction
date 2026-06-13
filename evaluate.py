import pandas as pd
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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
    "linear_model.pkl": None,
    "random_forest.pkl": None,
    "gradient_boosting.pkl": None
}

best_model = None
best_model_name = ""
best_r2 = -1

print("\nMODEL COMPARISON")
print("=" * 50)

for model_file in models:

    with open(model_file, "rb") as file:
        model = pickle.load(file)

    predictions = model.predict(X_test)

    rmse = np.sqrt(
        mean_squared_error(y_test, predictions)
    )

    r2 = r2_score(y_test, predictions)

    print(f"\nModel : {model_file}")
    print(f"RMSE  : {rmse:.2f}")
    print(f"R²    : {r2:.4f}")

    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_model_name = model_file

with open("best_model.pkl", "wb") as file:
    pickle.dump(best_model, file)

with open("best_model_name.txt", "w") as file:
    file.write(best_model_name)

print("\n" + "=" * 50)
print("BEST MODEL :", best_model_name)
print("BEST R²    :", round(best_r2, 4))
print("best_model.pkl saved")
print("best_model_name.txt saved")