import streamlit as st
import pandas as pd
import joblib


@st.cache_data
def load_data():
    return pd.read_csv("cord_real_estate.csv")


@st.cache_resource
def load_model():
    return joblib.load("best_xgb_model_v2.joblib")


@st.cache_resource
def load_model2():
    return joblib.load("best_bayesian_xgb_model.joblib")


# Recommender System
def load_recommender_data():
    return pd.read_csv("Final RS Dataset.csv")

@st.cache_resource
def load_recommender_model():
    return joblib.load("latest_weighted_nn_model.joblib")

@st.cache_resource
def load_recommender_matrix():
    return joblib.load("latest_X_weighted_matrix.joblib")