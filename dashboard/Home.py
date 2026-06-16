import streamlit as st
from utils import load_data


st.set_page_config(
    page_title="Mumbai Real Estate — Home",
    page_icon="🏙️",
    layout="wide",
)


st.markdown("""
<style>
    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
</style>
""", unsafe_allow_html=True)


df = load_data()


with st.sidebar:
    st.markdown("## Mumbai Real Estate")
    st.markdown("---")
    st.markdown("Data: Mumbai Real Estate\n\n10,036 listings")


st.title("Mumbai Real Estate")
st.subheader("Data Explorer")


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🏘️ Total Listings", f"{len(df):,}")
with col2:
    st.metric("📍 Unique Locations", df["location"].nunique())
with col3:
    avg_price = df["price"].mean()
    st.metric("💰 Avg Price (Cr)", f"₹ {avg_price:.2f}")
with col4:
    avg_area = df["buildup_area_sqft"].mean()
    st.metric("📐 Avg Area (sqft)", f"{avg_area:,.0f}")


st.subheader("About this Dashboard")
st.markdown("""
This app explores **Mumbai's residential real estate market** with over **10,000 property listings** across 100+ neighbourhoods.

Use the **Analytics** page from the sidebar to explore interactive charts, price distributions, location maps, and more.

* 🛏️ BHK 5+
* 📍 100+ Locations
* 🏗️ Furnishing Details
""")


st.markdown("### Data Preview")
st.dataframe(
    df.drop(columns=["latitude", "longitude", "is_ready_to_move"]).head(10),
    use_container_width=True,
    hide_index=True,
)