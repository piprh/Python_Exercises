#!/usr/bin/python3
#Import all modules learnt in Lecture 12
import os
import subprocess
import sys
import shutil

#Open and read DNA sequence using with, closes automatically

with open("/localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt") as dna_seq:
    dna_seq_contents = dna_seq.read().upper()
    dna_seq_contents
print("Is the connection closed?\n", dna_seq.closed)
#Show that we have the right file
print("dna_seq file is", len(dna_seq_contents), "bases long")
print("These are the first 50 characters:", dna_seq_contents[:50])
#Remove non-DNA characters
dna_seq_contents=dna_seq_contents.replace("X","").replace("S","").replace("K","").replace("L","")


#Retrieve exons 1 and 2
exon1 = dna_seq_contents[:63]
exon2 = dna_seq_contents[90:]

print("1st exon is", exon1, "\n2nd exon is", exon2)

#Get DNA sequence for accession number AJ223353 from NCBI in fasta format
subprocess.call("esearch -db nucleotide -query \"AJ223353\"  | efetch -format fasta | grep -v \">\" > DNA.fasta", shell=True)
#Look at the file
with open("DNA.fasta") as dna_fasta:
    dna_fasta_contents = dna_fasta.read().upper()
    dna_fasta_contents
print("Is the connection closed?\n", dna_fasta.closed)

#Show that we have the right file
print("dna_fasta file is", len(dna_fasta_contents), "bases long")
print("These are the contents:", dna_fasta_contents)

#Get DNA sequence again in GenBank format for annotation details, output only coding region line
print("Coding region is:")
subprocess.call("esearch -db nucleotide -query \"AJ223353\"  | efetch -format gb | grep \"CDS\"", shell=True)

#Look at the file
#with open("DNA.gb") as dna_gb:
 #   dna_gb_contents = dna_gb.read()
  #  dna_gb_contents
#print("Is the connection closed?\n", dna_gb.closed)

#Show that we have the right file
#print("dna_gb file is", len(dna_gb_contents), "characters long")
#print("These are the contents:", dna_gb_contents)

#Found that coding region is 29-409 bases
CDS = dna_fasta_contents[29:410]
NCDS = dna_fasta_contents[:29] + dna_fasta_contents[410:]

print("coding region is:", CDS)
print("non-coding region is:", NCDS)


#Write all sequences to files
with open("exon1.txt","w") as exon1_file:
     exon1_file.write(exon1.replace("\n",""))
with open("exon2.txt","w") as exon2_file:
     exon2_file.write(exon2.replace("\n",""))
with open("coding_reg.txt","w") as CDS_file:
     CDS_file.write(CDS.replace("\n",""))
with open("non-coding_reg.txt","w") as NCDS_file:
    NCDS_file.write(NCDS.replace("\n",""))
