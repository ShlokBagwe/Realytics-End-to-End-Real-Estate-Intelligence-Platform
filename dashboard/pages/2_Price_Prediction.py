import streamlit as st
import pandas as pd
import numpy as np
from utils import load_data, load_model

st.set_page_config(
    page_title="Mumbai Real Estate — Price Prediction",
    page_icon="💰",
    layout="wide",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
</style>
""", unsafe_allow_html=True)


df = load_data()
model = load_model()


with st.sidebar:
    st.markdown("## Mumbai Real Estate")
    st.markdown("---")
    st.markdown("Data: Mumbai Real Estate\n\n10,036 listings")


st.title("Price Prediction")
st.write("Enter property details below to estimate its market price.")

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Location", sorted(df["location"].dropna().unique()))
    buildup_area_sqft = st.number_input("Buildup Area (sqft)", min_value=100.0, max_value=15000.0, value=920.0, step=50.0)
    bhk = st.selectbox("BHK", [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], index=3)
    bathrooms = st.selectbox("Bathrooms", [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], index=1)
    balcony = st.selectbox("Balcony", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], index=1)

with col2:
    which_floor = st.selectbox("Which Floor", ["Lower", "Middle", "Higher", "Unknown"], index=1)
    furnishing = st.selectbox("Furnishing Status", ["Unfurnished", "Semi Furnished", "Fully Furnished", "Unknown"], index=1)
    age_category = st.selectbox("Property Age Category", ["New", "Relatively New", "Mid Age", "Old"], index=1)
    parking = st.selectbox("Parking Spots", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], index=1)

predict_btn = st.button("Predict Estimated Price", use_container_width=True)

if predict_btn:
    input_data = pd.DataFrame([{
        "bhk": bhk,
        "which_floor": which_floor,
        "bathrooms": bathrooms,
        "balcony": balcony,
        "parking": parking,
        "buildup_area_sqft": buildup_area_sqft,
        "furnishing": furnishing,
        "age_category": age_category,
        "location": location,
    }])

    try:
        pred_log = model.predict(input_data)[0]
        pred_price = np.expm1(pred_log)


        if pred_price < 2:
            margin = 0.15
        elif pred_price < 5:
            margin = 0.20
        else:
            margin = 0.40

        low_price = pred_price * (1 - margin)
        high_price = pred_price * (1 + margin)

        st.metric(
            label=f"**Estimated Market Price Range (Based on property configuration in {location})**",
            value=f"**₹ {low_price:.2f} Cr - ₹ {high_price:.2f} Cr**",
        )

    except Exception as e:
        st.error(f"Error making prediction: {e}")
