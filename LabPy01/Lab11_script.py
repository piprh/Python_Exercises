#!/usr/bin/python

#Define dna sequence
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Count A nucleotides
a_count = dna_seq.count('A')
#Count T nucleotides
t_count = dna_seq.count('T')
#Add up and divide by length of sequence
dna_len = len(dna_seq)
at_prob = (a_count + t_count)/dna_len

#Output
print("The number of A nucleotides is ", str(a_count),
        "The number of T nucleotides is ", str(t_count),
        "The proportion of As and Ts in the sequence is " + str(at_prob))

#Complementing DNA
#Define DNA sequence
dna_seq2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Create temporary sequence
dna2_temp_compl=dna_seq2.replace('A','1').replace('C','2').replace('G','3').replace('T','4')
#replace with final values ATCG
dna2_compl=dna2_temp_compl.replace('1','T').replace('2','G').replace('3','C').replace('4','A')
#Output
print("The complement of", dna_seq2, "is", dna2_compl)

#Restriction Fragment Lengths
#find position of GAATTC
dna_seq.find('GAATTC')


###SPLICING INTRONS###
dna_seq3 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#First exon given start to 63rd character
exon1 = dna_seq3[0:63]
#Second exon given 91st character to end of sequence
exon2 = dna_seq3[90:]

print("Exons joined\n" + exon1 + exon2)
coding_length = len(exon1+exon2)
total_length = len(dna_seq3)
print("Coding % (rounded)\n" +
        str(int((coding_length / total_length) * 100)))

#
