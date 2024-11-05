#!/usr/bin/python

def dna_X(seq, threshold = 0.5):
    bases = ['A', 'T', 'G', 'C']
    base_count = 0
    for base in bases:
        base_count += seq.count(base)
    X_count = len(seq) - base_count
    X_per = X_count/len(seq)

    if X_per > threshold:
        return "High"
    else:
        return "Low"

print("60% non-base", dna_X("ATGCXYZLMN"))
print("50% non-base", dna_X("ATGCAYZLMN"))
print("50% non-base, 0.3 threshold", dna_X("ATGCAYZLMN", 0.3))

assert dna_X("ATGCATGCXY") == "Low"
assert dna_X("ATGCATGCXY", threshold = 0.1) == "High"
