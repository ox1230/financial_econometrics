# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:48 2018

@author: InChoi
"""

import numpy as np
from statsmodels.tsa.api import VAR

k=2  # # of unknowns
alp = np.matrix([[0.7, 0.2], [0, 0.3]])   # AR계수
ts_length =200    # T
current_X = np.matrix(np.zeros((k,1)))
x_values = []
for i in range(ts_length):
    e= np.matrix(np.random.randn(k,1))
    current_X = alp * current_X + e
    x_values.append(current_X)   
 
var_order=1
model = VAR(x_values)
results = model.fit(var_order)
print(results.summary())

