import sys
sys.stdin = open("./dev/stdin")

from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append([n-1, n+1, n*2])
    cnt = 0
    while True:
        print(queue)
        cnt += 1
        que = queue.popleft()
        temp_queue = []
        for q in que:
            if (q < 0):
                continue
            if (q*2 == k):
                return cnt+1
            if (q == k):
                return cnt
            if (q*2 < k or (q*2 - 1) == k):
                temp_queue.append(q*2)
            temp_queue.append(q+1)
            temp_queue.append(q-1)
        queue.append(temp_queue)
        

N, K = list(map(int, input().split()))

if K < N:
    print(N - K)
elif K == N:
    print(0)
else:
    cnt = bfs(N, K)
    print(cnt)