# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:48 2018

@author: InChoi
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(n, generator_type):
    values=[]
    for i in range(n):
        e = generator_type()
        values.append(e)
    return values

data1 = generate_data(100,np.random.uniform) 
data2 = generate_data(100,np.random.normal)    
plt.plot(data1, data2)
plt.show()