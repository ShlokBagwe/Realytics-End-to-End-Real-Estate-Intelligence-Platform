# Realytics-End-to-End-Real-Estate-Intelligence-Platform
Realytics is an end-to-end data science platform for the Mumbai real estate market that combines price prediction, market analytics, and personalized recommendations using machine learning, deployed via Streamlit and AWS.

# Things done while Data Cleaning 
1. 1 RK units were encoded as 0.5 BHK to preserve the ordinal relationship and represent their smaller living configuration relative to standard 1 BHK units.
2. All prices were converted to Crore units.
3. Given property score based on furnishing, price_per_sqft, bathroom, and balcony.
