#!/usr/bin/python
#Lecture 14 Exercise1
import os, subprocess, shutil

#start counter
count = 0
flies=[]
#initialise list

with open("Lecture14/data.csv") as data:
    print("data: ", data)
    for line in data: 
        count+=1
            seq = line.split(',')
            flies.append(seq)
if 'melanogaster' in line or 'simulans' in line:

#check file is closed
print("file is closed", data.closed)


