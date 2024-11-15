reads = {}
with open("rosalind_gc.txt","r") as f:
    for line in f.readlines():
        if line[0] == '>':
            ids = line.lstrip(">")
        else:
            reads[ids]=line.strip()

gc_content = {x:0 for x in reads.keys()}
max_key = list(reads.keys())[0]

for key,read in reads.items():
    nucleotydes = {'A':0,'C':0,'G':0,'T':0}
    for i in read:
        nucleotydes[i]+=1
    val = 100*(nucleotydes['C']+nucleotydes['G'])/sum(nucleotydes.values())
    if val > gc_content[max_key]:
        max_key = key
    gc_content[key] = val

with open("submission.txt","w") as f:
    f.write(f"{max_key}")
    f.write(f"{gc_content[max_key]:.6f}")

