# -*- coding: utf-8 -*-

import numpy as np

x = np.random.randn(4,2)    # normal distribution을 따르는 랜덤넘버를 4행 1열로 만들어라.
print(x)
np.sort(x)
np.sort(x, axis = 0)

o = np.ones((2,3))   # np.ones((M,N)) : M by N array of 1s
print(o)

z = np.zeros((2,3))   # np.zeros((M,N)) : M by N array of 0s
print(z)

I = np.eye(5)      # np.eye(N) : 단위행렬  
print(I)

#### Array and Matrix Function

# 곱할떄의 차이 
# array: 원소끼리 곱한다.  ////   matrix: 행렬의 곱
x = np.array([[1,2],[3,4]])
print(x)

np.mat(x) * np.mat(x)  # matrix multiplication
x@x      # matrix multipliacation

x = np.random.randn(4,3)
x.shape     # size를 tuple로 return

x = np.array([[1,2],[3,4]])
print(x)
print("------")
y = np.reshape(x,(4,1))
print(y)
 
np.size(x)   # 원소의 개수

w = np.tile(x,(2,3))    # np.tile(A, (M,N))  :  A를 (M,N)로 반복한 것을 array로 return 
print(w)

x.ravel()   # 1차원으로 차원 축소

z = np.hstack((x,x,x))      # np.hstack()   : horizon -- 옆으로 쌓음
print(z)
print("-------")
y = np.vstack((z,z))      # np.vstack()   : vertical -- 아래로 쌓음
print(y)

z = np.vsplit(x,2)     # 수직으로 쪼갬
print(z) 
y = np.hsplit(x,2)    # 수평으로 쪼갬
print(y)


x = np.reshape(np.arange(20),(4,5))
print(x)

y = np.delete(x,1, axis= 0)   # same as x[[0,2,3]]
print(y)    
w = np.delete(x,[2,3],axis= 1)  # same as x[:,[0,1,4]]
print(w)

x = np.reshape(np.arange(4),(2,2))
print(x)
print("----")
print(np.fliplr(x))
print("-----")
print(np.flipud(x))

x = np.array([[1,2],[3,4]])
print(x)
y = np.diag(x)       # input값이 행렬이면 diag 부분만 뽑아 list로 만든다.
print(y)
z = np.diag(y)       # input값이 벡터이면 input이 diag, 나머지는 0인 행렬로 만든다. 
print(z)

x = np.reshape(np.arange(20),(4,5))
print(np.triu(x))       # 삼각 행렬
print()
print(np.tril(x))       # 삼각 행렬


# linalg 모듈

x = np.matrix([[1.0,0.5],[0.5,1]])
print(np.linalg.svd(x))    # singular valued decomposition

X = np.array([[1,2,3],[3,3,4],[1,1,4]])
y = np.array([[1],[2],[3]])
print(np.linalg.solve(X,y))   # solve the equation

X = np.random.randn(100,2)
y = np.random.randn(100,1)
print(np.linalg.lstsq(X,y))   # least square solution of linear matrix equation

X = np.matrix([[1,.5],[.5,1]])
C = np.linalg.cholesky(X)
print(C)
print(C*C.T)

print(np.linalg.inv(X))
print(X**(-1))


###########  Importing and Exporting Data ####################################
import pandas as pd

csv_data = pd.read_csv('test.csv')
print(csv_data)
print(type(csv_data))
csv_data = csv_data.values
print(csv_data)


###############   Inf, NaN#####################

print(np.inf)
print(2/np.inf)



