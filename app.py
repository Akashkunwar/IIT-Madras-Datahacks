import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import date
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
import tensorflow as tf
import math
from sklearn.metrics import mean_squared_error
import streamlit as st

start = "2010-01-01"
end = date.today().strftime("%Y-%m-%d")

st.title('Stock market Prediction')
user_input = st.text_input('Enter Stock Name', 'RELIANCE.NS')
# df = data.DataReader(user_input, 'yahoo' , start, end)
df = yf.download(user_input, start, end)

st.subheader('Data from 2010 - till today')
st.write(df.describe())