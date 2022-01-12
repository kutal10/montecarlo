# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Settings for Monte Carlo asset data, how long, and how many forecasts
ticker = 'Stock Price'  # ticker
t_intervals = 30  # time steps forecasted into future
iterations = 5  # amount of simulations
file_name = 'NVDA Historical Data.csv'

# Acquiring data
data = pd.read_csv(file_name, index_col=0, usecols=['Date', 'Price'])
data = data.rename(columns={"Price": ticker})

# Preparing log returns from data
log_returns = np.log(1 + data.pct_change())

# Setting up drift and random component in relation to asset data
u = log_returns.mean()
var = log_returns.var()

# drift represents the trend of a long term asset in the market
drift = u - (0.5 * var)
stdev = log_returns.std()


# setting up seed to make results reproducible
np.random.seed(7)

# convert each generated array value to its quantile value
brownian_motion = norm.ppf(np.random.rand(t_intervals, iterations))

# solution to stochastic equation on a logarithmic scale
# measure of the change that occurred in a stock's price expressed as a percentage of the previous day's closing price
daily_returns = np.exp(drift.values + stdev.values * brownian_motion)

# Takes last data point as startpoint point for next iteration
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0

# Applies Monte Carlo simulation in asset
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

# Plot simulations
plt.style.use('dark_background')
plt.figure(figsize=(10, 6))
plt.plot(price_list)
plt.title("Nvidia Simulation")
plt.xlabel("Future Timesteps")
plt.ylabel("Equity Price")
# plt.show()
