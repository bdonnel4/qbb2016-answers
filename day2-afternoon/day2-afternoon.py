#!/usr/bin/env python

#Submit your two Python scripts, with any instructions needed to run them in a documentation comment, and the first 100 lines of your output using each of the two options.

"""
Save the fly.txt file from http://www.uniprot.org/docs/fly.txt directly online, save as .txt.
"""

import sys
f = open ("/Users/cmdb/data/fly.txt")


new_list=[]
for line in f.readlines():
    if "DROME" in line:
        split_line=line.split()    
        if "FBgn" in line:
            new_list.append((split_line[-2],split_line[-1]) )
            continue
        else:
            new_list.append( (split_line[-1], new_list[-1][1]) )

for pair in new_list:
    print pair[0] + "\t" + pair[1]