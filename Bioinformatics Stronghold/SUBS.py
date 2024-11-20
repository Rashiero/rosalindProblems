with open("rosalind_subs.txt","r") as f:
    seq = f.readline().strip()
    pat = f.readline().strip()

# We want to search the sequence for the pattern and return the locations of occurances
# For that, a simple linear search and comparison might be enough
occurances = []
s_pat = len(pat)
for i in range(len(seq)-s_pat):
     if pat == seq[i:i+s_pat]:
        occurances.append(i+1) # because python indexes with 0

with open('submission.txt','w') as f:
    f.write(' '.join([str(x) for x in occurances]))
