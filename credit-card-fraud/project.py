import streamlit as st
import pickle
import pandas as pd

# Load the saved model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Credit Card Fraud Detector")

def predict(input_data):
    df = pd.DataFrame([input_data])
    X_scaled = scaler.transform(df)  # Use the loaded scaler to scale the input data
    prediction = model.predict(X_scaled)
    return prediction[0]

# Define the user input fields
user_input = {
    'cc_num': st.number_input('Credit Card Number', min_value=0),
    'amt': st.number_input('Amount', min_value=0.0),
    'zip': st.number_input('Zip', min_value=0),
    'lat': st.number_input('Latitude', min_value=-90.0, max_value=90.0),
    'long': st.number_input('Longitude', min_value=-180.0, max_value=180.0),
    'city_pop': st.number_input('City Population', min_value=0),
    'unix_time': st.number_input('Unix Time', min_value=0),
    'merch_lat': st.number_input('Merchant Latitude', min_value=-90.0, max_value=90.0),
    'merch_long': st.number_input('Merchant Longitude', min_value=-180.0, max_value=180.0),
    'trans_year': st.number_input('Transaction Year', min_value=1900, max_value=2100),
    'trans_month': st.number_input('Transaction Month', min_value=1, max_value=12),
    'trans_day': st.number_input('Transaction Day', min_value=1, max_value=31),
    'trans_hour': st.number_input('Transaction Hour', min_value=0, max_value=23),
    'dob_year': st.number_input('Date of Birth Year', min_value=1900, max_value=2100),
    'age': st.number_input('Age', min_value=0),
    'num_gender': st.number_input('Number of Genders', min_value=0),
    'num_cat': st.number_input('Number of Categories', min_value=0),
    'num_state': st.number_input('Number of States', min_value=0),
    'num_mer': st.number_input('Number of Merchants', min_value=0),
    'num_city': st.number_input('Number of Cities', min_value=0),
    'num_street': st.number_input('Number of Streets', min_value=0),
    'num_job': st.number_input('Number of Jobs', min_value=0),
    'new_trans_num': st.number_input('Number of New Transactions', min_value=0),
    'num_first': st.number_input('Number of First Names', min_value=0),
    'num_last': st.number_input('Number of Last Names', min_value=0)
}

# When the 'CHECK' button is pressed
if st.button('CHECK'):
    prediction = predict(user_input)
    st.write(f'Prediction: {"Fraud" if prediction == 1 else "Not Fraud"}')
