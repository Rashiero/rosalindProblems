counter = {}
with open("rosalind_ini6.txt") as f:
    str_list = f.read().split(" ")

str_list = [x.strip(" ").strip("\n") for x in str_list]

for x in str_list:
    if x not in counter.keys():
        counter[x] = 0
    counter[x]+=1

with open("submission.txt","w") as f:
    for key,val in counter.items():
        print(f"{key} {val}")
        f.write(f"{key} {val}\n")
