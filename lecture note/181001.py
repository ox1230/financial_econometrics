# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:28:09 2018

@author: ox112
"""

# pandas :  panel data 

# Series: Numpy의 array와 비슷    ~~ has an additional column (index)

import numpy as np
import pandas as pd

a= np.array([0.1,1.2,2.3,3.4,4.5])
b = pd.Series(a)

b1 = pd.Series(a, index = ['a','b','c','d','e'])
print(b1[['c','e']])
print(b1[[0,2]])

b2 = pd.Series({'a':0.1,'b':1.2,'c':2.3,'d':3.4,'e':4.5})
print(b2[['c','e']])
print(b2[[0,2]])

print(b1.values , b1.index , b1.index.values)

print(b1.describe())

print(b1.drop('a'))   # Series.drop(label)  - label의 데이터는 지운다

#Series와 관련된 method들

b3 = pd.Series(np.arange(1,4), index = ['a','b','c'])
b4 = pd.Series(np.arange(1,4), index = ['c','d','e'])
b5 = b3 + b4
print(b3, b4, b5)

print(b5.fillna(1.0))
print(b5)

print(b3.append(b1))
print(b3)

print(b3.replace([1,2],[0,-1]))
print(b3)

b3 = pd.Series(np.arange(1,4), index = ['a','b','c'])
b4 = pd.Series(np.arange(1,4), index = ['c','d','e'])
b3.update(b4)
print(b3, b4)


############  DataFrame #########################
a = np.array([[1.0,2],[3,4]])
df = pd.DataFrame(a)
print(df)

df = pd.DataFrame(np.array([[1,2],[3,4]]), columns = ['a','b'])
print(df)


df = pd.DataFrame(a)

df.columns= ['dogs','cats']
print(df)

df = pd.DataFrame(np.array([[1,2],[3,4]]), columns = ['dogs','cats'], index = ['Alice','Bob'])
print(df)

df.index = ['AA','BB']
print(df)


s1 = pd.Series(np.arange(0.0,5))
s2 = pd.Series(np.arange(1.0, 3))
dd = pd.DataFrame({'one':s1, 'two':s2})
print(dd)

#### excel 읽기
gdp_korea = pd.read_excel('gdp_korea.xlsx','Sheet1')
print(gdp_korea)

print(gdp_korea[['Q1-2011','Q2-2011']])


##  iloc  : index location ########
gdp_korea.iloc[0:3, 0:3]

gdp = gdp_korea.iloc[0,:]

print(np.transpose(gdp_korea))



# custom function
def lp_norm(x,y, p =2):
  d = x-y
  return (abs(d)**p)**(1/p)

print(lp_norm(2,3))
print(lp_norm(2,5,5))




