from collections import deque

M, N = map(int, input().split())

field = [list(map(int, input().split())) for n in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

que = deque()
cnt = 0

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            field[i][j] = 2
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M and not field[ni][nj]:
                    que.append([ni, nj, 1])
                    field[ni][nj] = 2

while que:
    i, j, cnt = que.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not field[ni][nj]:
            que.append([ni, nj, cnt + 1])
            field[ni][nj] = 2

for i in range(N):
    for j in range(M):
        if not field[i][j]:
            cnt = -1
            break
    if cnt == -1:
        break
print(cnt)