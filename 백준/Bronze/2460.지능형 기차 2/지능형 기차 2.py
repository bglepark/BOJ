import sys
total = 0
max_total = 0

for _ in range(10):
    a,b = map(int,sys.stdin.readline().split())
    total = total - a
    total = total + b
    max_total = max(total , max_total)

print(max_total)
