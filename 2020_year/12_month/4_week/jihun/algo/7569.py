import sys
sys.stdin = open("./dev/stdin")

from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dy = [1, 0, 0, -1, 0, 0]
dx = [0, 1, -1, 0, 0, 0]

def bfs(no_tmt):
    queue = deque()
    for z, y, x in tmt:
        queue.append((z, y, x))
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= nz < H and 0 <= ny < M and 0 <= nx < N and not data[nz][ny][nx] and not checked[nz][ny][nx]):
                queue.append((nz, ny, nx))
                checked[nz][ny][nx] = checked[z][y][x] + 1

def check():
    global N, M, H
    cnt = 0
    for z in range(H):
        for y in range(M):
            for x in range(N):
                if not checked[z][y][x]:
                    return 0
                if (cnt < checked[z][y][x]):
                    cnt = checked[z][y][x]
    return cnt

N, M, H = list(map(int, input().split()))

data = []
tmt = []
no_tmt = 0
for z in range(H):
    temp_data = []
    for y in range(M):
        temp_data.append(list(map(int, input().split())))
        for x in range(N):
            if (temp_data[y][x] == 0):
                no_tmt += 1
            if (temp_data[y][x] == 1):
                tmt.append((z, y, x))
    data.append(temp_data)

checked = data

bfs(no_tmt)
answer = check()
print(answer-1)