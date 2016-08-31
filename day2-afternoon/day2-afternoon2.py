#!/usr/bin/env python

#Identifier mapping, homework problem 2
"""
Write a python script for identifier mapping. 
Your script should take as input the mapping file (as above) 
and a c_tab file from StringTie and find the corresponding 
translation from the mapping file. If found, it should print the line 
from the c_tab file with the identifier. If not found, it should do one of 
two things depending on a command line argument: 
1.Print nothing (ignore the line). 
2. Print and fill the field with a default value
"""

import sys
f = open ("/Users/cmdb/qbb2016-answers/day2-afternoon/day2-afternoon.full.out")
g = open ("/Users/cmdb/data/t_data.ctab")


FBgn_dict = {}
for line in f:
    field = line.rstrip("\r\n").split("\t")
    FBgn_dict [field[1]] = field[0]
#print FBgn_dict

#the key here is the uniprot name and the value is the fly_id


for line in g:
    field = line.rstrip("\r\n").split("\t")
    # field[8] this is the FBgn stuff
    if field[8] in FBgn_dict.keys(): 
        #print "yes"
        #print line
        #line = line.rstrip("\r\n")
        line = line + "\t" + FBgn_dict[field[8]]
        # print line
    else:
        #line = line.rstrip("\r\n")
        line = line + "\t" + "*"

        #field[8]="*"
    print line

           
    # FBgn_dict.keys() in line:
    #     print "yes"
    #     field = line.strip("\r\n").split()
    #
    # print line
    # if line.startswith("t_id"):
    #     continue
    # field = line.rstrip("\r\n").split("\t")
    # if field[8] == FBgn_dict[field[0]]:
    #     continue
    # else:
    #     field[8] = "*"
    #