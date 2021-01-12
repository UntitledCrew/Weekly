import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def bfs(minN):
    queue = deque()
    queue.append((0, 0))
    checked[0][0] = 1
    while queue:
        y, x = queue.popleft()
        if (checked[y][x] > minN):
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N and 0 <= nx < M and not data[ny][nx] and not checked[ny][nx]):
                if (ny == N-1 and nx == M-1):
                    return checked[y][x] + 1
                queue.append((ny, nx))
                checked[ny][nx] = checked[y][x] + 1
    return 987654321

N, M = list(map(int, input().split()))
data = [list(map(int ,input())) for _ in range(N)]
checked = [[0] * M for _ in range(N)]
minN = bfs(987654321)

for y in range(N):
    for x in range(M):
        flag = False
        if data[y][x] == 1:
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= ny < N and 0 <= nx < M and not data[ny][nx]):
                    cnt += 1
                if (cnt >= 2):
                    data[y][x] = 0
                    flag = True
                    break
        if flag:
            checked = [[0] * M for _ in range(N)]
            temp_num = bfs(minN)
            if (temp_num < minN):
                minN = temp_num
            data[y][x] = 1

if (minN == 987654321):
    print(-1)
else:
    print(minN)