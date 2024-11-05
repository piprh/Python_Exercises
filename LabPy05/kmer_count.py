#!/usr/bin/python3
def kmer_count(dna, kmersize, minfrequency):
    startpoint=0
    endpoint=startpoint+kmersize+1
    kmer_list=[]
    while endpoint < len(dna):
        kmer = dna[startpoint,endpoint]
        print(kmer)
        startpoint =+ 1
        kmerlist.append(kmer)
        print(kmer_list)

