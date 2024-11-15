complement = {'A':'T','C':'G','G':'C','T':'A'}
with open("rosalind_revc.txt","r") as f:
    seq = f.read().strip()

comp = [complement[x] for x in seq]

with open("submission.txt","w") as f:
    f.write("".join(comp[::-1]))

