with open("rosalind_rna.txt","r") as f:
    rna = f.read().strip()

rna = rna.replace("T","U")

with open("submission.txt","w") as f:
    f.write(rna)

