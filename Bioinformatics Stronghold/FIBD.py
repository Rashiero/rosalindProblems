with open('rosalind_fibd.txt','r') as f:
    n,k = [int(x) for x in f.read().strip().split(' ')]

# The recurrence relation takes the shape of
# F_{n+1} = F_{n} + F_{n-1} - F_{n-k}
# For i<k, F_{n-k} follows the standard Fibonacci Sequence
F = [1,1]

for i in range(2,k):
    F.append(F[i-1]+F[i-2])
    print(i,F)

F.append(F[i]+F[i-1]-1)

for i in range(k,n-1):
    F.append(F[i]+F[i-1]-F[i-k])
    print(i,F)
print(F)
