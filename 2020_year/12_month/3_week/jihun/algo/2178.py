import sys
sys.stdin = open("./dev/stdin")

N, M = list(map(int, input().split()))
checked = [[0] * M for _ in range(N)]
data = []
for _ in range(N):
    data.append(list(map(int, list(input()))))

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def bfs(y, x):
    queue = [(y, x)]
    checked[y][x] = 1
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if (0 <= yy < N and 0 <= xx < M and not checked[yy][xx] and data[yy][xx]):
                queue.append((yy, xx))
                checked[yy][xx] = checked[y][x] + 1

bfs(0, 0)

print(checked[N-1][M-1])
