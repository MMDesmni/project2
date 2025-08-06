#Importing temporary libraries

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

#Download Bitcoin price data for the last 3 months
btc = yf.download("BTC-USD", period="3mo")
prices = btc['Close']
dates = btc.index

#Declaring variables

step = 7
lows_x = []
lows_y = []

#Finding highs using for loop and price

for i in range(0, len(prices), step):
    window = prices[i:i+step]
    if len(window) == 0:
        continue
    min_idx = window.idxmin()
    lows_x.append(min_idx)
    lows_y.append(prices.loc[min_idx])

#Declaring variables

highs_x = []
highs_y = []

#Finding lows using for loop and price

for i in range(0, len(prices), step):
    window = prices[i:i+step]
    if len(window) == 0:
        continue
    max_idx = window.idxmax()
    highs_x.append(max_idx)
    highs_y.append(prices.loc[max_idx])

plt.figure(figsize=(14, 6))
plt.plot(dates, prices, label='Bitcoin Price', color='black')

#Plotting hihgs and lows
 
plt.plot(lows_x, lows_y, 'g--', linewidth=2, label='Support Trendline (Lows)')
plt.scatter(lows_x, lows_y, color='green', label='Local Lows')
plt.plot(highs_x, highs_y, 'r--', linewidth=2, label='Resistance Trendline (Highs)')
plt.scatter(highs_x, highs_y, color='red', label='Local Highs')

#Plotting the price chart and Trendline together

plt.title('Bitcoin Price with Support & Resistance Trendlines')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()