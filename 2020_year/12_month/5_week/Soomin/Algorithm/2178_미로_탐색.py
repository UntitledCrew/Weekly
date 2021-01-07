from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def BFS(i, j):
    global N, M
    que = deque()
    que.append([i, j, 1])
    maze[i][j] = 0
    while que:
        i, j, cnt = que.popleft()
        for k in range(4):
            n_i = i + di[k]
            n_j = j + dj[k]
            if n_i == N - 1 and n_j == M - 1:
                return cnt + 1
            if 0 <= n_i < N and 0 <= n_j < M and maze[n_i][n_j]:
                que.append([n_i, n_j, cnt + 1])
                maze[n_i][n_j] = 0
    return False


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for n in range(N)]

print(BFS(0, 0))
