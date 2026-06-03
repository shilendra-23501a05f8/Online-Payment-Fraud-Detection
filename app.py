import streamlit as st
import pickle
import pandas as pd
metrics = pickle.load(open("model_metrics.pkl", "rb"))

# Load trained model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("💳 Online Payment Fraud Detection")
st.link_button(
    "🔗 View Project on GitHub",
    "https://github.com/shilendra-23501a05f8/Online-Payment-Fraud-Detection"
)

st.write("Enter transaction feature values to predict fraud.")

# EXACT feature list used during training
feature_names = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7',
    'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14',
    'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26',
    'V27', 'V28', 'normAmount'
]

st.subheader("Transaction Features")

# Collect inputs
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(
        feature,
        value=0.0,
        format="%.6f"
    )

# Predict
if st.button("Predict"):
    input_df = pd.DataFrame([input_data])  # ✅ THIS LINE FIXES THE ERROR
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")


st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", f"{metrics['Accuracy']*100:.2f}%")
col2.metric("Precision", f"{metrics['Precision']*100:.2f}%")
col3.metric("Recall", f"{metrics['Recall']*100:.2f}%")

col4, col5 = st.columns(2)
col4.metric("F1 Score", f"{metrics['F1 Score']:.3f}")
col5.metric("ROC AUC", f"{metrics['ROC AUC']:.3f}")

