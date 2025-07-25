import streamlit as st
import joblib
import numpy as np

# Load model and other assets
model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")
symptom_list = joblib.load("symptom_list.pkl")

# Streamlit App UI
st.title("🩺 AI-Powered Personal Health Assistant")
st.write("Select your symptoms to get an AI-generated diagnosis insight.")

selected_symptoms = st.multiselect("Choose symptoms", symptom_list)

if st.button("Get Diagnosis Insight"):
    input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptom_list]
    input_array = np.array([input_data])
    prediction = model.predict(input_array)[0]
    diagnosis = le.inverse_transform([prediction])[0]

    st.success(f"🧠 Predicted Condition: **{diagnosis}**")
    st.info("Note: This is an AI suggestion. Always consult a healthcare professional.")
