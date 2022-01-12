# Monte Carlo Simulation

Monte Carlo simulations are a powerful method in numerous fields, including operations research, game theory, physics, mathematics, actuarial sciences, finance, among others. It is a technique used to measure risk and uncertainty when making a decision. To put it simple: a Monte Carlo simulation runs an enormous number of statistical experiments with random numbers generated from an underlying distribution based on a given time series. Brownian motion, or random walk, is the main driver for forecasting the future price.

## Output

<p align="center">
  <img src="https://i.imgur.com/VnCdhdf.png" width =800/>
    <em>5 Iterations</em>

</p>  
<br />
<p align="center">
  <img src="https://i.imgur.com/XG0SEOL.png" width =800/>
    <em>25 Iterations</em>
</p>  
<br />
<p align="center">
  <img src="https://i.imgur.com/aiseXIw.png" width =800/>
    <em>35 Iterations and 50 time intervals</em >

</p>  


## Method
The method consist in obtaining a mean and standard deviation from a given sample data (time series)

### Step 1: Import libraries
The pandas library is an open source BSD-licensed library that contains data
structures and operations to manipulate high-performance numeric values for the
Python programming language.

SciPy is a collection of mathematical algorithms and functions based on NumPy.
It has a series of commands and high-level classes to manipulate and display data.
With SciPy, functionality is added to Python, making it a data processing and
system prototyping environment similar to commercial systems such as MATLAB.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
```

### Step 2: obtain percentage variation and apply logarithm
After reading the .csv file, I undertake processing the close price data by obtaining its percentage variation and applying the natural logarithm.

```python
log_returns = np.log(1 + data.pct_change())
```


### Step 3: compute drift
The drift is the direction that rates of returns have had in the past, i.e., the expected return. This parameter is obtained from the mean and variance of the given sample.

```python
u = log_returns.mean()
var = log_returns.var()

drift = u - (0.5 * var)
```

### Step 4: generate brownian motion
Now the brownian motion can be created by generating the random distribution

```python
brownian_motion = norm.ppf(np.random.rand(t_intervals, iterations))
```

A `t_intervals * iterations` matrix is returned, containing the random contribution for the amount of
simulations that we want to perform and for the `t_intervals` that we want
to consider.
years.


### Step 5: compute the expected returns
The expected returns are the given by the natural exponential of the drift plus the volatility.

```python
daily_returns = np.exp(drift.values + stdev.values * brownian_motion)
```

*Observation: since we are dealing with large numbers, there is a high risk of occurring overflow. To deal with this, the natural logarithm of the percentage variation was obtained and then transformed back using the inverse (exponential function) after computing drift and volatility. This mathematical “trick” was used in order to avoid overflow error.*

### Step 6: compute the future price
The future price is then obtained by multiplying the price from the past time by the expected return.

```python
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
```

This operation is repeated until the desired future date is achieved and then repeated `t_intervals` times to achieve better accuracy. 
