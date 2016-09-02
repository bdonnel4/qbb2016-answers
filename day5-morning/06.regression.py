#!/usr/bin/env python

import sys
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1]) ##ctab file
df2= pd.read_table(sys.argv[2], header=None)##histone file(s) 4 total



d= {}
for i in df.itertuples():
    t_name= i[6]
    d[t_name]=[i[-1]] ##dictionary with [key]:value = [t_name]:FPKM value
    ###I FIANALLY GET THIS! dicts, specifically
    #print d

for j in df2.itertuples():
    t_name2 =j[0]
    if t_name2 in d:
        d(value).append(j[0])
    print d        

#statsmodels.regression.linear_model.OLS(endog, exog=None, missing='none', hasconst=None, **kwargs)