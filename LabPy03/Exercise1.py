#!/usr/bin/python3
#29 Oct 24
#open file
input_file = open('Lecture13/input.txt','r')
lines = input_file.readlines()

#Initiate counter variable and open blank file
DNAnum=0
DNA_file = open("DNA.txt",'w')

#for loop to give each sequence a number, trim the 1st 14 bases, print line length to screen and read lines to a file.
for eachline in lines:
    DNAnum +=1
    DNAid = "seq" + str(DNAnum)
    line_trim = eachline[14:]
    print(DNAid, "is ", len(line_trim.rstrip()),"bases long.")
    print(line_trim.rstrip())
    DNA_file.write(f"{DNAid}: {line_trim}")
#Close files
input_file.close()
DNA_file.close()

#Open and read genomic file
exons = open('exons.txt').read().rstrip()
counter=0
for exon in exons:
    counter+=1
    print(counter, exon)
with
open('Exercise2_coding_sequence.fasta','w') as fullcoding:
    fullcoding.write('>Lecture13_exercise2_codingseq\n')
    for exon in exons:
        counter +=1
        startex = int(exon.split(',')[0])-1
        endex = int(exon.split(',')[1])
        exwanted = genomic_dna2[startex : endex]
        fullcoding.write(exwanted)
        regionsum = 'Exon'+str(counter)+' '+str(exons)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+ '.'
        print(regionsum,'\n\t',exwanted)

##SLIDING WINDOWS
print('Starting sliding window')
import os, shutil

