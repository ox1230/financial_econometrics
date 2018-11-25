# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:20:56 2018

@author: ox112
"""

from arch import arch_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#데이터 불러오기
sp500 = pd.read_csv("sp500_2018.csv")
print(sp500.head())

#종가(Close)의 수익률 구하
returns = np.diff(np.log(sp500['Close']))

xaxis = []   # x축을 위한 데이터를 정리하는 과정  ( 각 월의 첫번째 거래일만 x축에 표시한다.)
for month in range(1,12): 
  appended_date = "2018-"+ "{:02d}".format(month)+"-01"
  if appended_date not in list(sp500['Date']): 
    appended_date = "2018-"+ "{:02d}".format(month) +"-02"
    if appended_date not in list(sp500['Date']): 
      appended_date = "2018-"+ "{:02d}".format(month) +"-03"
      if appended_date not in list(sp500['Date']): 
        appended_date = "2018-"+ "{:02d}".format(month) +"-04" 
    
  xaxis.append(appended_date)

plt.figure(figsize=(20,10))  # figure의 크기 조절
plt.plot(sp500['Date'][:-1],returns)
plt.xticks(xaxis)  #xaixs의 데이터만 x축에 표시함
plt.show()

am = arch_model(returns) 
res = am.fit(update_freq=5)
print(res.summary())

fig = res.plot(annualize='D')
