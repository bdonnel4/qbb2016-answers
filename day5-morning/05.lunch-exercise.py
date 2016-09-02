#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_table(sys.argv[1])

lst=[]
for x in df.itertuples():
    chromosome= x[2]
    t_name = x[6]
    if chromosome in ("2L", "2R", "3L", "3R", "4", "X", "Y"): 
        if x[3]== "+":
            start=int(x[4]) -500
            end = int(x[4]) +500
            lst.append((chromosome, start, end, t_name))
        elif x[3]=="-":
            start=int(x[5]) +500
            end = int(x[5]) -500
            lst.append((chromosome, start, end, t_name))
df = pd.DataFrame(lst) 


df= df.to_csv("SRR072893_t_data.bed", index = None, header = None, sep ="\t")       

        
# for _, chromosome, _, start, end, t_name in df.itertuples():
#     d[sex + "_"+stage]= pd.read_table(sys.argv[1])