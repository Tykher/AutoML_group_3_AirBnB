import streamlit as st
from joblib import load
import pandas as pd
import math

# Set page configuration and layout
st.set_page_config(page_title='Airbnb Price Calculator', page_icon=':house:', layout='wide')

# Define colors
BACKGROUND_COLOR = "#1E1E1E"
TEXT_COLOR = "#FFFFFF"
INPUT_BACKGROUND_COLOR = "#FFFFFF"
BUTTON_COLOR = "#FFD700"

# Custom styles
st.markdown("""
    <style>
        /* General styles */
        .reportview-container {
            background-color: #1E1E1E;
        }
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
        }
        h1, h2, h3, h4, h5, h6, .caption, .stTextInput, .stSelectbox, .stTextArea, .stSlider, .stNumberInput {
            color: #FFFFFF;
        }

        /* Styles for buttons */
        .stButton > button {
            background-color: #FFD700;
            color: #1E1E1E;
            border: none;
        }

        /* Overriding checkbox styles */
        .stCheckbox .checkbox {
            background-color: #1E1E1E !important;
            border-color: #1E1E1E !important;
        }
        
        /* Overriding selectbox styles */
        .stSelectbox .selectbox {
            background-color: #1E1E1E !important;
            border-color: #1E1E1E !important;
        }

        /* Overriding the specific background color for the options in the select dropdown */
        .stSelectbox .css-2b097c-container .css-26l3qy-menu {
            background-color: #1E1E1E !important;
        }

        /* Overriding radio button styles, if you have any */
        .stRadio .radio {
            background-color: #1E1E1E !important;
            border-color: #1E1E1E !important;
        }
    </style>
""", unsafe_allow_html=True)
model_filename = '../rf_hyper_model.joblib'
feature_names = ['person_capacity', 'multi', 'biz', 'cleanliness_rating', 'guest_satisfaction_overall', 'bedrooms', 'dist', 'metro_dist', 'city', 'host_is_superhost', 'room_type']
model = load(model_filename)

# Define the form and form fields
with st.form("price_calculator"):
    st.markdown("## Airbnb Price Calculator")
    cities = ['Amsterdam', 'Athens', 'Barcelona', 'Berlin', 'Budapest', 'Lisbon', 'London', 'Paris', 'Rome', 'Vienna']
    room_types = ['Entire place', 'Private room', 'Shared room']
    city = st.selectbox('City', cities, index=0)
    multiple_rooms = st.checkbox('Multiple Rooms')
    capacity = st.number_input('Capacity', min_value=1, max_value=10, value=2, step=1)
    bedrooms = st.number_input('Bedrooms', min_value=1, max_value=5, value=1, step=1)
    cleanliness = st.slider('Cleanliness', min_value=1, max_value=5, value=3, step=1)
    distance_to_city_center = st.number_input('Distance to City Center (km)', value=0.0)
    distance_to_metro_station = st.number_input('Distance to Metro Station (km)', value=0.0)
    room_type = st.selectbox('Room Type', room_types, index=0)
    business = st.checkbox('Business')
    super_host = st.checkbox('Super Host')
    satisfaction_rating = st.slider('Satisfaction Rating', min_value=1, max_value=100, value=80, step=1)
    
    # Calculate button
    calculate_button = st.form_submit_button("Calculate")
    


if calculate_button:
    input = [capacity, multiple_rooms, business, cleanliness, satisfaction_rating, bedrooms, distance_to_city_center, distance_to_metro_station, cities.index(city), super_host, room_types.index(room_type)]
    sample_input_df = pd.DataFrame([input], columns=feature_names)
    price = model.predict(sample_input_df)
    price = math.floor(price/2)
    st.markdown(f"<h3>Price (€): {price}</h3>", unsafe_allow_html=True)
