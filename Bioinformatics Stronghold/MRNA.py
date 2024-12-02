codon_table = {
'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
'UAA':'X','CAA':'Q','AAA':'K','GAA':'E',
'UAG':'X','CAG':'Q','AAG':'K','GAG':'E',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
'UGA':'X','CGA':'R','AGA':'R','GGA':'G',
'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
}

with open('rosalind_mrna.txt','r') as f:
    seq = f.read().strip()

counts = {}
for key in codon_table.keys():
    codon = codon_table[key]
    if codon not in counts.keys():
        counts[codon] = 0
    counts[codon]+=1

seq+='X'

n_seq = 1

for aa in seq:
    n_seq*=counts[aa]
    n_seq%=1e6

with open('submission.txt','w') as f:
    f.write(str(int(n_seq)))
