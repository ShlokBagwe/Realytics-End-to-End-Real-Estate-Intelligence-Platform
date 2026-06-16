import streamlit as st
import seaborn as sns
import plotly.express as px
from utils import load_data


st.set_page_config(
    page_title="Mumbai Real Estate — Analytics",
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


df = load_data()


with st.sidebar:
    st.markdown("## Mumbai Real Estate")
    st.markdown("---")
    st.markdown("Data: Mumbai Real Estate\n\n10,036 listings")


st.title("Analytics")
st.write("Explore price trends, location insights and property distributions.")

CHART_TEMPLATE = "plotly_dark"


st.markdown("#### Avg Price by Location — Map")

map_data = (
    df.dropna(subset=["latitude", "longitude"])
    .groupby("location")
    .agg(
        avg_price=("price", "mean"),
        latitude=("latitude", "mean"),
        longitude=("longitude", "mean"),
        listings=("price", "count"),
    )
    .reset_index()
    .rename(columns={"avg_price": "Avg Price (Cr)", "listings": "Listings"})
)

map_style = st.radio("Map Style", ["open-street-map", "carto-darkmatter"])

fig_map = px.scatter_mapbox(
    map_data,
    lat="latitude",
    lon="longitude",
    color="Avg Price (Cr)",
    size="Avg Price (Cr)",
    size_max=30,
    color_continuous_scale=["#ffffb2", "#fecc5c", "#fd8d3c", "#f03b20", "#bd0026"],
    mapbox_style=map_style,
    zoom=10,
    center={"lat": 19.09, "lon": 72.87},
    hover_name="location",
    hover_data={
        "Avg Price (Cr)": ":.2f",
        "Listings": True,
        "latitude": False,
        "longitude": False,
    },
    template=CHART_TEMPLATE,
    height=560,
)
fig_map.update_traces(marker=dict(opacity=0.85))
fig_map.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=0, b=0),
    coloraxis_colorbar=dict(
        title=dict(text="Price (Cr)", font=dict(color="white")),
        tickfont=dict(color="white"),
    ),
)
st.plotly_chart(fig_map, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Price Distribution")
    fig_price = px.histogram(
        df, x="price", nbins=60,
        color_discrete_sequence=["#8b5cf6"],
        template=CHART_TEMPLATE,
        labels={"price": "Price (Cr)"},
    )
    fig_price.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        bargap=0.05,
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=40),
    )
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    st.markdown("#### Listings by BHK")
    bhk_counts = df["bhk"].value_counts().sort_index().reset_index()
    bhk_counts.columns = ["BHK", "Count"]
    fig_bhk = px.bar(
        bhk_counts, x="BHK", y="Count",
        color="Count",
        color_continuous_scale="Purples",
        template=CHART_TEMPLATE,
    )
    fig_bhk.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=10, b=40),
    )
    st.plotly_chart(fig_bhk, use_container_width=True)


st.markdown("#### Average Price by Location (Most Listings)")

top_popular_names = df["location"].value_counts().head(15).index
top_locations = (
    df[df["location"].isin(top_popular_names)]
    .groupby("location")["price"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig_loc = px.bar(
    top_locations, x="price", y="location",
    orientation="h",
    color="price",
    color_continuous_scale="Purp",
    template=CHART_TEMPLATE,
    labels={"price": "Avg Price (Cr)", "location": "Location"},
)
fig_loc.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(autorange="reversed"),
    coloraxis_showscale=False,
    margin=dict(l=10, r=10, t=10, b=40),
    height=420,
)
st.plotly_chart(fig_loc, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Price vs Buildup Area")
    fig_scatter = px.scatter(
        df,
        x="buildup_area_sqft", y="price",
        color="bhk",
        color_continuous_scale="Purp",
        template=CHART_TEMPLATE,
        labels={"buildup_area_sqft": "Area (sqft)", "price": "Price (Cr)", "bhk": "BHK"},
        opacity=0.6,
    )

    fig_scatter.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=40),
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col4:
    st.markdown("#### Furnishing Type")
    furnishing_counts = df["furnishing"].value_counts().reset_index()
    furnishing_counts.columns = ["Type", "Count"]
    fig_pie = px.pie(
        furnishing_counts, names="Type", values="Count",
        color_discrete_sequence=px.colors.sequential.Purpor,
        template=CHART_TEMPLATE,
        hole=0.45,
    )
    fig_pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=40),
    )
    st.plotly_chart(fig_pie, use_container_width=True)
