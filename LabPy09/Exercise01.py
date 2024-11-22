#/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace('\n','').upper()[0:100000]
window=10000

at = []

def slide_win(base, window=1000):    
    for start in range(int(base) - window):
        print("analysing window starting at: ", start)
        win = ecoli[start:start+window]
        AT_count = win.count('A')+win.count('T')
        print("found", AT_count, "As and Ts")
        at.append(AT_count / window)
    return at

at_prop = []

for base in [50000, 100000, len(ecoli)]:
    print("Working on "+str(base))
    at_prop.append(slide_win(base))

plt.figure(figsize=(20,10))

for i in at_prop:
    plt.plot(i, label=str(i),linewidth=3)

print("plotting...")

plt.ylabel('Overrepresentation of dinucleotide')
plt.xlabel('Position on genome')
plt.suptitle("Dinucleotide composition in the E coli genome",fontsize=20) # Note!
plt.title("Window size of "+str(window),fontsize=14)
plt.legend()
plt.savefig("Chart_"+str(i)+".png",transparent=True)
plt.show()


