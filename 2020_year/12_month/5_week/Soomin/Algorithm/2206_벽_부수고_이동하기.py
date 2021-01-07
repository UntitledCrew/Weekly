from collections import deque
import sys


def bfs():
    global N, M
    if N == 1 and M == 1:
        return 1
    que = deque()
    que.append([0, 0, 0, 1])
    visited[0][0] = 3
    while que:
        i, j, break_wall, cnt = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if ni == N - 1 and nj == M - 1:
                    return cnt + 1
                if not Map[ni][nj]:
                    if not break_wall:
                        if visited[ni][nj] == 0 or visited[ni][nj] == 2:
                            que.append([ni, nj, break_wall, cnt + 1])
                            if not visited[ni][nj]:
                                visited[ni][nj] = 1
                            else:
                                visited[ni][nj] = 3
                    else:
                        if visited[ni][nj] == 0 or visited[ni][nj] == 1:
                            que.append([ni, nj, break_wall, cnt + 1])
                            if not visited[ni][nj]:
                                visited[ni][nj] = 2
                            else:
                                visited[ni][nj] = 3
                else:
                    if not break_wall:
                        if visited[ni][nj] == 0 or visited[ni][nj] == 2:
                            que.append([ni, nj, 1, cnt + 1])
                            if not visited[ni][nj]:
                                visited[ni][nj] = 1
                            else:
                                visited[ni][nj] = 3
    return -1

# visited 규칙
# 0 : 한번도 안 통과
# 1 : 벽 안부수고 통과
# 2 : 벽 부수고 통과
# 3 : 둘 다 통과

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

input = sys.stdin.readline

N, M = map(int, input().split())

Map = [list(map(int, list(input())[:-1])) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


print(bfs())