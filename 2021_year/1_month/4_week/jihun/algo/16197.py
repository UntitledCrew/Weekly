import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(coin):
    queue = deque()
    queue.append(coin)
    while queue:
        y1, x1, y2, x2 = queue.popleft()
        if (checked[0][y1][x1] > 10 or checked[1][y2][x2] > 10):
            return -1
        for i in range(4):
            temp = []
            flag1 = False
            flag2 = False
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]
            if (ny1 < 0 or ny1 > N or nx1 < 0 or nx1 > M):
                flag1 = True
            if (ny2 < 0 or ny2 > N or nx2 < 0 or nx2 > M):
                flag2 = True
            if (flag1 and not flag2) or (not flag1 and flag2):
                print(checked)
                return checked[0][y1][x1]
            if (0 <= ny1 < N and 0 <= nx1 < M and data[ny1][nx1] != '#' and not checked[0][ny1][nx1]):
                temp.append(ny1)
                temp.append(nx1)
                checked[0][ny1][nx1] = checked[0][y1][x1] + 1
            else:
                temp.append(y1)
                temp.append(x1)
            if (0 <= ny2 < N and 0 <= nx2 < M and data[ny2][nx2] != '#' and not checked[1][ny2][nx2]):
                temp.append(ny2)
                temp.append(nx2)
                checked[1][ny2][nx2] = checked[1][y2][x2] + 1
            else:
                temp.append(y2)
                temp.append(x2)
            queue.append(temp)
    

N, M = list(map(int, input().split()))

data = []
for _ in range(N):
    data.append(list(input()))
checked = [[[0] * M for _ in range(N)] for _ in range(2)]
coin = []

temp = []
for y in range(N):
    for x in range(M):
        if (data[y][x] == 'o'):
            coin.append(y)
            coin.append(x)
print(bfs(coin))
