import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n , idx = map(int , sys.stdin.readline().split())
    q = list(map(int , sys.stdin.readline().split()))
    count = 0
    while q: #q가 빈 리스트가 아닐때
        max_q = max(q)
        first = q[0]
        del q[0]

        idx -=1


        if max_q == first: #첫 숫자가 가장 큰 숫자일 경우
            count += 1
            if idx == -1:
                print(count)
                break

        elif max_q != first:
            q.append(first)
            if idx ==-1:
                idx = len(q)-1