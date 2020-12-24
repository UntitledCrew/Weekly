from collections import deque

def check_group(i, j):
    global N
    que = deque()
    que.append([i, j])
    Map[i][j] = 0
    cnt = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and Map[ni][nj]:
                que.append([ni, nj])
                Map[ni][nj] = 0
                cnt += 1
    return cnt

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N = int(input())

Map = [list(map(int, list(input()))) for n in range(N)]

total_group = 0
answer_list = []
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            answer_list.append(check_group(i, j))
            total_group += 1

print(total_group)
for answer in sorted(answer_list):
    print(answer)
