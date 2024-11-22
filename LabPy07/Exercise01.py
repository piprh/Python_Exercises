#!/usr/bin/python3

import os, sys, subprocess
import pandas as pd
subprocess.call('wget -qO eukaryotes.tsv "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)
df = pd.read_csv('eukaryotes.tsv', sep='\t', na_values='-')
fungi = df[df['Group'] == 'Fungi']
big_fungus = fungi[fungi['Size (Mb)'] > 100]

print('Fungal species with genomes > 100Mb:\n ', big_fungus['#Organism/Name'])

hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[['#Organism/Name','Scaffolds']]


