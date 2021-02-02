import sys
sys.stdin = open('./dev/stdin')

from collections import deque

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs(coins):
    queue = deque()
    queue.append(coins[0])
    queue.append(coins[1])
    queue.append(coins[2])
    queue.append(coins[3])
    checked[0][coins[0]][coins[1]] = 1
    checked[1][coins[2]][coins[3]] = 1
    while queue:
        y1 = queue.popleft()
        x1 = queue.popleft()
        y2 = queue.popleft()
        x2 = queue.popleft()
        print(checked[0][y1][x1], checked[1][y2][x2])
        print(y1, x1, y2, x2)
        if (checked[0][y1][x1] > 10 or checked[1][y2][x2] > 10):
            return -1
        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]

            if ((ny1 < 0 or ny1 >= N or nx1 < 0 or nx1 >= M) and (ny2 < 0 or ny2 >= N or nx2 < 0 or nx2 >= M)):
                continue

            if ((ny1 < 0 or ny1 >= N or nx1 < 0 or nx1 >= M) and (0 <= ny2 < N and 0 <= nx2 < M)):
                return checked[0][y1][x1]
            
            if (((0 <= ny1 < N and 0 <= nx1 < M) and (ny2 < 0 or ny2 >= N or nx2 < 0 or nx2 >= M))):
                return checked[1][y2][x2]
            
            if (data[ny1][nx1] == '#'):
                ny1 = y1
                nx1 = x1

            if (data[ny2][nx2] == '#'):
                ny2 = y2
                nx2 = x2
                
            if (not checked[0][ny1][nx1]):
                checked[0][ny1][nx1] = checked[0][y1][x1] + 1
            queue.append(ny1)
            queue.append(nx1)
                

            if (not checked[1][ny2][nx2]):
                checked[1][ny2][nx2] = checked[1][y2][x2] + 1
            queue.append(ny2)
            queue.append(nx2)
                



N, M = list(map(int, input().split()))

data = []
for _ in range(N):
    data.append(list(input()))

checked = [[[0] * (M) for _ in range(N)] for _ in range(2)]

coins = []
for y in range(N):
    for x in range(M):
        if (data[y][x] == 'o'):
            coins.append(y)
            coins.append(x)

print(bfs(coins))