import heapq


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(cnt, i, j):
    global N
    que = []
    heapq.heappush(que, (cnt, i, j))
    visited[i][j] = True
    while que:
        cnt, i, j = heapq.heappop(que)
        for k in range(4):
            n_i = i + di[k]
            n_j = j + dj[k]
            if n_i == N - 1 and n_j == N - 1:
                return cnt
            if 0 <= n_i < N and 0 <= n_j < N:
                if maze[n_i][n_j]:
                    if not visited[n_i][n_j]:
                        heapq.heappush(que, (cnt, n_i, n_j))
                        visited[n_i][n_j] = True
                else:
                    if not visited[n_i][n_j]:
                        heapq.heappush(que, (cnt + 1, n_i, n_j))
                        visited[n_i][n_j] = True
    return cnt

N = int(input())

maze = [list(map(int, list(input()))) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

min_v = bfs(0, 0, 0)
print(min_v)