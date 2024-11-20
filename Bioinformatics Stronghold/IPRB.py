with open("rosalind_iprb.txt","r") as f:
    k,m,n = f.read().strip().split(" ")

k,m,n = int(k),int(m),int(n)
pop = k+m+n

# We want the concurrent probability P(X U Y), where X is having a dominant gene and Y are possible parents
# We have conditional probabilities of X given y (PXGY) from biology
PXGY = {"AAAA":1.,
        "AAAa":1.,
        "AAaa":1.,
        "AaAa":.75,
        "Aaaa":.5,
        "aaaa":0.,}

# And to get P(Y_i) we take the combinations
PY = {"AAAA":(k*(k-1))/(pop*(pop-1)),
        "AAAa":2*(k*m)/(pop*(pop-1)),
        "AAaa":2*(k*n)/(pop*(pop-1)),
        "AaAa":(m*(m-1))/(pop*(pop-1)),
        "Aaaa":2*(m*n)/(pop*(pop-1)),
        "aaaa":(n*(n-1))/(pop*(pop-1))}

PXUY = sum([PXGY[key]*PY[key] for key in PXGY.keys()])

with open("submission.txt","w") as f:
    f.write(f'{PXUY:.5f}')

