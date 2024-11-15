with open("rosalind_ini3.txt",'r') as f:
    string = f.readline()
    a,b,c,d = [int(i) for i in f.readline().split()]

print(string[a:b+1] +  " " + string[c:d+1])
