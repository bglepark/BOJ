M = int(input())
N = int(input())

lst = list()
for num in range(M,N+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                error += 1  
        if error == 0:
            lst.append(num)  

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)