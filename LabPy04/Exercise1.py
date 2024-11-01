#!/usr/bin/python
#Lecture 14 Exercise1

#start counter
count = 0
flies=[]
#initialise list

with open("Lecture14/data.csv") as data:
    entries = data.readlines()
    print("data: ", data)
    print("entries:", entries, entries[0])
    for seq in entries: 
        count+=1
        if 'melanogaster' in seq or 'simulans' in seq:
            seq_wanted = seq.split(',')
            print(count, seq_wanted[0], seq_wanted[2])
            flies.append(seq_wanted)
        else:
            print(count, 'is something else')



#check file is closed
print("file is closed", data.closed)


