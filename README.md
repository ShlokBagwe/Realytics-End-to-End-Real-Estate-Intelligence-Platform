# 🏢 Realytics – End-to-End Real Estate Intelligence Platform

### AI-Powered Real Estate Analytics and Property Valuation Platform

Realytics is an end-to-end Data Science and Machine Learning project focused on Mumbai's real estate market. The platform combines data collected from multiple sources, advanced feature engineering, machine learning models, explainable AI techniques, and an interactive Streamlit dashboard to analyze market trends and estimate property prices.

---

## Dashboard Link: 
https://realytics-real-estate.streamlit.app/

---

## Overview

The project was developed to answer two key questions:

* What factors drive property prices in Mumbai?
* Given a property's characteristics, what should its market price be?

The platform provides market insights, exploratory analysis, and machine learning-powered property valuation through an interactive web application.

---

## Dataset Sources

### 99acres (Web Scraping)

Property listings were collected using Selenium from 99acres.

Extracted information included:

* Property Name
* Location
* Price
* Amenities
* Project Information
* Property Configuration

### Kaggle Mumbai Housing Dataset

Structured housing dataset containing:

* Price
* BHK
* Bathrooms
* Area
* Furnishing
* Parking
* Property Age
* Location

---

## Data Engineering

The project involved extensive preprocessing and standardization before model development.

### Data Collection and Integration

* Scraped property listings from 99acres using Selenium.
* Integrated scraped listings with a Kaggle Mumbai housing dataset.
* Standardized units, formats, and feature representations across both sources.

### Data Cleaning

* Price normalization and unit conversion
* Area standardization
* Parking extraction and parsing
* Floor categorization
* Property age extraction
* Location standardization
* Missing value treatment
* Duplicate removal
* Data quality validation

### Feature Engineering

Created and evaluated features such as:

* Property age categories
* Floor categories
* Price per square foot
* Property quality indicators
* Location-based features

### Feature Selection

Applied multiple feature selection techniques:

* Correlation Analysis
* Random Forest Feature Importance
* Gradient Boosting Importance
* Permutation Importance
* LASSO
* Recursive Feature Elimination (RFE)
* SHAP Explainability

---

## Exploratory Data Analysis

Performed:

### Univariate Analysis

* Price Distribution
* BHK Distribution
* Area Distribution
* Property Age Distribution

### Bivariate Analysis

* BHK vs Price
* Area vs Price
* Location vs Price
* Furnishing vs Price
* Floor vs Price

### Multivariate Analysis

* Correlation Heatmaps
* Location-wise Price Trends
* Price-per-Sqft Analysis
* Premium Location Analysis

### Key Findings

* Area is the strongest predictor of property prices.
* Location has a significant impact on valuation.
* Luxury properties exhibit different pricing behavior compared to standard properties.
* Property age has relatively lower influence compared to area and location.

---

## Machine Learning Pipeline

### Target Transformation

Property prices exhibited strong positive skewness.

Applied:

```python
np.log1p(price)
```

to improve model learning and reduce the impact of extreme luxury-property prices.

### Models Evaluated

* Linear Regression
* Ridge Regression
* LASSO Regression
* Support Vector Regression (SVR)
* Random Forest Regressor
* Extra Trees Regressor
* Multi-Layer Perceptron (MLP)
* XGBoost Regressor

### Model Evaluation

Models were evaluated using:

* 10-Fold Cross Validation
* R² Score
* MAE
* Residual Analysis

---

## Hyperparameter Optimization

Performed multiple optimization strategies:

### Randomized Search

Efficient exploration of large parameter spaces.

### Grid Search

Fine-grained parameter tuning around promising regions.

### Bayesian Optimization (Hyperopt)

Optimized key XGBoost parameters including:

* max_depth
* learning_rate
* n_estimators
* subsample
* colsample_bytree
* min_child_weight

---

## Final Model Performance

### Bayesian Optimized XGBoost

| Metric   | Score      |
| -------- | ---------- |
| R² Score | ~0.92      |
| MAE      | ~₹77 Lakhs |

Support Vector Regression (RBF Kernel) achieved performance close to XGBoost, highlighting strong nonlinear relationships within the housing market.

---

## Model Explainability

SHAP (SHapley Additive Explanations) was used to interpret model predictions and validate feature importance.

Key influential features included:

* Build-up Area
* Location
* BHK
* Bathrooms
* Parking

---

## Dashboard

An interactive Streamlit application was developed with the following modules:

### Market Analytics

* Location-wise price analysis
* Distribution analysis
* Market insights

### Property Valuation

* Property price prediction
* Confidence range estimation
* Feature-driven valuation

### Interactive Visualizations

* Plotly visualizations
* Comparative market analysis
* Location-based insights

---

## Tech Stack

**Programming Language**

* Python

**Data Processing**

* Pandas
* NumPy

**Visualization**

* Matplotlib
* Seaborn
* Plotly

**Machine Learning**

* Scikit-Learn
* XGBoost
* Hyperopt

**Explainable AI**

* SHAP

**Web Scraping**

* Selenium
* BeautifulSoup

**Deployment**

* Streamlit
* Joblib

---

## Key Learnings

* Data engineering and cleaning contributed significantly to overall project success.
* Feature engineering produced larger gains than switching machine learning algorithms.
* Location and area are the strongest drivers of property valuation.
* Explainability techniques are essential for validating model behavior and feature importance.
* Luxury properties remain challenging due to limited project-level and amenity-level information.

---

## Future Improvements

* Property recommendation system
* Geospatial modeling using latitude and longitude
* Property image analysis
* Real-time listing integration
* Additional luxury-property features

This version is closer to what I'd expect in a professional GitHub repository and accurately reflects the current state of the project without mentioning unimplemented components.
