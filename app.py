import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('car_resale_price_prediction_rf.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the web app
st.title('Car Reselling Price Prediction')

# Get user input
age = st.number_input('Age of the car (in years)', min_value=0, max_value=50, value=5)
km_driven = st.number_input('Number of kilometers the car has been driven', min_value=0, max_value=1000000, value=10000)
fuel_type = st.selectbox('Fuel type of the car', ['Petrol', 'Diesel', 'CNG'])
transmission = st.selectbox('Gear transmission', ['Automatic', 'Manual'])
previous_owners = st.number_input('Number of previous owners', min_value=0, max_value=10, value=1)

# Preprocess the inputs to match the model's expected format
fuel_type_mapping = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
transmission_mapping = {'Manual': 0, 'Automatic': 1}

fuel_type_encoded = fuel_type_mapping[fuel_type]
transmission_encoded = transmission_mapping[transmission]

# Prepare the feature vector for prediction
features = np.array([age, km_driven, fuel_type_encoded, transmission_encoded, previous_owners]).reshape(1, -1)

# Make prediction
if st.button('Predict'):
    predicted_price = model.predict(features)[0]
    st.write(f'The predicted reselling price of the car is: ₹ {predicted_price:.2f}')

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
