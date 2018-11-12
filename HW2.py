# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:43:25 2018

@author: ox112
"""
import numpy as np

#1번
u = np.array([[1,1,2,3,5,8]])
v = np.array([
                [1],
                [1],
                [2],
                [3],
                [5],
                [8]])
x = np.array([[1,0],[0,1]])
y = np.array([[1,2],[3,4]])
z = np.array([[1,2,1,2],[3,4,3,4],[1,2,1,2]])
w = np.array([[x,x],[y,y]])

u+v.T
v+u.T
v@u
u@v
x@y

# no.2
np.arange(11)
np.arange(4,14)
np.linspace(0,1,5)

# 3번
y = [0,0.5,1.5,2.5,1.0,1.001,-0.5,-1,-1.5,-2.5]
np.round(y)
np.ceil(y)
np.floor(y)

# 4번
x = [-42,-9,-8,10]
y = np.sort(x)
x.sort()
x

#5번
y= [np.nan, 2.2,3.9,4.6,np.nan,2.4,6.1,1.8]
N = sum(1-np.isnan(y))    # y의 nan을 제외한 원소의 수
y_bar = np.nansum(y) / N    # y의 nan을 제외한 원소의 평균
squared_sum = np.nansum((y-y_bar)**2) # squared_sum
var = squared_sum / (N-1)   # 분산
print(var)

#6번
print(np.zeros((10,5)))
print(np.ones((10,5)))

#7번
I = np.eye(5)
print(I)
print(np.exp(I))

#8번
N=5
print(np.diag(np.ones(N)))

#9번
x = np.arange(12)
print(np.reshape(x,(1,12)))
print(np.reshape(x,(2,6)))
print(np.reshape(x,(3,4)))
print(np.reshape(x,(6,2)))
print(np.reshape(x,(2,2,3)))


#15번

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gspc = pd.read_csv('gspc.csv')   # 1998-08-31 ~ 2018-08-31의 s&p500 지수
print(gspc.head())


xaxis = []   # x축을 위한 데이터를 정리하는 과정  ( 각 연도의 8월 마지막 거래일만 x축에 표시한다.)
for year in range(1998,2019): 
  appended_date = str(year)+ "-08-31"
  if appended_date not in list(gspc['Date']): 
    appended_date = str(year) + "-08-30"
    if appended_date not in list(gspc['Date']): appended_date = str(year) + "-08-29" 
    
  xaxis.append(appended_date)



plt.figure(figsize=(25,10))  # figure의 크기 조절
plt.plot('Date','Close',data = gspc)
plt.xticks(xaxis)  #xaixs의 데이터만 x축에 표시함
plt.show()
plt.savefig('graph.jpg')

