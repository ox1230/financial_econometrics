# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:06:27 2018

@author: ox112
"""

import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.vector_ar import irf

#data불러오기
gdp = pd.read_table("gdp.txt",index_col = False)
print(gdp.head())

# VAR(1)으로 추정함
var_order=1
model = VAR(gdp)
results = model.fit(var_order)

print(results.summary())

# impulse response analysis
irf_result = irf.IRAnalysis(results)

irf_result.plot(impulse = 'Cinv',response = 'GDP')
irf_result.plot(impulse = 'Exp',response = 'GDP')


# forecast error variance decomposition 
fevd_result = results.fevd()
fevd_result.summary()
