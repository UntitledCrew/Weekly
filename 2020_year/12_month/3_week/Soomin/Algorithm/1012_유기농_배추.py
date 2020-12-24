from collections import deque

def check_group(i, j):
    global N
    que = deque()
    que.append([i, j])
    garden[i][j] = 0
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and garden[ni][nj]:
                que.append([ni, nj])
                garden[ni][nj] = 0
    return

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

    garden = [[0] * M for n in range(N)]

    for k in range(K):
        j, i = map(int, input().split())
        garden[i][j] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if garden[i][j]:
                check_group(i, j)
                result += 1
    print(result)