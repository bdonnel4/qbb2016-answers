#!/usr/bin/env python

"""
Extend k-mer counter to k-mer matcher
Implement a script that finds matching k-mers between a single 
query sequence and a database of targets. The matcher should take three arguments:
kmer_matcher.py <target.fa> <query.fa> <k>
Where target.fa is the database, potentially multiple sequences, 
query.fa is the sequence to align (assume just one sequnce), and k is the k-mer size 
(an integer).
The script should find k-mer matches and for each write:
target_sequence_name    target_start    query_start k-mer
Run the program for k=11 and submit the first 1000 lines.
"""

import sys , fasta


k = int (sys.argv[1]) ##kmer length defined

for indent, sequence in fasta.FASTAReader(open(sys.argv[2])): ##source fasta file
    sequence = sequence.upper()
    kmer_counts = {}
    
    for i in range(0, len(sequence)-k):
        kmer = sequence[ i : i+k ]
        if kmer not in kmer_counts:
            kmer_counts [kmer] = []
        kmer_counts[kmer].append(i)

    for indentQ, sequence in fasta.FASTAReader(open(sys.argv[3])):
        for i in range(0, len(sequence)-k):
            kmer_match = sequence [i: i+k]
            if kmer_match in kmer_counts:
                print indent, kmer_counts[kmer_match], i, kmer_match
            else:
                continue

     