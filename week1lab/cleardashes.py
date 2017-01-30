#!/usr/bin/env python

"""removes dashes from the aligned sequneces"""


import sys

for strand in sys.stdin:
    strands = strand.rstrip("\r\n").split("\t")
    strands[2] = strands[2].replace("-","")
    #print strands[0], strands[1], strands[2], strands[3]
    if strands[1]=="1" and strands[2]=="10293":
        print ">", strands[0]
        print strands [3]