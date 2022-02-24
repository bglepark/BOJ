import sys
T = int(sys.stdin.readline())

for _ in range(T):
    case = list(map(int, sys.stdin.readline().split()))
    case.sort(reverse=True)
    print(case[2])