seqs = {}
with open('rosalind_cons.txt','r') as f:
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

s_seq = len(seqs[key])

consensus_matrix = [[0]*s_seq for _ in range(4)]
base_map = {'A':0,'C':1,'G':2,'T':3}
map_base = {value:key for key,value in base_map.items()}

consensus_string = ''
for i in range(s_seq):
    for key in seqs.keys():
        consensus_matrix[base_map[seqs[key][i]]][i]+=1
    aux = [x[i] for x in consensus_matrix]
    consensus_string+=map_base[aux.index(max(aux))]

with open('submission.txt','w') as f:
    f.write(consensus_string+'\n')
    f.write('\n'.join([f'{key}: {" ".join([str(x) for x in consensus_matrix[base_map[key]]])}' for key in base_map.keys()]))
