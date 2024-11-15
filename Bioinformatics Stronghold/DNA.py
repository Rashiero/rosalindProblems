nucleotydes = {'A':0,'C':0,'G':0,'T':0}

with open("rosalind_dna.txt","r") as f:
    dna = f.read().strip()

for i in dna:
    nucleotydes[i]+=1

with open("submission.txt",'w') as f:
    f.write(f"{nucleotydes['A']} {nucleotydes['C']} {nucleotydes['G']} {nucleotydes['T']}")

