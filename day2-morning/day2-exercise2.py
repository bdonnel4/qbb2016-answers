#!/usr/bin/env python

#Count number of alignments that match perfectly to the genome
#HINT: This is encoded in one of the sam format's optional fields

import sys
f = open ("/Users/cmdb/data/893.sam")
count = 0

for line in f:
    if "NM:i:0" in line:
        count = count + 1
        
print count  