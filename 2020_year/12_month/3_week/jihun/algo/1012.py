import sys
sys.stdin = open("./dev/stdin")

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def bfs(y, x, cnt):
    queue = [(y, x)]
    checked[y][x] = cnt
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if (0 <= yy < M and 0 <= xx < N and not checked[yy][xx] and data[yy][xx]):
                queue.append((yy, xx))
                checked[yy][xx] = cnt
    

T = int(input())
for _ in range(T):
    N, M, K = list(map(int, input().split()))

    data = [[0] * N for _ in range(M)]
    checked = [[0] * N for _ in range(M)]

    for _ in range(K):
        n, m = list(map(int, input().split()))
        data[m][n] = 1

    cnt = 1
    for y in range(M):
        for x in range(N):
            if (data[y][x] and not checked[y][x]):
                bfs(y, x, cnt)
                cnt += 1
    
    print(cnt-1)