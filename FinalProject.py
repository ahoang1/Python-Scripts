# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:43:43 2018

@author: Angela
"""

#the purpose of this script is to retrieve a FASTA file from the same folder
#Original sequence base composition will be determined
#the sequence will then be mutated by a random mutation generator
#the new sequence will be aligned to the original sequence
#base composition of the new sequence will be determined
#a table will be constructed to observe the differences

seq = raw_input('Enter FASTA seq. file name:')
fh = open(seq,'r')
line = fh.read()

my_seq = line
print my_seq

ACount = 0
CCount = 0
TCount = 0
GCount = 0

for C in my_seq:
    if C == 'A':
        ACount = ACount + 1
    elif C == 'C':
        CCount = CCount + 1
    elif C == 'T':
        TCount = TCount + 1
    elif C == 'G':
        GCount = GCount + 1
SequenceLength = len(my_seq)
print "Original sequence:"
print my_seq
OriginalSequenceLength = len(my_seq)
print "Sequence length:", OriginalSequenceLength, "nucleotides"

print "Percentage of A's in sequence:", (float(ACount) / OriginalSequenceLength) * 100
print "Percentage of C's in sequence:", (float (CCount) / OriginalSequenceLength) * 100
print "Percentage of T's in sequence:", (float (TCount) / OriginalSequenceLength) * 100
print "Percentage of G's in sequence:", (float (GCount) / OriginalSequenceLength) * 100


#random mutation generator creates a new strand with X% mutation frequency
import random
def mutate(string, mutation, threshold):
    return ''.join([mutation[char] if random.random() < threshold
                                      and char in mutation else char
                                      for char in string])

mut_seq = mutate(my_seq, {"A": "G", "T": "C"}, 0.50)
print "Mutated Sequence:"
print mut_seq

MutSequenceLength = len(mut_seq)
ACount = 0
CCount = 0
TCount = 0
GCount = 0

for C in mut_seq:
    if C == 'A':
        ACount = ACount + 1
    elif C == 'C':
        CCount = CCount + 1
    elif C == 'T':
        TCount = TCount + 1
    elif C == 'G':
        GCount = GCount + 1
print "Sequence length:", MutSequenceLength, "nucleotides"

print "Percentage of A's in sequence:", (float(ACount) / MutSequenceLength) * 100
print "Percentage of C's in sequence:", (float (CCount) / MutSequenceLength) * 100
print "Percentage of T's in sequence:", (float (TCount) / MutSequenceLength) * 100
print "Percentage of G's in sequence:", (float (GCount) / MutSequenceLength) * 100

#aligns original and mutated sequences and score
print "Pairwise Alignment:"

from Bio import pairwise2
alignments = pairwise2.align.globalxx(my_seq, mut_seq)

from Bio.pairwise2 import format_alignment
print(format_alignment(*alignments[0]))