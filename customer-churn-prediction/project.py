import streamlit as st
import pickle
import pandas as pd

# Load the saved model and scaler
model = pickle.load(open('model.pkl', 'rb'))

st.title("Customer Churn Prediction")

def predict_churn(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]

geography_germany = st.selectbox("Geography Germany",["True","False"])
geography_germany = 1 if geography_germany == "True" else 0

geography_spain = st.selectbox("Geography Spain",["True","False"])
geography_spain = 1 if geography_spain == "True" else 0

gender_male = st.selectbox("Gender Male",["True","False"])
gender_male = 1 if gender_male == "True" else 0

user_input = {
    "credit_score": st.number_input("Credit Score", min_value=0, value=600),
    "age": st.number_input("Age", min_value=0, value=30),
    "tenure": st.number_input("Tenure (Years)", min_value=0, max_value=10, value=5),
    "balance": st.number_input("Balance", min_value=0.0, value=0.0),
    "num_of_products": st.number_input("Number of Products", min_value=1, max_value=4, value=1),
    "has_cr_card": st.number_input("Has Credit Card?", min_value=0,max_value=1,value=1),
    "is_active_member": st.number_input("Is Active Member?",min_value=0,max_value=1,value=1),
    "estimated_salary": st.number_input("Estimated Salary", min_value=0.0, value=50000.0),
    "geography_germany": geography_germany,
    "geography_spain": geography_spain,
    "gender_male": gender_male
}


if st.button('CHECK'):
    prediction = predict_churn(user_input)
    st.write(f'Churn Prediction: {"Churn" if prediction == 1 else "No Churn"}')