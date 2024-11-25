seqs = {}
with open('rosalind_grph.txt','r') as f:
    key = f.readline().strip().lstrip('>')
    seq = ''
    for line in f.readlines():
        if line.strip()[0] == '>':
            seqs[key] = seq
            key = line.strip().lstrip('>')
            seq = ''
        else:
            seq+=line.strip()
    seqs[key] = seq

# Recieve a collection of DNA strings in FASTA format having total length at most 10 kbp.

# Return the adjacency list corresponding to O3 graph

aux = {key:{'pre':seqs[key][:3],'suf':seqs[key][-3:]} for key in seqs.keys()}

output = ''
for key_suf in aux.keys():
    for key_pre in aux.keys():
        if key_pre == key_suf:
            continue
        if aux[key_suf]['suf'] == aux[key_pre]['pre']:
            output += f'{key_suf} {key_pre}\n'

with open('submission.txt','w') as f:
    f.write(output)
