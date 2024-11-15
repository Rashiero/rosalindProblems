outfile = []

with open("rosalind_ini5.txt",'r') as f:
    i = 0
    for line in f.readlines():
        i+=1
        if i%2 == 0:
            print(line)
            outfile.append(line)

with open("submission.txt","w") as f:
    for i in outfile:
        f.write(i)
