with open('rosalind_iev.txt','r') as f:
    pop = [int(x) for x in f.read().strip().split(" ")]

n_kids = 2
# We want the average of kids with 
Population = {
"AAAA":pop[0],
"AAAa":pop[1],
"AAaa":pop[2],
"AaAa":pop[3],
"Aaaa":pop[4],
"aaaa":pop[5]
}

PXGY = {
"AAAA":1.,
"AAAa":1.,
"AAaa":1.,
"AaAa":.75,
"Aaaa":.5,
"aaaa":0.
}

result = sum([n_kids*Population[key]*PXGY[key] for key in Population.keys()])

with open('submission.txt','w') as f:
    f.write(f'{result:.1f}')

