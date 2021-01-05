import sys
sys.stdin = open("./dev/stdin")

from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def bfs():
    queue = deque()
    for y, x in start_list:
        queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < M and 0 <= nx < N and not data[ny][nx] and not checked[ny][nx]):
                queue.append((ny, nx))
                checked[ny][nx] = checked[y][x] + 1

def check():
    global N, M
    cnt = 0
    for y in range(M):
        for x in range(N):
            if not checked[y][x]:
                return 0
            if (cnt < checked[y][x]):
                cnt = checked[y][x]
    return cnt

N, M = list(map(int, input().split()))

data = []
for _ in range(M):
    data.append(list(map(int, input().split())))

checked = data

answer = 987654321
start_list = []
for y in range(M):
    for x in range(N):
        if data[y][x] == 1:
            start_list.append((y, x))
bfs()
answer = check()

print(answer-1)