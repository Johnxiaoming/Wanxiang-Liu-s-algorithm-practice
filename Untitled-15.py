import time
start_time = time.time()
def FindCommonString(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    n = len(s2)
    for i in range(n):
        for j in range(i + 1):
            token = s2[j: n - i + j]
            if token in s1:
                return token
def reform(lines):
    for line in lines:
        if line.startswith(">"):
            a = line.replace(">", "")
            a = a.replace("\n", "")
            id.append(a)
        else:
            if len(id) > len(seq):
                line = line.replace("\n","")
                seq.append(line)
            else:
                line = line.replace("\n", "")
                seq[len(id) - 1] = seq[len(id) - 1] + line
    return id , seq

f = open("D:/datasets/rosalind_lcsm.txt","r")
lines = f.readlines()
id = []
seq = []
id, seq = reform(lines)
print(seq[1])
com = ""
for i in range(len(seq) -1):
    if com == "":
        com = FindCommonString(seq[i], seq[i+1])
        print(com)
    else:
        if len(com) >= len(FindCommonString(seq[i+1], com)):
            com = FindCommonString(seq[i+1],com)
print(com)
print("--- %s seconds ---" %(time.time() - start_time))
f.close()