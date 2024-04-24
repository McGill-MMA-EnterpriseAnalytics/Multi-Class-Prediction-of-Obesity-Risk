import streamlit as st
import requests
import json

# Define the FastAPI endpoint
url = "http://20.253.116.228/predict"

# Create form to input data
with st.form(key='my_form'):
    id_field = st.number_input('ID', value=0)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    age = st.slider('Age', min_value=18, max_value=100, value=25)
    height = st.number_input('Height (meters)')
    weight = st.number_input('Weight (kg)')
    family_history_with_overweight = st.selectbox('Family history of overweight', ['yes', 'no'])
    favc = st.selectbox('Frequent consumption of high caloric food', ['yes', 'no'])
    fcvc = st.slider('Frequency of vegetables consumption', min_value=1, max_value=3, value=2)
    ncp = st.number_input('Number of main meals', value=3.0)
    caec = st.selectbox('Consumption of food between meals', ['Never', 'Sometimes', 'Frequently', 'Always'])
    smoke = st.selectbox('Smoking', ['yes', 'no'])
    ch2o = st.number_input('Consumption of water daily (liters)', value=2.0)
    scc = st.selectbox('Calories consumption monitoring', ['yes', 'no'])
    faf = st.number_input('Physical activity frequency (times per week)', value=1.0)
    tue = st.number_input('Time using electronic devices (hours per day)', value=2.0)
    calc = st.selectbox('Consumption of alcohol', ['Never', 'Sometimes', 'Frequently', 'Always'])
    mtrans = st.selectbox('Transportation used', ['Automobile', 'Motorbike', 'Bike', 'Public_Transportation', 'Walking'])

    submit_button = st.form_submit_button(label='Predict')

# Handle form submission
if submit_button:
    # Construct the request payload
    data = {
        "id": id_field,
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }

    # Send a post request to the server
    response = requests.post(url, json=data)
    result = response.json()

    # Display the prediction result
    st.write('Prediction:', result)
