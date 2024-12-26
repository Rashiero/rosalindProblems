complement = {'A':'T','C':'G','G':'C','T':'A'}
s_min = 4
s_max = 12

seqs = {}
with open("rosalind_revp.txt","r") as f:
    seq = ''
    key = f.readline().strip().lstrip('>')
    for line in f.readlines():
        if line[0] == '>':
            seqs[key] = seq
            seq = ''
            key = line.strip().lstrip('>')
        else:
            seq+=line.strip()
    seqs[key] = seq

seq = seqs[key]
comp = "".join([complement[x] for x in seq][::-1])

m = len(seq)
palindromes = []
for i in range(m):
    for gap in range(s_min,s_max+1,2):
        if i+gap <= m or m >= (i+gap):
            if seq[i:(i+gap)] == comp[(m-(i+gap)):(m-(i))]:
                palindromes.append(f'{i+1} {gap}')
        else:
            break

with open("submission.txt","w") as f:
    for i in palindromes:
        f.write(i+'\n')
