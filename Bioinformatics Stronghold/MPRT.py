import requests

base_url = 'https://rest.uniprot.org/uniprotkb/'

with open('rosalind_mprt.txt','r') as f:
    ids = f.read().strip().split('\n')

seqs = {}
errors = []
for entry in ids:
    print(f'retrieving {entry}')
    text = requests.get(base_url+entry+'.fasta').text
    if text[0:14] == 'Error messages':
        entry.split('_')[0]
        text = requests.get(base_url+entry.split('_')[0]+'.fasta').text
    text = text.rstrip()
    print(f'sequence:\n{text}')
    if not text:
        errors.append(entry)
        continue
    seq = ''
    for line in text.split('\n'):
        if line[0] == '>':
            continue
        else:
            seq+=line
    seqs[entry] = seq

with open('sequences_mprt.txt','w') as f:
    for key,val in seqs.items():
        f.write(f'>{key}\n')
        f.write(f'{val}\n')

results = {}
flag = input(f'Are you done editting the file?\nKeep in mind the errors in {" ".join(errors)}\ny or n')

if flag != 'y':
    raise Exception('Certain codes were not retrievable')

with open('sequences_mprt.txt','r') as f:
    for line in f.readlines():
        if line[0] == '>':
            key = line.strip().lstrip('>')
        else:
            seqs[key] = line.strip()

# Find pattern N{P}[ST]{P}
for entry in seqs.keys():
    seq = seqs[entry]
    results[entry] = []
    # Bad practice hard code the pattern
    for i in range(len(seq)-4):
        if seq[i] == 'N':
            if seq[i+1] != 'P' and seq[i+3]!='P' and (seq[i+2]=='S' or seq[i+2]=='T'):
                results[entry].append(i+1)

with open('submission.txt','w') as f:
    for key in results.keys():
        if len(results[key]) > 0:
            f.write(key+'\n')
            f.write(' '.join([str(x) for x in results[key]])+'\n')
