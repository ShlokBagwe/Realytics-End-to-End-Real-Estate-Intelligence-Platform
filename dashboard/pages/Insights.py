import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Mumbai Real Estate - Insights",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
</style>
""", unsafe_allow_html=True)

location_coefs = {
    'South Mumbai': 0.4458,
    'Western Suburbs': 0.1570,
    'Western Suburbs East': 0.0300,
    'Thane / Navi Mumbai': -0.2545,
    'Outskirts': -0.4878
}

location_premium_df = pd.DataFrame(
    location_coefs.items(),
    columns=['Zone', 'Coefficient']
)

location_premium_df['Price Effect (%)'] = (
    np.expm1(location_premium_df['Coefficient']) * 100
).round(2)

location_premium_df = location_premium_df[
    ['Zone', 'Price Effect (%)']
].sort_values(
    by='Price Effect (%)',
    ascending=False
)

with st.sidebar:
    st.markdown("## Mumbai Real Estate")
    st.markdown("---")
    st.markdown("Data: Mumbai Real Estate\n\n10,036 listings")


st.title("Insights")
st.write("Get key insights which affects Price.")
st.markdown("---")

st.subheader(body = "📍 Location Premium Analysis")
st.dataframe(location_premium_df)
st.markdown("- Location is the strongest pricing driver. A comparable property in South Mumbai is expected to cost ~56% more than one in Central Mumbai, while properties in Outskirts trade at nearly 39% lower prices.")

st.markdown("---")

st.subheader("🏠 Bedroom Premium")
st.markdown("- Each additional BHK increases expected property prices by ~25%.")

st.markdown("---")

st.subheader("🏬 Area Impact")
st.markdown("- Every additional 100 sqft contributes only ~3.6% to property prices after controlling for location and BHK.")

st.markdown("---")

st.subheader("🔑 Ready To Move Premium")
st.markdown("- Ready-to-move properties command an ~8.5% premium over under-construction properties.")

st.markdown("---")

st.subheader("🛋️ Furnishing Impact")
st.markdown("- Furnishing status shows no statistically significant impact on price after accounting for location and configuration.")

st.markdown("---")

st.subheader("🏢 Floor Impact")
st.markdown("- Floor level has a weak negative effect (~2.4%) on price in this dataset.")

st.markdown("---")

st.markdown("""
## Key Conclusion

**Mumbai property prices are driven primarily by location, configuration (BHK), and property readiness. While factors such as furnishing and floor level have limited influence, location premiums can increase property values by over 50%. These insights help buyers, investors, and sellers understand the factors that contribute most to property valuation.**

""")