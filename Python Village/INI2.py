with open("rosalind_ini2.txt") as f:
	for line in f:
		a,b = [int(i) for i in line.split()]
print(a*a+b*b)
