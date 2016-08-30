#!/usr/bin/env python

#Exercise 3
#Count number of reads that map to exactly one location in the genome
#HINT: number of hits

import sys
f = open ("/Users/cmdb/data/893.sam")
count = 0

for line in f:
    if "NH:i:1" in line:
        count = count + 1
        
print count  