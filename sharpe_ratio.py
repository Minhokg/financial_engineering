import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
import random
from scipy import stats
from scipy.stats import norm

prices_df = pd.DataFrame()
companys = {'066570.KS':'LG electronics','035420.KS':'NAVER','015760.KS':'KEPCO','005930.KS':'Samsung Electronics','000100.KS':'Yuhan'}
start = '2016-01-04'
end = '2022-06-01'
for i,code in enumerate(companys):
    prices_df[i] = yf.download([code],start, end)['Adj Close']
prices_df.columns = list(companys.values())

# Get log returns 
returns = np.log(prices_df/prices_df.shift(1))[1:]

# Below function is to calculate a standard deviation and a return of a portfolio.
def portfolio_daily_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) 
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix,weights)))  
    return std, returns
  
# And the next function is for generating portfolio simulations.
# Weights are sampled from a standard normal distribution and sum to 1 
def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((3,num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(5)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_daily_performance(weights, mean_returns, cov_matrix)
        results[0,i] = round(portfolio_std_dev,6)
        results[1,i] = round(portfolio_return,6)
        #This function also gives us a sharpe ratio like below
        # Later, through this, we will find the maximum sharpe ratio. And that is the porfolio what we was looking for. 
        results[2,i] = (portfolio_return - risk_free_rate)/portfolio_std_dev 
    return results, weights_record
  
  
# And the below function is the finish line. 
# It exports two efficient porfolios based on 'sharpe ratio' and 'minimum of volatility'
# Also the function draw portfolio simulations and dot the two optimal efficient portfolio
# We have to fix returns of portfolios. 
# In this project, I'd like to find out the best portfolio with the 'Yuhan' sample mean.
def efficient_portfolio_yuhan(mean_returns,cov_matrix,num_portfolios,risk_free_rate):
    results, weights = random_portfolios(num_portfolios, mean_returns, cov_matrix,risk_free_rate)
    valid_idx = np.where(results[1]==mean_returns['Yuhan'])[0] # This is a step for trimming portolios with the same sample mean as 'Yuhan' 
    max_sharpe_idx = valid_idx[results[2,valid_idx].argmax()] # By using 'argmax', we are trying to find out the maximum sharpe ratio.
    sdp_max,return_Yuhan = results[0,max_sharpe_idx], mean_returns['Yuhan']
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx],index=prices_df.columns,columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i,2) for i in max_sharpe_allocation.allocation]
    max_sharpe_allocation = max_sharpe_allocation.T
    # Below is the part for the minimum volatility process 
    min_vol_idx = valid_idx[results[0,valid_idx].argmin()]
    sdp_min, return_Yuhan = results[0,min_vol_idx], mean_returns['Yuhan'] 
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx],index=prices_df.columns,columns=['allocation'])
    min_vol_allocation.allocation = [round(i,2) for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T
    
    print ('-'*80)
    print ('Maximum Sharpe Ratio Portfolio Allocation\n')
    print ('Return:', round(return_Yuhan,6))
    print ('Volatility', round(sdp_max,6))
    print ("\n")
    print (max_sharpe_allocation)   
    print ('-'*80)

    print ('Minimum Volatility Portfolio Allocation\n')
    print ('Return: ',round(return_Yuhan,6))
    print ('Volatility:',round(sdp_min,6))
    print ("\n")
    print (min_vol_allocation)
    
    plt.figure(figsize = (10,7))
    plt.scatter(results[0,:],results[1,:],marker='o')
    plt.scatter(sdp_max,return_Yuhan,marker='*',color='r',s=500,label = 'Maximum Sharpe ratio')
    plt.scatter(sdp_min, return_Yuhan, marker='*',color='g',s=500, label='Minimum volatility')
    plt.xlabel('volatility')
    plt.ylabel('returns')
    plt.legend(labelspacing=0.8)
    return return_Yuhan,sdp_max,max_sharpe_allocation.loc['allocation'].values

# Now, let's assume an annual risk free rate as 0.02. And we need to convert it to a daily risk free rate
daily_risk_free_rate = (1+0.02)**(1/365) - 1

# And the sample mean and the sample covariance matrix are as follow
# Also, I'd like to generate 50000 simulations
# Last, get those guys into our function
mean_returns = round(returns.mean(),6) 
cov_matrix = round(returns.cov(),6) 
num_portfolios = 50000
mean_portfolio, sdp_max, allocation = efficient_portfolio_yuhan(mean_returns, cov_matrix, num_portfolios, risk_free_rate=daily_risk_free_rate)








