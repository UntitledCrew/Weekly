import sys
sys.stdin = open("./dev/stdin")

from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append([n])
    checked[n] = 1
    cnt = 0
    while queue:
        q_list = queue.popleft()
        if (k in q_list):
            return cnt
        temp_list = []
        for q in q_list:
            if (0 <= q <= 100000):
                if not checked[q+1]:
                    temp_list.append(q+1)
                    checked[q+1] = 1
                if q != 0 and not checked[q-1]:
                    temp_list.append(q-1)
                    checked[q-1] = 1
                if not checked[q*2]:
                    temp_list.append(q*2)
                    checked[q*2] = 1
        queue.append(temp_list)
        cnt += 1


N, K = list(map(int, input().split()))

checked = [0] * 200001

if K < N:
    print(N - K)
elif K == N:
    print(0)
else:
    cnt = bfs(N, K)
    print(cnt)