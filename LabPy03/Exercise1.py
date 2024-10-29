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
    line_trim = eachline[15:]
    print(DNAid, "is ", len(line_trim.rstrip()),"bases long.")
    DNA_file.write(f"{DNAid}: {line_trim}")
#Close files
input_file.close()
DNA_file.close()
