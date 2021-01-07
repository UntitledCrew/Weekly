from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split()); visited = [0]*100001
que = deque(); cnt = 0

if N >= K: cnt = N - K
else: que.append([N, 0]); visited[N] = 1

while que:
    n, cnt = que.popleft()
    n1 = n + 1; n2 = n - 1; n3 = 2 * n
    if n1 == K or n2 == K or n3 == K: cnt += 1; break
    if n1 <= 100000 and not visited[n1]: que.append([n1, cnt + 1]); visited[n1] = 1
    if 0 <= n2 and not visited[n2]: que.append([n2, cnt + 1]); visited[n2] = 1
    if n3 <= 100000 and not visited[n3]: que.append([n3, cnt + 1]); visited[n3] = 1

print(cnt)