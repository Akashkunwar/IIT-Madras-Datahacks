import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
import tensorflow as tf
import math
from sklearn.metrics import mean_squared_error
print('done...')
df = pd.read_csv('df.csv')
close = df.Close

# Scaling data frame
scaler = MinMaxScaler(feature_range=(0,1))
close = scaler.fit_transform(np.array(close).reshape(-1,1))

##splitting dataframe
train_size = int(len(close)*0.70)
test_size = len(close)-train_size
train_df,test_df = close[0:train_size,:],close[train_size:len(close),:1]

def create_dataset(df, time_step=1):
	dfx, dfy = [], []
	for i in range(len(df)-time_step-1):
		a = df[i:(i+time_step), 0]
		dfx.append(a)
		dfy.append(df[i + time_step, 0])
	return np.array(dfx), np.array(dfy)

time_step = 100
X_train, y_train = create_dataset(train_df, time_step)
X_test, y_test = create_dataset(test_df, time_step)

# Reshaping input data to 3D shape for LSTM network

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)           
           
# Building LSTM model
model = Sequential()
model.add(LSTM(50,return_sequences = True,input_shape = (100,1)))
model.add(LSTM(50,return_sequences = True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss = 'mean_squared_error',optimizer = 'adam')

model.summary()
model.save('keras.h5')

# Fitting model to the training set 
model.fit(X_train,y_train,validation_data = (X_test,y_test),epochs = 100,batch_size = 50,verbose = 1)
           
# Making predictions and visualizing results    
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)


# Calculate RMSE metrics
print('Train RSME is',math.sqrt(mean_squared_error(y_train,train_predict)))
print('Test RSME is',math.sqrt(mean_squared_error(y_test,test_predict)))

# Plotting 
plt.figure(figsize = (20,10))

# shift train predictions for plotting
look_back = 100
trainPredictPlot = np.empty_like(close)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict

# shift test predictions for plotting
testPredictPlot = np.empty_like(close)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(close)-1, :] = test_predict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(close))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()