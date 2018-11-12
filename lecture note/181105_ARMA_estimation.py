# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:48 2018

@author: InChoi
"""

import numpy as np
# import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample

# Generate an ARMA process
arparams = np.array([.75])
maparams = np.array([.3])

arparams = np.r_[1, -arparams]
maparams = np.r_[1, maparams]
nobs = 250
y = arma_generate_sample(arparams, maparams, nobs)

# Generate data with index
dates = sm.tsa.datetools.dates_from_range('1980m1', length=nobs)
y = pd.Series(y, index=dates)

n = 5000
burn = 2000

# pick best order by aic 
# smallest aic value wins
best_aic = np.inf 
best_order = None
best_mdl = None

# i: optimal AR order?, j: optimal MA order?
for i in range(5):
    for j in range(5):
        try:
            tmp_mdl = sm.tsa.ARMA(y, order=(i, j)).fit(method='mle', trend='nc')
            tmp_aic = tmp_mdl.aic
            if tmp_aic < best_aic:
                best_aic = tmp_aic
                best_order = (i, j)
                best_mdl = tmp_mdl
        except: continue


print('aic: {:6.5f} | order: {}'.format(best_aic, best_order))

