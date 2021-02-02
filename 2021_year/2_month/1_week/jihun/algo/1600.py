import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

ddy = [-2, -2, -1, -1, 1, 1, 2, 2]
ddx = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs():
    global H, W, K
    queue = deque()
    queue.append((0, 0, 0, 0))
    checked[0][0][0][0] = 1
    cnt = 0
    while queue:
        flag = False
        y, x, hy, hx = queue.popleft()
        if ((y == H-1 and x == W-1) or (hy == H-1 and hx == W-1)):
            return checked[y][x][hy][hx] - 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < H and 0 <= nx < W and not checked[ny][nx][hy][hx] and not data[ny][nx]):
                queue.append((ny, nx, hy, hx))
                checked[ny][nx][hy][hx] = checked[y][x][hy][hx] + 1
            ny = hy + dy[i]
            nx = hx + dx[i]
            if (0 <= ny < H and 0 <= nx < W and not checked[y][x][ny][nx] and not data[ny][nx]):
                queue.append((y, x, ny, nx))
                checked[y][x][ny][nx] = checked[y][x][hy][hx] + 1

        if (cnt < K):
            for i in range(8):
                ny = hy + ddy[i]
                nx = hx + ddx[i]
                if (0 <= ny < H and 0 <= nx < W and not checked[y][x][ny][nx] and not data[ny][nx]):
                    queue.append((y, x, ny, nx))
                    checked[y][x][ny][nx] = checked[y][x][hy][hx] + 1
                    cnt += 1
                ny = y + ddy[i]
                nx = x + ddx[i]
                if (0 <= ny < H and 0 <= nx < W and not checked[ny][nx][hy][hx] and not data[ny][nx]):
                    queue.append((ny, nx, hy, hx))
                    checked[ny][nx][hy][hx] = checked[y][x][hy][hx] + 1
                    cnt += 1
    return -1



K = int(input())
W, H = list(map(int, input().split()))
data = []
for i in range(H):
    data.append(list(map(int, input().split())))
checked = [[[[0] * W for _ in range(H)] for _ in range(W)] for _ in range(H)]

print(bfs())