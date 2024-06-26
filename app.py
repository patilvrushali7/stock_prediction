import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Define feature names
features = [
    'open', 'high', 'low', 'close', 'tick_volume', 'spread', 'hour_of_day',
    'day_of_week', 'rolling_mean_5', 'rolling_mean_10', 'rolling_std_5',
    'rolling_std_10', 'open_lag_1', 'open_lag_2',
    'high_lag_1', 'high_lag_2', 'low_lag_1', 'low_lag_2',
    'close_lag_1', 'close_lag_2'
]

# Feature engineering functions
def add_lag_features(df):
    lags = 2
    lagged_columns = ['open', 'high', 'low', 'close']
    for col in lagged_columns:
        for lag in range(1, lags + 1):
            df[f'{col}_lag_{lag}'] = df[col].shift(lag)
    return df

def add_rolling_features(df):
    df['rolling_mean_5'] = df['close'].rolling(window=5).mean()
    df['rolling_mean_10'] = df['close'].rolling(window=10).mean()
    df['rolling_std_5'] = df['close'].rolling(window=5).std()
    df['rolling_std_10'] = df['close'].rolling(window=10).std()
    return df

# Streamlit app
st.title('HH/LL Prediction App')

# User inputs
time = st.text_input('Time (YYYY-MM-DD HH:MM)', '2023-01-09 00:00')
open_ = st.number_input('Open', value=1.08342)
high = st.number_input('High', value=1.08378)
low = st.number_input('Low', value=1.08342)
close = st.number_input('Close', value=1.08378)
tick_volume = st.number_input('Tick Volume', value=7)
spread = st.number_input('Spread', value=67)

# Convert time to datetime
try:
    time = pd.to_datetime(time)
    hour_of_day = time.hour
    day_of_week = time.dayofweek
except ValueError:
    st.warning("Please enter a valid date and time format (YYYY-MM-DD HH:MM)")
    hour_of_day = 0
    day_of_week = 0

# Create a DataFrame from inputs
input_data = pd.DataFrame({
    'open': [open_], 'high': [high], 'low': [low], 'close': [close],
    'tick_volume': [tick_volume], 'spread': [spread],
    'hour_of_day': [hour_of_day], 'day_of_week': [day_of_week]
})

# Feature engineering
input_data = add_rolling_features(input_data)
input_data = add_lag_features(input_data)

# Handle missing values
if input_data.isnull().any().any():
    st.warning("Please fill all input fields.")
else:
    input_data.fillna(method='ffill', inplace=True)
    input_data = input_data[features]
    
    # Prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.write('Stocks Predicted HH/LL Label:', 'HH' if prediction == 1 else 'LL')




