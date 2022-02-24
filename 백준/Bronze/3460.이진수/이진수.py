import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n1=int(sys.stdin.readline())
    n2=bin(n1)
    n2=str(n2)[2:]
    n_list=[]
    for i in range(len(n2)):
        n_list.append(n2[i])



    n_list = list(reversed(n_list))
    idx1 = [i for i in range(len(n_list)) if '1' in n_list[i]]
    for i in range(len(idx1)):
        print(idx1[i], end=" ")