# In this project, Capital Asset Pricing Model is the main subject. 
# That is, finding the most efficient portfolio is what we are going to do here
# I'd like to deal with the portfolio of five companys: 'LG Electronics', 'Naver', 'KEPCO','KCTC','Yuhan'


import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as sco

prices_df = pd.DataFrame()
companys = {'066570.KS':'LG electronics','035420.KS':'NAVER','015760.KS':'KEPCO','009070.KS':'KCTC','000100.KS':'Yuhan'}
start = '2016-01-04'
end = '2022-06-01'
for i,code in enumerate(companys):
    prices_df[i] = yf.download([code],start, end)['Adj Close']
prices_df.columns = list(companys.values())

# Calculate log returns covariance matrix 
returns_daily= np.log(prices_df/prices_df.shift(1))[1:]
mean_returns = returns_daily.mean()
cov_daily = returns_daily.cov()

# Below is the function to get efficient frontier 
# 'optimize' from scipy library is used for calculating the least volatility given the return

def portfolio_daily_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) 
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix,weights)))  
    return std, returns

def portfolio_volatility(weights, mean_returns, cov_matrix):
    return portfolio_daily_performance(weights, mean_returns, cov_matrix)[0]

def efficient_return(mean_returns, cov_matrix, target):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    def portfolio_return(weights):
        return portfolio_daily_performance(weights, mean_returns, cov_matrix)[1]
    constraints = ({'type': 'eq', 'fun': lambda x: portfolio_return(x) - target},
                   {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0,1) for asset in range(num_assets))
    result = sco.minimize(portfolio_volatility, num_assets*[1./num_assets,], args=args, method='SLSQP', bounds=bounds, constraints=constraints)
    return result

def efficient_frontier(mean_returns, cov_matrix, returns_range):
    efficients = []
    for ret in returns_range:
        efficients.append(efficient_return(mean_returns, cov_matrix, ret))
    return efficients

# Simulate 50000 portfolios
port_returns = []
port_volatility = []
stock_weights = []
num_companys = len(companys)
num_portfolios = 50000
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_companys)
    weights /= np.sum(weights)
    returns = round(np.dot(weights, mean_returns),5)
    volatility = round(np.sqrt(np.dot(weights.T, np.dot(cov_daily, weights))),5)
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# Plotting 50000 portfolios and efficient frontier

portfolio = {'Returns':port_returns,'Volatility':port_volatility }
df = pd.DataFrame(portfolio)
plt.style.use('seaborn')
df.plot.scatter(x='Volatility',y='Returns')
target = np.linspace(0.0001, 0.0005, 50)
efficient_portfolios = efficient_frontier(mean_returns, cov_daily, target)
plt.plot([p['fun'] for p in efficient_portfolios], target, linestyle='-.',color='black',label='efficient frontier')
plt.xlabel('volatility')
plt.ylabel('returns')
plt.legend(labelspacing=0.8)

