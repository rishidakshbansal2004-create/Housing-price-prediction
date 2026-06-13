import streamlit as st
import pickle
import pandas as pd

with open("best_model_name.txt", "r") as file:
    best_model_name = file.read()

selected_model = st.selectbox(
    "Choose Model",
    [
        "linear_model.pkl",
        "random_forest.pkl",
        "gradient_boosting.pkl"
    ]
)

with open(selected_model, "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")

st.write(f"**Best Model:** {best_model_name}")

st.subheader("Enter House Details")

df = pd.read_csv("housing.csv")

features = list(df.columns)
features.remove("Price")

inputs = {}

for feature in features:
    if feature.lower() == "area":
        inputs[feature] = st.number_input(
            "Area(Sq.ft)",
            min_value=300,
            step=50,
            value=1000
        )

    elif feature.lower() == "floors":
        inputs[feature] = st.number_input(
            "Floors",
            min_value=1,
            step=1,
            value=1
        )

    else:
        inputs[feature] = st.number_input(
            feature,
            min_value=0,
            step=1
        )

if st.button("Predict Price"):

    house = pd.DataFrame([inputs])

    prediction = model.predict(house)

    st.success(
        f"Predicted House Price: ₹{prediction[0]:,.2f}"
    )