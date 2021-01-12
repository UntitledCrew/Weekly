import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [-2, -1, -2, -1, 2, 1, 2, 1]
dx = [1, 2, -1, -2, 1, 2, -1, -2]

def bfs(sy, sx):
    global I, gx, gy
    queue = deque()
    queue.append((sy, sx))
    checked[sy][sx] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < I and 0 <= nx < I and not checked[ny][nx]):
                if (ny == gy and nx == gx):
                    return checked[y][x]
                queue.append((ny, nx))
                checked[ny][nx] = checked[y][x] + 1

T = int(input())
for _ in range(T):
    I = int(input())
    sx, sy = list(map(int, input().split()))
    gx, gy = list(map(int, input().split()))

    checked = [[0] * I for _ in range(I)]

    if (sx == gx and sy == gy):
        print(0)
    else:
        print(bfs(sy, sx))
    
