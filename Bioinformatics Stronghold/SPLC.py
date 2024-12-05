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
introns = {}
seqs = {}
with open('rosalind_splc.txt','r') as f:
    seq = ''
    key = f.readline().strip().lstrip('>')
    for line in f:
        if line[0] != '>':
            seq+=line.strip()
        else:
            break
    seqs[key] = seq
    key = line.strip().lstrip('>')
    seq = ''
    for line in f:
        if line[0] == '>':
            introns[key] = seq
            seq = ''
            key = line.strip().lstrip('>')
        else:
            seq+=line.strip()
    introns[key] = seq

# Remove Introns
key = list(seqs.keys())[0]
mrna = seqs[key]

for pattern in introns.values():
    mrna = mrna.replace(pattern,'')

# Translate
mrna = mrna.replace('T','U')
prot=''
for i in range(len(mrna)//3):
    current_aa = codon_table[mrna[3*i:3*(i+1)]]
    if current_aa == 'X': break
    prot+= current_aa

with open('submission.txt','w') as f:
    f.write(prot)
