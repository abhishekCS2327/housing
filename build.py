
import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="House's Price")
st.title("Price of House")

filename = 'build.pkl'
if not os.path.exists(filename):
    st.error(f"File {filename} does not exist.")
else:
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        st.success("Model loaded successfully.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.header("Input Features")

# Input fields
area = st.text_input("Area")
try:
     area = float(area)
except ValueError:
     st.text("Please enter valid numerical values for area.")
    #  st.stop()
bedrooms = st.slider("Bedrooms", min_value=1, max_value=6, step=1)
bathroom = st.slider("Bathroom", min_value=1, max_value=4, step=1)
Stories = st.slider("Stories", min_value=1, max_value=4, step=1)
road = st.radio("Main Road", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
Gst_room = st.radio("Guest Room", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
basement = st.radio("Basement", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
h_water = st.radio("Water Heating", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
Ac = st.radio("Air conditioning", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
park = st.slider("Parking", min_value=0, max_value=3, step=1)
Prefarea = st.radio("Preference Area", options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])
# # Collect input into a dictionary and convert to DataFrame
# try:
furnishingstatus_mapping = {
    'furnished': 0,
    'semi-furnished': 1,
    'unfurnished': 2
}
Embarked_encoded = furnishingstatus_mapping[furnishingstatus]

test_input = {
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathroom],
        "stories": [Stories],
        "mainroad": [road],
        "guestroom": [Gst_room],
        "basement": [basement],
        "hotwaterheating": [h_water],
        "airconditioning": [Ac],
        "parking": [park],
        "prefarea": [Prefarea],
        "furnishingstatus": [Embarked_encoded],
        
    }
test_df = pd.DataFrame(test_input)
# except ValueError as ve:
#     st.error(f"Invalid input for area: {ve}")

if st.button("Predict"):
    try:
        prediction = model.predict(test_df)

        st.subheader("Prediction")
        st.write(f"The predicted price is: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")


