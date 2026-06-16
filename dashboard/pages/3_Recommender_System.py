import streamlit as st
import pandas as pd
import numpy as np
from utils import load_recommender_data, load_recommender_model, load_recommender_matrix

st.set_page_config(
    page_title="Mumbai Real Estate — Price Prediction",
    page_icon="🏙️",
    layout="wide",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
</style>
""", unsafe_allow_html=True)

new_df = load_recommender_data()
model = load_recommender_model()
X_matrix = load_recommender_matrix()

new_df.drop(index=[2222, 6701], inplace=True, errors='ignore')
new_df = new_df.reset_index(drop=True)

with st.sidebar:
    st.markdown("## Mumbai Real Estate")
    st.markdown("---")
    st.markdown("Data: Mumbai Real Estate\n\n9,943 listings")


st.title("Flat Recommender")
st.write("Enter property details below.")



def filter_properties(new_df, project_name="Any", location="Any", bhk="Any", property_type="Any", furnishing="Any",
                    min_price=None,max_price=None):

    filtered_df = new_df.copy()

    filters = {
        "Project Name": project_name,
        "Area Name": location,
        "bedroom": bhk,
        "Type of Property": property_type,
        "furnished Type": furnishing
    }

    for col, value in filters.items():
        if value != "Any":
            filtered_df = filtered_df[filtered_df[col] == value]

    if min_price is not None:
      filtered_df = filtered_df[filtered_df["Price"] >= min_price]

    if max_price is not None:
      filtered_df = filtered_df[filtered_df["Price"] <= max_price]

    return filtered_df


def recommend_v2(property_idx, property_type, n=5):

    query_vector = X_matrix[property_idx].reshape(1, -1)


    distances, indices = model.kneighbors(query_vector, n_neighbors=n+1)


    rec_indices = indices[0][1:]
    rec_distances = distances[0][1:]

    results = new_df.iloc[rec_indices].copy()
    results = results.rename({"Property":"BHK"}, axis=1)

    if property_type != "Any":
        results = results[results["Type of Property"]==property_type]
        
    return results[[
        'Project Name', 'Area Name', 'BHK', 'Price',
        'bedroom', 'Type of Property', 'furnished Type'
    ]]



col1, col2 = st.columns(2)

with col1:
    project_names = ["Any"] + sorted(new_df["Project Name"].dropna().unique().tolist())
    select_project_name = st.selectbox("Project Name", project_names)

    locations = ["Any"] + sorted(new_df["Area Name"].dropna().unique().tolist())
    select_location = st.selectbox("Location", locations)

    bhk = ["Any"] + sorted(new_df["Property"].dropna().unique().tolist())
    select_bhk = st.selectbox("BHK", bhk)

with col2:
    property_type = ["Any"] + sorted(new_df["Type of Property"].dropna().unique().tolist())
    select_property_type = st.selectbox("Type of Property", property_type)

    furnishing = ["Any"] + sorted(new_df["furnished Type"].dropna().unique().tolist())
    select_furnishing = st.selectbox("Furnished Type", furnishing)

    min_val, max_val = st.slider(
        label="Price Range",
        min_value=new_df["Price"].min(), 
        max_value=float(new_df["Price"].max()),
        value=(new_df["Price"].min(), float(new_df["Price"].max())), 
        step=0.2
    )



if "search_results" not in st.session_state:
    st.session_state.search_results = None

Search = st.button(label="Search")

if Search:
    results = filter_properties(
        new_df,
        project_name=select_project_name,
        location=select_location,
        bhk=select_bhk,
        furnishing=select_furnishing,
        min_price=min_val,
        max_price=max_val,
        property_type=select_property_type
    ).copy()

    if not results.empty:
        results["label"] = (
            results["Project Name"] + " | " +
            results["Area Name"] + " | ₹" +
            results["Price"].astype(str) + " Cr | " +
            results["Property"].astype(str) + " BHK"
        )
        st.session_state.search_results = results
    else:
        st.session_state.search_results = results 

if st.session_state.search_results is not None:
    search_results = st.session_state.search_results

    if search_results.empty:
        st.warning("No properties found matching those filters.")
    else:
        selected_label = st.selectbox(
            "Select a property to find similar ones",
            search_results["label"],
        )

        # Get the df index of the selected property
        match = search_results[search_results["label"] == selected_label]
        if not match.empty:
            selected_property_index = match.index[0]
            recommendations = recommend_v2(selected_property_index, n=5, property_type=select_property_type)
            st.markdown("### Similar Properties")
            
            st.dataframe(recommendations, use_container_width=True)
        else:
            st.warning("Selected property not found. Please search again.")
