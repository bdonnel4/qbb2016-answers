#!/usr/bin/env python

#Exercise 4

#For the first 10 alignments, print just the column indicating which chromosome a given read aligns to
#HINT: .split()

import sys
f = open ("/Users/cmdb/data/893.sam")
count = 0

for line in f:
    if line.startswith("SRR"):
        print line.split("\t")[2]
        count = count + 1
        if count == 10: 
            break
       
        