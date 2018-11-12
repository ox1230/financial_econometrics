# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:05:10 2018

@author: InChoi

Purpose: Plotting autocorrelation function
"""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa import stattools


# Generate data
alp = 0.5
ts_length = 500
current_x = 0
x_values = []
for i in range(ts_length+1):
    x_values.append(current_x)
    current_x = alp * current_x + np.random.randn() 
    # np.random.randn() generates a single data

# Calculate ACF, q-stat and plot ACF
n_nlags=40
atcf_qs =stattools.acf(x_values,\
                                       unbiased=True, nlags=n_nlags,
                                       qstat=True, fft=False, alpha=None, missing='none')
   # atcf[0] ((n_nlags+1) by 1) contains values of ACF, 
   # atcf[1] (n_nlags by 1) those of q-stat, and atcf[3] p-values of the q-stat  ~ qstat=True
    
temp_acf = n_nlags +1
plt.figure(figsize = (10,10))
g = sns.barplot(x = list(range(temp_acf)) , y = atcf_qs[0])
g.set_xlabel("lag")

g.show()

