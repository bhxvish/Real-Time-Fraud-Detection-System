import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")
st.title("Real-Time Fraud Detector")
st.markdown("Enter transaction details to check for fraud:")
type_map = {"TRANSFER":0, "CASH_OUT":1}
transaction_type = st.selectbox("Transaction Type", list(type_map.keys()))
amount = st.number_input("Transaction Amount", min_value = 0.0, step=10.0)
oldbalanceOrg = st.number_input("Sender Balance Before Transaction", min_value=0.0, step = 10.0)
oldbalanceDest = st.number_input("Receiver Balance Before Transaction", min_value = 0.0, step = 10.0)
if st.button("Predict Fraud"):
    input_data = np.array([type_map[transaction_type], amount, oldbalanceOrg, oldbalanceDest])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Looks like a Fraudlent Transaction!")
    else:
        st.success("Transaction is Safe!")