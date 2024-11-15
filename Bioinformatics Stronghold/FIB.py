with open("rosalind_fib.txt","r") as f:
    n,k = [int(x) for x in f.read().strip().split()]

F = [1,1]

for i in range(2,n):
    F.append(F[i-1]+k*F[i-2])

with open("submission.txt","w") as f:
    f.write(f"{F[n-1]}")

