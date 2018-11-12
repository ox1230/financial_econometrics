# -*- coding: utf-8 -*-

import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_process import arma_generate_sample    #arma process를 generate 가능
import pandas as pd
import matplotlib.pyplot as plt


#Generate an ARMA process
# r(t) +bt(t-1) = a(t)+da(t-1)      
ar_params = np.array([1,-0.75])  #(1,b)
ma_params = np.array([1, 0.35]) #(1,d)
number_of_obs = 250

y = arma_generate_sample(ar_params,ma_params,number_of_obs)

print(type(y),y)

#Generage data with index
dates = sm.tsa.datetools.dates_from_range('1980m1',length = number_of_obs)

y = pd.Series(y, index = dates)
print(y.head())

plt.plot(y)

# ARMA model estimation
arma_mod = sm.tsa.ARMA(y,order = (1,1))
arma_result = arma_mod.fit(trend = 'c')   # disp: 음수이면 중간 과정 생략  , trend: 'c'/ 'nc'

print(arma_result.summary())
# 
