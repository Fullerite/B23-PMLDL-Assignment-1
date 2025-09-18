import requests
import streamlit as st


st.set_page_config(
    page_title="Car MPG Prediction",
    layout="centered"
)

st.title("Car MPG Prediction")

st.sidebar.header("Input Car Features")
cylinders = st.sidebar.slider(
    "Cylinders",
    min_value=1,
    max_value=16,
    value=8,
    step=1,
    help="Number of cylinders in the car's engine."
)
horsepower = st.sidebar.slider(
    "Horsepower",
    min_value=50,
    max_value=1800,
    value=150,
    step=5,
    help="Engine horsepower."
)
weight = st.sidebar.slider(
    "Weight (lbs)",
    min_value=1000,
    max_value=5000,
    value=3500,
    step=100,
    help="Total weight of the car **in pounds**."
)

if st.sidebar.button("Predict MPG"):
    input_data = {
        "cylinders": cylinders,
        "horsepower": horsepower,
        "weight": weight
    }

    try:
        api_url = "http://fastapi:80/predict"
        response = requests.post(api_url, json=input_data)
        response.raise_for_status()
        prediction = response.json()
        predicted_mpg = prediction["mpg"]
        st.metric(label="Predicted Fuel Efficiency (MPG)", value=predicted_mpg)
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
