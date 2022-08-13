from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def get_data(x):
  global data_name
  data_name = x
  global df
  df = yf.download(x)

def show_data():
  print(df)

def plot_data():
  plt.figure(figsize = (20,10))
  plt.title('Plot of Stock price of {}'.format(data_name))
  plt.plot(df['Open'])
  plt.show()