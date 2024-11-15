with open("rosalind_hamm.txt","r") as f:
    seq1,seq2 = f.read().strip().split("\n")
str_size = len(seq1)
mismatch = 0
for i in range(str_size):
    if seq1[i]!=seq2[i]:
        mismatch+=1
with open("submission.txt","w") as f:
	f.write(f"{mismatch}\n")
