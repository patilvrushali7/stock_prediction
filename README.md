

# Stock Price Prediction Project

## Overview

This project aims to predict high (HH) or low (LL) stock prices based on historical data and various features.

## Table of Contents

- [Features](#features)
- [Models Explored](#models-explored)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Features

- Historical stock data preprocessing
- Machine learning model training (Random Forest, Logistic Regression, etc.)
- Feature engineering (lagged features, rolling statistics)
- Deployment using Streamlit

## Models Explored

- **Random Forest**: Used for initial prediction due to its robustness with noisy data.
- **Logistic Regression**: Explored for its interpretability and efficiency with binary classification tasks.

## Project Structure

The project structure is organized as follows:
stock_prediction/

- app.py # Streamlit application for model deployment
- model.py.ipynb # Jupyter notebook containing model training and feature engineering
- random_forest_model.pkl # Pickled file of the trained Random Forest model
- requirements.txt # Python dependencies required to run the project

 ## Accuracy and Evaluation Metrics

The accuracy metric measures the overall correctness of the predictions made by the models.


## Deployment

To deploy the model locally:

1. Clone the repository:

git clone https://github.com/your_username/stock_prediction.git
cd stock_prediction


2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py



