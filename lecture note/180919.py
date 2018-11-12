# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:36:14 2018

@author: ox112
"""

import numpy as np

######## Logical Operators ####################
x = np.array([[1,2],[3,4]])
x > 0
x == 3

## 
print(np.logical_and(x>0, x==3))
print(np.logical_or(x>0, x==3))
print((x>0) & (x==3))
print((x>0) | (x==3))

print( np.all(x>0))
print( np.any(x==0))

########### logical indexing  #####################

sel = (x<=3)
indices = np.nonzero(sel)   
print(indices)
x[indices]   #  x[(0,0,1),(0,1,0)]

## 위와 같은 방법?
x = np.arange(3,5)
x[ x < 0 ]
x[abs(x) >= 2]

####
x = np.random.randn(3)
np.argwhere(x < 0.6)    #  조건을 만족하는 원소의 index를 return
np.extract(x <0, x)     #   조건을 만족하는 원소의 값을 return

######### Flow Control
# if - elif - else
x = 5
if x<5:
    x += 1
elif x>5:
    x -= 1
else:
    x *= 2

#for
cnt = 0
for i in range(1,101):
    cnt += i

print(cnt)

###
x = np.linspace(1,500,50)

cnt = 0
for i in x:
    cnt += i
print(cnt)

##
returns = np.random.randn(100)
cnt = 0

for ret in returns:
    if ret < 0: 
        cnt += 1

print(cnt)

#### break/continue #####

x = np.random.randn(100)

for i in x:
    print(i)
    if i>2 : break 
        
for i in x:
    if i>=0:
        continue
    print(i)

## while
i = 1
count = 0
while i < 10:
    count += 1
    i += 1

print(i)


###################   Dates and Times #################################
import datetime as dt

yr, mm, dd = 2012,12,31
d = dt.date(yr,mm,dd)
d2 = dt.date(yr+1,mm,dd)
d2-d

###################### Graphics ###########################
import matplotlib.pyplot as plt
import scipy.stats as stats

import seaborn as sns

x = np.random.rand(100)
y = np.random.rand(100)

#plot
plt.plot(y,'g-')
plt.autoscale(tight = 'x')
plt.tight_layout()

#scatter
plt.scatter(x,y)

#
x = np.arange(5)
y = np.random.randn(5)

plt.bar(x,y)
plt.pie(x)
plt.hist(y)

## Exporting Plots
y = np.random.randn(100)
plt.plot(y,'g-')
plt.autoscale(tight= 'x')
plt.tight_layout()
plt.savefig('figure.jpg')


############ Pandas! ####################################

# Series
import pandas as pd
s = pd.Series({'a':0.1,'b':1.2,'c':2.3,'d':3.4,'e':4.5})


 