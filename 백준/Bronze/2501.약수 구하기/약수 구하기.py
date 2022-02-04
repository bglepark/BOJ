N , K = map(int, input().split())
list = []

for i in range(N):
    if (N%(i+1))==0:
        list.append(i+1)
list.sort()
if len(list)<K:
    print(0)
else:
    print(list[K-1])