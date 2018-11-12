# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:34:43 2018

Ploting Random Walk

@author: ox112
"""

import numpy as np
import seaborn as sns  # 그래프를 꾸며 준다
import matplotlib.pyplot as plt

zero_mean_series = np.random.normal(loc = 0, scale = 1, size = 500)
# N(0,1)인 WN 500개를 generate

random_walk = np.cumsum(zero_mean_series)
# random walk는 사실 기존 WN의 cumulative sum과 같다

#random_walk += np.linspace(0,30,num = 500)  # randomwalk with drift

# 그래프 그리기
plt.figure(figsize = (5.5, 5.5))
g = sns.tsplot(random_walk)
g.set_title('Figure 1: Random Walk')
g.set_xlabel('Time Index')

plt.savefig('Random Walk.pdf', dpi =300, format = 'pdf')

