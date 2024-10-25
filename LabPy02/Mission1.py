#!/usr/bin/python3
#Import all modules learnt in Lecture 12
import os
import subprocess
import sys
import shutil

#Open and read DNA sequence using with, closes automatically

with open("/localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt") as dna_seq:
    dna_seq_contents = dna_seq.read()
    dna_seq_contents
print("Is the connection closed?\n", dna_seq.closed)
#Show that we have the right file
print("dna_seq file is", len(dna_seq_contents), "bases long")
print("These are the first 50 characters:", dna_seq_contents[:50])

#Retrieve exons 1 and 2
exon1 = dna_seq_contents[:63]
exon2 = dna_seq_contents[90:]

print("1st exon is", exon1, "\n2nd exon is", exon2)

#Get DNA sequence for accession number AJ223353 from NCBI in fasta format
subprocess.call("esearch -db nucleotide -query \"AJ223353\"  | efetch -format fasta > DNA.fasta", shell=True)
#Look at the file
with open("DNA.fasta") as dna_fasta:
    dna_fasta_contents = dna_fasta.read()
    dna_fasta_contents
print("Is the connection closed?\n", dna_fasta.closed)

#Show that we have the right file
print("dna_fasta file is", len(dna_fasta_contents), "bases long")
print("These are the first 50 characters:", dna_fasta_contents[:50])
