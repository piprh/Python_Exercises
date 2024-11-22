#/usr/bin/python3

from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email = "s2691680@ed.ac.uk"
Entrez.api_key = 'dc8be440b795966fc6768ec367aefce33308'

#fetch COX1 protein records
#must be: COX1 in gene name, protein database, mammal in organism  taxonomy
#Search the database
mysearch = Entrez.esearch(db="protein", term="Mammalia COX1 complete")
print(mysearch)
#Get IDs from search
myresult_IDs = Entrez.read(mysearch)['IdList']
print("number of results from search:" + str(len(myresult_IDs)))

#Fetch genbank records
for ID in myresult_IDs:
    genbank = Entrez.efetch(db="protein", id=ID, rettype="gb")
    record = SeqIO.read(genbank, "genbank")
    print(record.description)


