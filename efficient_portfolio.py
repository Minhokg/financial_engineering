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

# Calculate Log returns 
# Covariance Matrix 
