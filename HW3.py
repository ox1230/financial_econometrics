# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:06:39 2018

@author: ox112
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa import stattools

### 1

def getS(xLists):
  """ get test statistics of skewness of xLists"""
  mu = np.mean(xLists)
  sigma = np.var(xLists) ** 0.5
  
  tripleSum = 0
  for x in xLists:
    tripleSum += (x - mu)**3
    
  skew = tripleSum/( (len(xLists)-1)*(sigma**3) )
  return skew/ ((6/len(xLists)**0.5)) 

def getK(xLists):
  """get test statistics of kurtosis of xLists"""
  mu = np.mean(xLists)
  sigma = np.var(xLists) ** 0.5
  
  quadraSum = 0
  for x in xLists:
    quadraSum += (x-mu)**4
  
  kurto = quadraSum/( (len(xLists)-1)*(sigma **4) )
  
  return (kurto-3)/( (24/len(xLists))**0.5 )

def getJB(xLists):
  return getS(xLists)**2 + getK(xLists)**2

xLists = np.random.randn(100) 
print(getK(xLists))
print(getS(xLists))
print(getJB(xLists))


#2번

kospi = pd.read_csv('kospi.csv',dtype={'date':str,'KOSPI':float})
print(kospi.head())

print("test the null of symmetry")
if -1.96< getS(kospi['KOSPI']) <1.96:
  print("Do not Reject H0: symmetry")
else:
  print("Reject H0: asymmetry")

print("test the null of normal tails")
K = getK(kospi['KOSPI'])
if K < -1.96:
  print("Reject H0: thin tail")
elif K > 1.96:
  print("Reject H0: thick tail")
else:
  print("Do not Reject H0: normal tail")

print("tes the null of normality")
if getJB(kospi['KOSPI']) > 5.99 :
  print("Reject H0: not normal")
else:
  print("Do not Reject H0: normal")

n_nlags=40
atcf_qs =stattools.acf(kospi['KOSPI'],\
                       unbiased=True, nlags=n_nlags,
                       qstat=True, fft=False, alpha=None, missing='none')
    
plt.bar(range(n_nlags+1),atcf_qs[0])

print(atcf_qs[2])   # Ljung-Box test 결과의 p-value

#3번
def getPV(n,FV, pmt = 0, r = 0.04):
  """ get PV of bonds,  
  n: period, pmt: coupon, FV: face value, r = discount factor"""
  
  PV = 0
  for i in range(1,n+1):
    PV += pmt/ ((1+r)**i)
  
  PV += FV/ ((1+r)**n)
  return PV


print(getPV(5,100000000,2000000,0.04)) #2015~ 2019: 5번, n=4, FV = 100000000, pmt = 2000000, r = 0.04



# 4번
diff_kospi = np.diff(np.log(kospi['KOSPI']))
print(diff_kospi)

n_nlags=40
atcf_qs =stattools.acf(diff_kospi,\
                       unbiased=True, nlags=n_nlags,
                       qstat=True, fft=False, alpha=None, missing='none')
    
plt.bar(range(n_nlags+1),atcf_qs[0])

print(atcf_qs[2])   # Ljung-Box test 결과의 p-value

