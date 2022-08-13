# ̥
# # !pip install yfinance
# # importing liberary
# from datetime import datetime
# import yfinance as yf
# import matplotlib.pyplot as plt

# # Downloading Data
# df = yf.download('RELIANCE.NS')

# # Plotting graph 
# plt.figure(figsize = (20,10))
# plt.title('Price ')
# plt.plot(df['Open'])
# plt.show()
# print(df)

import functions as fn
fn.get_data('RELIANCE.NS')
fn.show_data()
fn.plot_data()