#!/usr/bin/python
import re
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']


for acc in accessions:
    if re.search(r'5', acc):
        print(f'Contains 5: {acc}')
    if re.search(r'(d|e)',acc):
        print(f'contains D or E: {acc}')
    if re.search(r'(de)',acc):
        print(f'contains D and E: {acc}')
    if re.search(r'(d.e)',acc):
        print(f'contains D something E: {acc}')
    if re.search(r'[de]',acc):
        print(f'contains d and e in any order: {acc}')
