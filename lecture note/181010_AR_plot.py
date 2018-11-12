# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:48 2018

@author: InChoi

X(t) = alpha*X(t-1) + a(t)
  a(t) ~ WN(0,1)

plot of X

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

alp = 0.999
ts_length = 10000
current_x = 0    # initial value of x
x_values = []   # series of x

for i in range(ts_length+1):
    x_values.append(current_x)
    current_x = alp * current_x + np.random.randn() # np.random.randn() generates a single data

g = sns.tsplot(x_values)
g.set_title( "AR(1) plot")
g.set_xlabel("t")
g.show()