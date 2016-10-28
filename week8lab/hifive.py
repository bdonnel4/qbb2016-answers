#!/usr/bin/env python

import numpy as np
import sys
import h5py

control = open(sys.argv[1]) #ctcf_peaks.tsv

control1 = []

for i in control:
    line=i.split("\t")
    if line[0]=='chrX':
        control1.append(int(line[1])) 

file = h5py.File("Out.heat")
file.keys()
[u'0.counts', u'0.expected', u'0.positions', u'regions']
counts = file['0.counts'][...]
positions = file['0.positions'][...]
#print counts

e=file['0.expected'][...]

enrichment=(counts/e)
enrich = enrichment+1

#print np.log10(enrich)


for i in range(counts.shape[0]):
    value=0
    for j in range(counts.shape[1]):
        if counts[i,j]>0:
            for k in control1:
                if k >= positions[i,0]:
                    if k < positions[i,1]:
                        for l in control1:
                            if l >= positions[j,0]:
                                if l < positions[j,1]:
                                    if enrichment[i,j]>value:
                                        value=enrichment[i,j]
                                        pos=j
                    
                    

#if counts[0,0]>0:
    # if control1 > positions[0,0]:
    #     if control1 <= positions[0,1]:
    #         if control1[] > positions[1,0]:
    #             if control1 <= positions[1,1]:
    #                 if enrichment[0,0]>value:
    #                     value=enrichment[0,0]
            
            
        

