import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i1, j1, i2, j2):
    global N, M
    que = deque()
    que.append((i1, j1, i2, j2, 0))
    visited[i1][j1].add((i2, j2))
    while que:
        i1, j1, i2, j2, cnt = que.popleft()
        for k in range(4):
            ni1 = i1 + di[k]
            nj1 = j1 + dj[k]
            ni2 = i2 + di[k]
            nj2 = j2 + dj[k]
            if (((ni1 < 0 or ni1 >= N) or (nj1 < 0 or nj1 >= M)) and (0 <= ni2 < N and 0 <= nj2 < M)) or\
                    (((ni2 < 0 or ni2 >= N) or (nj2 < 0 or nj2 >= M)) and (0 <= ni1 < N and 0 <= nj1 < M)):
                return cnt + 1
            elif 0 <= ni1 < N and 0 <= nj1 < M and 0 <= ni2 < N and 0 <= nj2 < M:
                if cnt >= 9:
                    continue
                if board[ni1][nj1] == '#' and board[ni2][nj2] == '#':
                    continue
                elif board[ni1][nj1] == '#':
                    ni1, nj1 = i1, j1
                elif board[ni2][nj2] == '#':
                    ni2, nj2 = i2, j2
                originLen = len(visited[ni1][nj1])
                visited[ni1][nj1].add((ni2, nj2))
                if len(visited[ni1][nj1]) > originLen:
                    que.append((ni1, nj1, ni2, nj2, cnt + 1))
    return -1

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[set() for _ in range(M)] for __ in range(N)]

coin_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin_list.extend([i, j])
            if len(coin_list) == 4:
                break
    if len(coin_list) == 4:
        break

print(bfs(*coin_list))