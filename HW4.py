# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:13:25 2018

@author: ox112
"""

import numpy as np
# import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd


# pick best order by aic 
# smallest aic value wins
best_bic = np.inf 
best_order = None
best_mdl = None

kospi200 = pd.read_csv('kospi200.csv')

print(kospi200.head())

y = kospi200['close']
print(y)

# i: optimal AR order?, j: optimal MA order?
best_bic = np.inf 
best_order = None
best_mdl = None


for i in range(5):
    for j in range(5):
        try:
            tmp_mdl = sm.tsa.ARMA(y, order=(i, j)).fit(method='mle', trend='nc')
            tmp_bic = tmp_mdl.bic
            if tmp_bic < best_bic:
                best_bic = tmp_bic
                best_order = (i, j)
                best_mdl = tmp_mdl
        except: continue


print('bic: {:6.5f} | order: {}'.format(best_bic, best_order))

######################

print(sm.tsa.adfuller(y,regression = "nc"))

