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

complement = {'A':'U','C':'G','G':'C','U':'A'}

seqs = {}
with open('rosalind_orf.txt','r') as f:
    seq = ''
    key = f.readline().strip().lstrip('>')
    for line in f.readlines():
        if line[0] == '>':
            seqs[key] = seq.replace('T','U')
            seq = ''
            key = line.strip().lstrip('>')
        else:
            seq+=line.strip()
    seqs[key] = seq.replace('T','U')
    comp = [complement[x] for x in seqs[key]]
    seqs['Comp'] = ''.join(comp[::-1])

def ORF(seq):
    orfs = []
    key = list(seqs.keys())[0]
    occurances = []
    for i in range(len(seq)-3):
        if 'AUG' == seq[i:i+3]:
            occurances.append(i) # because python indexes with 0
    for ini in occurances:
        prot = ''
        for i in range(ini,len(seq),3):
            current = codon_table[seq[i:i+3]]
            if current == 'X':
                prot+=current
                break
            else:
                prot+=current
        if prot[-1] == 'X':
            orfs.append(prot.rstrip('X'))
    return orfs

orfs = []
for key in seqs.keys():
    orfs.extend(ORF(seqs[key]))

with open('submission.txt','w') as f:
    for value in set(orfs):
        f.write(value+'\n')
