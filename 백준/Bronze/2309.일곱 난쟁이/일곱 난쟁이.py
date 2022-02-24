list = []
for _ in range(9):
    n=int(input())
    list.append(n)

total = sum(list)


for i in range(9):
    for j in range(9):
        if (int(total - (list[i] + list[j]))==100) and i!=j:
            tall_1 = list[i]
            tall_2 = list[j]


list.remove(tall_1)
list.remove(tall_2)
list.sort()
for i in range(len(list)):
    print(list[i])