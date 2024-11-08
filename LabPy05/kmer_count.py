#!/usr/bin/python3
#Import modules
import sys
import os

def kmer_count(dna, kmersize):
    startpoint=0
    endpoint=startpoint+int(kmersize)
    kmer_list=[]
    while endpoint < len(dna):
        kmer = dna[startpoint:endpoint]
        #print(kmer)
        kmer_list.append(kmer)
        #print(kmer_list)
        startpoint += 1
        endpoint += 1
    return kmer_list

#sequence = ("ATGCATCATG")
#kmer_count(sequence, 2)
print(kmer_count(sys.argv[1], sys.argv[2]))

def kmer_most(dna, kmersize, minfreq):
    kmer_list = kmer_count(dna, int(kmersize))
    print(kmer_list)
    kmer_most_list = []
    for kmer in kmer_list:
        kmer_count = kmer_list.count(kmer) # count each kmer in list of kmers
        if kmer_count > int(minfreq):
            kmer_most_list.append(kmer) 
    return kmer_most_list

kmer_most(sys.argv[1], sys.argv[2], sys.argv[3])


#how to link argv's to function
#error variabale ref before assignment
