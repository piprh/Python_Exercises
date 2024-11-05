#Define function
def aa_per(seq, aa='x'):
    aacount = 0
    seq = seq.upper()
    checked = []
    for each_aa in aa:
        if each_aa.upper() in seq and each_aa.upper() not in checked:
            aacount += seq.count(each_aa)
            #print('aacount:', aacount)
            checked.append(each_aa)
        else:
            continue
        #print('checked: ', checked)
    aa_percent = (len(each_aa)*aacount)/len(seq)*100
    return aa_percent

#Testing
print('assert1: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "M")),'%')
print('assert1: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5))
print('assert2: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "r")),'%')
print('assert2: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10))
print('assert3: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "L")),'%')
print('assert3: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50))
print('assert4: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "Y")),'%')
print('assert4: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0))

print('assert5: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", ["M"])),'%')
print('assert5: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5)
print('assert6: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])),'%')
print('assert6: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70)
print('assert7: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP")), '%')
print('assert7: ', round(aa_per("MSRSLLLRFLLFLLLLPPLP")) == 65)

