# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:48 2018

@author: InChoi
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(n:int, generator_type:str):
    """ n: sample size
    generator_type : distribution of generated data"""
    values=[]
    for i in range(n):
        if generator_type=='U':
            e=np.random.uniform(0,1)
        else:
            e=np.random.randn() # Generate a single data
        values.append(e)
    return values

data = generate_data(100,'n')    
plt.plot(data)
plt.show()
