a , b = map(int, input().split())
list = []

for i in range(1 , b+1):
    for j in range(i):
        list.append(i)

sum=0
for i in range(a-1,b):
    sum+=list[i]

print(sum)