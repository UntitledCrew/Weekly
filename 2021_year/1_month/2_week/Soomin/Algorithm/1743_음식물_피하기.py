from collections import deque
import sys

def bfs(n, m):
    global N, M
    que = deque()
    que.append([n, m])
    Map[n][m] = 2
    cnt = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            n_i = i + di[k]
            n_j = j + dj[k]
            if 0 <= n_i < N and 0 <= n_j < M and Map[n_i][n_j] == 1:
                que.append([n_i, n_j])
                Map[n_i][n_j] = 2
                cnt += 1
    return cnt



input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M, K = map(int, input().split())

Map = [[0] * M for _ in range(N)]

for k in range(K):
    r, c = map(int, input().split())
    Map[r-1][c-1] = 1

max_size = 0
for n in range(N):
    for m in range(M):
        if Map[n][m] == 1:
            size = bfs(n, m)
            if max_size < size:
                max_size = size

print(max_size)