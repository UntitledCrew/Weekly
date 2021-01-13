from collections import deque
import sys


def bfs(I, s_i, s_j, e_i, e_j):
    que = deque()
    que.append([s_i, s_j, 0])
    chess[s_i][s_j] = True

    while que:
        i, j, cnt = que.popleft()
        for k in range(8):
            n_i = i + di[k]
            n_j = j + dj[k]
            if n_i == e_i and n_j == e_j:
                return cnt + 1
            if 0 <= n_i < I and 0 <= n_j < I and not chess[n_i][n_j]:
                que.append([n_i, n_j, cnt + 1])
                chess[n_i][n_j] = True


input = sys.stdin.readline

di = [1, 1, -1, -1, 2, 2, -2, -2]
dj = [2, -2, 2, -2, 1, -1, 1, -1]

T = int(input())
for tc in range(T):
    I = int(input())
    s_i, s_j = map(int, input().split())
    e_i, e_j = map(int, input().split())
    chess = [[False] * I for _ in range(I)]

    if s_i == e_i and s_j == e_j:
        cnt = 0
    else:
        cnt = bfs(I, s_i, s_j, e_i, e_j)

    print(cnt)
