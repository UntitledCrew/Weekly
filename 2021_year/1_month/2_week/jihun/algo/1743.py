import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def bfs(sy, sx):
    global N, M
    queue = deque()
    queue.append((sy, sx))
    cnt = 1
    checked[sy][sx] = cnt
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N and 0 <= nx < M and data[ny][nx] and not checked[ny][nx]):
                queue.append((ny, nx))
                cnt += 1
                checked[ny][nx] = cnt
    return cnt

N, M, K = list(map(int, input().split()))
data = [[0] * (M) for _ in range(N)]
for _ in range(K):
    r, c = list(map(int, input().split()))
    data[r-1][c-1] = 1
checked = [[0] * (M) for _ in range(N)]

answer = 0
for y in range(N):
    for x in range(M):
        if data[y][x] and not checked[y][x]:
            temp_answer = bfs(y, x)
            if (temp_answer > answer):
                answer = temp_answer

print(answer)