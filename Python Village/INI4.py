with open("rosalind_ini4.txt",'r') as f:
    a,b = [int(i) for i in f.read().split()]

soma = 0
for i in range(a,b+1):
    if(i%2 == 1):
        soma += i

print(soma)
