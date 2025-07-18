# app.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scalers
model = joblib.load("xgb_fraud_model.pkl")
amount_scaler = joblib.load("amount_scaler.pkl")
time_scaler = joblib.load("time_scaler.pkl")

# Load known transactions
known_df = pd.read_csv("known_transactions.csv")

# Streamlit UI
st.set_page_config(page_title="💳 UPI Fraud Detection", layout="centered")

st.title("💳 UPI Fraud Detection System")
st.markdown("Enter UPI transaction details to check for fraud.")

amount = st.number_input("Transaction Amount (₹)", min_value=0.0, value=149.62, step=0.01)
time = st.number_input("Transaction Time (seconds since first)", min_value=0.0, value=0.02, step=0.01)

if st.button("Detect Fraud"):
    # Step 1: Check if time & amount match known transactions
    matched = known_df[(known_df["Time"] == time) & (known_df["Amount"] == amount)]

    if not matched.empty:
        row_class = matched.iloc[0]["Class"]
        if row_class == 0:
            st.success("✅ Legitimate Transaction (from training data)")
        else:
            st.error("❌ Fraudulent Transaction (from training data)")
    else:
        # Step 2: Use model prediction if not matched
        scaled_amt = amount_scaler.transform([[amount]])[0][0]
        scaled_time = time_scaler.transform([[time]])[0][0]

        prediction = model.predict([[scaled_amt, scaled_time]])[0]
        probability = model.predict_proba([[scaled_amt, scaled_time]])[0][1]

        if prediction == 1:
            st.error(f"❌ Predicted: Fraudulent Transaction (Confidence: {probability:.2%})")
        else:
            st.success(f"✅ Predicted: Legitimate Transaction (Confidence: {1 - probability:.2%})")
